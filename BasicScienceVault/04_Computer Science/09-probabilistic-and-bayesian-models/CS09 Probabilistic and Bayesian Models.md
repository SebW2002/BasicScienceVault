---
aliases: [Probabilistic and Bayesian Models, Bayesian Inference, Gaussian Process, Hidden Markov Model, Kalman Filter, MCMC, Variational Inference, GLM Spike Trains]
tags: [computer-science, bayes, hmm, kalman, glm, type/overview, neuro]
---
# CS09 Probabilistic and Bayesian Models

> [[MOC-computer-science|↑ CS MOC]] · [[CS09 Probabilistic and Bayesian Models - Worksheet|✏️ Worksheet]] · [[CS09 Probabilistic and Bayesian Models - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
Probabilistic models describe data **together with their uncertainty**. They let us infer hidden quantities we can't measure directly: latent brain states, the intended movement of a BCI user, the stimulus feature driving a neuron. They are also candidate models of what the brain itself does: inferring hidden causes of noisy sensory input.

## Bayesian inference and posterior distributions
$$p(\theta\mid D)\propto p(D\mid\theta)\,p(\theta)$$
- The result is a **distribution** over parameters, not a single best value. Summarise it with the posterior mean or median, a **credible interval** ("95 % probability that θ lies in this interval, given model and data"; a frequentist CI has a different meaning), or full samples.
- **Conjugate priors** give closed-form posteriors:
  - **Beta–Binomial:** prior $\text{Beta}(a, b)$ on a probability $p$; observe $k$ successes in $n$ trials; posterior $\text{Beta}(a + k,\ b + n - k)$. The posterior mean is $\frac{a + k}{a + b + n}$, a compromise between the prior mean and the data.
  - **Gaussian–Gaussian:** prior $\mathcal N(\mu_0, \sigma_0^2)$ plus measurement $x$ with noise $\sigma^2$ give a posterior mean that is the **precision-weighted average**, $\mu_\text{post} = \frac{\mu_0/\sigma_0^2 + x/\sigma^2}{1/\sigma_0^2 + 1/\sigma^2}$, and a posterior precision that is the **sum of precisions**.
- **Posterior predictive** distribution: average predictions over the posterior.
- **Model comparison:** marginal likelihood $p(D\mid M) = \int p(D\mid\theta, M)p(\theta\mid M)d\theta$ and **Bayes factors**. Approximations: BIC, cross-validation (LOO).
- **Hierarchical models:** parameters of individual subjects or neurons are drawn from a group distribution, so individual estimates "borrow strength" from the group (partial pooling), which is ideal for multi-animal data.

## Gaussian processes as priors over functions
- A **Gaussian process** $f\sim\mathcal{GP}(m(x), k(x, x'))$ is a distribution over functions: any finite set of function values is jointly Gaussian, with covariance given by the **kernel** $k$.
- **RBF (squared exponential) kernel:** $k(x, x') = \sigma_f^2\exp\!\left(-\frac{(x - x')^2}{2\ell^2}\right)$. The **length scale** $\ell$ sets how quickly the function can vary; $\sigma_f$ sets its amplitude.
- **GP regression:** conditioning on noisy observations gives a posterior mean (prediction) **and** a posterior variance (uncertainty that grows away from data), all in closed form by Gaussian algebra (cost $O(n^3)$).
- **Neuro:**
  - smooth tuning curves and place fields with uncertainty
  - **GPFA** (Gaussian-process factor analysis) for smooth single-trial latent trajectories (Yu et al. 2009)
  - Bayesian optimisation of stimulation parameters (DBS, closed-loop experiments)

## Hidden Markov models (HMMs)
- A **hidden state** $s_t\in\{1,\dots,K\}$ evolves as a Markov chain with **transition matrix** $A_{ij} = P(s_{t+1} = j\mid s_t = i)$ (rows sum to 1). Each state emits observations according to an **emission distribution** $P(y_t\mid s_t)$ (e.g. Poisson spike counts, Gaussian features).
- **Algorithms:**
  - **forward algorithm**: likelihood and filtered state probabilities
  - forward–backward: smoothed state probabilities
  - **Viterbi**: the most likely state sequence
  - **Baum–Welch** (EM): learn $A$ and the emissions from data
- **Stationary distribution** $\boldsymbol\pi$: $\boldsymbol\pi^TA = \boldsymbol\pi^T$, the left eigenvector with eigenvalue 1 ([[C4 Eigenvalues and Eigenvectors]]). Expected dwell time in state $i$: $\frac{1}{1 - A_{ii}}$.
- **Neuro:**
  - UP/DOWN states in cortex
  - discrete states in population activity during decisions
  - behavioural states (engaged vs. disengaged; GLM-HMMs, Ashwood et al. 2022)
  - sleep staging
  - ion channel gating: single-channel records as open/closed states

## State-space models and the Kalman filter
- **Linear-Gaussian state-space model:**
  $$\mathbf x_t = A\mathbf x_{t-1} + \mathbf w_t,\quad\mathbf w_t\sim\mathcal N(0, Q)\qquad\text{(latent dynamics)}$$
  $$\mathbf y_t = C\mathbf x_t + \mathbf v_t,\quad\mathbf v_t\sim\mathcal N(0, R)\qquad\text{(observations)}$$
  It is like an HMM with continuous states.
- **Kalman filter:** the optimal recursive estimator of $\mathbf x_t$ from the observations up to time $t$.
  1. **Predict:** $\hat{\mathbf x}^- = A\hat{\mathbf x}$, $P^- = APA^T + Q$ (uncertainty grows).
  2. **Update:** $K = P^-C^T(CP^-C^T + R)^{-1}$ (**Kalman gain**); $\hat{\mathbf x} = \hat{\mathbf x}^- + K(\mathbf y - C\hat{\mathbf x}^-)$; $P = (I - KC)P^-$ (uncertainty shrinks).
  - Scalar intuition: $K = \frac{P^-}{P^- + R}$. If the measurement is reliable ($R$ small), $K\to1$ and the filter trusts the data. If it is noisy, $K\to0$ and the filter trusts the prediction. The update is the same precision weighting as in Bayes' theorem.
- **Neuro:**
  - **BCI cursor control**: the Kalman filter decodes intended velocity from motor cortex spikes (BrainGate)
  - tracking latent dynamics
  - models of sensorimotor integration (the brain combines predictions from an internal forward model with sensory feedback)
  - Rauch–Tung–Striebel smoothing for offline analysis

## MCMC and variational inference (conceptual)
Most posteriors have no closed form. Two families of approximations:
| | **MCMC** (Markov chain Monte Carlo) | **Variational inference (VI)** |
|---|---|---|
| Idea | construct a random walk whose long-run distribution is the posterior; collect **samples** | choose a simple family $q(\theta)$ (e.g. Gaussian) and **optimise** it to be close to the posterior: minimise $D_{KL}(q\|p)$, i.e. maximise the ELBO |
| Example | **Metropolis–Hastings**: propose $\theta'$, accept with probability $\min\left(1, \frac{p(\theta'\mid D)}{p(\theta\mid D)}\right)$ (for symmetric proposals; only ratios are needed, so the normalising constant cancels); Hamiltonian MC / NUTS (Stan, PyMC) | mean-field VI; amortised VI in VAEs ([[CS08 Deep Neural Networks]]) |
| Pros | asymptotically exact; flexible | fast, scales to big data and big models |
| Cons | slow; must check convergence (multiple chains, $\hat R$) | biased (typically underestimates uncertainty) |

