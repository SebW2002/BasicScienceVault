---
tags: [computer-science, data-science, type/solution]
---
# CS06 Data Science Workflow – Solutions

> Worksheet: [[CS06 Data Science Workflow - Worksheet]] · Theory: [[CS06 Data Science Workflow]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. Sorted: 4, 5, 5, **6**, 7, 8, 30, so the median is 6. Lower half 4, 5, 5 gives Q1 = 5; upper half 7, 8, 30 gives Q3 = 8. IQR = 3. Fences: $5 - 4.5 = 0.5$ and $8 + 4.5 = 12.5$. **30 is an outlier.**
2. Mean $= 65/7\approx9.3$, pulled up by one value and larger than six of the seven data points. Median and IQR are **robust**: one extreme value barely changes them.
3. **MNAR** (or at least MAR, if severity is measured and can be modelled). Analysing only complete cases biases the sample towards milder cases, so effects of severity are underestimated.
4. Otherwise you can (consciously or not) choose criteria that produce the desired result: one form of p-hacking / garden of forking paths. Pre-defined criteria applied blindly to all conditions prevent this.

## Level 2
5. 20 trials per test fold; 5 models.
6. You chose the hyperparameter that performed best on exactly these folds, partly due to chance fluctuations, so its score overestimates performance on new data. **Nested CV** (or a separate untouched test set) gives an unbiased estimate.
7. **Leave-one-subject-out** (or grouped k-fold by subject). A random trial-wise split puts trials from the same subject in train and test, so it measures generalisation **within** known subjects, which is usually much higher.
8. Overlapping windows share data, and neighbouring windows are strongly autocorrelated, so the test windows are nearly copies of training windows (leakage). Use **blocked** splits (contiguous time blocks with gaps) or split by recording session.

## Level 3
9. a) **Leakage**: the mean and SD include test data. Fix: fit the scaler on the training set only. b) **Leakage** (double dipping): voxel selection used test trials. Fix: select voxels inside each training fold. c) **No leakage**: preprocessing fitted only on training runs, split by run. d) **Leakage**: augmented versions of the same image end up in both train and test. Fix: split first, then augment only the training set.
10. **Circular analysis (double dipping):** voxels were selected precisely because they correlate with anxiety in this sample, including by chance. Re-testing the same data inflates r (Vul et al. 2009). Fix: define the ROI independently (another dataset, anatomy, a localiser, or cross-validated selection) and test on held-out data.

## Level 4
11. $n\propto1/d^2$: $d = 0.25$ needs about $64\cdot4 = 256$ per group; $d = 1$ needs about $64/4 = 16$ per group.
12. With low power, only studies whose effect estimate happens to come out large (through noise) reach significance. Published significant effects are therefore systematically **overestimated**, and replications with realistic $n$ find smaller effects.
13. No: non-overlapping SEM bars don't reliably imply p < 0.05 (and overlapping 95 % CIs don't imply non-significance). Better: show individual data points (or paired lines for within-subject data), state what the bars mean, and report the test, effect size and CI of the **difference**.
14. Jet is not perceptually uniform: brightness changes non-monotonically, which creates **artificial edges** (e.g. at yellow/cyan) and hides real gradients. It is also bad for colour-blind readers and in greyscale. Use viridis/magma for sequential data, and a diverging map centred on 0 for signed data.
15. $d = 1.2$: $16/1.44\approx11$ per group. $d = 0.6$: $16/0.36\approx44$ per group. Small pilots give very noisy effect size estimates, and pilots are often continued or published *because* the effect looked large (selection), so pilot effect sizes tend to be inflated (winner's curse).
