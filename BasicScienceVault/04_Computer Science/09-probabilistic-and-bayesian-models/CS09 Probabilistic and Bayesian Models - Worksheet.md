---
tags: [computer-science, bayes, type/worksheet]
---
# CS09 Probabilistic and Bayesian Models – Worksheet

> Theory: [[CS09 Probabilistic and Bayesian Models]] · Solutions: [[CS09 Probabilistic and Bayesian Models - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮. $e^{-0.5}\approx0.61$, $e^{-2}\approx0.14$, $e^{1}\approx2.72$.

## Level 1 – Bayesian updating
1. Prior on release probability $p$: $\text{Beta}(2, 2)$. You observe 7 releases in 10 trials. Give the posterior and its mean. Compare with the MLE.
2. A prior belief about a stimulus position is $\mathcal N(0, 4)$ (variance 4). A measurement gives $x = 3$ with noise variance 1. Compute the posterior mean and variance.
3. What is the difference between a 95 % credible interval and a 95 % confidence interval?

## Level 2 – GPs and HMMs
4. RBF kernel with $\sigma_f = 1$, $\ell = 1$: compute $k(x, x')$ for distances 0, 1, 2. What does increasing $\ell$ do?
5. Where is the uncertainty of a GP prediction largest, and why?
6. A two-state HMM (engaged E, disengaged D) has $A = \begin{pmatrix}0.9&0.1\\0.3&0.7\end{pmatrix}$ (rows: from E, from D). Compute the stationary distribution and the expected dwell time in each state.
7. Name the HMM algorithm for each question: a) most probable state sequence, b) learning the transition matrix, c) the probability of being in state 2 at time $t$ given all data.

## Level 3 – Kalman filter & sampling
8. Scalar Kalman update: predicted state $\hat x^- = 10$ with variance $P^- = 4$; measurement $y = 14$ with noise variance $R = 4$ ($C = 1$). Compute $K$, the updated estimate and its variance. Repeat with $R = 1$.
9. Why does the Kalman filter's uncertainty grow in the prediction step and shrink in the update step?
10. Metropolis–Hastings: the current posterior density is $p(\theta) = 0.2$; a proposal has $p(\theta') = 0.1$. What is the acceptance probability? And if $p(\theta') = 0.4$? Why don't you need the normalising constant?
11. Name one advantage and one disadvantage of variational inference compared with MCMC.

## Level 4 – GLMs and neuro transfer
12. A Poisson GLM has $\lambda = \exp(b + kx)$ with $b = \ln5$ (Hz) and $k = 1$. Compute the firing rate for $x = 0$, $x = 1$ and $x = -2$. Why use the exponential?
13. A fitted spike-history filter is strongly negative for 1–3 ms and slightly positive at 5–10 ms. Interpret.
14. Explain how a BCI uses a Kalman filter to move a cursor from motor cortex activity.
15. 🧮 Beta posterior from task 1: compute its variance using $\text{Var} = \frac{ab}{(a + b)^2(a + b + 1)}$ and give the posterior standard deviation.
