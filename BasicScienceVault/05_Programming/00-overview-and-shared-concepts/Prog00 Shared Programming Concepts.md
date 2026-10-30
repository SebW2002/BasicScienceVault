---
aliases: [Shared Programming Concepts, Programming Basics, Programmier-Grundlagen, Vectorization, Indexing, NaN and NA, Working Directory]
tags: [programming, shared-concepts, vectorization, indexing, missing-values, reproducibility, type/overview, neuro]
---
# Prog00 Shared Programming Concepts

> [[MOC-programming|↑ Programming MOC]] · [[Prog00 Shared Programming Concepts - Worksheet|✏️ Worksheet]] · [[Prog00 Shared Programming Concepts - Solutions|✅ Solutions]] · [[Mistakes - Programming Basics|⚠️ Mistake log]]

## Why this matters
Python, R and MATLAB look different, but they are built from the **same eight ideas**: variables and types, indexing, loops and conditions, functions, vectorisation, missing values, reproducibility and paths. If these sit, switching languages is mostly learning new spelling. Most bugs in analysis scripts come from exactly these places: an off-by-one index, a NaN that silently propagates, a path that only works on your laptop.

## 1 · Variables and data types
A **variable** is a name bound to a value. The **type** says what the value is and what you can do with it.

| Concept | Python | R | MATLAB |
|---|---|---|---|
| assign | `x = 3` | `x <- 3` | `x = 3;` |
| integer / float | `3` (int), `3.0` (float) | `3L` (integer), `3` (double!) | `3` is a double; `int32(3)` |
| string | `"spike"` | `"spike"` (a character vector) | `"spike"` (string), `'spike'` (char array) |
| logical | `True`, `False` | `TRUE`, `FALSE` | `true`, `false` |
| array / vector | `np.array([1, 2, 3])` | `c(1, 2, 3)` | `[1 2 3]` |
| check the type | `type(x)` | `class(x)`, `typeof(x)` | `class(x)` |

- **Floating-point numbers** are stored in binary with ~16 significant digits: `0.1 + 0.2 == 0.3` is **false** in all three languages. Compare with a tolerance: $\lvert a - b\rvert < 10^{-9}$ (see [[CS05 Data Formats and Representation]]).
- **Integers can overflow** in fixed-size types: an `int16` ADC sample holds −32768 … 32767; adding two large samples can wrap around.
- **Dynamic typing:** in all three, a variable's type comes from its current value (`x = 3`, then `x = "three"` works). Convenient, but type errors only appear at run time.

## 2 · Indexing: 0-based vs. 1-based
| | Python (NumPy) | R | MATLAB |
|---|---|---|---|
| first element | `x[0]` | `x[1]` | `x(1)` |
| last element | `x[-1]` | `x[length(x)]` | `x(end)` |
| elements 2–4 (1-based counting) | `x[1:4]` (**stop excluded**) | `x[2:4]` (both included) | `x(2:4)` (both included) |
| negative index | counts from the end | **removes** that element | error |
| matrix element row 2, col 3 | `A[1, 2]` | `A[2, 3]` | `A(2, 3)` |

**Python's half-open ranges** `[start, stop)`: `x[a:b]` has `b − a` elements, and `x[:k]` + `x[k:]` is the whole array without overlap. This makes off-by-one errors rarer *once you think in it*, but translating code between languages is where they creep in.

> [!example] Sample index ↔ time
> Sampling rate $f_s = 1000$ Hz, time of sample $k$: Python $t = k/f_s$ (sample 0 at $t = 0$); R/MATLAB $t = (k - 1)/f_s$ (sample 1 at $t = 0$). The window 100–200 ms is `x[100:200]` in Python (100 samples) but `x(101:200)` in MATLAB.

## 3 · Loops and conditions
```text
for each item in a collection:        while condition is true:
    do something with item                do something (and change the condition!)

if condition:          # evaluates to a single TRUE/FALSE
    ...
else:
    ...
```
- **for** when you know what to iterate over (trials, subjects, files); **while** when you stop on a condition (until convergence, until a key is pressed).
- A `while` loop must change something that ends it, otherwise it runs forever.
- **Logical operators:** and/or/not are `and or not` (Python), `&& || !` (R, MATLAB, scalar) and `& |` (element-wise on arrays in R/MATLAB/NumPy).
- `if` needs **one** truth value. `if x > 0` with a vector `x` is an error in R (≥ 4.2) and in Python/NumPy ("truth value of an array is ambiguous"); MATLAB treats it as "all elements true". Use `any()` / `all()` explicitly.

