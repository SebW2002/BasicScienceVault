---
aliases: [Python Basics, Python Syntax, Jupyter, f-strings, Docstrings]
tags: [programming, python, syntax, jupyter, type/overview, neuro]
---
# Py01 Python Basics and Syntax

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py01 Python Basics and Syntax - Worksheet|✏️ Worksheet]] · [[Py01 Python Basics and Syntax - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
Python is the most widely used language in computational neuroscience: MNE, Nilearn, SpikeInterface, PsychoPy and PyTorch are all Python. Its syntax is small, but two things trip up people coming from R or MATLAB: **indentation is part of the syntax**, and **indexing starts at 0** ([[Prog00 Shared Programming Concepts]]).

## Interpreter, scripts, notebooks
| Way to run | What it is | Good for |
|---|---|---|
| **Interactive interpreter** (`python`, IPython) | type a line, see the result | quick checks |
| **Script** (`analysis.py`, run with `python analysis.py`) | a file executed top to bottom | pipelines, batch jobs, anything you rerun |
| **Jupyter notebook** (`.ipynb`) | cells of code, output and Markdown text | exploring data, teaching, figures with explanations |

- **Python is interpreted:** the interpreter reads and executes your code line by line; there is no separate compile step.
- **Notebook trap:** cells can be run in any order, so the state in memory may not match the code you see. Before trusting a result: *Kernel → Restart & Run All*. Move finished analysis code into `.py` files and import it.
- In VS Code, `# %%` lines turn a script into runnable cells, combining both worlds.

## Indentation as syntax, comments, docstrings
```python
def mean_rate(counts, duration):
    """Return the mean firing rate in Hz.

    counts   : list of spike counts per trial
    duration : trial duration in seconds
    """
    total = 0
    for c in counts:          # the loop body is indented
        total += c
    return total / (len(counts) * duration)   # back at function level
```
- A colon `:` opens a **block**; everything indented under it (4 spaces by convention) belongs to it. Dedenting ends the block. No braces, no `end`.
- Mixing tabs and spaces → `TabError`; wrong indentation → `IndentationError`, or worse, **valid code that does something else** (a line accidentally outside the loop).
- `#` starts a comment. Comment *why*, not *what*.
- A **docstring** (`"""..."""` as first statement of a function, class or module) is the official documentation; `help(mean_rate)` shows it. Common formats: NumPy style, Google style ([[Py13 Python Reproducible Projects and Testing]]).

## Numbers, strings, Booleans
```python
n = 42            # int: unlimited precision
fs = 1000.0       # float: 64-bit double
z = 3 + 4j        # complex (j, not i!) → abs(z) == 5.0
7 / 2             # 3.5   true division always gives a float
7 // 2            # 3     floor division
7 % 2             # 1     remainder (modulo)
2 ** 10           # 1024  power (not ^ ! ^ is bitwise XOR)
```
- **Strings** are text in `'...'` or `"..."`; they are immutable sequences: `"theta"[0] == "t"`, `"theta"[-1] == "a"`, `len("theta") == 5`, `"sub-" + "01"`, `"ab" * 3 == "ababab"`. Useful methods: `.upper()`, `.split("_")`, `.replace()`, `.startswith()`, `.zfill(3)` (`"7".zfill(3) == "007"`).
- **Booleans:** `True`, `False` (capitalised); operators `and`, `or`, `not`; comparisons `==`, `!=`, `<`, `<=`; chained comparisons `0.15 <= rt <= 2`.
- **Truthiness:** `0`, `0.0`, `""`, `[]`, `None` count as false in `if`.
- **None** means "no value" (not the same as NaN, which is a float).
- **Type conversion:** `int("3")`, `float("0.5")`, `str(12)`, `int(3.9) == 3` (truncates).

## f-strings for output
```python
subj, rate, p = 7, 12.3456, 0.00042
print(f"sub-{subj:02d}: rate = {rate:.1f} Hz, p = {p:.2e}")
# sub-07: rate = 12.3 Hz, p = 4.20e-04
print(f"{rate=}")      # debugging shortcut → rate=12.3456
```
Format spec after `:` – `.2f` (2 decimals), `.3g` (3 significant digits), `.1%` (percent), `05d` (zero-padded integer), `>8` (right-aligned in width 8), `,` (thousands separator).

## Same idea in R and MATLAB
| Python | R | MATLAB |
|---|---|---|
| indentation defines blocks | `{ }` | `end` |
| `#` comment | `#` | `%` |
| `**` power | `^` | `^` (matrix) / `.^` (element-wise) |
| `7 // 2`, `7 % 2` | `7 %/% 2`, `7 %% 2` | `floor(7/2)`, `mod(7, 2)` |
| f-string | `sprintf("%.1f", x)`, `glue` | `sprintf("%.1f", x)` |
| `help(f)` | `?f` | `help f`, `doc f` |
→ [[R01 R Basics and Syntax]], [[MAT01 MATLAB Basics and Syntax]]

## In neuroscience #neuro
- **File names from loops:** `f"sub-{i:02d}_task-rest_eeg.edf"` builds BIDS-style names ([[CS05 Data Formats and Representation]]).
- **Notebooks** are standard for exploring a recording; the final pipeline should be scripts so it can run on a cluster.
- **Integer division bug:** converting a time to a sample index needs an int: `idx = int(round(t * fs))`; using `t * fs` directly gives a float, which can't index arrays.
- **Complex numbers** appear as FFT outputs: `abs()` gives amplitude, `np.angle()` the phase ([[E2 Complex Numbers]], [[B12 Fourier Analysis]]).

## Math links #math-link
- Powers and scientific notation (`1e-3`) → [[A1 Exponent Rules]]
- Floor division and modulo (sample → cycle number and phase within a cycle) → [[A5 Fractions]]
- Complex numbers `3 + 4j` → [[E2 Complex Numbers]]

## Connections
- Shared concepts (types, indexing, floats) → [[Prog00 Shared Programming Concepts]]
- Next: collections → [[Py02 Python Data Structures]]; control flow → [[Py03 Python Control Flow and Functions]]
- Notebooks and literate programming in other tools → [[R10 R Markdown and Quarto]], [[MAT11 MATLAB Live Scripts and Reports]]
- Markdown cells in Jupyter → [[Doc01 Markdown Syntax]], [[Doc02 Math in Markdown]]

## Key takeaways
- Scripts for pipelines, notebooks for exploration; restart & run all before trusting a notebook.
- Indentation defines blocks; 4 spaces; colon opens a block.
- `/` always gives a float, `//` floors, `**` is power (never `^`).
- f-strings: `f"{x:.2f}"`; docstrings document functions.
