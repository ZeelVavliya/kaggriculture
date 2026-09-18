"""Behaviour-cloning warm start: a small MLP that predicts a RESIDUAL
(delta_frac, delta_prio) on top of v41's own market decision at the seam
(lab/p2/market_env.apply_policy). The final Linear layer of each head is
zero-initialised, so before a single gradient step the network outputs
exactly (0, 0) and market_env.apply_policy reproduces v41's sells exactly --
"warm start" is a property of the parameterisation, not something merely
learned approximately (an earlier absolute-fraction version of this file
learned an approximate identity, and imperfect approximation was enough to
fail the fidelity gate 0-20 vs raw v41; see lab/p2/data/bc_model.metrics.json
and the p2-bc-fidelity-9011af92 batch for that evidence).

collect.py logs games via the *identity* wrapper (policy=None), so the
logged "target" (frac, prio) *is* v41's own action restated in the policy's
action space -- which is exactly what apply_policy calls the residual base
for that same turn. Target delta is therefore identically zero on this
dataset by construction: BC here is not fitting a nontrivial function, it is
confirming the residual stays near its zero fixed point (loss should start
at ~0 and stay there). The nontrivial learning signal for market ORDERING
decisions comes later, from RL reward on win/loss (out of scope for this
module) -- BC's job is only to hand RL a warm start that is provably
identical to v41 before any of that training happens.

Usage: python -m lab.p2.bc --data lab/p2/data/bc_data_500.npz --epochs 30
"""
import argparse
import json
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

from lab.p2.market_env import FREE_ITEMS

N_ITEMS = len(FREE_ITEMS)


class MarketMLP(nn.Module):
    def __init__(self, in_dim, hidden=256, n_items=N_ITEMS):
        super().__init__()
        self.body = nn.Sequential(
            nn.Linear(in_dim, hidden), nn.ReLU(),
            nn.Linear(hidden, hidden), nn.ReLU(),
        )
        self.frac_head = nn.Linear(hidden, n_items)   # -> tanh * scale, delta_frac
        self.prio_head = nn.Linear(hidden, n_items)   # unconstrained, delta_prio
        # Zero-init the output layers only (not the body -- it still needs to
        # learn useful features under RL later): at construction every input
        # produces (0, 0), so market_env.apply_policy's residual is exactly
        # v41's own action until training moves these weights.
        for head in (self.frac_head, self.prio_head):
            nn.init.zeros_(head.weight)
            nn.init.zeros_(head.bias)

    def forward(self, x):
        h = self.body(x)
        delta_frac = torch.tanh(self.frac_head(h))  # in [-1, 1]; apply_policy clips base+delta to [0,1]
        delta_prio = self.prio_head(h)
        return delta_frac, delta_prio

    def as_policy(self):
        """Wraps this module as the callable market_env.apply_policy expects:
        features (np.ndarray) -> (delta_frac, delta_prio) numpy arrays."""
        self.eval()

        @torch.no_grad()
        def policy(features):
            x = torch.from_numpy(np.asarray(features, dtype=np.float32)).unsqueeze(0)
            delta_frac, delta_prio = self(x)
            return delta_frac.squeeze(0).numpy(), delta_prio.squeeze(0).numpy()

        return policy


def _game_split(game_ids, holdout_frac=0.2, seed=0):
    games = np.unique(game_ids)
    rng = np.random.RandomState(seed)
    rng.shuffle(games)
    n_holdout = max(1, int(len(games) * holdout_frac))
    holdout, train = set(games[:n_holdout]), set(games[n_holdout:])
    train_mask = np.array([g in train for g in game_ids])
    return train_mask, ~train_mask


