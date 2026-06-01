"""Rolling mean and std (pandas-compatible sample std)."""

from __future__ import annotations

import numpy as np


def rolling_mean_std(values: np.ndarray, window: int) -> tuple[np.ndarray, np.ndarray]:
    v = np.asarray(values, dtype=float)
    n = len(v)
    means = np.full(n, np.nan)
    stds = np.full(n, np.nan)
    if window <= 0 or n == 0:
        return means, stds
    for i in range(window - 1, n):
        sl = v[i + 1 - window : i + 1]
        means[i] = sl.mean()
        stds[i] = sl.std(ddof=1) if window > 1 else 0.0
    return means, stds
