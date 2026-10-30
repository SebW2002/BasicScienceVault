---
tags: [analysis, limit, continuity, type/solution]
---
# B5 Limits and Continuity – Solutions

> Worksheet: [[B5 Limits and Continuity - Worksheet]] · Theory: [[B5 Limits and Continuity]] · Wrong? → [[Mistakes - Analysis]]

## Level 1
1. Continuous → plug in: $12 - 1 = 11$
2. $\frac00$ → factor: $\frac{(x-3)(x+3)}{x-3} = x + 3 \to 6$
3. $\frac{x(x+2)}{x} = x + 2 \to 2$
4. $\frac{(x+1)(x+2)}{x+1} = x + 2 \to 1$

## Level 2
5. Divide by $x^2$: $\frac{3 + 1/x^2}{1 - 5/x^2} \to 3$
6. Divide by $x^2$: $\frac{2/x + 1/x^2}{1 + 1/x^2} \to \frac01 = 0$
7. Divide by $x^2$: $\frac{x}{1 + 1/x^2} \to \infty$
8. $+\infty$ and $-\infty$. The one-sided limits differ → $\lim_{x\to0}\frac1x$ does not exist.
9. $0$ (exponential beats power)

## Level 3
10. Multiply by $\sqrt x + 2$: $\frac{x - 4}{(x-4)(\sqrt x + 2)} = \frac1{\sqrt x + 2} \to \frac14$
11. $3\cdot\frac{\sin 3x}{3x} \to 3 \cdot 1 = 3$
12. $e^2$
13. $\frac{4 + 4h + h^2 - 4}{h} = 4 + h \to 4$. This is the derivative of $x^2$ at $x = 2$ (difference quotient, see [[B6 Differentiation Rules]]).

## Level 4
14. Left limit at 1: $1 + 1 = 2$. Right value: $a\cdot1 = a$. Continuous iff $a = 2$.
15. a) removable (limit = 2 exists, value doesn't) b) pole c) jump (left limit 0, right limit 1)
16. $\lim_{t\to\infty} = 20$ (since $e^{-t/5}\to0$); $\lim_{t\to0} = 20(1 - 1) = 0$
17. $\frac{3}{0.05\,\text{s}} = 60\,\text{Hz}$. The instantaneous rate is the limit $\Delta t \to 0$; a finite window averages over 50 ms, and for tiny windows the count is just 0 or 1 → in practice one averages over trials or uses smoothing kernels.
