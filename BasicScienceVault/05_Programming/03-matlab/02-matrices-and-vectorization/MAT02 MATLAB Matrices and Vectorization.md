---
aliases: [MATLAB Matrices, Element-wise Operators, Logical Indexing, find, end keyword, Implicit Expansion]
tags: [programming, matlab, vectorization, linear-algebra, indexing, type/overview, neuro]
---
# MAT02 MATLAB Matrices and Vectorization

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT02 MATLAB Matrices and Vectorization - Worksheet|✏️ Worksheet]] · [[MAT02 MATLAB Matrices and Vectorization - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
In MATLAB the **matrix is the basic data type** – a direct translation of linear algebra ([[C1 Matrices]]). This makes it powerful for EEG (channels × time), fMRI (time × voxels) and models ($\mathbf y = A\mathbf x$). The price: you must always know whether you mean a **matrix operation** (`*`) or an **element-wise operation** (`.*`). This one dot causes more MATLAB bugs than anything else.

## Matrices as the basic type; 1-based indexing
```matlab
A = [1 2 3; 4 5 6];      % 2 × 3: spaces/commas separate columns, ; separates rows
size(A)                  % [2 3]
size(A, 1), numel(A)     % rows = 2, elements = 6
zeros(64, 5000); ones(3); eye(3); rand(2, 3); randn(100, 1); nan(1, 10)
t = 0:0.001:0.999;       % colon: start:step:stop (stop included if reached)
t = linspace(0, 1, 1001);
A(2, 3)                  % row 2, column 3 → 6
A(1, :)                  % first row
A(:, end)                % last column
A(end, end-1)            % 5
A(5)                     % linear indexing (column-major order!) → 3
A(:)                     % all elements as a column: [1 4 2 5 3 6]'
A'                       % transpose (conjugate transpose for complex; .' plain transpose)
B = reshape(1:6, 2, 3)   % column-major filling: [1 3 5; 2 4 6]
[A; 7 8 9]               % append a row;  [A, [0; 0]] append a column
A(:, 2) = []             % delete column 2
```
- Indices start at **1**; `end` = last index in that dimension (`x(end-9:end)` = last 10 samples).
- **Column-major:** elements are stored column by column, so `A(:)` and `reshape` run down columns first (same as R; NumPy's default is row-major).
- `x(0)` is an error; indices must be positive integers or logicals.
- Assigning beyond the size grows the matrix (padding with zeros) – convenient and a source of silent bugs; pre-allocate (`zeros(n, 1)`).

## Element-wise vs. matrix operators
| Operator | Matrix meaning | Element-wise version |
|---|---|---|
| `*` | matrix product (inner dimensions must agree) | `.*` |
| `/` | `A/B` = $AB^{-1}$ (solves $xB = A$) | `./` |
| `\` | `A\b` = solves $Ax = b$ | `.\` |
| `^` | matrix power ($A^2 = AA$, square $A$ only) | `.^` |
| `'` | conjugate transpose | `.'` (transpose without conjugation) |
`+`, `-`, comparisons (`<`, `==`) and functions like `exp`, `sin`, `abs`, `log` are always element-wise.
```matlab
x = [1 2 3];
x .^ 2          % [1 4 9]
x ^ 2           % error: matrix must be square
x * x'          % 14 (inner product: 1×3 times 3×1)
x' * x          % 3×3 outer product
1 ./ x          % [1 0.5 0.333]
2 * x           % scalar times matrix is fine without a dot
A \ b           % solve the linear system (Gaussian elimination / QR), better than inv(A)*b
```
**Implicit expansion** (R2016b+): arrays with compatible sizes (equal or 1 in each dimension) are expanded automatically – like NumPy broadcasting ([[Py05 NumPy and Arrays]]):
```matlab
X = randn(64, 5000);
Xc = X - mean(X, 2);     % (64×5000) − (64×1): remove each channel's mean
Xavg = X - mean(X, 1);   % (64×5000) − (1×5000): common average reference
```
Older code uses `bsxfun(@minus, X, mean(X, 2))` for the same thing.

## Aggregation along dimensions
```matlab
mean(X, 1)     % average over rows (dimension 1) → 1 × 5000
mean(X, 2)     % average over columns → 64 × 1
sum(X, "all"), max(X, [], 2), std(X, 0, 2)   % std with n−1 (flag 0) along dim 2
mean(x, "omitnan"), median(x), prctile(x, [25 50 75])
cumsum(x), diff(x)
```
- For a **vector**, `mean(x)` works on its non-singleton dimension; for a **matrix** the default is **dimension 1 (columns)** – with channels × time data, `mean(X)` averages over channels, not time! Always give the dimension.
- `std(x)` uses $n - 1$ by default (`std(x, 1)` for $n$).
- `max` returns value **and** index: `[m, idx] = max(x)`.

## Logical indexing, find, end
```matlab
rt = [0.45 NaN 0.52 0.10 0.61];
valid = ~isnan(rt) & rt >= 0.15 & rt <= 2   % logical array [1 0 1 0 1]
rt(valid)                                   % [0.45 0.52 0.61]
mean(rt(valid))
rt(rt < 0.15) = NaN;                        % assign through a mask
idx = find(valid)                           % indices of true elements: [1 3 5]
first_spike = find(v > 0, 1)                % first index where v > 0
[r, c] = find(A > 4)                        % row and column indices
any(isnan(rt)), all(rt > 0), nnz(valid)     % nnz = number of nonzeros
```
- `&`, `|`, `~` are element-wise; `&&`, `||` are scalar short-circuit operators (for `if`).
- Logical indexing is usually clearer and faster than `find`; use `find` when you need the **positions** (event samples, first threshold crossing).

## Same idea in Python and R
| MATLAB | NumPy | R |
|---|---|---|
| `A(2, 3)` | `A[1, 2]` | `A[2, 3]` |
| `x(end)` | `x[-1]` | `x[length(x)]` |
| `A * B` / `A .* B` | `A @ B` / `A * B` | `A %*% B` / `A * B` |
| `A \ b` | `np.linalg.solve(A, b)` | `solve(A, b)` |
| `mean(X, 2)` | `X.mean(axis=1, keepdims=True)` | `rowMeans(X)` |
| `find(x > 0)` | `np.flatnonzero(x > 0) + 1` (0-based!) | `which(x > 0)` |
| column-major | row-major (default) | column-major |
→ [[Py05 NumPy and Arrays]], [[R02 R Data Structures and Vectorization]]

## In neuroscience #neuro
- **ERP:** EEGLAB stores epochs as channels × time × trials: `erp = mean(EEG.data, 3);` ([[MAT09 EEGLAB]]).
- **Baseline correction:** `data - mean(data(:, base_idx, :), 2)` with implicit expansion.
- **Threshold crossings:** `spikes = find(diff(v > thr) == 1) + 1;` gives the samples where the voltage first exceeds the threshold.
- **GLM:** `beta = X \ y;` fits a design matrix to a voxel time course ([[C3 Linear Systems and Gaussian Elimination]], [[CS12 Neuroimaging Data Analysis]]).
- **Population vectors:** firing rates (neurons × time); `W * r` maps them through a weight matrix ([[CS01 Mathematical Foundations]]).

## Math links #math-link
- Matrix product, transpose, inner/outer product → [[C1 Matrices]], [[D2 Dot and Cross Product]]
- `A\b` = Gaussian elimination → [[C3 Linear Systems and Gaussian Elimination]]
- Determinants and eigenvalues (`det`, `eig`) → [[C2 Determinants]], [[C4 Eigenvalues and Eigenvectors]]
- Logical masks as sets → [[E1 Sets Logic and Quantifiers]]

## Connections
- Shared concepts (vectorisation, indexing) → [[Prog00 Shared Programming Concepts]]
- Basics → [[MAT01 MATLAB Basics and Syntax]]; loops vs. vectorisation → [[MAT03 MATLAB Control Flow and Functions]]
- Signal processing on matrices → [[MAT06 MATLAB Signal Processing Toolbox]]

## Key takeaways
- Everything is a matrix; indices start at 1; `end` = last; storage is column-major.
- `*`, `/`, `^` are matrix operations – use `.*`, `./`, `.^` for element-wise.
- Always specify the dimension: `mean(X, 2)`; defaults work along dimension 1.
- Logical masks for selection; `find` for positions; `A\b` instead of `inv(A)*b`.
