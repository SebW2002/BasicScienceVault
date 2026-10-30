---
tags: [computer-science, probability, statistics, type/solution]
---
# CS02 Probability and Statistics – Solutions

> Worksheet: [[CS02 Probability and Statistics - Worksheet]] · Theory: [[CS02 Probability and Statistics]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. $\lambda = 20\cdot0.1 = 2$ spikes; variance also 2.
2. $P(0) = e^{-2}\approx0.135$; $P(2) = \frac{4e^{-2}}{2}\approx0.27$.
3. $\mathbb E = 2\cdot3 + 1 = 7$; $\text{Var} = 4\cdot4 = 16$ (adding a constant doesn't change variance).
4. Mean $np = 1$; variance $np(1-p) = 0.8$.
5. Mean 5; squared deviations $1 + 1 + 0 + 4 + 4 = 10$, so variance $10/4 = 2.5$; Fano factor $2.5/5 = 0.5$ (more regular than Poisson).

## Level 2
6. $\frac{0.95\cdot0.01}{0.95\cdot0.01 + 0.02\cdot0.99} = \frac{0.0095}{0.0095 + 0.0198} = \frac{0.0095}{0.0293}\approx32\,\%$. Two out of three alarms are false.
7. $\ell(\lambda) = \sum_i[x_i\ln\lambda - \lambda - \ln x_i!]$, so $\frac{d\ell}{d\lambda} = \frac{\sum x_i}{\lambda} - n = 0$ and $\hat\lambda = \bar x$. For 3, 5, 4: $\hat\lambda = 4$.
8. Reliabilities $1/4$ and $1$: weights $w_V = \frac{1/4}{5/4} = 0.2$, $w_T = 0.8$. Combined variance $\frac{1}{1/4 + 1} = 0.8$ (σ ≈ 0.89, better than touch alone).
9. $\log P(\mathbf w\mid D) = \log P(D\mid\mathbf w) + \log P(\mathbf w) + \text{const}$. With the prior $\mathbf w\sim\mathcal N(0, \tau^2I)$: $\log P(\mathbf w) = -\frac{\lVert\mathbf w\rVert^2}{2\tau^2} + \text{const}$. Maximising the posterior means minimising $-\log\text{likelihood} + \lambda\lVert\mathbf w\rVert^2$ with $\lambda = \frac{1}{2\tau^2}$, which is L2 regularisation (ridge).

## Level 3
10. $x$: mean 2; $y$: mean 4. $\text{Cov} = \frac{(-1)(-2) + 0 + (1)(2)}{2} = 2$; $\sigma_x = 1$, $\sigma_y = 2$, so $\rho = 1$. For $z$: $\text{Cov} = \frac{(-1)(1) + 0 + (1)(-1)}{2} = -1$, so $\rho = -1$.
11. It means: **if** $H_0$ were true, data at least this extreme would occur in 3 % of repetitions. It does **not** mean: a 3 % probability that $H_0$ is true, a 97 % probability that the effect is real, or that the effect is large or important.
12. $d = 2/4 = 0.5$, a medium effect.
13. $1 - 0.95^{20}\approx1 - 0.36 = 0.64$. Bonferroni: $0.05/20 = 0.0025$.
14. Thresholds $\frac{k}{5}\cdot0.05$: 0.01, 0.02, 0.03, 0.04, 0.05. Comparisons: $0.001\le0.01$ ✓, $0.008\le0.02$ ✓, $0.039 > 0.03$ ✗, $0.041 > 0.04$ ✗, $0.20 > 0.05$ ✗. The largest $k$ satisfying the condition is $k = 2$, so **the first two** are significant.

## Level 4
15. (1) Compute the real cross-validated accuracy (62 %). (2) Randomly shuffle the class labels across trials (keeping the label counts), re-run the **entire** cross-validated decoding pipeline and store the accuracy. (3) Repeat 1000+ times to build the null distribution. (4) p = fraction of shuffled accuracies ≥ 62 % (with +1 correction in numerator and denominator). Note: with 100 trials, chance-level accuracies spread quite widely around 50 %, so 62 % may or may not be significant.
16. Cells from the same mouse share genetics, preparation and state, so they are **not independent** (pseudoreplication). This inflates the effective $n$ and gives too-small p-values. Better: use **mixed models** (mouse as a random effect), or a **hierarchical bootstrap**: resample mice with replacement, then cells within each selected mouse.
17. $P(N\le4) = e^{-3}\left(1 + 3 + \frac92 + \frac{27}{6} + \frac{81}{24}\right) = e^{-3}\cdot16.375\approx0.0498\cdot16.375\approx0.815$, so $P(N\ge5)\approx0.185$.
