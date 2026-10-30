---
tags: [computer-science, neuroimaging, type/worksheet]
---
# CS12 Neuroimaging Data Analysis – Worksheet

> Theory: [[CS12 Neuroimaging Data Analysis]] · Solutions: [[CS12 Neuroimaging Data Analysis - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮.

## Level 1 – Preprocessing
1. Put in a typical order: normalisation to MNI, slice timing correction, spatial smoothing, motion correction, coregistration.
2. How many parameters does a rigid-body transform in 3D have? An affine one? What do the extra parameters describe?
3. A smoothing kernel has FWHM = 6 mm. What is its standard deviation σ?
4. Why are motion parameters included as regressors in the GLM?

## Level 2 – GLM
5. A design has three regressors: faces, houses, intercept. Write the contrast vectors for a) faces > houses, b) faces > baseline, c) the average of faces and houses > baseline.
6. Why must task regressors be convolved with the HRF?
7. Two regressors are almost identical (correlation 0.95). What happens to the variance of their β estimates and to the t-value of their difference?
8. What is the difference between a first-level and a second-level analysis? Why is a random-effects analysis needed to generalise to the population?

## Level 3 – MVPA and RSA
9. Why should MVPA cross-validation be done across runs and not across individual volumes?
10. How many unique dissimilarities does an RDM for 92 conditions have?
11. Patterns (3 voxels) for conditions A, B, C: $A = (1, 2, 3)$, $B = (2, 4, 6)$, $C = (3, 2, 1)$. Compute the correlation-distance RDM ($1 - r$).
12. A decoder reaches 58 % on two classes. Describe how you would establish significance.

## Level 4 – Multiple comparisons & source localisation
13. A whole-brain analysis tests 60,000 voxels. Bonferroni threshold for α = 0.05? Why is Bonferroni conservative here, and what alternatives exist?
14. Why did cluster-based inference with a cluster-forming threshold of p < 0.01 produce too many false positives in parametric software (Eklund et al. 2016)?
15. An MEG system has 306 sensors and the source space has 8,000 dipoles. Why can't the inverse problem be solved uniquely? How does the minimum-norm estimate choose a solution?
16. 🧮 Compute the t-statistic of a contrast with $\mathbf c^T\hat{\boldsymbol\beta} = 0.8$, $\hat\sigma^2 = 4$ and $\mathbf c^T(X^TX)^{-1}\mathbf c = 0.01$.
