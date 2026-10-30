---
tags: [analysis, differential-equation, type/worksheet]
---
# B10 Differential Equations – Worksheet

> Theory: [[B10 Differential Equations]] · Solutions: [[B10 Differential Equations - Solutions]] · Log mistakes in [[Mistakes - Analysis]]
> No calculator unless marked 🧮. $e^{-1}\approx0.37$, $\ln2\approx0.69$.

## Level 1 – Checking and basic solutions
1. Check that $x(t) = 3e^{-2t}$ solves $\dot x = -2x$ with $x(0) = 3$.
2. Solve $\dot x = -0.5x$, $x(0) = 4$. What is $x(2)$?
3. Solve $\dot N = 0.1N$, $N(0) = 100$. When has $N$ doubled?
4. Classify: order, linear or non-linear? a) $\dot x = -3x + 2$ b) $\ddot x + 4x = 0$ c) $\dot x = x^2$ d) $\frac{\partial c}{\partial t} = D\frac{\partial^2c}{\partial x^2}$

## Level 2 – Steady state and time constant
5. For $\dot x = 6 - 2x$ with $x(0) = 0$: find $x_\infty$, τ and the full solution.
6. Membrane: $10\,\text{ms}\cdot\frac{dV}{dt} = -(V + 70) + 20$ (mV). Find $V_\infty$, τ and $V(t)$ for $V(0) = -70$ mV. What is $V$ after 10 ms?
7. Use separation of variables to solve $\frac{dx}{dt} = -kx$ step by step.
8. Gating variable: $\frac{dn}{dt} = \alpha(1 - n) - \beta n$ with $\alpha = 3\,\text{ms}^{-1}$, $\beta = 1\,\text{ms}^{-1}$ (at a fixed voltage). Find $n_\infty$ and $\tau_n$.

## Level 3 – Stability and systems
9. Find the fixed points of $\dot x = x(1 - x)$ and classify their stability. Sketch the phase line.
10. Same for $\dot x = x^2 - 4$.
11. $\dot{\mathbf x} = A\mathbf x$ with $A = \begin{pmatrix}-1&0\\0&-3\end{pmatrix}$. Write the general solution. Which component decays faster?
12. Write $\ddot x = -4x$ as a first-order system. Compute the eigenvalues of the system matrix. What is the period of the oscillation?

## Level 4 – Numerics and applications
13. Two Euler steps with $\Delta t = 0.5$ for $\dot x = -x$, $x(0) = 1$. Compare with $e^{-1}\approx0.37$. What happens with $\Delta t = 2.5$?
14. A drug is cleared with half-life 4 h ($\dot c = -kc$). Compute $k$. What fraction remains after 12 h?
15. 🧮 mRNA: $\dot m = k - \gamma m$ with $k = 10$ molecules/min and $\gamma = 0.05\,\text{min}^{-1}$, $m(0) = 0$. Compute $m_\infty$ and $m(30\,\text{min})$.
