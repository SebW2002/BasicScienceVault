---
tags: [programming, matlab, statistics, type/solution]
---
# MAT07 MATLAB Statistics Toolbox – Solutions

> Worksheet: [[MAT07 MATLAB Statistics Toolbox - Worksheet]] · Theory: [[MAT07 MATLAB Statistics Toolbox]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. a) `ttest(x, y)` b) `ttest2(a, b, "Vartype", "unequal")` c) `signrank` d) `ranksum` e) `fitglm(..., "Distribution", "binomial")` f) `fitlme(T, "y ~ x + (1|subject)")` g) `multcompare` h) `bootci`.
2. The null hypothesis is rejected at α = 0.05. Report the test statistic (`stats.tstat`), df (`stats.df`), the exact p-value, the CI and an effect size.
3. Otherwise a numeric or text column is not treated as a set of categories: numbers would be a continuous predictor, and strings must be converted anyway. `categorical` creates dummy variables relative to the reference category.

## Level 2
4. house = 0.55 s, face = 0.49 s.
5. A: $e^{1.609} = 5$ Hz; B: $5\cdot e^{0.693} = 10$ Hz.
6. Report Welch's test (unequal variances) unless you have good reason to assume equal variances – it's the safer default. They differ when group variances (and sizes) differ: the Student test pools variances, which is wrong if one group is much more variable.

## Level 3
7. $2^8 = 256$ sign patterns. Smallest exact two-sided p = 2/256 ≈ 0.0078 (the observed pattern and its mirror image are the most extreme).
8. The observed data are themselves one possible permutation; including them makes the test exact/valid and avoids p = 0, which would be an impossible claim with finitely many permutations.
9. Shuffle the group labels:
   ```matlab
   pooled = [patients; controls]; n1 = numel(patients);
   idx = randperm(numel(pooled));
   null(k) = mean(pooled(idx(1:n1))) - mean(pooled(idx(n1+1:end)));
   ```
10. 32,000 tests at p < 0.05 give ~1600 false positives under H0. Cluster-based tests exploit that true effects are extended in space/time, and control the **family-wise** error rate by comparing to the permutation distribution of the maximum cluster statistic – one test per data set, with good sensitivity.

## Level 4
11. ```matlab
    T.condition = categorical(T.condition);
    m1 = fitlme(T, "amp ~ condition + (1 + condition | subject)", "FitMethod", "ML");
    m0 = fitlme(T, "amp ~ 1 + (1 + condition | subject)", "FitMethod", "ML");
    compare(m0, m1)
    ```
12. Shuffle the class labels (within the cross-validation's grouping structure, e.g. within runs), **rerun the entire cross-validation** (training + testing) for each permutation to get a null distribution of accuracies (e.g. 1000×), and compute p as the proportion of null accuracies ≥ 61 % (with the +1 correction). Shuffling only the test predictions is not enough.
13. ```matlab
    rng(1); d = 0.3 + randn(20, 1);
    obs = mean(d); nPerm = 10000; null = zeros(nPerm, 1);
    for k = 1:nPerm
        null(k) = mean(sign(rand(20, 1) - 0.5) .* d);
    end
    p_perm = (sum(abs(null) >= abs(obs)) + 1) / (nPerm + 1)
    [~, p_t] = ttest(d)
    ```
    Both p-values are similar (for roughly normal data the t-test and the permutation test agree closely).
