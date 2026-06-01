use dickey_fuller_test_for_stationarity_in_time_series_with_python_core::rolling_mean_std;
use numpy::{PyArray1, PyReadonlyArray1, IntoPyArray};
use pyo3::prelude::*;

#[pyfunction]
fn rolling_mean_std_py<'py>(
    py: Python<'py>,
    values: PyReadonlyArray1<f64>,
    window: usize,
) -> PyResult<(Bound<'py, PyArray1<f64>>, Bound<'py, PyArray1<f64>>)> {
    let (m, s) = rolling_mean_std(values.as_slice()?, window);
    Ok((m.into_pyarray(py), s.into_pyarray(py)))
}

#[pyfunction]
#[pyo3(signature = (values, window, iterations=500))]
fn bench_kernel_py(values: PyReadonlyArray1<f64>, window: usize, iterations: usize) -> PyResult<f64> {
    let buf = values.as_slice()?.to_vec();
    let start = std::time::Instant::now();
    for _ in 0..iterations {
        let _ = rolling_mean_std(&buf, window);
    }
    Ok(start.elapsed().as_secs_f64())
}

#[pymodule]
fn dickey_fuller_test_for_stationarity_in_time_series_with_python_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rolling_mean_std_py, m)?)?;
    m.add_function(wrap_pyfunction!(bench_kernel_py, m)?)?;
    Ok(())
}
