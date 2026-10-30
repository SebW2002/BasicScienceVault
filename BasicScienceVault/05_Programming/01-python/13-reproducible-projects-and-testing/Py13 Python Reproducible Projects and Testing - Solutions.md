---
tags: [programming, python, reproducibility, type/solution]
---
# Py13 Python Reproducible Projects and Testing – Solutions

> Worksheet: [[Py13 Python Reproducible Projects and Testing - Worksheet]] · Theory: [[Py13 Python Reproducible Projects and Testing]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. `data/raw/`: original recordings, never modified. `data/derived/`: everything produced by code. `src/`: importable functions (the logic). `scripts/`: short entry points that call `src` functions in order. `tests/`: test files.
2. `pip freeze` records **all** installed packages with exact versions (exact rebuild, but includes things you don't really depend on and may be platform-specific). A hand-written file lists only direct dependencies with ranges (flexible, but different installs may get different versions).
3. It collects files named `test_*.py` or `*_test.py` and runs functions named `test_*` (and methods in classes `Test*`).
4. DEBUG < INFO < WARNING < ERROR < CRITICAL.

## Level 2
5. Functions can be imported, tested, reused across scripts and run in batch on a cluster; notebooks have hidden state and out-of-order execution, and their code is hard to test or diff in git.
6. Float rounding: the mean will be something like `1e-17`, not exactly 0. Use `np.testing.assert_allclose(np.mean(x), 0, atol=1e-12)` or `pytest.approx`.
7. A timestamped file entry for each subject (started, finished, warnings, the error message and traceback for subject 23), so you'd know what failed and why without rerunning.
8. Different package versions (ICA algorithm/defaults changed) and no fixed random seed (ICA starts from random initial values). Fix: pinned environment file/lock file, `random_state=` set and recorded.

## Level 3
9. ```python
   import pytest
   from mytools.rates import firing_rate
   def test_rate_simple():
       assert firing_rate([0.1 * i for i in range(10)], t_stop=2.0) == pytest.approx(5.0)
   def test_rate_empty():
       assert firing_rate([], t_stop=2.0) == 0.0
   ```
10. ```python
    def epoch(x, events, tmin, tmax, fs):
        """Cut continuous data into epochs around events.

        Parameters
        ----------
        x : ndarray, shape (n_channels, n_times)
            Continuous data.
        events : array of int, shape (n_events,)
            Event sample indices (0-based).
        tmin, tmax : float
            Epoch start and end relative to each event, in seconds.
        fs : float
            Sampling rate in Hz.

        Returns
        -------
        ndarray, shape (n_events, n_channels, n_samples)
            Epoched data (a copy); n_samples = round((tmax - tmin) * fs) + 1.
        """
    ```
11. ```python
    import numpy as np
    def test_exp_fit_recovers_tau():
        t = np.linspace(0, 0.2, 2001)
        v = -70 + 10 * np.exp(-t / 0.020)
        tau_hat = exp_fit(t, v)
        assert tau_hat == pytest.approx(0.020, rel=0.01)
    ```

## Level 4
12. Parameters in a **config file** (change `l_freq`), logic in functions, numbered scripts or a workflow manager (`make`/`snakemake`) to rerun everything from raw data, outputs written to `derived/` (old results versioned or tagged in git).
13. Python version, versions of key packages (MNE, NumPy, SciPy, scikit-learn …), relevant non-default parameters, random seeds, link to the code (repository + commit/DOI). Source: environment file / `pip freeze` / `mne.sys_info()`, the config file and the git log.
14. ```text
    mytools/
    ├── pyproject.toml          # [project] name = "mytools"
    ├── src/mytools/__init__.py
    ├── src/mytools/rates.py    # def firing_rate(st, t_stop): return len(st) / t_stop
    └── tests/test_rates.py
    ```
    `pip install -e .` then `pytest` → 2 passed. Change the function to `len(st) * t_stop` → `test_rate_simple` fails with a clear message showing expected vs. actual value.
