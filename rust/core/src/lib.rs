//! Rolling mean and standard deviation (sample std, ddof=1 like pandas).

pub fn rolling_mean_std(values: &[f64], window: usize) -> (Vec<f64>, Vec<f64>) {
    let n = values.len();
    let mut means = vec![f64::NAN; n];
    let mut stds = vec![f64::NAN; n];
    if window == 0 || n == 0 {
        return (means, stds);
    }
    for i in (window - 1)..n {
        let start = i + 1 - window;
        let slice = &values[start..=i];
        let m = slice.iter().sum::<f64>() / window as f64;
        means[i] = m;
        if window > 1 {
            let var = slice.iter().map(|v| (v - m).powi(2)).sum::<f64>() / (window - 1) as f64;
            stds[i] = var.sqrt();
        } else {
            stds[i] = 0.0;
        }
    }
    (means, stds)
}
