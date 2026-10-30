---
aliases: [Optimization, Gradient Descent, SGD, Adam, Regularization, Bias-Variance, Lagrange Multipliers, Optimierung]
tags: [computer-science, optimization, gradient-descent, regularization, type/overview, neuro]
---
# CS04 Optimization

> [[MOC-computer-science|↑ CS MOC]] · [[CS04 Optimization - Worksheet|✏️ Worksheet]] · [[CS04 Optimization - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
Fitting **any** model, from a regression line to a deep network or a biophysical neuron model, means finding parameters that minimise a loss. How you define the loss, how you search, and how you prevent overfitting decide whether the result is meaningful. Learning in the brain is also often described as optimisation: synaptic plasticity as gradient descent on some objective.

## Loss and objective functions
An **objective function** $J(\theta)$ is what we optimise; a **loss** $L$ is minimised (often averaged over data points, $J(\theta) = \frac1N\sum_iL(y_i, f_\theta(\mathbf x_i))$ + regularisation).
| Loss | Formula | Use / probabilistic meaning |
|---|---|---|
| Mean squared error | $\frac1N\sum(y_i - \hat y_i)^2$ | regression; MLE under Gaussian noise |
| Mean absolute error | $\frac1N\sum\lvert y_i - \hat y_i\rvert$ | robust to outliers; Laplace noise |
| Cross-entropy | $-\sum_kt_k\log\hat p_k$ | classification ([[CS03 Information Theory]]) |
| Poisson negative log-likelihood | $\sum(\hat\lambda_i - y_i\log\hat\lambda_i)$ | spike-count models (GLMs, [[CS09 Probabilistic and Bayesian Models]]) |
| Hinge | $\max(0, 1 - y\cdot f(\mathbf x))$ | SVM ([[CS07 Machine Learning Fundamentals]]) |

**General principle:** minimising negative log-likelihood = maximum likelihood ([[CS02 Probability and Statistics]]).

## Gradient descent and its variants
**Gradient descent:**
$$\theta_{t+1} = \theta_t - \eta\,\nabla_\theta J(\theta_t)$$
($\eta$ = **learning rate**). Step against the gradient, i.e. downhill ([[CS01 Mathematical Foundations]]).
- $\eta$ too small: very slow. $\eta$ too large: oscillation or **divergence**. For a quadratic $J = \frac a2(\theta - \theta^*)^2$, each step multiplies the error by $(1 - \eta a)$, so convergence requires $0 < \eta < 2/a$.
- **Ill-conditioning:** if curvature differs strongly between directions (Hessian eigenvalues spread), gradient descent zig-zags in a narrow valley. Feature standardisation helps.

| Variant | Update | Idea |
|---|---|---|
| **Batch GD** | gradient over all $N$ samples | exact but expensive |
| **Stochastic GD (SGD)** | gradient over a random **mini-batch** (e.g. 32–512 samples) | cheap, noisy steps; the noise can help escape saddles and sharp minima |
| **Momentum** | $\mathbf v\leftarrow\beta\mathbf v + \nabla J$; $\theta\leftarrow\theta - \eta\mathbf v$ ($\beta\approx0.9$) | a rolling ball: averages out zig-zags, accelerates along consistent directions |
| **Adam** | running mean $\mathbf m$ and running mean square $\mathbf s$ of gradients (with bias correction); $\theta\leftarrow\theta - \eta\frac{\hat{\mathbf m}}{\sqrt{\hat{\mathbf s}} + \epsilon}$ | momentum + **per-parameter adaptive step size**; the default in deep learning |
| Second-order (Newton, L-BFGS) | uses curvature (Hessian) $\theta\leftarrow\theta - H^{-1}\nabla J$ | fast near minima; used for small, smooth problems (GLMs, model fitting) |

**Learning-rate schedules:** decay, warm-up, cosine annealing. **Early stopping:** stop when the validation loss rises ([[CS06 Data Science Workflow]]).

## Convexity, local vs. global minima
- A function is **convex** if the line segment between any two points on its graph lies above the graph: $f(\lambda x + (1-\lambda)y)\le\lambda f(x) + (1-\lambda)f(y)$. Equivalently (if twice differentiable), $f''\ge0$, or the Hessian is positive semi-definite.
- **Convex problems:** every local minimum is a **global** minimum, so the optimiser can't get stuck. Examples: linear regression (MSE), logistic regression, Poisson GLMs with canonical link, lasso, ridge, SVMs.
- **Non-convex problems:** neural networks, biophysical model fitting, k-means. These have many local minima and **saddle points** (in high dimensions, saddles are far more common than bad local minima). Use multiple random initialisations, and report variability across seeds.
- Critical point: $\nabla J = 0$. Classify by Hessian eigenvalues: all > 0 means minimum; mixed signs mean saddle ([[CS01 Mathematical Foundations]], [[B8 Curve Sketching]]).

## Regularisation and the bias–variance trade-off
Adding a penalty to discourage overly complex solutions:
$$J(\mathbf w) = \text{Loss}(\mathbf w) + \lambda\,R(\mathbf w)$$
| Regulariser | $R(\mathbf w)$ | Effect | Bayesian view |
|---|---|---|---|
| **L2 (ridge, weight decay)** | $\lVert\mathbf w\rVert_2^2 = \sum w_i^2$ | shrinks all weights smoothly towards 0; handles collinearity | Gaussian prior |
| **L1 (lasso)** | $\lVert\mathbf w\rVert_1 = \sum\lvert w_i\rvert$ | drives many weights **exactly to 0**, i.e. sparse feature selection | Laplace prior |
| Elastic net | mix of L1 and L2 | sparse + stable for correlated features | – |
| Smoothness | $\sum(w_{i+1} - w_i)^2$ | smooth temporal or spatial filters (receptive fields) | Gaussian process prior |

- **Ridge closed form:** $\hat{\mathbf w} = (X^TX + \lambda I)^{-1}X^T\mathbf y$. Adding $\lambda I$ makes the matrix invertible even when $X^TX$ is singular ([[C2 Determinants]]).
- **Why L1 gives zeros:** the L1 ball has corners on the axes, so the optimum often lands on a corner.
- **Choose λ by cross-validation**, never on the test set.

**Bias–variance decomposition** of the expected squared error at a point:
$$\mathbb E[(y - \hat f)^2] = \underbrace{(\mathbb E[\hat f] - f)^2}_{\text{bias}^2} + \underbrace{\text{Var}(\hat f)}_{\text{variance}} + \underbrace{\sigma^2}_{\text{irreducible noise}}$$
- **Simple models** have high bias and low variance (underfit). **Complex models** have low bias and high variance (overfit). Regularisation trades a bit of bias for a large reduction in variance.
- In modern deep learning, heavily over-parameterised models can generalise well anyway ("double descent"), but the trade-off still explains most classical situations.

## Constrained optimisation and Lagrange multipliers (conceptual)
To optimise $f(\mathbf x)$ subject to $g(\mathbf x) = 0$: at the optimum, the gradients are parallel,
$$\nabla f = \mu\,\nabla g$$
Equivalently, find stationary points of the **Lagrangian** $\mathcal L(\mathbf x, \mu) = f(\mathbf x) - \mu\,g(\mathbf x)$.
- **Example:** maximise $xy$ subject to $x + y = 10$: $(y, x) = \mu(1, 1)$, so $x = y = 5$, giving the maximum 25.
- **Interpretation:** $\mu$ is the "price" of the constraint, i.e. how much the optimum improves if the constraint is relaxed slightly.
- Inequality constraints use KKT conditions (the basis of SVMs).
- **Neuro / science uses:**
  - **maximum-entropy distributions** under constraints (fixed mean gives the exponential distribution; fixed mean and variance give the Gaussian; Boltzmann under fixed mean energy)
  - **efficient coding** under energy or spike constraints
  - optimal control of movements (minimise effort subject to reaching the target)

## In neuroscience #neuro
- **Model fitting:** biophysical models (Hodgkin–Huxley parameters), encoding models (GLMs), drift-diffusion models of decisions, all by minimising losses.
- **Synaptic plasticity as optimisation (analogy):**
  - The **delta rule** $\Delta w = \eta(t - y)x$ is gradient descent on squared error.
  - Cerebellar learning is often modelled as supervised error correction (climbing-fibre error signal).
  - Dopamine-modulated plasticity implements reinforcement-learning updates.
  - Whether cortex computes true gradients (as backprop does) is an open question ([[CS10 Dynamical and Computational Neuro Models]]).
- **Weight decay ↔ homeostatic plasticity:** both keep weights bounded, but homeostasis regulates activity, not a loss term.

## Math links #math-link
- Partial derivatives, gradients, Jacobians, multiple integrals → [[B11 Multivariable Calculus]]
- Derivatives, extrema, second-derivative test → [[B6 Differentiation Rules]], [[B8 Curve Sketching]]
- Gradients, Hessians → [[CS01 Mathematical Foundations]]
- Convergence of the iteration: geometric sequence $(1 - \eta a)^t$ → [[A7 Sums Products and Factorials]], [[B5 Limits and Continuity]]
- Ridge: matrix inverse, determinant ≠ 0 → [[C1 Matrices]], [[C2 Determinants]]
- Eigenvalues of the Hessian and conditioning → [[C4 Eigenvalues and Eigenvectors]]

## Connections
- In code → [[Py08 SciPy Scientific Computing]] (`scipy.optimize`), [[Py09 Python Machine Learning Libraries]] (optimisers in PyTorch)
- Losses from likelihoods → [[CS02 Probability and Statistics]], [[CS03 Information Theory]]
- Overfitting, validation → [[CS06 Data Science Workflow]], [[CS07 Machine Learning Fundamentals]]
- Training deep networks → [[CS08 Deep Neural Networks]]
- Plasticity → [[Bio06 Synapses and Neurotransmitters]]

## Key takeaways
- Fitting = minimising a loss; negative log-likelihood is the principled default.
- GD: $\theta\leftarrow\theta - \eta\nabla J$; SGD uses mini-batches; momentum smooths; Adam adapts per parameter.
- Convex: every local minimum is global (linear/logistic regression, GLMs). Neural networks are non-convex.
- L2 shrinks (Gaussian prior), L1 sparsifies (Laplace prior). Choose λ by cross-validation. Error = bias² + variance + noise.
- Lagrange: at a constrained optimum, $\nabla f\parallel\nabla g$.
