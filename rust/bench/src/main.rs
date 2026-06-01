use dickey_fuller_test_for_stationarity_in_time_series_with_python_core::rolling_mean_std;

fn main() {
    let v: Vec<f64> = (0..8000).map(|i| (i as f64 * 0.01).sin()).collect();
    for _ in 0..500 {
        let _ = rolling_mean_std(&v, 24);
    }
}
