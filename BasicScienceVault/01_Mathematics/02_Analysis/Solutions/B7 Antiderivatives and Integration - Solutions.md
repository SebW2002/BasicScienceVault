---
tags: [analysis, integral, type/solution]
---
# B7 Antiderivatives and Integration – Solutions

> Worksheet: [[B7 Antiderivatives and Integration - Worksheet]] · Theory: [[B7 Antiderivatives and Integration]] · Wrong? → [[Mistakes - Analysis]]

## Level 1
1. $\frac{x^4}{4} + C$
2. $2x^3 - 2x^2 + x + C$
3. $\ln\lvert x\rvert + C$; $\;\frac13e^{3x} + C$
4. $\int(x^{1/2} + 2x^{-2})dx = \frac23x^{3/2} - 2x^{-1} + C = \frac23x\sqrt x - \frac2x + C$
5. $\sin x + 2\cos x + C$

## Level 2
6. $\left[\frac{x^3}{3}\right]_0^2 = \frac83$
7. $\ln e - \ln 1 = 1$
8. $[-\cos x]_0^\pi = -(-1) - (-1) = 2$
9. $\left[\frac{x^4}4\right]_{-1}^1 = \frac14 - \frac14 = 0$ – $x^3$ is odd, the area below the axis cancels the area above.
10. Fundamental theorem: $e^{x^2}$

## Level 3
11. $u = x^2$, $du = 2x\,dx$ → $e^{x^2} + C$
12. $u = x^2 + 1$, $du = 2x\,dx$, bounds $u: 1 \to 2$ → $\frac12\int_1^2u^3du = \frac12\left[\frac{u^4}4\right]_1^2 = \frac18(16 - 1) = \frac{15}8$
13. $u = x$, $v' = e^x$ → $xe^x - \int e^xdx = (x-1)e^x + C$
14. $u = \ln x$, $v' = 1$ → $x\ln x - \int x\cdot\frac1x dx = x\ln x - x + C$
15. $\int_0^1(x - x^2)dx = \frac12 - \frac13 = \frac16$
16. $\frac13\int_0^3x^2dx = \frac13\cdot9 = 3$

## Level 4
17. $Q = I_0\left[-\tau e^{-t/\tau}\right]_0^\infty = I_0\tau = 100\times10^{-12}\,\text{A}\cdot5\times10^{-3}\,\text{s} = 5\times10^{-13}\,\text{C} = 0.5\,\text{pC}$
18. $\int_0^\infty\lambda e^{-\lambda t}dt = \left[-e^{-\lambda t}\right]_0^\infty = 0 - (-1) = 1$ ✓
    Mean by parts ($u = t$, $v' = \lambda e^{-\lambda t}$, $v = -e^{-\lambda t}$): $\left[-te^{-\lambda t}\right]_0^\infty + \int_0^\infty e^{-\lambda t}dt = 0 + \frac1\lambda$ ✓
19. $\int_0^{10}50e^{-t/5}dt = 50\cdot\left[-5e^{-t/5}\right]_0^{10} = 250(1 - e^{-2}) \approx 250\cdot0.8647 \approx 216$ spikes
