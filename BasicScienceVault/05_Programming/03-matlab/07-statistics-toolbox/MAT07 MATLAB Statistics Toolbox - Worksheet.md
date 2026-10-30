---
tags: [programming, matlab, statistics, type/worksheet]
---
# MAT07 MATLAB Statistics Toolbox – Worksheet

> Theory: [[MAT07 MATLAB Statistics Toolbox]] · Solutions: [[MAT07 MATLAB Statistics Toolbox - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper; no calculator unless marked. Run code only for tasks marked 💻.

## Level 1 – Which function?
1. Which function: a) paired t-test b) Welch two-sample test c) Wilcoxon signed-rank d) Mann–Whitney U e) logistic regression f) mixed model with random intercepts per subject g) post-hoc comparisons after `anova1` h) bootstrap CI.
2. What does `h = 1` in `[h, p] = ttest(...)` mean? What should you report instead of `h`?
3. Why must `condition` be `categorical` before `fitlm(T, "rt ~ condition")`?

## Level 2 – Read output
4. `fitlm` with reference "house": `(Intercept) 0.55`, `condition_face −0.06`. Mean RTs per condition?
5. `fitglm` Poisson with offset log(duration): `(Intercept) = 1.609` (= ln 5), `stimulus_B = 0.693` (= ln 2). Firing rates for A and B?
6. `ttest2(a, b)` gives p = 0.03, `ttest2(a, b, "Vartype", "unequal")` gives p = 0.09. Which do you report and why might they differ?

## Level 3 – Permutation logic
7. Paired design with 8 subjects: how many distinct sign-flip permutations exist? What's the smallest achievable two-sided exact p-value?
8. Why do we add 1 to numerator and denominator in $p = \frac{\#\{|null| \ge |obs|\} + 1}{n_\text{perm} + 1}$?
9. Two independent groups (patients n = 12, controls n = 15): what do you shuffle? Write the loop body.
10. Why is a cluster-based permutation test better than running a t-test at each of 64 channels × 500 time points and thresholding at p < 0.05?

## Level 4 – Neuro transfer
11. Write the `fitlme` call for single-trial P300 amplitudes `amp` with fixed effect `condition` and random intercepts and slopes for subject; then the likelihood-ratio test against a model without condition.
12. A decoder reaches 61 % accuracy (chance 50 %) with 80 trials. Describe a permutation test for its significance. What must be repeated in each permutation?
13. 💻 Simulate 20 subjects' paired differences `d = 0.3 + randn(20, 1)` with `rng(1)`, compute the sign-flip permutation p-value (10,000 permutations) and compare with `ttest(d)`.
