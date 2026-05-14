# Description: Short example for Dickey Fuller Test for Stationarity in Time Series with Python.



from data_io import read_csv
from dataclasses import dataclass
from pathlib import Path
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
import signalplot
import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)



def load_data(url):
    return read_csv(url, parse_dates=['Month'], index_col='Month')

def perform_adf_test(data):
    return adfuller(data.values)

def print_adf_results(adf_result):
    logger.info("Augmented Dickey-Fuller Test Results:")
    logger.info(f"ADF Statistic: {adf_result[0]:.4f}")
    logger.info(f"p-value: {adf_result[1]:.4f}")
    logger.info(f"Lags: {adf_result[2]}")
    logger.info(f"Observations: {adf_result[3]}")
    logger.info("Critical Values:")
    for key, value in adf_result[4].items():
        logger.info(f"  {key}: {value:.4f}")

def interpret_results(p_value):
    return "stationary (reject H₀)" if p_value < 0.05 else "non-stationary (fail to reject H₀)"

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
    df = load_data(url)
    adf_result = perform_adf_test(df)
    print_adf_results(adf_result)
    logger.info(f"The time series is {interpret_results(adf_result[1])}.")

#Differencing
df_diff = df.diff().dropna()

#Log Transform
df_log = np.log(df)

adf_result_diff = adfuller(df_diff)
logger.info(f"ADF Statistic after Differencing: {adf_result_diff[0]}")
logger.info(f"p-value after Differencing: {adf_result_diff[1]}")

adf_result_log = adfuller(df_log)
logger.info(f"ADF Statistic after Log: {adf_result_log[0]}")
logger.info(f"p-value after Log: {adf_result_log[1]}")


result = adfuller(df['weight'])
logger.info(f"ADF Statistic: {result[0]}, p-value: {result[1]}")


np.random.seed(42)
signalplot.apply(font_family='serif')


@dataclass
class Config:
    csv_path: str = "2001-2025 Net_generation_United_States_all_sectors_monthly.csv"
    freq: str = "MS"
    season: int = 12


def load_series(cfg: Config) -> pd.Series:
    p = Path(cfg.csv_path)
    df = read_csv(p, header=None, usecols=[0,1], names=["date","value"], sep=",")
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    s = df.dropna().sort_values("date").set_index("date")["value"].asfreq(cfg.freq)
    return s


def adf_summary(y: pd.Series) -> dict:
    res = adfuller(y.dropna().values, autolag='AIC')
    keys = ['ADF Statistic','p-value','lags used','nobs']
    out = dict(zip(keys, res[:4]))
    return out


def main(plot: bool = False):
    cfg = Config()
    s = load_series(cfg)
    base = adf_summary(s)

    sd = s.diff(cfg.season).dropna()
    seas = adf_summary(sd)

    logger.info("ADF on raw:", base)
    logger.info("ADF on seasonal-differenced:", seas)

    if plot:
        fig, ax = plt.subplots(2, 2, figsize=(10,6))
        ax[0,0].plot(s.index, s.values); ax[0,0].set_title('EIA series')
        ax[0,1].plot(sd.index, sd.values); ax[0,1].set_title('Seasonal diff (12)')
        plot_acf(sd.dropna(), ax=ax[1,0], lags=24)
        plot_pacf(sd.dropna(), ax=ax[1,1], lags=24, method='ywm')
        signalplot.save('eia_adf.png')

if __name__ == "__main__":
    main()
