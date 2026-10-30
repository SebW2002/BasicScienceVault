---
tags: [computer-science, bayes, type/solution]
---
# CS09 Probabilistic and Bayesian Models – Solutions

> Worksheet: [[CS09 Probabilistic and Bayesian Models - Worksheet]] · Theory: [[CS09 Probabilistic and Bayesian Models]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. Posterior $\text{Beta}(2 + 7, 2 + 3) = \text{Beta}(9, 5)$; mean $9/14\approx0.64$. MLE $= 0.7$. The prior (mean 0.5) pulls the estimate slightly towards 0.5.
2. Precisions: prior $1/4$, measurement $1$, posterior $1.25$, so the variance is $0.8$. Mean $= \frac{0\cdot\frac14 + 3\cdot1}{1.25} = 2.4$. The estimate lies closer to the more reliable measurement.
3. **Credible interval:** given the data (and prior), θ lies in the interval with 95 % probability. **Confidence interval:** a procedure that, over many repetitions, captures the fixed true θ in 95 % of cases. One particular CI either contains θ or not.

## Level 2
4. Distance 0: 1. Distance 1: $e^{-0.5}\approx0.61$. Distance 2: $e^{-2}\approx0.14$. Increasing $\ell$ makes correlations decay more slowly, giving **smoother** functions.
5. **Far from the training points**: the kernel correlations with observed points are small, so the data provide little information and the variance returns to the prior variance $\sigma_f^2$ (plus noise).
6. Solve $\pi_E = 0.9\pi_E + 0.3\pi_D$, which gives $0.1\pi_E = 0.3\pi_D$, so $\pi_E = 3\pi_D$. With $\pi_E + \pi_D = 1$: $\pi = (0.75, 0.25)$. Dwell times: E: $1/(1 - 0.9) = 10$ steps; D: $1/(1 - 0.7)\approx3.3$ steps.
7. a) Viterbi b) Baum–Welch (EM) c) forward–backward (smoothing)

## Level 3
8. $R = 4$: $K = \frac{4}{4 + 4} = 0.5$; $\hat x = 10 + 0.5\cdot4 = 12$; $P = (1 - 0.5)\cdot4 = 2$. $R = 1$: $K = 0.8$; $\hat x = 10 + 3.2 = 13.2$; $P = 0.2\cdot4 = 0.8$. A more reliable measurement gets more weight.
9. **Prediction:** process noise $Q$ is added and dynamics spread out the uncertainty, so we know less about the future than the present. **Update:** a new measurement adds information (precisions add), so uncertainty decreases.
10. $\min(1, 0.1/0.2) = 0.5$. With $p(\theta') = 0.4$: $\min(1, 2) = 1$ (always accept). Only the **ratio** matters, so the normalising constant $p(D)$ cancels, which is why MCMC works even though the evidence is usually intractable.
11. Advantage: much faster, scales to large data and models (optimisation instead of sampling). Disadvantage: approximate and biased; it usually **underestimates** posterior uncertainty and can miss multimodality.

## Level 4
12. $x = 0$: 5 Hz. $x = 1$: $5e\approx13.6$ Hz. $x = -2$: $5e^{-2}\approx0.68$ Hz. The exponential keeps rates **positive** for any input, gives multiplicative effects (an additive change in input is a multiplicative change in rate), and, as the canonical link for Poisson, makes the log-likelihood concave.
13. Strongly negative at 1–3 ms: **refractoriness** (spiking is suppressed right after a spike). Slightly positive at 5–10 ms: a **rebound** tendency, i.e. bursting or rhythmic firing (a preferred interval of 5–10 ms).
14. Latent state = cursor kinematics (position, velocity), with linear dynamics (smooth movements). Observation model = firing rates of recorded neurons as a linear function of velocity (their tuning, fitted during calibration). At each time step, the filter **predicts** the next kinematics from the dynamics, **compares** the predicted with the observed firing rates, and **corrects** the estimate in proportion to the Kalman gain. The result is a smooth, noise-robust cursor trajectory.
15. $\text{Beta}(9, 5)$: $\text{Var} = \frac{45}{196\cdot15} = \frac{45}{2940}\approx0.0153$; SD ≈ 0.124.
