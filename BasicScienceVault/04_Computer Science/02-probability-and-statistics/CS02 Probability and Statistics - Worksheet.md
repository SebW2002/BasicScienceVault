---
tags: [computer-science, probability, statistics, type/worksheet]
---
# CS02 Probability and Statistics – Worksheet

> Theory: [[CS02 Probability and Statistics]] · Solutions: [[CS02 Probability and Statistics - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮. $e^{-2}\approx0.135$, $0.95^{20}\approx0.36$.

## Level 1 – Distributions & expectation
1. A neuron fires at 20 Hz. What is the expected spike count in a 100 ms window? What is the variance if the spikes are Poisson?
2. With $\lambda = 2$, compute $P(N = 0)$ and $P(N = 2)$ for a Poisson count.
3. $X$ has mean 3 and variance 4. Compute $\mathbb E[2X + 1]$ and $\text{Var}(2X + 1)$.
4. A synapse has 5 release sites with $p = 0.2$. Mean and variance of the number of released vesicles?
5. Spike counts over 5 trials: 4, 6, 5, 3, 7. Compute the mean, the variance (divide by $n - 1$) and the Fano factor.

## Level 2 – Bayes, MLE, MAP
6. A seizure detector flags 95 % of real seizures and falsely flags 2 % of non-seizure windows. 1 % of windows contain seizures. What is the probability that a flagged window really contains a seizure?
7. Derive the MLE of the Poisson rate $\lambda$ for counts $x_1,\dots,x_n$. Compute it for the counts 3, 5, 4.
8. **Cue combination:** vision estimates a position with σ = 2, touch with σ = 1 (Gaussian, independent). What are the optimal weights and the variance of the combined estimate?
9. Why does a Gaussian prior on regression weights correspond to L2 regularisation? (Write down the log-posterior.)

## Level 3 – Correlation & testing
10. Compute the covariance and correlation of $x = (1, 2, 3)$ and $y = (2, 4, 6)$. And of $x$ and $z = (3, 2, 1)$?
11. Explain what "p = 0.03" means and what it does not mean.
12. Two groups have means 10 and 12 with pooled SD 4. Compute Cohen's $d$. Is this large?
13. With 20 independent tests at α = 0.05 and no true effects, what is the probability of at least one false positive? What is the Bonferroni threshold?
14. Apply Benjamini–Hochberg with $q = 0.05$ to the p-values 0.001, 0.008, 0.039, 0.041, 0.20 ($m = 5$). Which are significant?

## Level 4 – Resampling & neuro transfer
15. Describe how to test whether a decoder's accuracy of 62 % (two classes, 100 trials) is above chance using a permutation test.
16. You record 200 cells from 4 mice and compare two conditions. Why is treating the 200 cells as independent samples problematic? How would you bootstrap correctly?
17. 🧮 Using the Poisson distribution with $\lambda = 3$, compute $P(N\ge5)$.
