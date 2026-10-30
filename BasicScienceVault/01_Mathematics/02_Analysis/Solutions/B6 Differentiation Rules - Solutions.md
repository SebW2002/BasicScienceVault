---
tags: [analysis, derivative, type/solution]
---
# B6 Differentiation Rules – Solutions

> Worksheet: [[B6 Differentiation Rules - Worksheet]] · Theory: [[B6 Differentiation Rules]] · Wrong? → [[Mistakes - Analysis]]

## Level 1
1. $20x^4$
2. $6x - 2$
3. $x^{1/2} + x^{-1}$ → $\dfrac{1}{2\sqrt x} - \dfrac{1}{x^2}$
4. $2x^{-3} - x^{1/3}$ → $-6x^{-4} - \tfrac13 x^{-2/3} = -\dfrac{6}{x^4} - \dfrac{1}{3\sqrt[3]{x^2}}$
5. $f' = 3x^2 - 3$, $\;f'' = 6x$

## Level 2
6. $2x e^x + x^2e^x = e^x(x^2 + 2x)$
7. $1\cdot\ln x + x\cdot\frac1x = \ln x + 1$
8. $\dfrac{1\cdot(x-1) - (x+1)\cdot1}{(x-1)^2} = \dfrac{-2}{(x-1)^2}$
9. $\dfrac{x\cos x - \sin x}{x^2}$

## Level 3
10. $4(3x+2)^3\cdot3 = 12(3x+2)^3$
11. $-2x\,e^{-x^2}$
12. $\dfrac{2x}{x^2+1}$
13. $-\dfrac1\tau e^{-t/\tau}$
14. $\dfrac{1}{2\sqrt{1 + e^{2x}}}\cdot 2e^{2x} = \dfrac{e^{2x}}{\sqrt{1 + e^{2x}}}$
15. $2\cos(2x)\cos x - \sin(2x)\sin x$

## Level 4
16. $\sigma = (1 + e^{-x})^{-1}$ → chain rule: $\sigma' = -(1+e^{-x})^{-2}\cdot(-e^{-x}) = \dfrac{e^{-x}}{(1+e^{-x})^2}$.
    Now $\sigma(1-\sigma) = \dfrac{1}{1+e^{-x}}\cdot\dfrac{e^{-x}}{1+e^{-x}}$ – identical ✓. $\;\sigma'(0) = \tfrac12\cdot\tfrac12 = \tfrac14$.
17. $\frac{dV}{dt} = 10\cdot 2\pi\cdot5\cos(10\pi t)\,\text{mV/s} = 100\pi\cos(10\pi t)\,\text{mV/s}$. At $t = 0$: $100\pi\,\text{mV/s} = 0.1\pi\,\text{V/s}$.
    $I_C = 100\times10^{-12}\,\text{F}\cdot0.1\pi\,\text{V/s} = 10\pi\times10^{-12}\,\text{A} = 10\pi\,\text{pA}$ ($\approx 31\,\text{pA}$).
18. a) Chain rule: $\frac{dE}{dw} = 2(y - wx)\cdot(-x) = -2x(y - wx)$
    b) $\frac{dE}{dw} = -2\cdot2\cdot(3 - 2) = -4$ → $w_\text{new} = 1 - 0.1\cdot(-4) = 1.4$. (Check: error before $(3-2)^2 = 1$, after $(3 - 2.8)^2 = 0.04$ ✓)
