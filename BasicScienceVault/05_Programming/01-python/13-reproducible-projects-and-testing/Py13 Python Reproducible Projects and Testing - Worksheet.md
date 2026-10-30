---
tags: [programming, python, reproducibility, type/worksheet]
---
# Py13 Python Reproducible Projects and Testing – Worksheet

> Theory: [[Py13 Python Reproducible Projects and Testing]] · Solutions: [[Py13 Python Reproducible Projects and Testing - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper. Run code only for tasks marked 💻.

## Level 1 – Recall
1. What belongs in `data/raw/`, `data/derived/`, `src/`, `scripts/` and `tests/`?
2. Difference between `pip freeze > requirements.txt` and a hand-written `requirements.txt` with `mne>=1.8`?
3. How does pytest find tests?
4. Order the logging levels from least to most severe.

## Level 2 – Understanding
5. Why should analysis logic live in functions in `src/` rather than in notebooks?
6. Why does `assert np.mean(x) == 0.0` make a bad test after baseline correction? What do you write instead?
7. Your pipeline ran over 40 subjects overnight with `print` statements. In the morning, subject 23 has no output. What would logging have given you?
8. Why might a colleague get different ICA components with "the same code"? Name two reasons and the fix.

## Level 3 – Write code
9. Write a pytest test for `firing_rate(spike_times, t_stop)` that checks: 10 spikes in 2 s → 5 Hz, and an empty spike list → 0 Hz.
10. Write a NumPy-style docstring for `epoch(x, events, tmin, tmax, fs)` that cuts continuous data `x` (channels × times) into epochs.
11. Write a test that checks a function `exp_fit(t, v)` recovers τ = 20 ms (within 1 %) from noise-free synthetic data $v(t) = -70 + 10e^{-t/\tau}$.

## Level 4 – Neuro transfer
12. A reviewer asks you to rerun your analysis with a different high-pass filter. Which project features make this a one-line change and a single command?
13. List what you would put in the methods section about software, and where you'd get the information.
14. 💻 Create a tiny project with `src/mytools/rates.py` (a `firing_rate` function), `tests/test_rates.py` (task 9) and run `pytest`. Then break the function on purpose and watch the test fail.