def train(data_path, epochs=30, hidden=256, lr=1e-3, batch_size=512, seed=0, out_path=None):
    d = np.load(data_path, allow_pickle=True)
    X, Yf, Yp, gids = d["features"], d["frac_targets"], d["prio_targets"], d["game_ids"]
    print(f"loaded {X.shape[0]} rows, {len(np.unique(gids))} games, feature dim {X.shape[1]}")

    train_mask, held_mask = _game_split(gids, seed=seed)
    Xtr, Yftr, Yptr = X[train_mask], Yf[train_mask], Yp[train_mask]
    Xho, Yfho, Ypho = X[held_mask], Yf[held_mask], Yp[held_mask]
    print(f"train rows={len(Xtr)} held-out rows={len(Xho)} "
          f"({train_mask.sum()/len(gids)*100:.0f}%/{held_mask.sum()/len(gids)*100:.0f}% by row, split by game)")

    torch.manual_seed(seed)
    model = MarketMLP(X.shape[1], hidden=hidden)
    opt = torch.optim.Adam(model.parameters(), lr=lr)

    Xtr_t = torch.from_numpy(Xtr)
    Yftr_t = torch.from_numpy(Yftr)
    Yptr_t = torch.from_numpy(Yptr)
    n = len(Xtr_t)

    # collect.py logs games via the identity wrapper, so Yf/Yp *are* this
    # turn's residual base (market_env.base_frac_prio) -- the correct BC
    # target-delta on this dataset is (Yf - Yf) == 0 everywhere. Training
    # toward zero (with zero-initialised heads, see MarketMLP) is what
    # guarantees the exported policy stays an exact warm start.
    zeros_f = torch.zeros_like(Yftr_t)
    zeros_p = torch.zeros_like(Yptr_t)
    for epoch in range(epochs):
        model.train()
        perm = torch.randperm(n)
        tot_loss = 0.0
        for i in range(0, n, batch_size):
            idx = perm[i:i + batch_size]
            xb = Xtr_t[idx]
            delta_frac, delta_prio = model(xb)
            loss = nn.functional.mse_loss(delta_frac, zeros_f[:len(idx)]) + \
                nn.functional.mse_loss(delta_prio, zeros_p[:len(idx)])
            opt.zero_grad()
            loss.backward()
            opt.step()
            tot_loss += loss.item() * len(idx)
        if epoch % 5 == 0 or epoch == epochs - 1:
            print(f"epoch {epoch}: train loss {tot_loss / n:.5f}")

    model.eval()
    with torch.no_grad():
        delta_frac_ho, delta_prio_ho = model(torch.from_numpy(Xho))
    per_item = {}
    for j, item in enumerate(FREE_ITEMS):
        # "held_out_delta_*_mse" is distance from identity (target is 0 by
        # construction on this dataset) -- this IS the fidelity-relevant
        # number: how far the warm start has drifted from reproducing v41.
        delta_frac_mse = float((delta_frac_ho[:, j] ** 2).mean())
        delta_prio_mse = float((delta_prio_ho[:, j] ** 2).mean())
        active = Ypho[:, j] > 0
        per_item[item] = {"held_out_delta_frac_mse": delta_frac_mse, "held_out_delta_prio_mse": delta_prio_mse,
                           "n_active_rows": int(active.sum())}
    print("\nheld-out per-item metrics (distance from identity; target is 0 by construction):")
    for item, m in per_item.items():
        print(f"  {item:10s} delta_frac_mse={m['held_out_delta_frac_mse']:.6f}  "
              f"delta_prio_mse={m['held_out_delta_prio_mse']:.6f}  n_active={m['n_active_rows']}")

    if out_path:
        torch.save({"state_dict": model.state_dict(), "in_dim": X.shape[1], "hidden": hidden}, out_path)
        Path(out_path).with_suffix(".metrics.json").write_text(json.dumps(per_item, indent=2), encoding="utf-8")
        print(f"\nsaved checkpoint to {out_path}")
    return model, per_item


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=str(Path(__file__).resolve().parent / "data" / "bc_data.npz"))
    ap.add_argument("--epochs", type=int, default=30)
    ap.add_argument("--hidden", type=int, default=256)
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent / "data" / "bc_model.pt"))
    args = ap.parse_args()
    train(args.data, epochs=args.epochs, hidden=args.hidden, out_path=args.out)


if __name__ == "__main__":
    main()
