---
tags: [analysis, taylor, type/worksheet]
---
# B9 Taylor Series – Worksheet

> Theory: [[B9 Taylor Series]] · Solutions: [[B9 Taylor Series - Solutions]] · Log mistakes in [[Mistakes - Analysis]]
> No calculator unless marked 🧮.

## Level 1 – Standard series
1. Derive $T_3$ of $e^x$ at $a = 0$ from the definition.
2. Derive $T_2$ of $\cos x$ at $a = 0$.
3. Derive $T_3$ of $\sin x$ at $a = 0$.
4. Derive $T_2$ of $\ln(1 + x)$ at $a = 0$.

## Level 2 – Approximations
5. Approximate $e^{0.1}$ with $T_2$.
6. Linearise $f(x) = \sqrt x$ at $a = 4$ and use it to approximate $\sqrt{4.1}$.
7. Derive $T_2$ of $\frac1{1-x}$ at $a = 0$ and approximate $\frac1{0.9}$.
8. Use the series of $e^u$ with $u = -x^2$ to find the series of $e^{-x^2}$ up to $x^4$.

## Level 3 – Other expansion points & applications
9. Compute $T_2$ of $f(x) = x^3 - 2x + 1$ at $a = 1$.
10. Use series to compute $\displaystyle\lim_{x\to0}\frac{e^x - 1 - x}{x^2}$.
11. Show with the series that $\frac{d}{dx}e^x = e^x$ (differentiate term by term).
12. Estimate the error of $\sin(0.05)\approx 0.05$ using the next term of the series.

## Level 4 – Neuro
13. **Linearised sigmoid:** with $\sigma(0) = \tfrac12$ and $\sigma'(0) = \tfrac14$, give the linearisation of $\sigma(x) = \frac1{1+e^{-x}}$ at $0$. Estimate $\sigma(0.2)$.
14. **Euler step:** $\tau\frac{dV}{dt} = -(V - E_L)$ with $\tau = 10\,\text{ms}$, $E_L = -70\,\text{mV}$, $V(0) = -60\,\text{mV}$. Compute one Euler step with $\Delta t = 1\,\text{ms}$. The exact solution is $V(t) = -70 + 10e^{-t/10}$ – write down $V(1)$ exactly and compare with $T_1$ of $e^{-0.1}$.
15. 🧮 Compare $T_3$ of $\sin x$ at $x = 1$ with the true value $\sin 1$.
