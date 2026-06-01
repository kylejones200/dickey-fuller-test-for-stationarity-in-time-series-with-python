#!/usr/bin/env python3
"""Python vs Rust kernel benchmark."""

from __future__ import annotations

import time
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from compute_kernel import rolling_mean_std  # noqa: E402

def main() -> None:
    v = np.ascontiguousarray(np.sin(np.arange(8000) * 0.01)); w = 24
    t0 = time.perf_counter()
    for _ in range(200):
        rolling_mean_std(v, w)
    py_s = time.perf_counter() - t0
    try:
        import dickey_fuller_test_for_stationarity_in_time_series_with_python_rs as rs
    except ImportError:
        print("Build: maturin develop --release -m rust/py/Cargo.toml")
        print(f"Python {py_s:.3f}s")
        return
    rs_s = rs.bench_kernel_py(v, w, 500)
    print(f"Python {py_s:.3f}s Rust {rs_s:.3f}s speedup {py_s / max(rs_s, 1e-9):.1f}x")
    pm, ps = rolling_mean_std(v, w)
    rm, rs_std = rs.rolling_mean_std_py(v, w)
    np.testing.assert_allclose(pm, np.asarray(rm), rtol=1e-10, equal_nan=True)
    np.testing.assert_allclose(ps, np.asarray(rs_std), rtol=1e-10, equal_nan=True)
    print("Correctness: OK")

if __name__ == "__main__":
    main()
