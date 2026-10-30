---
tags: [programming, shared-concepts, type/solution]
---
# Prog00 Shared Programming Concepts – Solutions

> Worksheet: [[Prog00 Shared Programming Concepts - Worksheet]] · Theory: [[Prog00 Shared Programming Concepts]] · Wrong? → [[Mistakes - Programming Basics]]

## Level 1
1. a) `20` (0-based) b) `10` (1-based) c) `50` d) `[20, 30]` (indices 1 and 2; 3 excluded) e) `[20 30]` f) `20 30 40 50` (in R a negative index **removes** element 1).
2. 0.1 and 0.2 have no exact binary representation; the sum is `0.30000000000000004`. Compare with a tolerance: `abs(a - b) < 1e-9` (Python `math.isclose`/`np.isclose`, R `isTRUE(all.equal(a, b))`).
3. Logical: `TRUE` (R), `True` (Python), `true` (MATLAB). Strings: `"TRUE"`, `'true'` (in MATLAB a char array, in Python a str).
4. `b − a` elements (indices a, a+1, …, b−1). `x[:k]` = indices 0…k−1, `x[k:]` = indices k…end. No index is in both, none is missing.

## Level 2
5. `6` (2 + 4).
6. `v` never changes, so `v < threshold` stays true. Fix: change `v` inside the loop, e.g. `v = v + 0.1`.
7. Any two of: the result depends on hidden state (calling it twice gives different results); hard to test; can't reuse it on other data; other code that uses `data` breaks unexpectedly; the order of calls matters.
8. It is **local**: visible only inside the function, created on each call, deleted when the function returns (unless returned).

## Level 3
9. `y = 2 * x + 1` (Python with NumPy, R); MATLAB `y = 2 * x + 1` (scalar × array needs no dot).
10. a) `NaN` (NaN propagates). b) `~isnan(rt) & rt >= 0.15 & rt <= 2` (R: `!is.na(rt) & ...`; Python: `~np.isnan(rt) & (rt >= 0.15) & (rt <= 2)`, mind the parentheses). c) `0.45, 0.52, 0.61` (0.10 is too fast, NaN is missing). Note: comparisons with NaN are false anyway, but writing the NaN test explicitly documents intent and is required in R, where `NA >= 0.15` gives `NA`, not `FALSE`.
11. By definition NaN is unequal to everything, including NaN, so the comparison is always false (R: `NA == NA` is `NA`). Use `isnan(x)` / `np.isnan(x)` / `is.na(x)`.
12. It subtracts the mean across channels from each channel at each time point (broadcasting the 1 × 5000 row over all 64 rows): **re-referencing to the common average reference**.

## Level 4
13. The permutation test uses random shuffles and no seed is set, so each run uses different permutations (and p near 0.05 flips). Set a seed, report it, and use enough permutations (e.g. 10,000) that the Monte-Carlo error is small. Don't interpret 0.048 vs 0.052 as a real difference anyway.
14. The path only exists on Anna's computer; the script fails everywhere else. Instead: open the project folder as the working directory (RStudio Project) and use project-relative paths, e.g. `here::here("data", "raw", "sub-01.csv")`.
15. `../data/raw/sub-01.csv`
16. a) 1-based sample 2500 is the 2499th sample after the first: $t = (2500 - 1)/500 = 4.998$ s. b) Python index `2499`. Check, e.g. in Python:
    ```python
    fs = 500
    k_matlab = 2500
    k_py = k_matlab - 1
    print(k_py, k_py / fs)   # 2499 4.998
    ```
