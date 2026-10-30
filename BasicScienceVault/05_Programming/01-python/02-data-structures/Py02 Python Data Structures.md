---
aliases: [Python Data Structures, Lists Tuples Dictionaries Sets, List Comprehensions, Mutable vs Immutable]
tags: [programming, python, data-structures, type/overview, neuro]
---
# Py02 Python Data Structures

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py02 Python Data Structures - Worksheet|✏️ Worksheet]] · [[Py02 Python Data Structures - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
Before arrays and data frames, Python organises data in four built-in **collections**. You'll use them for everything that isn't a big numeric array: lists of files, dictionaries of parameters, sets of channel names, tuples of shapes. The difference between **mutable** and **immutable** objects explains one of the most confusing Python bugs: changing a list "somewhere else" changes it everywhere.

## The four collections
| Type | Literal | Ordered | Mutable | Duplicates | Typical use |
|---|---|---|---|---|---|
| **list** | `[1, 2, 3]` | yes | yes | yes | sequence of items you add to: files, trials, results |
| **tuple** | `(64, 5000)` | yes | **no** | yes | fixed records: shapes, (x, y) coordinates, return values |
| **dict** | `{"fs": 1000, "n_ch": 64}` | insertion order | yes | keys unique | look-up by name: parameters, metadata, subject → data |
| **set** | `{"Fz", "Cz", "Pz"}` | **no** | yes | **no** | membership tests, unique values, set algebra |

### Lists
```python
files = ["sub-01.edf", "sub-02.edf"]
files.append("sub-03.edf")      # add at the end (in place, returns None!)
files[0]                        # 'sub-01.edf'
files[-1]                       # last
files[1:]                       # slice → new list
len(files), "sub-02.edf" in files
files.sort(); sorted(files)     # in place vs. new sorted copy
```
Lists can hold anything, including mixed types and other lists; but a list of numbers is **not** a vector: `[1, 2] * 2 == [1, 2, 1, 2]` and `[1, 2] + [3] == [1, 2, 3]`. For maths use NumPy ([[Py05 NumPy and Arrays]]).

### Tuples
```python
shape = (64, 5000)
n_ch, n_t = shape               # unpacking
def minmax(x): return min(x), max(x)   # returns a tuple
lo, hi = minmax([3, 1, 4])
```
Single-element tuple needs a comma: `(5,)`.

### Dictionaries
```python
params = {"fs": 1000, "l_freq": 1.0, "h_freq": 40.0}
params["fs"]                    # 1000; KeyError if missing
params.get("notch", None)       # default instead of error
params["notch"] = 50            # add / overwrite
for key, value in params.items():
    print(key, value)
```
Keys must be immutable (strings, numbers, tuples). Dicts map naturally to JSON ([[Py04 Python Files and Data Formats]]).

### Sets
```python
recorded = {"Fz", "Cz", "Pz", "Oz"}
bad = {"Oz", "T7"}
recorded - bad        # {'Fz', 'Cz', 'Pz'}  difference
recorded & bad        # {'Oz'}              intersection
recorded | bad        # union
"Cz" in recorded      # fast membership test
```
Exactly the set operations from [[E1 Sets Logic and Quantifiers]]. `set(list_with_duplicates)` gives the unique values (order lost).

## List comprehensions
A compact way to build a list from another iterable, mirroring set-builder notation $\{f(x) : x\in A,\ P(x)\}$:
```python
squares = [x**2 for x in range(5)]                 # [0, 1, 4, 9, 16]
valid   = [rt for rt in rts if 0.15 <= rt <= 2]    # filter
files   = [f"sub-{i:02d}.edf" for i in range(1, 4)]
lookup  = {ch: i for i, ch in enumerate(channels)} # dict comprehension
uniq    = {f.split("_")[0] for f in files}         # set comprehension
```
Keep them short; if it needs nested loops and conditions, write a normal loop.

## Mutable vs. immutable
- **Immutable** (int, float, str, tuple, frozenset): can't be changed in place; "changing" creates a new object.
- **Mutable** (list, dict, set, NumPy array): can be changed in place.
- **Names are labels, not boxes.** `b = a` does **not** copy; both names point to the same object:
```python
a = [1, 2, 3]
b = a          # same list
b.append(4)
a              # [1, 2, 3, 4]  ← surprise
c = a.copy()   # or list(a), a[:] → independent (shallow) copy
```
- **Shallow vs. deep copy:** `a.copy()` copies the outer list only; nested lists inside are still shared. Use `copy.deepcopy()` for nested structures.
- **Default argument trap:** `def f(x, acc=[])` creates the list **once**; every call shares it. Use `acc=None` and create the list inside.
- **Functions can modify mutable arguments** in place, which is efficient but surprising. Document it, or return a new object.

## Same idea in R and MATLAB
| Python | R | MATLAB |
|---|---|---|
| list | `list()` (or atomic vector `c()`) | cell array `{}` |
| dict | named list `list(fs = 1000)` | `struct` (`s.fs = 1000`), `dictionary` (R2022b+) |
| set operations | `union`, `intersect`, `setdiff` | `union`, `intersect`, `setdiff` |
| comprehension | `sapply`, `purrr::map` | `arrayfun`, `cellfun` |
| reference semantics | R and MATLAB **copy on modify**: `b <- a; b[1] <- 0` leaves `a` unchanged | same (except handle objects) |
→ [[R02 R Data Structures and Vectorization]], [[MAT04 MATLAB Data Import and Files]] (structs and cells)

## In neuroscience #neuro
- **Metadata as dicts:** `{"subject": "01", "fs": 1000, "reference": "average", "bad_channels": ["T7"]}` maps 1:1 to a BIDS sidecar JSON ([[CS05 Data Formats and Representation]]).
- **Channel bookkeeping with sets:** which channels are in every subject? `set.intersection(*[set(s) for s in channel_lists])`.
- **Trial lists:** a list of dicts, one per trial (`{"condition": "face", "rt": 0.43}`), is the natural input to `pandas.DataFrame` ([[Py06 pandas and Tabular Data]]) and to PsychoPy's trial handler ([[Py11 PsychoPy Experiment Control]]).
- **Aliasing bug:** modifying "a copy" of a list of bad channels that is actually the same object changes the bad channels for every subject.

## Math links #math-link
- Sets, union, intersection, difference, set-builder notation → [[E1 Sets Logic and Quantifiers]]
- Tuples as ordered pairs / coordinates → [[D1 Vectors in 2D and 3D]]

## Connections
- Basics → [[Py01 Python Basics and Syntax]]; loops over collections → [[Py03 Python Control Flow and Functions]]
- Dicts ↔ JSON → [[Py04 Python Files and Data Formats]]
- Lists are not vectors → [[Py05 NumPy and Arrays]]
- Shared concepts → [[Prog00 Shared Programming Concepts]]

## Key takeaways
- list = ordered, mutable; tuple = ordered, immutable; dict = key → value; set = unique, unordered.
- Comprehensions: `[f(x) for x in xs if cond]`.
- `b = a` shares the object; copy explicitly (`.copy()`, `deepcopy`).
- Never use a mutable default argument.
