---
tags: [computer-science, neuroimaging, type/solution]
---
# CS12 Neuroimaging Data Analysis – Solutions

> Worksheet: [[CS12 Neuroimaging Data Analysis - Worksheet]] · Theory: [[CS12 Neuroimaging Data Analysis]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. Slice timing → motion correction → coregistration → normalisation → smoothing. (Slice timing and motion correction are sometimes swapped; pipelines like fMRIPrep combine transforms to resample only once.)
2. Rigid: 6 (3 translations + 3 rotations). Affine: 12; the extra 6 describe **scaling** (3) and **shearing** (3), which compensate for differences in brain size and shape.
3. $\sigma = \text{FWHM}/2.355\approx2.55$ mm.
4. Head motion causes signal changes that can correlate with the task (e.g. movement during responses). Including the motion parameters (and often their derivatives) removes this variance and reduces false positives and noise.

## Level 2
5. a) $(1, -1, 0)$ b) $(1, 0, 0)$ c) $(\tfrac12, \tfrac12, 0)$
6. BOLD responses are delayed (peak ~4–6 s) and smoothed relative to neural activity. The regressor must predict the expected **BOLD** time course, i.e. neural events convolved with the HRF; otherwise the model fits poorly and loses power.
7. $X^TX$ is close to singular, so $(X^TX)^{-1}$ has large entries: the β estimates become very **variable** (large standard errors), and the t-value for their difference is small (unstable), even if the effect is real. Fix with a better design (jitter, decorrelated timing).
8. First level: the GLM within each subject's time series, giving contrast images per subject. Second level: statistics **across subjects** on those contrast images. Random effects treat subjects as a random sample, so inter-subject variability enters the error term; only then can you generalise to the population (fixed effects would only describe these subjects).

## Level 3
9. Volumes within a run are **temporally autocorrelated** (the HRF spans several TRs, slow drifts), so neighbouring volumes in training and test sets are not independent, which inflates accuracy (leakage). Runs are separated in time and preprocessed separately, so they are approximately independent.
10. $\frac{92\cdot91}{2} = 4186$
11. $r(A, B) = 1$, so distance 0. $r(A, C) = -1$, so distance 2. $r(B, C) = -1$, so distance 2. The RDM is $\begin{pmatrix}0&0&2\\0&0&2\\2&2&0\end{pmatrix}$. (A and B have the same pattern at different gain; correlation ignores amplitude.)
12. A **permutation test**: shuffle the labels (within runs, preserving the structure), re-run the whole cross-validated pipeline 1000+ times, and compare 58 % with the null distribution. At group level, test subject accuracies (or use permutation-based group tests). Also report the CI and check for confounds.

## Level 4
13. $0.05/60{,}000\approx8.3\times10^{-7}$. Neighbouring voxels are strongly correlated (intrinsic and applied smoothness), so the effective number of independent tests is much smaller and Bonferroni is too strict. Alternatives: random field theory, permutation max-statistic, FDR, cluster-level inference with strict thresholds or TFCE, independent ROIs.
14. Parametric cluster inference (random field theory) assumes a Gaussian-shaped spatial autocorrelation function and sufficient smoothness. Real fMRI noise has a heavier-tailed autocorrelation, and at lenient thresholds (p < 0.01) these deviations matter most, so large noise clusters appeared more often than predicted. Familywise error rates reached up to ~70 % instead of 5 %. Fixes: a stricter cluster-forming threshold (p < 0.001), non-parametric permutation, TFCE, better ACF models.
15. With 306 equations and 8,000 unknowns (or 24,000 with free orientation), the system is **underdetermined**: infinitely many source configurations fit the data equally well (and some sources produce no field at all). MNE adds the constraint of minimal total source power: it picks the solution with the smallest $\lVert\mathbf s\rVert^2$, via the regularised pseudo-inverse $L^T(LL^T + \lambda I)^{-1}$. This is ridge regression, where λ balances data fit against noise.
16. $t = \frac{0.8}{\sqrt{4\cdot0.01}} = \frac{0.8}{0.2} = 4$
