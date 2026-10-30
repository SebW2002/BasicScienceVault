---
tags: [programming, python, type/worksheet]
---
# Py01 Python Basics and Syntax – Worksheet

> Theory: [[Py01 Python Basics and Syntax]] · Solutions: [[Py01 Python Basics and Syntax - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Predict the output
1. `7 / 2`, `7 // 2`, `-7 // 2`, `7 % 3`, `2 ** 3 ** 2`
2. `"gamma"[1:3]`, `"gamma"[-2:]`, `len("sub-01")`, `"7".zfill(3)`
3. `bool(0)`, `bool("0")`, `bool([])`, `0.15 <= 0.2 <= 2`
4. `int(3.99)`, `round(2.5)`, `round(3.5)`, `float("1e-3")`

## Level 2 – Syntax and formatting
5. What does `2 ^ 3` give in Python and why is it not 8?
6. Write an f-string that prints `sub-03 | 12.35 Hz | p = 3.1e-04` from `s = 3`, `r = 12.3456`, `p = 0.000312`.
7. Find the bug: the function should return the sum of all counts.
   ```python
   def total(counts):
       s = 0
       for c in counts:
           s += c
           return s
   ```
8. Name one situation where a Jupyter notebook gives a different result than running the same code as a script.

## Level 3 – Write code
9. Write a function `samples_to_ms(n, fs)` with a docstring that converts a number of samples to milliseconds.
10. Using `//` and `%`: a 10 Hz rhythm sampled at 1000 Hz has 100 samples per cycle. For sample index 1234, give the cycle number and the position within the cycle.
11. Given `fname = "sub-12_ses-02_task-nback_bold.nii.gz"`, write code that extracts the subject number `12` as an int.

## Level 4 – Neuro transfer
12. `t_event = 0.2537` s, `fs = 512` Hz. `x[t_event * fs]` raises an error. Why? Write the correct line.
13. An FFT coefficient is `c = 3 + 4j`. What are its amplitude and phase (in radians, as an expression)? Which Python functions give them?
14. 💻 Write a loop that prints the BIDS file names `sub-01_task-rest_eeg.edf` … `sub-12_task-rest_eeg.edf`, then run it.
