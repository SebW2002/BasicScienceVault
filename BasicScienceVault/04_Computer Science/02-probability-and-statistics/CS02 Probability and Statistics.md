---
aliases: [Probability and Statistics, Bayes Theorem, MLE, MAP, Hypothesis Testing, Bootstrap, Permutation Test]
tags: [computer-science, probability, statistics, bayes, type/overview, neuro]
---
# CS02 Probability and Statistics

> [[MOC-computer-science|↑ CS MOC]] · [[CS02 Probability and Statistics - Worksheet|✏️ Worksheet]] · [[CS02 Probability and Statistics - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
Neural data are **noisy**: the same stimulus never evokes exactly the same spikes. Probability describes this variability, and statistics lets us draw conclusions despite it. Bayes' theorem is also a leading theory of how the brain itself handles uncertainty (the "Bayesian brain").

## Random variables, distributions, expectation
- A **random variable** $X$ maps outcomes to numbers. It can be **discrete** (spike count) with a probability mass function $P(X = k)$, or **continuous** (membrane potential) with a probability density $p(x)$, where $P(a\le X\le b) = \int_a^bp(x)\,dx$.
- **Expectation:** $\mathbb E[X] = \sum_kk\,P(k)$ or $\int x\,p(x)\,dx$. It is **linear**: $\mathbb E[aX + bY] = a\mathbb E[X] + b\mathbb E[Y]$ (always, even for dependent variables).
- **Variance:** $\text{Var}(X) = \mathbb E[(X - \mu)^2] = \mathbb E[X^2] - \mu^2$. Standard deviation $\sigma = \sqrt{\text{Var}}$. Note $\text{Var}(aX) = a^2\text{Var}(X)$.
- For **independent** variables, $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$. The mean of $n$ independent samples has variance $\sigma^2/n$, so $\text{SEM} = \sigma/\sqrt n$ ([[A2 Root Rules]]).

## The four key distributions
| Distribution | Models | PMF / PDF | Mean | Variance |
|---|---|---|---|---|
| **Bernoulli**($p$) | one yes/no event (spike in a bin, release at one site) | $P(1) = p$, $P(0) = 1 - p$ | $p$ | $p(1-p)$ |
| **Binomial**($n, p$) | number of successes in $n$ independent trials (quantal release) | $\binom nkp^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| **Poisson**($\lambda$) | counts of rare independent events in a window (**spike counts**) | $\frac{\lambda^ke^{-\lambda}}{k!}$ | $\lambda$ | $\lambda$ |
| **Gaussian**($\mu,\sigma^2$) | sums of many small effects (central limit theorem); measurement noise | $\frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ |

- **Poisson spiking:** if a neuron fires at rate $r$ and spikes are independent, the count in window $T$ is Poisson with $\lambda = rT$. Inter-spike intervals are exponential ([[B2 Exponential Functions]]).
- **Fano factor** $F = \frac{\text{Var}(N)}{\mathbb E[N]}$ = 1 for Poisson. Real cortical neurons often have $F\approx1$–1.5; refractoriness pushes $F$ below 1, bursting pushes it above.
- **Central limit theorem:** sums or means of many independent variables are approximately Gaussian, whatever their own distribution.
- Binomial → Poisson when $n$ is large and $p$ small with $np = \lambda$ fixed. Binomial → Gaussian for large $n$.

## Conditional probability and Bayes' theorem
$$P(A\mid B) = \frac{P(A\cap B)}{P(B)},\qquad\text{independence: }P(A\mid B) = P(A)$$
$$\boxed{P(\theta\mid D) = \frac{P(D\mid\theta)\,P(\theta)}{P(D)}}\qquad\text{posterior} = \frac{\text{likelihood}\times\text{prior}}{\text{evidence}}$$
with $P(D) = \sum_\theta P(D\mid\theta)P(\theta)$ (law of total probability).

**Base-rate example:** a disease affects 1 % of people. A test detects 90 % of cases (sensitivity) and has 5 % false positives (specificity 95 %). After a positive test,
$$P(\text{ill}\mid+) = \frac{0.9\cdot0.01}{0.9\cdot0.01 + 0.05\cdot0.99} = \frac{0.009}{0.0585}\approx15\,\%$$
Low prior probability means most positives are false. This applies to biomarkers, seizure detectors and "significant" findings in underpowered studies alike.

## MLE and MAP
- **Likelihood** $\mathcal L(\theta) = P(D\mid\theta)$: how well parameters explain the data (a function of $\theta$, not a probability distribution over it). For independent data, $\mathcal L = \prod_iP(x_i\mid\theta)$, so we maximise the **log-likelihood** $\ell(\theta) = \sum_i\log P(x_i\mid\theta)$ ([[A3 Logarithms]]).
- **Maximum likelihood estimate:** $\hat\theta_\text{MLE} = \arg\max_\theta\ell(\theta)$. Set $\frac{d\ell}{d\theta} = 0$.
  - Poisson: $\hat\lambda = \bar x$ (the mean count).
  - Gaussian: $\hat\mu = \bar x$, $\hat\sigma^2 = \frac1n\sum(x_i - \bar x)^2$ (biased; the unbiased estimate divides by $n - 1$).
  - Gaussian noise: MLE = least squares.
- **Maximum a posteriori:** $\hat\theta_\text{MAP} = \arg\max_\theta[\log P(D\mid\theta) + \log P(\theta)]$. The prior acts as a **regulariser**: a Gaussian prior on weights gives L2 regularisation, a Laplace prior gives L1 ([[CS04 Optimization]]). With lots of data, MAP → MLE.

## Variance, covariance, correlation
- **Covariance:** $\text{Cov}(X, Y) = \mathbb E[(X - \mu_X)(Y - \mu_Y)]$; covariance matrix $C_{ij} = \text{Cov}(X_i, X_j)$ (symmetric, positive semi-definite; PCA uses it, [[CS01 Mathematical Foundations]]).
- **Pearson correlation:** $\rho = \frac{\text{Cov}(X, Y)}{\sigma_X\sigma_Y}\in[-1, 1]$. It measures **linear** association only. **Spearman** correlation uses ranks (monotonic, robust).
- **Correlation ≠ causation.** Confounds (common input, arousal, motion) create correlations.
- **Neuro:** **signal correlations** (similar tuning) vs. **noise correlations** (shared trial-to-trial fluctuations). Noise correlations can limit how much information a population carries.

## Hypothesis testing, p-values, effect sizes, multiple comparisons
- **Null hypothesis** $H_0$ (e.g. no difference). The **p-value** is the probability of data **at least as extreme** as observed, **assuming $H_0$ is true**. It is **not** the probability that $H_0$ is true.

| | $H_0$ true | $H_0$ false |
|---|---|---|
| reject $H_0$ | **type I error** (rate α, e.g. 5 %) | correct (**power** $1 - \beta$) |
| keep $H_0$ | correct | **type II error** (rate β) |

- **Tests:** t-test (means; Student's for equal variances, Welch's otherwise; paired vs. unpaired), ANOVA, χ², non-parametric (Wilcoxon, Mann–Whitney). Their assumptions (independence, normality, equal variances) matter. Repeated measures and hierarchical data (cells within animals) need **mixed models** to avoid pseudoreplication.
- **Effect sizes:** Cohen's $d = \frac{\bar x_1 - \bar x_2}{s_\text{pooled}}$ (0.2 small, 0.5 medium, 0.8 large), $r$, $R^2$, odds ratios. **Always report effect sizes and confidence intervals**, not just p-values. A tiny effect can be "significant" with large $n$.
- **Multiple comparisons:** with $m$ independent tests at α, $P(\ge1\text{ false positive}) = 1 - (1 - \alpha)^m$ (20 tests: 64 %).
  - **Bonferroni:** use $\alpha/m$. It controls the family-wise error rate (FWER) but is conservative. **Holm** is a uniformly better step-down version.
  - **Benjamini–Hochberg (FDR):** sort p-values $p_{(1)}\le\dots\le p_{(m)}$ and find the largest $k$ with $p_{(k)}\le\frac{k}{m}q$. Reject hypotheses $1\dots k$. On average, at most a fraction $q$ of the discoveries are false.

## Bootstrapping and permutation tests
- **Bootstrap** (estimating uncertainty): resample the data **with replacement** (same $n$) many times (e.g. 10,000), recompute the statistic each time, and use the distribution of results for standard errors and **confidence intervals** (e.g. 2.5th–97.5th percentiles). Few assumptions. Resample at the right level (animals, not cells, if animals are the independent units).
- **Permutation test** (testing $H_0$): if labels don't matter under $H_0$, **shuffle the labels** (e.g. condition A/B, or stimulus identities) many times and recompute the statistic. This builds the null distribution. The p-value is the fraction of shuffles with a statistic at least as extreme as the observed one. It is used for decoding accuracy vs. chance and cluster-based tests in EEG/fMRI ([[CS12 Neuroimaging Data Analysis]]).
- **Respect the dependency structure** when shuffling or resampling. Time series need circular shifts or block resampling.

## In neuroscience #neuro
- **Spike count statistics** (Poisson, Fano factor) → encoding models ([[CS09 Probabilistic and Bayesian Models]]).
- **Bayesian observer models:** combining two cues with Gaussian likelihoods gives a weighted average, with weights ∝ reliability ($1/\sigma^2$) and a combined variance $\sigma^2 = \frac{1}{1/\sigma_1^2 + 1/\sigma_2^2}$, smaller than either alone. Humans combine vision and touch close to this optimum (Ernst & Banks 2002).
- **Predictive coding:** the brain as a Bayesian inference machine, combining priors (predictions) with sensory evidence (likelihood).
- **Statistics in neuroscience papers:** low power, pseudoreplication and uncorrected multiple comparisons are common pitfalls ([[CS06 Data Science Workflow]]).

## Math links #math-link
- Partial derivatives, gradients, Jacobians, multiple integrals → [[B11 Multivariable Calculus]]
- Sums, products, factorials, binomial coefficients → [[A7 Sums Products and Factorials]], [[A6 Binomial Formulas and Theorem]]
- Log-likelihoods → [[A3 Logarithms]]; maximisation by derivative → [[B8 Curve Sketching]]
- Integrals of densities → [[B7 Antiderivatives and Integration]]
- Covariance matrix and PCA → [[C4 Eigenvalues and Eigenvectors]]
- Logic of conditional statements and negation in hypothesis testing → [[E1 Sets Logic and Quantifiers]]

## Connections
- In code → [[Py08 SciPy Scientific Computing]] (`scipy.stats`), [[R07 R Statistical Modelling]], [[R08 R Mixed-Effects Models]], [[MAT07 MATLAB Statistics Toolbox]] (permutation tests)
- Quantal release → [[Bio06 Synapses and Neurotransmitters]]
- Boltzmann probabilities → [[Ph08 Thermodynamics and Statistics]]
- Information theory builds on distributions → [[CS03 Information Theory]]
- Bayesian models → [[CS09 Probabilistic and Bayesian Models]]
- Multiple comparisons in omics and imaging → [[Meth06 Omics and Sequencing]], [[CS12 Neuroimaging Data Analysis]]

## Key takeaways
- $\mathbb E$ is linear; independent variances add; SEM $= \sigma/\sqrt n$.
- Poisson for spike counts (mean = variance, Fano factor 1); binomial for release; Gaussian by the central limit theorem.
- Bayes: posterior ∝ likelihood × prior. Base rates matter.
- MLE maximises the likelihood; MAP adds a prior, which acts as regularisation.
- p-value = P(data at least this extreme | $H_0$). Report effect sizes; correct for multiple tests (Bonferroni/Holm for FWER, BH for FDR).
- Bootstrap (resample with replacement) gives CIs; permutation (shuffle labels) gives null distributions.
