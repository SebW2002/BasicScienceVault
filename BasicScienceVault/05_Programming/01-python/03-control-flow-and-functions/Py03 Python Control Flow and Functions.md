---
aliases: [Python Control Flow, Python Functions, args kwargs, Lambda, Generators, yield]
tags: [programming, python, control-flow, functions, type/overview, neuro]
---
# Py03 Python Control Flow and Functions

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py03 Python Control Flow and Functions - Worksheet|✏️ Worksheet]] · [[Py03 Python Control Flow and Functions - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
Control flow decides **which code runs and how often**; functions decide **how code is organised**. A clean analysis is a sequence of small functions (`load → filter → epoch → average`) called in a loop over subjects. Python's argument system (defaults, keywords, `*args`, `**kwargs`) is also how every scientific library is called, so reading `mne.io.read_raw_edf(fname, preload=True, **kwargs)` requires knowing it.

## Conditions: if / elif / else
```python
if rt is None:
    status = "miss"
elif rt < 0.15:
    status = "anticipation"
elif rt > 2.0:
    status = "too slow"
else:
    status = "valid"
```
- Conditions are tested top to bottom; **only the first true branch** runs.
- One-line conditional expression: `label = "high" if power > thr else "low"`.
- `match`/`case` (Python ≥ 3.10) matches structured patterns; rarely needed in analysis code.

## Loops: for, while, break, continue
```python
for i, fname in enumerate(files):      # index and item
    ...
for ch, w in zip(channels, weights):   # walk two lists in parallel
    ...
for k in range(0, 1000, 100):          # 0, 100, …, 900
    ...
while not converged:                   # until a condition
    ...
```
- `break` leaves the loop immediately; `continue` skips to the next iteration.
- `for … else`: the `else` block runs only if the loop finished **without** `break` (useful for "searched and didn't find").
- `range(start, stop, step)` excludes `stop`, like slicing.
- Don't modify a list while looping over it; build a new one (comprehension).

## Functions
```python
def bandpower(x, fs, band=(8, 12), method="welch"):
    """Power of signal x in a frequency band."""
    ...
    return power

bandpower(x, 500)                       # defaults used
bandpower(x, 500, band=(4, 8))          # keyword argument
bandpower(x, fs=500, method="fft")      # any order with keywords
```
- **Positional** arguments are matched by order, **keyword** arguments by name. Keywords make calls self-documenting.
- **Defaults** are evaluated **once** at definition time: never use a mutable default (`[]`, `{}`) ([[Py02 Python Data Structures]]).
- A function without `return` returns `None`.
- Return several values as a tuple: `return mean, sd` → `m, s = stats(x)`.
- **Scope (LEGB):** Python looks a name up in **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in scope. Assigning inside a function creates a local variable.
- **Type hints** (optional) document intent: `def rate(n: int, T: float) -> float:`.

### *args and **kwargs
```python
def log(*args, **kwargs):
    print(args)     # tuple of extra positional arguments
    print(kwargs)   # dict of extra keyword arguments
log(1, 2, sub="01")        # (1, 2)  {'sub': '01'}

def my_plot(x, y, **kwargs):
    plt.plot(x, y, **kwargs)   # pass options through unchanged
my_plot(t, v, color="k", lw=0.5)
```
- `*` and `**` also **unpack** at call time: `f(*shape)`, `f(**params)` with `params = {"fs": 500}`.
- Order in a definition: positional, `*args`, keyword-only, `**kwargs`.

### Lambda functions
Anonymous one-expression functions, mainly as arguments to other functions:
```python
sorted(files, key=lambda f: int(f.split("-")[1][:2]))
sigmoid = lambda x: 1 / (1 + np.exp(-x))     # fine, but a def is clearer
```

## Generators and yield
A **generator** produces values one at a time, on demand, instead of building the whole list in memory:
```python
def epochs(signal, length):
    """Yield consecutive non-overlapping windows."""
    for start in range(0, len(signal) - length + 1, length):
        yield signal[start:start + length]

for win in epochs(x, 1000):    # one window at a time
    process(win)
```
- Calling a generator function returns a generator object; the body runs only when you iterate. After each `yield`, execution pauses and resumes at the next request.
- **Generator expression:** `(x**2 for x in data)`, like a list comprehension with `()`. `sum(x**2 for x in data)` never builds the list.
- A generator can be consumed **only once**.
- Use for **large data streamed from disk** (files, chunks of a long recording) and data loaders ([[Py09 Python Machine Learning Libraries]]).

## Same idea in R and MATLAB
| Python | R | MATLAB |
|---|---|---|
| `elif` | `else if` | `elseif` |
| `for x in xs:` | `for (x in xs) { }` | `for x = xs ... end` |
| `break`, `continue` | `break`, `next` | `break`, `continue` |
| defaults `def f(x, a=1)` | `function(x, a = 1)` | `arguments` block, or `nargin` checks |
| `*args, **kwargs` | `...` | `varargin`, name-value arguments |
| `lambda x: x**2` | `\(x) x^2` | `@(x) x.^2` |
→ [[R03 R Control Flow and Functions]], [[MAT03 MATLAB Control Flow and Functions]]

## In neuroscience #neuro
- **Batch loop over subjects** with `try/except` so one corrupted file doesn't stop the whole pipeline (log which failed):
  ```python
  for sub in subjects:
      try:
          run_pipeline(sub)
      except Exception as err:
          logger.error(f"{sub}: {err}")
  ```
- **Trial classification** (miss / anticipation / valid) is an `if/elif` chain – or, vectorised, `np.select` ([[Py05 NumPy and Arrays]]).
- **Simulation loops:** an integrate-and-fire neuron updated with Euler steps needs a `for` loop over time with an `if v >= v_th:` spike-and-reset condition ([[CS10 Dynamical and Computational Neuro Models]], [[B10 Differential Equations]]).
- **Generators** read a multi-hour recording chunk by chunk without loading 50 GB into memory ([[CS14 Hardware Essentials]]).
- `**kwargs` pass-through is how wrappers around MNE or matplotlib functions keep all options available.

## Math links #math-link
- Functions as mappings, composition, piecewise definitions (if/elif) → [[B1 Properties of Functions]]
- Iterative updates $x_{t+1} = x_t + \Delta t\,f(x_t)$ → [[B10 Differential Equations]]
- Lambda as an anonymous function $x\mapsto x^2$ → [[B1 Properties of Functions]]

## Connections
- Shared concepts (loops, scope) → [[Prog00 Shared Programming Concepts]]
- Collections to loop over → [[Py02 Python Data Structures]]
- Replacing loops with array operations → [[Py05 NumPy and Arrays]]
- Testing functions → [[Py13 Python Reproducible Projects and Testing]]
- Functions grouped with data → [[Py12 Python Object-Oriented Programming]]

## Key takeaways
- `if/elif/else`: first true branch wins. `break` exits, `continue` skips.
- Keyword arguments and defaults make calls readable; no mutable defaults.
- `*args` collects positional, `**kwargs` collects keyword arguments; `*`/`**` unpack at call time.
- Generators (`yield`) stream data lazily and can be used once.
