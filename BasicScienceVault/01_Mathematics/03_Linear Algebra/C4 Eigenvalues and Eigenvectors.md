---
aliases: [Eigenvalues and Eigenvectors, Eigenvalues, Eigenwerte, Eigenvektoren]
tags: [linear-algebra, eigenvalue, matrix, type/overview, neuro]
---
# C4 Eigenvalues and Eigenvectors

> [[C0 Linear Algebra MOC|↑ Linear Algebra MOC]] · [[C4 Eigenvalues and Eigenvectors - Worksheet|✏️ Worksheet]] · [[C4 Eigenvalues and Eigenvectors - Solutions|✅ Solutions]] · [[Mistakes - Linear Algebra|⚠️ Mistake log]]

## Why this matters
Eigenvectors are the "natural directions" of a matrix – directions that are only stretched, not rotated. This one idea underlies **PCA** (the most used dimensionality-reduction method in neuroscience), the **stability** of neural dynamics, the behaviour of **recurrent networks** and Hebbian learning.

## Definition
$$A\mathbf v = \lambda\mathbf v, \qquad \mathbf v\neq\mathbf 0$$
$\mathbf v$ is an **eigenvector**, $\lambda$ the corresponding **eigenvalue**: applying $A$ to $\mathbf v$ just scales it by $\lambda$ (flips it if $\lambda < 0$).
Eigenvectors are only defined up to a factor: if $\mathbf v$ is one, so is $2\mathbf v$ or $-\mathbf v$.

## How to compute them
1. **Characteristic polynomial:** $A\mathbf v = \lambda\mathbf v \iff (A - \lambda I)\mathbf v = \mathbf 0$ has a non-zero solution $\iff$
   $$\det(A - \lambda I) = 0$$
   For a 2×2 matrix: $\lambda^2 - \operatorname{tr}(A)\,\lambda + \det A = 0$, where $\operatorname{tr}A = a_{11} + a_{22}$.
2. Solve for the eigenvalues $\lambda_i$ ([[A8 Solving Equations]]).
3. For each $\lambda_i$, solve $(A - \lambda_iI)\mathbf v = \mathbf 0$ with Gauss ([[C3 Linear Systems and Gaussian Elimination]]) – there is always at least one free parameter.

**Example:** $A = \begin{pmatrix}4&1\\2&3\end{pmatrix}$: $\;\lambda^2 - 7\lambda + 10 = 0\Rightarrow\lambda_1 = 5$, $\lambda_2 = 2$.
- $\lambda = 5$: $\begin{pmatrix}-1&1\\2&-2\end{pmatrix}\mathbf v = 0\Rightarrow\mathbf v_1 = \begin{pmatrix}1\\1\end{pmatrix}$
- $\lambda = 2$: $\begin{pmatrix}2&1\\2&1\end{pmatrix}\mathbf v = 0\Rightarrow\mathbf v_2 = \begin{pmatrix}1\\-2\end{pmatrix}$

## Useful facts
| Fact | Formula |
|---|---|
| Sum of eigenvalues | $\lambda_1 + \dots + \lambda_n = \operatorname{tr}A$ |
| Product of eigenvalues | $\lambda_1\cdots\lambda_n = \det A$ ([[C2 Determinants]]) |
| Triangular / diagonal matrix | eigenvalues = diagonal entries |
| Singular matrix | has eigenvalue 0 |
| **Symmetric matrix** ($A = A^T$) | real eigenvalues, **orthogonal** eigenvectors |
| Powers | $A^k\mathbf v = \lambda^k\mathbf v$ |
| Complex eigenvalues $\lambda = a\pm bi$ | rotation component → oscillations ([[E2 Complex Numbers]]) |

**Diagonalisation:** if $A$ has $n$ independent eigenvectors (columns of $V$), then
$$A = V\Lambda V^{-1},\quad \Lambda = \operatorname{diag}(\lambda_1,\dots,\lambda_n), \qquad A^k = V\Lambda^kV^{-1}$$
In the eigenvector coordinate system, $A$ acts as simple independent scaling along each axis.

## Stability of dynamical systems
| System | Stable (returns to fixed point) iff |
|---|---|
| Continuous: $\frac{d\mathbf x}{dt} = A\mathbf x$ | all $\operatorname{Re}(\lambda_i) < 0$ |
| Discrete: $\mathbf x_{t+1} = A\mathbf x_t$ | all $\lvert\lambda_i\rvert < 1$ |

