---
tags: [analysis, derivative, type/worksheet]
---
# B6 Differentiation Rules – Worksheet

> Theory: [[B6 Differentiation Rules]] · Solutions: [[B6 Differentiation Rules - Solutions]] · Log mistakes in [[Mistakes - Analysis]]
> No calculator needed. Find $f'(x)$ unless stated otherwise.

## Level 1 – Power & sum rule
1. $f(x) = 4x^5$
2. $f(x) = 3x^2 - 2x + 7$
3. $f(x) = \sqrt x + \dfrac1x$
4. $f(x) = \dfrac{2}{x^3} - \sqrt[3]{x}$
5. $f(x) = x^3 - 3x$; also compute $f''(x)$.

## Level 2 – Product & quotient rule
6. $f(x) = x^2e^x$
7. $f(x) = x\ln x$
8. $f(x) = \dfrac{x+1}{x-1}$
9. $f(x) = \dfrac{\sin x}{x}$

## Level 3 – Chain rule
10. $f(x) = (3x + 2)^4$
11. $f(x) = e^{-x^2}$
12. $f(x) = \ln(x^2 + 1)$
13. $f(t) = e^{-t/\tau}$ ($\tau$ constant)
14. $f(x) = \sqrt{1 + e^{2x}}$
15. $f(x) = \sin(2x)\cos x$ (product + chain)

## Level 4 – Neuro
16. **Sigmoid:** show that $\sigma(x) = \dfrac{1}{1 + e^{-x}}$ has the derivative $\sigma'(x) = \sigma(x)(1 - \sigma(x))$. Compute $\sigma'(0)$.
17. **Capacitive current:** $V(t) = -70 + 10\sin(2\pi\cdot5\,t)$ mV ($t$ in s), $C = 100\,\text{pF}$. Compute $I_C = C\frac{dV}{dt}$ at $t = 0$ (exact, in pA).
18. **Gradient descent:** error $E(w) = (y - wx)^2$. a) Compute $\frac{dE}{dw}$. b) For $x = 2$, $y = 3$, $w = 1$ and learning rate $\eta = 0.1$, perform one update $w_\text{new} = w - \eta\frac{dE}{dw}$.
