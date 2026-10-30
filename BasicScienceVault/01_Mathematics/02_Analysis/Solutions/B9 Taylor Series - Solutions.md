---
tags: [analysis, taylor, type/solution]
---
# B9 Taylor Series – Solutions

> Worksheet: [[B9 Taylor Series - Worksheet]] · Theory: [[B9 Taylor Series]] · Wrong? → [[Mistakes - Analysis]]

## Level 1
1. All derivatives of $e^x$ are $e^x$, at 0 all equal 1: $T_3 = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}$
2. $f = \cos$, $f' = -\sin$, $f'' = -\cos$ → at 0: $1, 0, -1$ → $T_2 = 1 - \frac{x^2}{2}$
3. $\sin, \cos, -\sin, -\cos$ at 0: $0, 1, 0, -1$ → $T_3 = x - \frac{x^3}{6}$
4. $f = \ln(1+x)$, $f' = \frac1{1+x}$, $f'' = -\frac1{(1+x)^2}$ → at 0: $0, 1, -1$ → $T_2 = x - \frac{x^2}2$

## Level 2
5. $1 + 0.1 + 0.005 = 1.105$ (true: 1.10517…)
6. $f(4) = 2$, $f'(x) = \frac1{2\sqrt x}$, $f'(4) = \frac14$ → $T_1 = 2 + \frac14(x - 4)$; $\sqrt{4.1}\approx 2 + 0.025 = 2.025$ (true: 2.02485…)
7. $f = (1-x)^{-1}$, $f' = (1-x)^{-2}$, $f'' = 2(1-x)^{-3}$ → $1, 1, 2$ → $T_2 = 1 + x + x^2$. $\frac1{0.9} = \frac{1}{1 - 0.1}\approx 1 + 0.1 + 0.01 = 1.11$ (true: 1.111…)
8. $e^u = 1 + u + \frac{u^2}2 + \dots$ with $u = -x^2$: $e^{-x^2}\approx 1 - x^2 + \frac{x^4}2$

## Level 3
9. $f(1) = 0$; $f' = 3x^2 - 2$, $f'(1) = 1$; $f'' = 6x$, $f''(1) = 6$ → $T_2 = (x - 1) + 3(x-1)^2$
10. $e^x - 1 - x = \frac{x^2}{2} + \frac{x^3}6 + \dots$ → divided by $x^2$: $\frac12 + \frac x6 + \dots \to \frac12$
11. $\frac{d}{dx}\left(1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots\right) = 0 + 1 + x + \frac{x^2}{2!} + \dots = e^x$ ✓
12. Next term $-\frac{x^3}{6}$: $\frac{0.05^3}{6} = \frac{1.25\times10^{-4}}{6}\approx 2\times10^{-5}$ – tiny.

## Level 4
13. $\sigma(x)\approx\frac12 + \frac x4$; $\sigma(0.2)\approx 0.5 + 0.05 = 0.55$ (true: 0.5498…)
14. $\frac{dV}{dt}\big|_{t=0} = -\frac{-60 + 70}{10} = -1\,\text{mV/ms}$ → $V(1)\approx -60 + 1\cdot(-1) = -61\,\text{mV}$.
    Exact: $V(1) = -70 + 10e^{-0.1}$. With $e^{-0.1}\approx 1 - 0.1 = 0.9$ (first-order Taylor) → $-70 + 9 = -61$: the Euler step **is** the first-order Taylor approximation. True value: $-70 + 9.048 = -60.95\,\text{mV}$.
15. $T_3(1) = 1 - \frac16\approx 0.8333$; $\sin 1\approx 0.8415$ → error ≈ 0.008 (≈ the next term $\frac{1}{120}\approx 0.0083$).
