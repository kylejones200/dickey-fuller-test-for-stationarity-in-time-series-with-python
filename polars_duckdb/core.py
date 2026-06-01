"""Dickey-Fuller demo — rolling stats via DuckDB window functions."""

from pathlib import Path
from typing import Any

import duckdb
import matplotlib.pyplot as plt
import numpy as np
import polars as pl
from statsmodels.tsa.stattools import adfuller


def generate_random_walk(n_samples: int = 200, seed: int = 42) -> pl.DataFrame:
    rng = np.random.default_rng(seed)
    x = np.cumsum(rng.normal(loc=0, scale=1, size=n_samples))
    return pl.DataFrame({"value": x.tolist()})


def calculate_rolling_stats(df: pl.DataFrame, window: int = 12) -> pl.DataFrame:
    w = window - 1
    work = df.with_row_index("idx")
    return duckdb.sql(f"""
        SELECT
            value,
            AVG(value) OVER (ORDER BY idx ROWS BETWEEN {w} PRECEDING AND CURRENT ROW)
                AS rolling_mean,
            STDDEV_SAMP(value) OVER (ORDER BY idx ROWS BETWEEN {w} PRECEDING AND CURRENT ROW)
                AS rolling_std
        FROM work
        ORDER BY idx
    """).pl()


def test_stationarity(series: pl.Series) -> dict[str, Any]:
    values = series.drop_nulls().to_numpy()
    stat, pval, *_rest = adfuller(values, autolag="AIC")
    return {
        "adf_statistic": float(stat),
        "p_value": float(pval),
        "is_stationary": pval <= 0.05,
    }


def plot_rolling_stats(stats_df: pl.DataFrame, output_path: Path, plot: bool = False) -> None:
    if not plot:
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(stats_df["value"].to_list(), label="Original", color="#4A90A4", linewidth=1.2)
    ax.plot(stats_df["rolling_mean"].to_list(), label="Rolling Mean", color="#D4A574", linewidth=1.2)
    ax.plot(stats_df["rolling_std"].to_list(), label="Rolling Std", color="#8B6F9E", linewidth=1.2)
    ax.legend(loc="best")
    plt.savefig(output_path, dpi=100, bbox_inches="tight")
    plt.close()