Link to [[CS03 Information Theory]] (KL, ELBO) and to the **free-energy principle** in theoretical neuroscience.

## Generalised linear models (GLMs) for spike trains and neural encoding
- **GLM:** linear predictor $\eta = \mathbf w^T\mathbf x$ → **link function** → distribution. Linear regression (identity link, Gaussian) and logistic regression (logit link, Bernoulli) are special cases.
- **Poisson GLM for spikes:**
  $$\lambda(t) = \exp\!\left(\mathbf k^T\mathbf s(t) + \mathbf h^T\mathbf y_\text{hist}(t) + \sum_j\mathbf c_j^T\mathbf y_j(t) + b\right),\qquad y(t)\sim\text{Poisson}(\lambda(t)\Delta t)$$
  - $\mathbf k$: **stimulus filter** (receptive field)
  - $\mathbf h$: **spike-history filter** (refractoriness, bursting)
  - $\mathbf c_j$: **coupling filters** to other neurons
  - The exponential (log link) keeps rates positive.
  - The **log-likelihood is concave**, so a unique optimum exists and fitting is reliable ([[CS04 Optimization]]).
- The **LNP** model (linear–nonlinear–Poisson) is the simplest case. Pillow et al. (2008) used coupled GLMs to show that correlations in retinal ganglion cell populations carry stimulus information.
- **Uses:** estimating receptive fields, quantifying how much behaviour vs. stimulus drives a neuron, building encoding models of whole populations.

## In neuroscience #neuro
- **Bayesian brain / predictive coding:** perception as posterior inference (priors + likelihoods); illusions and adaptation explained as optimal inference under particular priors; cue combination ([[CS02 Probability and Statistics]]).
- **Uncertainty in analyses:** hierarchical Bayesian models for multi-level data (trials within neurons within animals) give honest uncertainty.

## Math links #math-link
- Differential equations (steady state, time constant, stability, Euler steps) → [[B10 Differential Equations]]
- Gaussian algebra (precision-weighted averages) → [[A5 Fractions]]
- Transition matrices, eigenvectors with eigenvalue 1 → [[C4 Eigenvalues and Eigenvectors]], [[C1 Matrices]]
- Exponential link function → [[B2 Exponential Functions]]; log-likelihood → [[A3 Logarithms]]
- Integrals for marginal likelihoods → [[B7 Antiderivatives and Integration]]
- Kernel functions as distance-based similarities → [[CS01 Mathematical Foundations]]

## Connections
- In code → [[R08 R Mixed-Effects Models]] (brms), [[R09 R Neuroscience Packages]] (BayesFactor, rstan), [[R07 R Statistical Modelling]] (Poisson GLMs)
- Bayes, MLE/MAP, distributions → [[CS02 Probability and Statistics]]
- KL, ELBO → [[CS03 Information Theory]]
- Kernels in SVMs; GMMs → [[CS07 Machine Learning Fundamentals]]
- Dynamical models → [[CS10 Dynamical and Computational Neuro Models]]
- Spike trains → [[CS11 Time Series and Signal Processing]]

## Key takeaways
- Posterior ∝ likelihood × prior. Conjugate examples: Beta–Binomial; Gaussian = precision-weighted average.
- GP = prior over functions defined by a kernel; it gives predictions with uncertainty.
- HMM: discrete hidden states, transition matrix, emissions; Viterbi, forward–backward, Baum–Welch.
- Kalman filter: predict (uncertainty ↑), update with gain $K$ (uncertainty ↓). Used in BCIs.
- MCMC samples (exact but slow); VI optimises an approximation (fast but biased).
- Poisson GLM: $\lambda = \exp(\text{stimulus filter} + \text{history} + \text{coupling})$, with a concave likelihood.
