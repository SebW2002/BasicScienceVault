---
tags: [analysis, differential-equation, type/solution]
---
# B10 Differential Equations – Solutions

> Worksheet: [[B10 Differential Equations - Worksheet]] · Theory: [[B10 Differential Equations]] · Wrong? → [[Mistakes - Analysis]]

## Level 1
1. $\dot x = 3\cdot(-2)e^{-2t} = -2\cdot3e^{-2t} = -2x$ ✓; $x(0) = 3$ ✓
2. $x(t) = 4e^{-0.5t}$; $x(2) = 4e^{-1}\approx1.47$
3. $N = 100e^{0.1t}$; doubling: $e^{0.1t} = 2\Rightarrow t = 10\ln2\approx6.9$
4. a) first order, linear b) second order, linear c) first order, **non-linear** ($x^2$) d) PDE, second order in space, linear

## Level 2
5. $x_\infty = 3$, $\tau = 1/2$; $x(t) = 3 - 3e^{-2t} = 3(1 - e^{-2t})$
6. $V_\infty = -70 + 20 = -50$ mV, τ = 10 ms. $V(t) = -50 + (-70 + 50)e^{-t/10} = -50 - 20e^{-t/10}$. After 10 ms: $-50 - 20\cdot0.37\approx-57.4$ mV.
7. $\frac{dx}{x} = -k\,dt$, so $\int\frac{dx}{x} = -\int k\,dt$, giving $\ln\lvert x\rvert = -kt + C$, so $\lvert x\rvert = e^Ce^{-kt}$, i.e. $x = x_0e^{-kt}$ with $x_0 = x(0)$.
8. Rewrite: $\dot n = \alpha - (\alpha + \beta)n$. Then $n_\infty = \frac{\alpha}{\alpha + \beta} = \frac34$ and $\tau_n = \frac{1}{\alpha + \beta} = 0.25$ ms.

## Level 3
9. $f(x) = x - x^2$; fixed points 0 and 1. $f'(x) = 1 - 2x$: $f'(0) = 1$, so 0 is unstable; $f'(1) = -1$, so 1 is stable. Phase line: for $x < 0$, $f < 0$ (arrow left); for $0 < x < 1$, $f > 0$ (right, towards 1); for $x > 1$, $f < 0$ (left, towards 1).
10. $x^2 = 4\Rightarrow x = \pm2$. $f'(x) = 2x$: $f'(-2) = -4$, so −2 is stable; $f'(2) = 4$, so 2 is unstable.
11. $\mathbf x(t) = c_1e^{-t}\begin{pmatrix}1\\0\end{pmatrix} + c_2e^{-3t}\begin{pmatrix}0\\1\end{pmatrix}$. The second component decays faster (τ = 1/3 vs. 1).
12. $\dot x = v$, $\dot v = -4x$, i.e. $\frac{d}{dt}\begin{pmatrix}x\\v\end{pmatrix} = \begin{pmatrix}0&1\\-4&0\end{pmatrix}\begin{pmatrix}x\\v\end{pmatrix}$. $\lambda^2 + 4 = 0\Rightarrow\lambda = \pm2i$, so ω = 2 and the period is $T = 2\pi/\omega = \pi$.

## Level 4
13. $x_1 = 1 - 0.5\cdot1 = 0.5$; $x_2 = 0.5 - 0.25 = 0.25$ (exact: 0.37; Euler is too fast here). With $\Delta t = 2.5$: $x_{n+1} = (1 - 2.5)x_n = -1.5x_n$, so the sign flips and the amplitude grows: **unstable** (needs $\Delta t < 2$).
14. $k = \ln2/4\approx0.173\,\text{h}^{-1}$. 12 h = 3 half-lives, so $\frac18 = 12.5\,\%$ remains.
15. $m_\infty = k/\gamma = 200$; $\tau = 20$ min. $m(30) = 200(1 - e^{-1.5})\approx200\cdot0.777\approx155$ molecules.
