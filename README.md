# Dickey-Fuller Test for Stationarity in Time Series with Python

This project demonstrates the Augmented Dickey-Fuller (ADF) test for testing stationarity in time series data.

## Business context

One of the key properties to evaluate in a time series is stationarity. A stationary time series has statistical properties --- like mean, variance, and autocorrelation --- that remain constant over time.

<figcaption>Photo by <a class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Annie Spratt</a> on <a class="markup--anchor markup--figure-anchor"

Many statistical models for time series assume stationarity, such as ARIMA. we use the Dickey-Fuller Test to validation that assumption. Dickey-Fuller is a statistical test that determines whether a time series has a unit root, which indicates non-stationarity.

## Article

Medium article: [Dickey-Fuller Test for Stationarity](https://medium.com/@kylejones_47003/dickey-fuller-test-for-stationarity-in-time-series-with-python-4e4bf1953eed)

## Project Structure

```
.
├── README.md           # This file
├── main.py            # Main entry point
├── config.yaml        # Configuration file
├── requirements.txt   # Python dependencies
├── src/               # Core functions
│   ├── core.py        # Stationarity testing functions
│   └── plotting.py    # Tufte-style plotting utilities
├── tests/             # Unit tests
├── data/              # Data files (if needed)
└── images/            # Generated plots and figures
```

## Configuration

Edit `config.yaml` to customize:
- Data generation parameters (n_samples, seed)
- Rolling window size
- Output settings

## Caveats

- By default, the script generates synthetic random walk data (non-stationary).
- The ADF test assumes the time series has sufficient length for meaningful statistical inference.
- A p-value ≤ 0.05 indicates the series is stationary (reject null hypothesis of non-stationarity).

## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).