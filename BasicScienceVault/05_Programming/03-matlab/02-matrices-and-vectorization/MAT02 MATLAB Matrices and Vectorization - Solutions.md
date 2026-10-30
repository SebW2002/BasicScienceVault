---
tags: [programming, matlab, type/solution]
---
# MAT02 MATLAB Matrices and Vectorization – Solutions

> Worksheet: [[MAT02 MATLAB Matrices and Vectorization - Worksheet]] · Theory: [[MAT02 MATLAB Matrices and Vectorization]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. `[4 5 6]`; `[3; 6; 9]`; `7`; `2` (column-major: 1, 4, 7, **2**, …); `[4 6; 7 9]`; `[9 1]`.
2. `[50 60]`; `[10 60]`; `6`; `[40 50 60]`.
3. ```text
   1 4
   2 5
   3 6
   ```
4. 5 elements (0, 0.25, 0.5, 0.75, 1); `0:0.3:1` → 4 elements (0, 0.3, 0.6, 0.9) – 1 isn't reached.

## Level 2
5. a) `[4 10 18]` b) **error** (1×3 times 1×3: inner dimensions 3 ≠ 1) c) `32` (inner product) d) 3×3 outer product `[4 5 6; 8 10 12; 12 15 18]` e) `[0.25 0.4 0.5]` f) `[1 4 9]` g) **error** (matrix power needs a square matrix).
6. $2x_1 + x_2 = 3$, $x_1 + 3x_2 = 5$ → $x = (0.8, 1.4)^T$. `\` solves the system directly by factorisation: faster and numerically more accurate than computing the inverse ([[C3 Linear Systems and Gaussian Elimination]]).
7. `mean(X)` → 1 × 5000 (average over channels at each time point – default dimension 1!). `mean(X, 2)` → 64 × 1 (each channel's mean over time). `X - mean(X, 2)` → 64 × 5000, each channel centred at zero (removes DC offset). `X - mean(X)` → 64 × 5000, common average reference.
8. `m = 9`, `i = 2` (the first occurrence).

## Level 3
9. `v > -50` = `[0 0 1 1 0 1 1 0]`; `find(...)` = `[3 4 6 7]`; `diff(v > -50)` = `[0 1 0 -1 1 0 -1]`, `== 1` at positions 2 and 5, +1 → `[3 6]`: the samples where the voltage **crosses** the threshold upwards (one per event, not every sample above threshold).
10. `rt(rt < 0.15 | rt > 2) = NaN;` → `[0.3 NaN NaN 0.6 NaN]`; `mean(rt, "omitnan")` → 0.45.
11. `y = x.^2 .* exp(-x);`

## Level 4
12. `data = EEG.data - mean(EEG.data(:, 1:100, :), 2);` and `erp = mean(data, 3);` → ERP size 32 × 500.
13. `beta = D \ y;` (3 × 1) and `res = y - D * beta;` (300 × 1).
14. ```matlab
    X = randn(4, 1000);
    Xref = X - mean(X, 1);
    max(abs(mean(Xref, 1)))   % ~1e-16: zero up to floating-point rounding
    ```
