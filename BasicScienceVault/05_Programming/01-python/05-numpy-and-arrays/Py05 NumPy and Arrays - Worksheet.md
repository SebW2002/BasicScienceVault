---
tags: [programming, python, numpy, type/worksheet]
---
# Py05 NumPy and Arrays – Worksheet

> Theory: [[Py05 NumPy and Arrays]] · Solutions: [[Py05 NumPy and Arrays - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper: predict outputs and shapes, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Shapes and dtypes
1. Give the shape: a) `np.zeros((3, 4))[1]` b) `np.arange(12).reshape(3, 4)[:, 1:3]` c) `np.ones((200, 64, 500)).mean(axis=0)` d) `np.ones((200, 64, 500)).mean(axis=(0, 2))`
2. `a = np.arange(6).reshape(2, 3)`. Write out `a`, `a.T`, `a[1, -1]`, `a.sum(axis=0)`, `a.sum(axis=1)`.
3. `len(np.arange(0, 1, 0.25))` and `len(np.linspace(0, 1, 5))`?
4. `a = np.array([1, 2, 3]); a[0] = 2.9; a` – what is stored and why?

## Level 2 – Broadcasting and indexing
5. Which combinations broadcast, and to which shape? a) (64, 5000) and (5000,) b) (64, 5000) and (64,) c) (64, 5000) and (64, 1) d) (10, 1, 5) and (3, 1)
6. `x = np.array([0.1, 0.5, 2.5, 0.3])`. Give `x[x > 0.2]`, `np.where(x > 0.2)[0]`, `(x > 0.2).sum()`, `(x > 0.2).mean()`.
7. Why does `x[(x > 0.2) and (x < 1)]` fail? Correct it.
8. `y = x[1:3]; y[0] = 99`. Is `x` changed? What if `y = x[[1, 2]]`?

## Level 3 – Linear algebra
9. $A = \begin{pmatrix}2&1\\1&3\end{pmatrix}$, $b = \begin{pmatrix}3\\5\end{pmatrix}$. Solve $Ax = b$ by hand and write the NumPy line. Why `solve` rather than `inv(A) @ b`?
10. For `A` above, what is `A * A` versus `A @ A`?
11. Data matrix `X` (100 samples × 3 features). Write the steps to get the first principal component with `np.linalg.svd`. Which shape has `Vt`?

## Level 4 – Neuro transfer
12. Epochs `E` with shape (trials, channels, time) = (120, 32, 400), baseline = first 100 samples. Write one line for baseline correction and one for the ERP.
13. Spike times (s) `st = np.array([0.012, 0.018, 0.140, 0.151, 0.153, 0.420])`. Bin into 100 ms bins from 0 to 0.5 s. Give the counts and rates (Hz).
14. 💻 With `rng = np.random.default_rng(1)`, simulate 1000 trials of Poisson spike counts with λ = 4. Check that mean and variance are both ≈ 4 (Fano factor ≈ 1). Rerun – are the numbers the same?
