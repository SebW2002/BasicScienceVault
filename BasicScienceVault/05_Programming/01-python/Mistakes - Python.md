---
aliases: [Mistake Log Python, Fehler Python, Python Bugs]
tags: [programming, python, type/mistakes]
---
# ⚠️ Mistakes – Python

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · Template: [[Mistake Entry Template]]

**How to use:** after every worksheet – and every real bug that cost you more than 10 minutes – add a row to *My mistakes*: what you wrote, what's correct, and the quick check (a print, a shape, a test) that would have caught it.

## Classic traps (pre-filled)
| ❌ Wrong | ✅ Right | Quick check / why | Topic |
|---|---|---|---|
| `2 ^ 3` for a power | `2 ** 3` | `^` is XOR → 1 | [[Py01 Python Basics and Syntax]] |
| `x[1]` for the first element | `x[0]` | 0-based | [[Py01 Python Basics and Syntax]] |
| `x[100:200]` has 101 elements | 100 (stop excluded) | `len(x[a:b]) == b - a` | [[Py01 Python Basics and Syntax]] |
| `return` inside the loop | dedent to function level | test with ≥ 2 items | [[Py01 Python Basics and Syntax]] |
| `round(2.5) == 3` | `2` (round half to even) | – | [[Py01 Python Basics and Syntax]] |
| `b = a` to copy a list | `b = a.copy()` / `deepcopy` | `b is a` → True | [[Py02 Python Data Structures]] |
| `def f(x, acc=[])` | `acc=None`, create inside | call twice | [[Py02 Python Data Structures]] |
| `[1, 2] * 2` as vector maths | NumPy array | gives `[1, 2, 1, 2]` | [[Py02 Python Data Structures]] |
| `files.append(x)` assigned: `files = files.append(x)` | `files.append(x)` (returns None) | `files` becomes None | [[Py02 Python Data Structures]] |
| positional argument after keyword | positional first | `SyntaxError` | [[Py03 Python Control Flow and Functions]] |
| reusing an exhausted generator | recreate it / use a list | second `list(g)` is `[]` | [[Py03 Python Control Flow and Functions]] |
| `rt < 0.15` before checking `rt is None` | check `None` first | `TypeError` | [[Py03 Python Control Flow and Functions]] |
| file opened without `with` / encoding | `with open(p, encoding="utf-8")` | µ and ä garbled | [[Py04 Python Files and Data Formats]] |
| `pickle.load` on downloaded files | only own, trusted files | can run code | [[Py04 Python Files and Data Formats]] |
| csv module values used as numbers | `float(row["rt"])` | they're strings | [[Py04 Python Files and Data Formats]] |
| `(64, 5000) - (64,)` | `x - m[:, None]` or `keepdims=True` | broadcasting aligns from the right | [[Py05 NumPy and Arrays]] |
| `mean(axis=1)` to average trials of (trials, ch, t) | `axis=0` | axis = dimension that disappears | [[Py05 NumPy and Arrays]] |
| `(x > a) and (x < b)` on arrays | `(x > a) & (x < b)` | ambiguous truth value | [[Py05 NumPy and Arrays]] |
| `x > a & x < b` | parentheses: `(x > a) & (x < b)` | `&` binds stronger than `>` | [[Py05 NumPy and Arrays]] |
| modifying a slice thinking it's a copy | `.copy()` | slices are views | [[Py05 NumPy and Arrays]] |
| `np.std(x)` as sample SD | `np.std(x, ddof=1)` | pandas/R use n − 1 | [[Py05 NumPy and Arrays]] |
| summing raw `int16` data | `x.astype(float)` first | overflow wraps around | [[Py05 NumPy and Arrays]] |
| `np.linalg.inv(A) @ b` | `np.linalg.solve(A, b)` | accuracy, speed | [[Py05 NumPy and Arrays]] |
| `np.random.seed()` globally in libraries | `rng = np.random.default_rng(seed)` | pass `rng` around | [[Py05 NumPy and Arrays]] |
| chained assignment `df[mask]["rt"] = …` | `df.loc[mask, "rt"] = …` | no effect under Copy-on-Write | [[Py06 pandas and Tabular Data]] |
| merge on duplicated keys unnoticed | `validate="many_to_one"`, compare `len()` | rows multiply | [[Py06 pandas and Tabular Data]] |
| `.loc[0:2]` vs `.iloc[0:2]` confused | `.loc` label-inclusive, `.iloc` position-exclusive | 3 vs 2 rows | [[Py06 pandas and Tabular Data]] |
| trial-level CIs across subjects | aggregate per subject first | pseudoreplication | [[Py07 Python Plotting and Visualization]] |
| `jet` colour map, uncentred diverging map | viridis; symmetric `vmin/vmax` | false edges | [[Py07 Python Plotting and Visualization]] |
| `imshow` spectrogram upside down | `origin="lower"`, `extent=` | – | [[Py07 Python Plotting and Visualization]] |
| filter design without `fs=` | `butter(4, 40, fs=500)` | cut-off in Nyquist units | [[Py08 SciPy Scientific Computing]] |
| causal `lfilter` for ERP latencies | `filtfilt`/`sosfiltfilt` offline | phase shift moves peaks | [[Py08 SciPy Scientific Computing]] |
| `curve_fit` without `p0` | sensible starting values, check units | absurd τ | [[Py08 SciPy Scientific Computing]] |
| scaling/PCA/feature selection before CV | inside a `Pipeline` | leakage | [[Py09 Python Machine Learning Libraries]] |
| X as features × samples | samples × features | `X.shape[0] == len(y)` | [[Py09 Python Machine Learning Libraries]] |
| forgot `opt.zero_grad()` | call it every iteration | gradients accumulate | [[Py09 Python Machine Learning Libraries]] |
| evaluating without `model.eval()` | `eval()` + `no_grad()` | dropout still active | [[Py09 Python Machine Learning Libraries]] |
| MNE data assumed in µV | volts | 50 µV = 5e-5 | [[Py10 Python Neuroscience Packages]] |
| loading images inside the trial loop | preload before trials | dropped frames | [[Py11 PsychoPy Experiment Control]] |
| clock-based durations for brief stimuli | count frames | durations snap to refreshes | [[Py11 PsychoPy Experiment Control]] |
| RT clock reset before `flip()` | `win.callOnFlip(kb.clock.reset)` | up to one frame error | [[Py11 PsychoPy Experiment Control]] |
| forgot `self` in a method | `def step(self, …)` | `TypeError` about arguments | [[Py12 Python Object-Oriented Programming]] |
| `assert x.mean() == 0` | `assert_allclose(..., atol=…)` | floats | [[Py13 Python Reproducible Projects and Testing]] |
| `print` for batch-run diagnostics | `logging` to a file | output lost | [[Py13 Python Reproducible Projects and Testing]] |

## My mistakes
| Date | ❌ What I did | ✅ Correct | Why / quick check | Link |
|---|---|---|---|---|
| | | | | |

## Patterns I notice
- 