## 4 · Functions: inputs, outputs, scope
A **function** packages a computation: inputs (arguments) → body → output (return value).
```python
def firing_rate(n_spikes, duration_s):      # Python
    return n_spikes / duration_s
```
```r
firing_rate <- function(n_spikes, duration_s) n_spikes / duration_s   # R: last value is returned
```
```matlab
function r = firing_rate(n_spikes, duration_s)   % MATLAB: output variable named in the header
    r = n_spikes ./ duration_s;
end
```
- **Scope:** variables created inside a function are **local**; they vanish when it returns. A function should get everything it needs through its arguments and give results back through its return value, not through global variables.
- **Pure functions** (same input → same output, no side effects) are easy to test and reuse ([[Py13 Python Reproducible Projects and Testing]]).
- **Mathematically**, a function is exactly a mapping $f: D\to W$ ([[B1 Properties of Functions]]); composition `g(f(x))` is $g\circ f$.

## 5 · Vectorisation: the most important way of thinking
**Vectorisation** = writing an operation for the **whole array** instead of looping over elements.
```python
# loop (slow, long)                     # vectorised (fast, close to the maths)
z = np.empty(len(x))
for i in range(len(x)):
    z[i] = (x[i] - mu) / sd             z = (x - mu) / sd
```
- **Why faster:** the loop over elements runs in compiled C/Fortran code (NumPy, R internals, MATLAB's engine) instead of the interpreter. Typical speed-ups are 10–100×.
- **Why clearer:** the code looks like the formula: $z = \frac{x - \mu}{\sigma}$, $\bar x = \frac1n\sum x_i$ ([[A7 Sums Products and Factorials]]), $\mathbf y = A\mathbf x$ ([[C1 Matrices]]).
- **Building blocks:** element-wise arithmetic, comparisons that give logical arrays, logical indexing (`x[x > 0]`), aggregations along an axis (`mean`, `sum`), cumulative functions (`cumsum`), matrix products.
- **Broadcasting / recycling:** combining arrays of different shapes, e.g. subtracting a per-channel mean (channels × 1) from a channels × time matrix. NumPy and MATLAB broadcast by shape rules; R **recycles** the shorter vector (with a warning only if lengths don't divide).
- Loops are still fine for things that are inherently sequential (a simulation where step $t+1$ depends on step $t$, [[B10 Differential Equations]]) and for looping over **files or subjects**.

## 6 · Missing values: NaN and NA
| | Python | R | MATLAB |
|---|---|---|---|
| missing number | `np.nan` (float) | `NA` (any type), `NaN` (numeric) | `NaN` |
| missing in tables | `NaN` / `pd.NA`, `None` | `NA` | `NaN`, `missing`, `<undefined>` |
| test | `np.isnan(x)`, `pd.isna(x)` | `is.na(x)` | `isnan(x)`, `ismissing(x)` |
| mean ignoring missing | `np.nanmean(x)`; pandas `.mean()` skips by default | `mean(x, na.rm = TRUE)` | `mean(x, "omitnan")` |

- **NaN propagates:** any arithmetic with NaN gives NaN, so `mean([1, 2, NaN])` is NaN. That is a feature: you notice.
- **NaN is not equal to anything, not even itself:** `NaN == NaN` is false. Never test `x == NaN`; use `isnan`/`is.na`.
- **Silent defaults differ:** pandas skips NaN in `.mean()` by default, NumPy does not. Know which one you're using.
- **Don't code missing values as 0 or −999.** A missing reaction time is not a 0 ms reaction time. Why values are missing matters (MCAR/MAR/MNAR, [[CS06 Data Science Workflow]]).

## 7 · Reproducibility: scripts instead of clicks, seeds for random numbers
- **A script is a record.** Every step from raw data to figure should be code that someone else (or you in a year) can rerun. Clicking through a GUI leaves no trace unless the tool logs a script (EEGLAB's `EEG.history`, PsychoPy Builder's generated code).
- **Never edit raw data.** Read raw → write derived files to a separate folder.
- **Random seeds:** pseudo-random generators are deterministic given a seed. Fix the seed (`np.random.default_rng(42)`, `set.seed(42)`, `rng(42)`) so permutation tests, bootstraps, train/test splits and simulations give the same numbers every run, and **report it**.
- **Record versions** of the language and packages ([[Py13 Python Reproducible Projects and Testing]], [[R11 R Reproducible Projects]], [[MAT12 MATLAB Reproducible Projects]]).
- The bigger picture (git, containers, FAIR, preregistration) → [[CS13 Reproducibility and Research Software]].

## 8 · Paths, working directory, relative vs. absolute
- The **working directory** (WD) is where your program "stands". Relative paths start from there. Check it: `os.getcwd()` / `Path.cwd()`, `getwd()`, `pwd`.
- **Absolute path:** from the root, `/Users/anna/project/data/sub-01.csv` or `C:\Users\anna\...`. Works from anywhere, but only on *that* computer.
- **Relative path:** `data/sub-01.csv` or `../data/sub-01.csv` (`..` = one folder up). Works on every computer, as long as the program starts in the project folder.
- **Rule:** inside a project, use paths **relative to the project root**, built with path functions (`pathlib.Path("data") / "sub-01.csv"`, `here::here("data", "sub-01.csv")`, `fullfile("data", "sub-01.csv")`) instead of gluing strings with `/` or `\`. Never `setwd()`/`cd` to an absolute path at the top of a shared script.
- Typical project layout:
```text
my-project/
├── data/raw/          # never modified
├── data/derived/      # produced by code
├── code/
├── figures/
└── README.md
```
(BIDS for neuroimaging data structure → [[CS05 Data Formats and Representation]].)

## In neuroscience #neuro
- **EEG data** are a channels × time matrix; re-referencing to the average reference is one vectorised line: subtract the mean across channels from every channel (broadcasting).
- **Spike trains:** bin spike times into counts with a histogram function instead of a loop; firing rate = counts / bin width.
- **Trial exclusion:** a logical mask `rt > 0.15 & rt < 2` selects valid trials in all three languages.
- **Missing trials** (no response, artefact rejected) must be NaN/NA, not 0, or every average is wrong.
- **Permutation tests and bootstrap CIs** ([[CS02 Probability and Statistics]]) depend on random numbers: without a seed, the p-value changes on every run.
- **Off-by-one in event times** shifts every epoch by one sample (1 ms at 1 kHz). It's a subtle, common bug when moving between Python and MATLAB/EEGLAB.

## Math links #math-link
- Vectorised sums and means $\sum_i x_i$ → [[A7 Sums Products and Factorials]]
- Arrays as vectors and matrices, broadcasting as adding a vector to each column → [[C1 Matrices]], [[D1 Vectors in 2D and 3D]]
- Functions as mappings, composition → [[B1 Properties of Functions]]
- Logical masks as sets, `&`/`|` as $\cap$/$\cup$ → [[E1 Sets Logic and Quantifiers]]
- Sequential simulation (Euler steps) → [[B10 Differential Equations]]

## Connections
- In Python → [[Py01 Python Basics and Syntax]], [[Py03 Python Control Flow and Functions]], [[Py05 NumPy and Arrays]]
- In R → [[R01 R Basics and Syntax]], [[R02 R Data Structures and Vectorization]], [[R03 R Control Flow and Functions]]
- In MATLAB → [[MAT01 MATLAB Basics and Syntax]], [[MAT02 MATLAB Matrices and Vectorization]], [[MAT03 MATLAB Control Flow and Functions]]
- Data types, floats, file formats → [[CS05 Data Formats and Representation]]
- Missing data mechanisms → [[CS06 Data Science Workflow]]
- Reproducibility in general → [[CS13 Reproducibility and Research Software]]

## Key takeaways
- Python counts from **0** with half-open slices; R and MATLAB count from **1** with inclusive ranges.
- Think in **whole arrays**: element-wise operations, logical masks, aggregations along an axis.
- NaN/NA propagate and are never `==` anything; check how each function treats them.
- Scripts + seeds + recorded versions = reproducible results.
- Use project-relative paths built with path functions.
