---
tags: [programming, matlab, type/worksheet]
---
# MAT02 MATLAB Matrices and Vectorization – Worksheet

> Theory: [[MAT02 MATLAB Matrices and Vectorization]] · Solutions: [[MAT02 MATLAB Matrices and Vectorization - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper: predict outputs and sizes, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Indexing
1. `A = [1 2 3; 4 5 6; 7 8 9]`. Give: `A(2, :)`, `A(:, end)`, `A(end, 1)`, `A(4)`, `A(2:3, [1 3])`, `size(A(:))`.
2. `x = 10:10:60`. Give `x(end-1:end)`, `x([1 end])`, `numel(x)`, `x(x > 35)`.
3. `reshape(1:6, 3, 2)` – write it out.
4. `t = 0:0.25:1` – how many elements? `0:0.3:1`?

## Level 2 – Operators
5. `x = [1 2 3]; y = [4 5 6];` Which work, and what do they give? a) `x .* y` b) `x * y` c) `x * y'` d) `x' * y` e) `x ./ y` f) `x .^ 2` g) `x ^ 2`
6. `A = [2 1; 1 3]; b = [3; 5];` Solve `A\b` by hand. Why is it preferred over `inv(A)*b`?
7. `X` is 64 × 5000 (channels × time). What sizes do `mean(X)`, `mean(X, 2)`, `X - mean(X, 2)` and `X - mean(X)` have, and what do the last two compute?
8. `[m, i] = max([3 9 2 9])` – values of `m` and `i`?

## Level 3 – Logical indexing and find
9. `v = [-70 -65 -40 10 -60 -45 5 -70]`, threshold −50. Give `v > -50`, `find(v > -50)`, `find(diff(v > -50) == 1) + 1`. What does the last expression detect?
10. `rt = [0.3 NaN 2.5 0.6 0.12]`: write one line that sets all RTs outside 0.15–2 s to NaN, and one line for the mean of the remaining values.
11. Rewrite without a loop: `for k = 1:numel(x), y(k) = x(k)^2 * exp(-x(k)); end`

## Level 4 – Neuro transfer
12. EEGLAB data `EEG.data` is channels × time × trials (32 × 500 × 120); baseline = samples 1–100. Write the baseline correction and the ERP in two lines. Size of the ERP?
13. A design matrix `D` (300 × 3) and a voxel time course `y` (300 × 1). Write the GLM fit and the residuals. What is the size of `beta`?
14. 💻 Create `X = randn(4, 1000)`, apply the common average reference with implicit expansion, and check that `mean(Xref, 1)` is (numerically) zero at every time point.
