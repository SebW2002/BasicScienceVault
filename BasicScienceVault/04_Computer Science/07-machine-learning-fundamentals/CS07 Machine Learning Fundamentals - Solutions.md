---
tags: [computer-science, machine-learning, type/solution]
---
# CS07 Machine Learning Fundamentals – Solutions

> Worksheet: [[CS07 Machine Learning Fundamentals - Worksheet]] · Theory: [[CS07 Machine Learning Fundamentals]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. a) supervised regression b) unsupervised clustering c) supervised classification d) unsupervised dimensionality reduction (PCA)
2. $\bar x = 2$, $\bar y = 10/3$. $\sum(x - \bar x)(y - \bar y) = (-1)(-\tfrac43) + 0 + (1)(\tfrac53) = 3$; $\sum(x - \bar x)^2 = 2$. Slope $= 1.5$; intercept $= \tfrac{10}{3} - 3 = \tfrac13$. So $\hat y = 1.5x + \tfrac13$.
3. $x = 1$: $\sigma(-2)\approx0.12$. $x = 2$: $\sigma(0) = 0.5$. $x = 3$: $\sigma(2)\approx0.88$. The boundary is at $2x - 4 = 0$, i.e. $x = 2$.

## Level 2
4. $G = 1 - (0.8^2 + 0.2^2) = 1 - 0.68 = 0.32$. A pure node has $G = 0$.
5. A single deep tree has high **variance** (it fits noise and changes a lot with small data changes). A forest averages many trees that were made different by bootstrap samples and random feature subsets. Averaging decorrelated errors reduces variance with little increase in bias.
6. Iteration 1: with centroids 1 and 3.5, points 1 and 2 are closer to 1, so {1, 2} → cluster 1. Points 3, 10, 11 and 12 are closer to 3.5, so {3, 10, 11, 12} → cluster 2. New centroids: $\mu_1 = 1.5$, $\mu_2 = 9$.
   Iteration 2: 1 and 2 go to $\mu_1$; 3 is closer to 1.5 (1.5) than to 9 (6), so it moves to cluster 1; 10, 11, 12 go to cluster 2. Centroids: $\mu_1 = 2$, $\mu_2 = 11$. This has converged.
7. k-means makes **hard** assignments with spherical, equal-variance clusters. A GMM makes **soft** (probabilistic) assignments, each cluster has its own covariance (elliptical shapes, different sizes) and mixing weight, and it is fitted by maximum likelihood (EM).

## Level 3
8. Total 1000. Accuracy $= 970/1000 = 97\%$. Precision $= 40/60\approx0.67$. Recall $= 40/50 = 0.8$. Specificity $= 930/950\approx0.979$. F1 $= 2\cdot\frac{0.67\cdot0.8}{0.67 + 0.8}\approx0.73$. (High accuracy hides the fact that one third of the alarms are false.)
9. Accuracy 95 %; balanced accuracy $= (1.0 + 0.0)/2 = 50\%$, i.e. chance. With imbalanced classes, accuracy is meaningless on its own. Report balanced accuracy, per-class recall, or AUC.
10. AUC 0.5: no separation (chance). AUC 0.9: a random positive is ranked above a random negative in 90 % of pairs. Yes: AUC only measures **ranking**. The predicted probabilities can still be systematically too high or too low (poor calibration).

## Level 4
11. Reasons: **non-stationarity** (electrode drift, changed neurons or units, plasticity, changes in behavioural state), or **overfitting** to session-specific noise. Remedies: train on multiple days, recalibrate daily, use features that are stable over time (latent dynamics alignment), regularise more.
12. No. Decoding shows that information about speed is **present and linearly readable** in V1. It may reflect modulation by locomotion or arousal (inputs), not a computation V1 performs or that downstream areas use. Causal tests are needed (perturbation) together with behavioural relevance.
13. A kernel computes dot products in a high-dimensional feature space without constructing it, so a linear algorithm can learn nonlinear boundaries. With $p\gg n$, the data are already linearly separable in input space and a flexible RBF kernel overfits easily (high variance). A regularised linear model is usually as good and more interpretable.
14. Pairs (3 × 3 = 9). 0.9 beats all three negatives (3); 0.8 beats all three (3); 0.4 beats 0.3 and 0.2 (2) but not 0.7. Total 8/9, so AUC ≈ 0.89.
