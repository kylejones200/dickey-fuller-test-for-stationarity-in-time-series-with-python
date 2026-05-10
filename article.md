# Dickey-Fuller Test for Stationarity in Time Series with Python One of the key properties to evaluate in a time series is stationarity.
A stationary time series has statistical properties --- like mean...

### **Dickey**-Fuller Test for Stationarity in Time Series with Python
#### The Dickey-Fuller test validates that a time series is stationarity with is a key assumption for many forecasting models.
One of the key properties to evaluate in a time series is stationarity. A stationary time series has statistical properties --- like mean, variance, and autocorrelation --- that remain constant over time.


<figcaption>Photo by <a class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Annie Spratt</a> on <a class="markup--anchor markup--figure-anchor"


Many statistical models for time series assume stationarity, such as ARIMA. we use the Dickey-Fuller Test to validation that assumption. Dickey-Fuller is a statistical test that determines whether a time series has a unit root, which indicates non-stationarity.

#### What is the (augmented) Dickey-Fuller Test?
The Dickey-Fuller Test is a hypothesis test for stationarity. It evaluates whether the time series has a unit root, which implies that the series is non-stationary. Everyone uses the Augmented version, so we will focus on that.

Null Hypothesis (H₀): The time series is not stationary.

Alternative Hypothesis (H₁): The time series is stationary.

If the p-value from the test is less than a chosen significance level (e.g., 0.05), we reject the null hypothesis and conclude that the time series is stationary.

Stationarity simplifies the analysis of time series data because forecasting models (e.g., ARIMA) assume stationarity for reliable predictions. If the time series is stationary, then the statistical relationships between time points remain stable over time.

If a series is non-stationary, we can often transform it into a stationary series using differencing, log transformations, or other techniques.

#### Augmented Dickey-Fuller (ADF) Test
The Augmented Dickey-Fuller Test is an extension of the Dickey-Fuller Test. It adds lagged difference terms to account for autocorrelation in the time series, making the test more robust.

The test equation is:


This looks scary, but it isn't that bad.

#### Implementing the Dickey-Fuller Test
To perform the Dickey-Fuller test, we can use the adfuller function from the statsmodels package.

Python Code for the Augmented Dickey-Fuller Test:


#### Interpreting the Results
ADF test produces the ADF Statistic which we compare it with the critical values at different significance levels (1%, 5%, 10%) --- just like we the alpha value from a t-test.

We assume the series is not statioary. So if the p-value is less than the significance level (e.g., 0.05), then we reject the null hypothesis and conclude that the series is (in fact) stationary.

The critical values represent thresholds for rejecting the null hypothesis at specific confidence levels.

#### Transforming a Non-Stationary Series
If the test indicates that the series is non-stationary, you can transform it to stationarity. My favorite ways of dealing with non-stationarity are differencing and log transformation.

1.  [Differencing: Subtract consecutive values to remove trends.]
2.  [Log Transformation: Apply a logarithmic transformation to stabilize the variance.]


#### Benefits and Drawbacks of the Dickey-Fuller Test
ADF is something you should know and use. It is a formal statistical test for stationarity with easy to interpret with clear p-value thresholds. But it is not sufficient by itself.

ADF is a statistical test and like most statistical tests it struggles with very large, noisy, or complex datasets. It is also sensitive to the choice of lag length which can cause it to overfit or underfit the model. It also assumes linear relationships; non-linear trends require different tests.

#### Next Steps
The Dickey-Fuller Test is a tool for evaluating time series stationarity, which is a prerequisite for many forecasting models. If the series is not stationarity, then we can apply methods of transforming the data like differencing. Python's statsmodels library makes it easy to test and determine whether your time series meets stationarity requirements.

#### Bee example (continued)
You decide to test if hive weight is stationary or contains a trend. If not stationary, apply differencing to remove trends.


#### Related Posts
This article is part of a series of posts on time series forecasting. Here is the list of articles in the order they were designed to be read.

1.  [[Time Series for Business Analytics with Python](https://medium.com/@kylejones_47003/time-series-for-business-analytics-with-python-a92b30eecf62?source=your_stories_page-------------------------------------)]
2.  [[Time Series Visualization for Business Analysis with Python](https://medium.com/@kylejones_47003/time-series-visualization-for-business-analysis-with-python-5df695543d4a?source=your_stories_page-------------------------------------)]
3.  [[Patterns in Time Series for Forecasting](https://medium.com/@kylejones_47003/patterns-in-time-series-for-forecasting-8a0d3ad3b7f5?source=your_stories_page-------------------------------------)]
4.  [[Imputing Missing Values in Time Series Data for Business Analytics with Python](https://medium.com/@kylejones_47003/imputing-missing-values-in-time-series-data-for-business-analytics-with-python-b30a1ef6aaa6?source=your_stories_page-------------------------------------)]
5.  [[Measuring Error in Time Series Forecasting with Python](https://medium.com/@kylejones_47003/measuring-error-in-time-series-forecasting-with-python-18d743a535fd?source=your_stories_page-------------------------------------)]
6.  [[Univariate and Multivariate Time Series Analysis with Python](https://medium.com/@kylejones_47003/univariate-and-multivariate-time-series-analysis-with-python-b22c6ec8f133?source=your_stories_page-------------------------------------)]
7.  [[Feature Engineering for Time Series Forecasting in Python](https://medium.com/@kylejones_47003/feature-engineering-for-time-series-forecasting-in-python-7c469f69e260?source=your_stories_page-------------------------------------)]
8.  [[Anomaly Detection in Time Series Data with Python](https://medium.com/@kylejones_47003/anomaly-detection-in-time-series-data-with-python-5a15089636db?source=your_stories_page-------------------------------------)]
9.  [[Dickey-Fuller Test for Stationarity in Time Series with Python](https://medium.com/@kylejones_47003/dickey-fuller-test-for-stationarity-in-time-series-with-python-4e4bf1953eed?source=your_stories_page-------------------------------------)]
10. [[Using Classification Model for Time Series Forecasting with Python](https://medium.com/@kylejones_47003/using-classification-model-for-time-series-forecasting-with-python-d74a1021a5c4?source=your_stories_page-------------------------------------)]
11. [[Measuring Error in Time Series Forecasting with Python](https://medium.com/@kylejones_47003/measuring-error-in-time-series-forecasting-with-python-18d743a535fd?source=your_stories_page-------------------------------------)]
12. [[Physics-informed anomaly detection in a wind turbine using Python with an autoencoder transformer](https://medium.com/@kylejones_47003/physics-informed-anomaly-detection-in-a-wind-turbine-using-python-with-an-autoencoder-transformer-06eb68aeb0e8?source=your_stories_page-------------------------------------)]

I redid this analysis using EIA energy generation data.