Complex eigenvalues → spiralling (oscillation); positive real part → explosion; the eigenvalue with the largest real part dominates the long-term behaviour. For nonlinear systems, use the **Jacobian** at the fixed point (linearisation, [[B9 Taylor Series]]).

## In neuroscience #neuro
- **PCA:** the eigenvectors of the covariance matrix $C$ ([[C1 Matrices]]) are the principal components – directions of maximal variance in neural population activity. Eigenvalue $\lambda_i$ = variance along PC $i$; explained variance $= \lambda_i/\sum\lambda_j$. Because $C$ is symmetric, the PCs are orthogonal.
- **Linear recurrent networks:** $\tau\frac{d\mathbf r}{dt} = -\mathbf r + W\mathbf r + \mathbf h$. Eigenvalues of $W$ with $\lambda > 1$ → runaway activity; $\lambda = 1$ → **line attractor** (persistent activity, e.g. oculomotor integrator); complex $\lambda$ → oscillations. Inhibition-stabilised networks are analysed exactly this way.
- **Wilson–Cowan / E–I models:** Jacobian eigenvalues with negative real part and non-zero imaginary part → damped oscillations; crossing $\operatorname{Re}\lambda = 0$ → onset of rhythmic activity (Hopf bifurcation, e.g. gamma oscillations).
- **Hebbian learning (Oja's rule):** a neuron with Hebbian plasticity converges to the **principal eigenvector** of its input covariance – the neuron "performs PCA".
- **Graph theory / connectomics:** eigenvector centrality identifies hub regions; Laplacian eigenvectors give "connectome harmonics".

## Connections
- Solutions $e^{\lambda t}\mathbf v$ of linear ODE systems → [[B10 Differential Equations]]; Hessian eigenvalues → [[B11 Multivariable Calculus]]
- $\det(A - \lambda I) = 0$ → [[C2 Determinants]]
- Eigenvectors from $(A - \lambda I)\mathbf v = 0$ → [[C3 Linear Systems and Gaussian Elimination]]
- Matrices, covariance → [[C1 Matrices]]
- Linearisation & Jacobian → [[B9 Taylor Series]], [[B6 Differentiation Rules]]
- Complex eigenvalues → [[E2 Complex Numbers]]
- Orthogonality → [[D2 Dot and Cross Product]]

## Where this is used in the vault
**Most important applications:** PCA everywhere — spike sorting, scRNA-seq, population dynamics ([[CS01 Mathematical Foundations]], [[CS11 Time Series and Signal Processing]], [[Meth06 Omics and Sequencing]]); stability of networks and neuron models ([[CS10 Dynamical and Computational Neuro Models]]); DTI ([[Ph07 Diffusion and Transport]]); HMM stationary distributions ([[CS09 Probabilistic and Bayesian Models]]).

**All notes that build on this topic:**
- *Physics:* [[Ph07 Diffusion and Transport]] · [[Ph09 Waves and Oscillations]] · [[Ph10 Signal Propagation and Cable Theory]]
- *Biology:* [[Bio05 Neurons and Action Potentials]] · [[Bio07 Neural Circuits and Systems]]
- *Methods:* [[Meth03 Electrophysiology]] · [[Meth04 In Vivo Imaging]] · [[Meth06 Omics and Sequencing]]
- *Computer Science:* [[CS01 Mathematical Foundations]] · [[CS02 Probability and Statistics]] · [[CS04 Optimization]] · [[CS08 Deep Neural Networks]] · [[CS09 Probabilistic and Bayesian Models]] · [[CS10 Dynamical and Computational Neuro Models]] · [[CS11 Time Series and Signal Processing]]
- *Programming:* [[Py05 NumPy and Arrays]] · [[Py10 Python Neuroscience Packages]] · [[MAT02 MATLAB Matrices and Vectorization]] · [[MAT09 EEGLAB]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- $\det(A - \lambda I) = 0$ → eigenvalues; $(A - \lambda I)\mathbf v = 0$ → eigenvectors.
- Check: $\sum\lambda = \operatorname{tr}A$, $\prod\lambda = \det A$.
- Symmetric matrices: real eigenvalues, orthogonal eigenvectors (→ PCA).
- Stability: $\operatorname{Re}\lambda < 0$ (continuous), $\lvert\lambda\rvert < 1$ (discrete).
