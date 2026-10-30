---
aliases: [NumPy, ndarray, Broadcasting, Boolean Indexing, numpy.linalg, numpy.random]
tags: [programming, python, numpy, vectorization, linear-algebra, type/overview, neuro]
---
# Py05 NumPy and Arrays

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py05 NumPy and Arrays - Worksheet|✏️ Worksheet]] · [[Py05 NumPy and Arrays - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
NumPy is the foundation of scientific Python: pandas, SciPy, scikit-learn, MNE and Nilearn all store data as NumPy arrays. It brings **vectorisation** ([[Prog00 Shared Programming Concepts]]) and **linear algebra** ([[C1 Matrices]]) to Python. Getting `shape`, `axis` and broadcasting right is 80 % of working with neural data.

## The ndarray: shape and dtype
```python
import numpy as np
x = np.array([1.0, 2.0, 3.0])          # 1-d, shape (3,)
X = np.zeros((64, 5000))               # 2-d: channels × time
E = np.empty((200, 64, 500))           # 3-d: trials × channels × time
X.shape, X.ndim, X.size, X.dtype       # (64, 5000), 2, 320000, float64
np.arange(0, 1, 0.001)                 # 0, 0.001, …, 0.999 (stop excluded)
np.linspace(0, 1, 1001)                # 1001 points incl. both ends
```
- All elements share **one dtype**: `float64` (default), `float32` (half the memory, GPUs), `int16` (raw ADC), `uint8` (images), `bool`, `complex128` (FFT).
- **Integer pitfalls:** `np.array([1, 2]) / 2` → float, but `a = np.array([1, 2]); a[0] = 0.7` stores `0` (cast to int). Raw `int16` data can **overflow** in sums: convert first (`x.astype(np.float64)`).
- `reshape` changes the shape without copying data (row-major / "C" order: last index varies fastest): `np.arange(6).reshape(2, 3)` → `[[0,1,2],[3,4,5]]`.

## Element-wise operations and broadcasting
Arithmetic, comparisons and functions (`np.exp`, `np.log`, `np.sin`) act **element-wise**. `*` is element-wise; matrix product is `@`.

**Broadcasting rules:** compare shapes from the **right**; two dimensions are compatible if they're **equal or one of them is 1**; missing dimensions count as 1. The size-1 dimension is "stretched".
| A | B | Result |
|---|---|---|
| (64, 5000) | (5000,) | (64, 5000) – same row subtracted from every channel |
| (64, 5000) | (64, 1) | (64, 5000) – one value per channel |
| (64, 5000) | (64,) | **error** (5000 vs 64) |
| (200, 64, 500) | (64, 1) | (200, 64, 500) |
```python
X_centered = X - X.mean(axis=1, keepdims=True)   # remove each channel's mean
X_avgref   = X - X.mean(axis=0)                  # common average reference
```
`keepdims=True` keeps the reduced axis as size 1 so broadcasting works.

## Slicing and Boolean indexing
```python
X[0]            # first channel, all time points  → shape (5000,)
X[:, 100:200]   # all channels, samples 100–199
X[::2]          # every second channel
E[:, 10, :]     # channel 10 across all trials  → (200, 500)
mask = rt > 0.15                      # Boolean array
rt[mask]                              # only valid trials (copy)
E[mask]                               # trials where mask is True
rt[(rt > 0.15) & (rt < 2)]            # & | ~ with parentheses!
np.where(v > thr)[0]                  # indices where True
np.select([rt < .15, rt > 2], ["fast", "slow"], default="ok")
```
- **Basic slices are views** (no copy): changing `X[:, :10]` changes `X`. **Boolean and integer-array indexing returns copies.** Use `.copy()` when you want independence.
- Python's `and`/`or` don't work on arrays – use `&`, `|`, `~` and parenthesise comparisons.

## Aggregation and the axis argument
```python
E.mean(axis=0)       # average over trials → ERP, shape (64, 500)
E.std(axis=0, ddof=1)  # sample SD (n−1) across trials
X.max(axis=1)        # maximum per channel
np.nanmean(rt)       # ignores NaN
np.percentile(rt, [25, 50, 75])
np.cumsum(spike_counts)
```
**axis = the dimension that disappears.** For (trials, channels, time), `axis=0` averages over trials. NumPy's `std` defaults to `ddof=0` (population SD); statistics usually want `ddof=1` (pandas and R default to n − 1).

## Linear algebra with numpy.linalg
```python
A @ x                         # matrix–vector product
np.linalg.solve(A, b)         # solve Ax = b (better than inv(A) @ b)
np.linalg.inv(A)              # inverse (rarely needed)
np.linalg.det(A)
w, V = np.linalg.eig(A)       # eigenvalues, eigenvectors (columns of V)
w, V = np.linalg.eigh(C)      # symmetric matrices (covariance): real, sorted
U, s, Vt = np.linalg.svd(X, full_matrices=False)   # X = U @ diag(s) @ Vt
beta, *_ = np.linalg.lstsq(D, y, rcond=None)      # least squares (GLM)
```
- **PCA via SVD:** centre the data (samples × features), `U, s, Vt = svd(Xc)`; rows of `Vt` are principal axes, explained variance ∝ `s**2` ([[CS01 Mathematical Foundations]], [[C4 Eigenvalues and Eigenvectors]]).
- **GLM:** $\hat\beta = \arg\min\lVert y - D\beta\rVert^2$ via `lstsq` ([[C3 Linear Systems and Gaussian Elimination]], [[CS12 Neuroimaging Data Analysis]]).

## Random numbers and seeds
```python
rng = np.random.default_rng(42)          # modern Generator API, seeded
rng.normal(0, 1, size=(100, 3))          # Gaussian noise
rng.poisson(lam=5, size=1000)            # spike counts
rng.uniform(0.8, 1.2, size=200)          # jittered ITIs
rng.permutation(n_trials)                # shuffled order
rng.choice(a, size=n, replace=True)      # bootstrap resample
```
- Create **one** generator per script (or per independent stream) and pass it to functions; avoid the old global `np.random.seed()`.
- Same seed → same numbers on the same NumPy version ([[Prog00 Shared Programming Concepts]]).

## Same idea in R and MATLAB
| NumPy | R | MATLAB |
|---|---|---|
| `X.shape` | `dim(X)` | `size(X)` |
| `A @ B`, `A * B` | `A %*% B`, `A * B` | `A * B`, `A .* B` |
| `X.mean(axis=0)` | `colMeans(X)`, `apply(X, 2, mean)` | `mean(X, 1)` |
| broadcasting | recycling, `sweep()` | implicit expansion (R2016b+) |
| `np.linalg.solve(A, b)` | `solve(A, b)` | `A \ b` |
| `default_rng(42)` | `set.seed(42)` | `rng(42)` |
| row-major (C) | column-major | column-major |
→ [[R02 R Data Structures and Vectorization]], [[MAT02 MATLAB Matrices and Vectorization]]

## In neuroscience #neuro
- **ERP:** epochs (trials × channels × time) → `E.mean(axis=0)`; baseline correction: `E - E[..., :n_base].mean(axis=-1, keepdims=True)`.
- **Spike binning:** `counts, edges = np.histogram(spike_times, bins=np.arange(0, T + dt, dt))`; rate = counts / dt.
- **ΔF/F** for calcium imaging: `(F - F0[:, None]) / F0[:, None]` with one baseline per cell.
- **Population vectors:** a time × neurons matrix; cosine similarity between states uses `@` and `np.linalg.norm` ([[D2 Dot and Cross Product]]).
- **Surrogates:** shuffle trial labels with `rng.permutation` for permutation tests ([[CS02 Probability and Statistics]]).

## Math links #math-link
- Matrices, products, transposes → [[C1 Matrices]]; solving systems → [[C3 Linear Systems and Gaussian Elimination]]; determinants → [[C2 Determinants]]
- Eigenvalues, PCA → [[C4 Eigenvalues and Eigenvectors]]
- Vector norms and dot products → [[D2 Dot and Cross Product]]
- Sums and means → [[A7 Sums Products and Factorials]]

## Connections
- Vectorisation, NaN, seeds → [[Prog00 Shared Programming Concepts]]
- Lists are not arrays → [[Py02 Python Data Structures]]
- Built on NumPy: [[Py06 pandas and Tabular Data]], [[Py08 SciPy Scientific Computing]], [[Py09 Python Machine Learning Libraries]]
- Concepts: SVD, PCA, tensors → [[CS01 Mathematical Foundations]]

## Key takeaways
- Know your `shape` and `dtype`; print them when in doubt.
- Broadcasting: align shapes from the right; sizes must be equal or 1; use `keepdims=True`.
- `axis` = the dimension that is collapsed.
- Slices are views; Boolean/fancy indexing copies. Use `& | ~` with parentheses.
- `solve` instead of `inv`; `default_rng(seed)` for random numbers.
