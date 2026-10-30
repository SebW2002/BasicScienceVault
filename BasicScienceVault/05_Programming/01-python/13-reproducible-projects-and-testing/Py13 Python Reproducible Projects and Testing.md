---
aliases: [Python Project Structure, requirements.txt, environment.yml, pytest, Python Logging, Virtual Environments]
tags: [programming, python, reproducibility, testing, environments, type/overview, neuro]
---
# Py13 Python Reproducible Projects and Testing

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py13 Python Reproducible Projects and Testing - Worksheet|✏️ Worksheet]] · [[Py13 Python Reproducible Projects and Testing - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
"It worked on my laptop last year" is not a method. A reproducible project has a **predictable structure**, a **recorded environment** (which packages, which versions), **tests** that check the code still computes what you think, **logs** that record what happened, and **documentation**. The general principles are in [[CS13 Reproducibility and Research Software]]; this is the Python toolkit.

## Project structure
```text
eeg-oddball/
├── README.md              # what, how to run, where data come from
├── pyproject.toml         # package metadata + dependencies (modern standard)
├── requirements.txt       # or: pinned pip dependencies
├── environment.yml        # or: conda environment
├── config.yaml            # parameters (filter limits, paths relative to the root)
├── src/oddball/           # your importable code
│   ├── __init__.py
│   ├── preprocessing.py
│   └── stats.py
├── scripts/               # thin entry points: 01_preprocess.py, 02_erp.py, 03_figures.py
├── notebooks/             # exploration only
├── tests/
│   └── test_preprocessing.py
├── data/raw/              # read-only, often not in git
├── data/derived/
└── figures/
```
- **Logic in functions inside `src/`**, scripts only call them. Install your own package in editable mode (`pip install -e .`) so `import oddball` works everywhere.
- **Parameters in a config file**, not scattered through the code.
- Numbered scripts make the order obvious; a `Makefile`/`snakemake` can run the whole chain.
- **git** for code (not for large data; use DataLad/git-annex or DANDI/OpenNeuro for those; [[CS13 Reproducibility and Research Software]]).

## Recording the environment
**requirements.txt (pip)** – version numbers here are only examples:
```text
numpy==2.3.4
scipy==1.16.2
mne==1.10.1
```
`pip freeze > requirements.txt` records **everything installed** (exact versions); `pip install -r requirements.txt` recreates it. Hand-written files list only direct dependencies, often with minimum versions (`mne>=1.8`): flexible, but less exact.

**environment.yml (conda/mamba):**
```yaml
name: oddball
channels: [conda-forge]
dependencies:
  - python=3.12
  - numpy=2.3
  - mne=1.10
  - pip
  - pip:
      - autoreject==0.4.3
```
`conda env create -f environment.yml`; export with `conda env export --from-history`. Conda also manages non-Python libraries (compilers, HDF5, MKL).

**Virtual environments (briefly):** one isolated environment per project (`python -m venv .venv`, `conda create -n …`, or `uv venv`) so projects with different versions don't interfere. Never install research packages into the system Python. **Lock files** (`uv.lock`, `conda-lock`) pin every transitive dependency for exact rebuilds; containers (Docker/Apptainer) go further and fix the operating system too.

## Unit tests with pytest
A **unit test** calls a function with an input whose correct output you know and checks the result.
```python
# tests/test_preprocessing.py
import numpy as np
import pytest
from oddball.preprocessing import baseline_correct, samples_to_ms

def test_samples_to_ms():
    assert samples_to_ms(500, fs=1000) == 500

def test_baseline_removes_mean():
    rng = np.random.default_rng(0)
    x = rng.normal(5, 1, size=(10, 200))
    y = baseline_correct(x, n_base=50)
    np.testing.assert_allclose(y[:, :50].mean(axis=1), 0, atol=1e-12)

def test_rejects_negative_fs():
    with pytest.raises(ValueError):
        samples_to_ms(10, fs=-1)

@pytest.mark.parametrize("f", [5, 10, 40])
def test_welch_peak(f):
    ...   # a pure sine of frequency f must give a PSD peak at f
```
Run with `pytest` in the project root: it finds files `test_*.py` and functions `test_*`.
- **What to test in science code:** known analytical results (exponential decay → τ, sine → spectral peak), invariants (baseline mean = 0, probabilities sum to 1, output shapes), edge cases (empty input, NaN, one trial), and bugs you've fixed (**regression tests**).
- Compare floats with `np.testing.assert_allclose` / `pytest.approx`, never `==`.
- Tests on **synthetic data** with known ground truth (simulated spikes with a known rate) are the best check of an analysis pipeline.
- Run tests automatically on every push (GitHub Actions: continuous integration).

## Logging instead of print
```python
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logs/preprocess.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger.info("sub-01: %d bad channels interpolated", n_bad)
logger.warning("sub-07: only %d trials left after rejection", n_trials)
logger.error("sub-12: file not found")
```
- Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL; set the threshold once, keep the messages in the code.
- Logs go to a **file** with timestamps, so a batch run over 40 subjects leaves a record of what happened to each – `print` output vanishes.
- Also log versions (`mne.sys_info()`, `np.__version__`), parameters and the git commit.

## Documentation with docstrings
```python
def baseline_correct(x, n_base):
    """Subtract the mean of the first `n_base` samples from each trial.

    Parameters
    ----------
    x : ndarray, shape (n_trials, n_times)
        Epoched data.
    n_base : int
        Number of baseline samples at the start of each epoch.

    Returns
    -------
    ndarray, shape (n_trials, n_times)
        Baseline-corrected copy of `x`.
    """
    return x - x[:, :n_base].mean(axis=1, keepdims=True)
```
**NumPy docstring style** is standard in scientific Python (MNE, SciPy); tools like Sphinx turn it into web documentation. State shapes, units and what is modified in place. The README explains the project; docstrings explain functions; comments explain *why*.

## Same idea in R and MATLAB
R: RStudio Projects + `here`, `renv.lock`, `testthat` ([[R11 R Reproducible Projects]]). MATLAB: projects, `matlab.unittest`, Git integration ([[MAT12 MATLAB Reproducible Projects]]).

## In neuroscience #neuro
- **Pipelines run on clusters** over many subjects: logs and tests are the only way to know that all 40 subjects were processed correctly.
- **Software versions change results:** filter defaults, ICA implementations and spike sorter versions differ – record them in the methods section (from your environment file).
- **Ground-truth tests:** simulate a recording with spikes at known times (e.g. with Brian2 or SpikeInterface's generators) and check that your pipeline recovers them.
- **BIDS derivatives** + a config file + the code at a tagged git commit = a reproducible analysis that reviewers can rerun.

## Math links #math-link
- Analytical results as test oracles (e.g. $V(\tau) = V_\infty + (V_0 - V_\infty)e^{-1}$) → [[B2 Exponential Functions]], [[B10 Differential Equations]]
- Float tolerance in comparisons → [[Prog00 Shared Programming Concepts]]

## Connections
- Principles (git, containers, FAIR, preregistration) → [[CS13 Reproducibility and Research Software]]
- Seeds and paths → [[Prog00 Shared Programming Concepts]]
- Functions and docstrings → [[Py01 Python Basics and Syntax]], [[Py03 Python Control Flow and Functions]]
- Same in other languages → [[R11 R Reproducible Projects]], [[MAT12 MATLAB Reproducible Projects]]
- Documentation formats → [[Doc01 Markdown Syntax]] (README)

## Key takeaways
- Standard layout: `src/` code, `scripts/` entry points, `tests/`, `data/raw` read-only, config file.
- Record the environment (`requirements.txt`, `environment.yml`, lock file); one environment per project.
- pytest: small tests with known answers, tolerances for floats, regression tests for fixed bugs.
- `logging` to files instead of `print`; NumPy-style docstrings with shapes and units.
