---
tags: [analysis, multivariable, type/solution]
---
# B11 Multivariable Calculus – Solutions

> Worksheet: [[B11 Multivariable Calculus - Worksheet]] · Theory: [[B11 Multivariable Calculus]] · Wrong? → [[Mistakes - Analysis]]

## Level 1
1. a) $f_x = 6xy$, $f_y = 3x^2 - 3y^2$ b) $f_x = ye^{xy}$, $f_y = xe^{xy}$ c) $f_x = \frac{2x}{x^2 + y^2}$, $f_y = \frac{2y}{x^2 + y^2}$
2. $f_x = 3x^2y^2$, $f_y = 2x^3y$; $f_{xx} = 6xy^2$, $f_{yy} = 2x^3$, $f_{xy} = 6x^2y = f_{yx}$ ✓
3. $\nabla f = (2x, 8y)$, so $(2, 8)$ at $(1, 1)$. The contour $x^2 + 4y^2 = 5$ is an ellipse; the gradient points outwards, perpendicular to it.

## Level 2
4. $D_\mathbf uf = (2, 8)\cdot\frac{1}{\sqrt2}(1, 1) = \frac{10}{\sqrt2}\approx7.07$. The maximum is in the direction of $\nabla f$, with slope $\lVert(2, 8)\rVert = \sqrt{68}\approx8.25$.
5. $(2x + y - 3,\ x + 2y) = 0$ gives $x = -2y$, then $-4y + y = 3$, so $y = -1$, $x = 2$. $H = \begin{pmatrix}2&1\\1&2\end{pmatrix}$, $\det = 3 > 0$, $f_{xx} > 0$: **minimum** at $(2, -1)$ with $f = 4 - 2 + 1 - 6 = -3$.
6. $(2x, -2y) = 0$ gives the origin. $H = \operatorname{diag}(2, -2)$, $\det < 0$: **saddle**.
7. The critical point is $(1, -2)$. $H = \operatorname{diag}(-2, -4)$, both negative: **maximum** with value 5.

## Level 3
8. $J = \begin{pmatrix}2x&-1\\y&x\end{pmatrix}$, so at $(1, 2)$: $\begin{pmatrix}2&-1\\2&1\end{pmatrix}$.
9. $\frac{df}{dt} = 2x\cdot(-\sin t) + 2y\cdot\cos t = -2\cos t\sin t + 2\sin t\cos t = 0$. The particle moves on the unit circle, which is a contour line of $f$, so $f$ stays constant (motion perpendicular to the gradient).
10. $J = \begin{pmatrix}-1&1\\0&-2\end{pmatrix}$ (triangular), so the eigenvalues are −1 and −2, both negative: **stable** node.

## Level 4
11. Inner: $\int_0^2(x + y)dy = 2x + 2$. Outer: $\int_0^1(2x + 2)dx = 1 + 2 = 3$.
12. $\int_0^{2\pi}\int_0^\infty e^{-r^2}r\,dr\,d\theta = 2\pi\cdot\left[-\tfrac12e^{-r^2}\right]_0^\infty = 2\pi\cdot\tfrac12 = \pi$. Since the double integral is $\left(\int e^{-x^2}dx\right)^2$, we get $\int_{-\infty}^\infty e^{-x^2}dx = \sqrt\pi$.
13. $\nabla r = r\cdot(-x, -y)$, so at $(1, 0)$: $20e^{-1/2}\cdot(-1, 0)\approx(-12.1, 0)$ Hz per unit. The animal must move in the $-x$ direction, **towards the field centre**.
14. $\iint20e^{-r^2/2}r\,dr\,d\theta = 20\cdot2\pi\cdot\left[-e^{-r^2/2}\right]_0^\infty = 40\pi\approx125.7$ (Hz × area units, i.e. Hz × 100 cm²).
