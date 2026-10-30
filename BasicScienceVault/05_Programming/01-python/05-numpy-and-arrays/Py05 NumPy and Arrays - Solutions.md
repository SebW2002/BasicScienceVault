---
tags: [programming, python, numpy, type/solution]
---
# Py05 NumPy and Arrays – Solutions

> Worksheet: [[Py05 NumPy and Arrays - Worksheet]] · Theory: [[Py05 NumPy and Arrays]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. a) `(4,)` b) `(3, 2)` c) `(64, 500)` d) `(64,)`
2. `a = [[0,1,2],[3,4,5]]`; `a.T = [[0,3],[1,4],[2,5]]`; `a[1,-1] = 5`; `a.sum(axis=0) = [3, 5, 7]`; `a.sum(axis=1) = [3, 12]`.
3. `4` (0, 0.25, 0.5, 0.75; stop excluded) and `5` (0, 0.25, …, 1).
4. `[2, 2, 3]`: `a` has an integer dtype, so 2.9 is truncated to 2 on assignment.

## Level 2
5. a) yes → (64, 5000) b) **no** (5000 ≠ 64 at the last axis) c) yes → (64, 5000) d) yes → (10, 3, 5) (align right: (10,1,5) vs (·,3,1)).
6. `[0.5, 2.5, 0.3]`, `[1, 2, 3]`, `3`, `0.75`.
7. `and` needs a single truth value; an array is ambiguous. Use `x[(x > 0.2) & (x < 1)]` → `[0.5, 0.3]`.
8. Basic slice = **view**: `x[1]` becomes 99. Integer-array indexing = **copy**: `x` unchanged.

## Level 3
9. $2x_1 + x_2 = 3$, $x_1 + 3x_2 = 5$ → from the first, $x_2 = 3 - 2x_1$; substitute: $x_1 + 9 - 6x_1 = 5$ → $x_1 = 0.8$, $x_2 = 1.4$. `np.linalg.solve(A, b)`. `solve` is faster and numerically more accurate (no explicit inverse; [[C3 Linear Systems and Gaussian Elimination]]).
10. `A * A` = element-wise `[[4,1],[1,9]]`; `A @ A` = matrix product `[[5,5],[5,10]]`.
11. `Xc = X - X.mean(axis=0)`; `U, s, Vt = np.linalg.svd(Xc, full_matrices=False)`; first PC = `Vt[0]` (a unit vector in feature space); scores `Xc @ Vt[0]` (= `U[:, 0] * s[0]`); explained variance ratio `s**2 / (s**2).sum()`. `Vt` has shape (3, 3).

## Level 4
12. `E_bc = E - E[:, :, :100].mean(axis=2, keepdims=True)`; `erp = E_bc.mean(axis=0)` → shape (32, 400).
13. Bins [0,0.1), [0.1,0.2), …, [0.4,0.5]: counts `[2, 3, 0, 0, 1]`, rates = counts / 0.1 s = `[20, 30, 0, 0, 10]` Hz.
    `np.histogram(st, bins=np.arange(0, 0.6, 0.1))` – beware: `arange` with float steps can produce tiny rounding errors in the edges; `np.linspace(0, 0.5, 6)` is safer.
14. ```python
    rng = np.random.default_rng(1)
    c = rng.poisson(4, size=1000)
    print(c.mean(), c.var(ddof=1), c.var(ddof=1) / c.mean())
    ```
    Mean and variance both ≈ 4, Fano ≈ 1. With the same seed the numbers are identical on every run.
