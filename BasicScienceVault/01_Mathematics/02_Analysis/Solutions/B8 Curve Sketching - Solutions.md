---
tags: [analysis, curve-sketching, type/solution]
---
# B8 Curve Sketching – Solutions

> Worksheet: [[B8 Curve Sketching - Worksheet]] · Theory: [[B8 Curve Sketching]] · Wrong? → [[Mistakes - Analysis]]

## Level 1
1. $(x-1)(x-3) = 0$ → zeros $1, 3$. $f' = 2x - 4 = 0 \Rightarrow x = 2$, $f'' = 2 > 0$ → minimum $(2, -1)$.
2. See theory note: odd; zeros $0, \pm\sqrt3$; max $(-1, 2)$, min $(1, -2)$; inflection $(0, 0)$; $f\to\pm\infty$ for $x\to\pm\infty$.
3. $f = x(x-3)^2$ → zeros $0$ and $3$ (double zero = touches the axis). No symmetry.
   $f' = 3x^2 - 12x + 9 = 3(x-1)(x-3)$ → $x = 1, 3$. $f'' = 6x - 12$: $f''(1) = -6$ → max $(1, 4)$; $f''(3) = 6$ → min $(3, 0)$.
   $f'' = 0 \Rightarrow x = 2$ → inflection $(2, 2)$. $f\to\pm\infty$ for $x\to\pm\infty$.

## Level 2
4. Even. $x^2(x^2 - 2) = 0$ → zeros $0, \pm\sqrt2$.
   $f' = 4x^3 - 4x = 4x(x-1)(x+1)$ → $x = 0, \pm1$. $f'' = 12x^2 - 4$: $f''(0) = -4$ → max $(0, 0)$; $f''(\pm1) = 8$ → minima $(\pm1, -1)$.
   $f'' = 0 \Rightarrow x = \pm\frac1{\sqrt3}$ → inflection points $\left(\pm\frac1{\sqrt3}, -\frac59\right)$ (since $\frac19 - \frac23 = -\frac59$). $f\to\infty$ at both ends.
5. Odd; zero $x = 0$; asymptote $y = 0$.
   $f' = \dfrac{(x^2+1) - x\cdot2x}{(x^2+1)^2} = \dfrac{1 - x^2}{(x^2+1)^2} = 0 \Rightarrow x = \pm1$. Sign of $f'$ changes from $-$ to $+$ at $-1$ → min $(-1, -\tfrac12)$; from $+$ to $-$ at $1$ → max $(1, \tfrac12)$.
6. $f'(0) = 0$, but $f' = 3x^2 \ge 0$ doesn't change sign → no extremum, it's a saddle (inflection) point.

## Level 3
7. Zero: $x = 0$. $x\to\infty$: $\to 0$ (exponential wins); $x\to-\infty$: $\to-\infty$.
   $f' = e^{-x} - xe^{-x} = (1 - x)e^{-x} = 0 \Rightarrow x = 1$; max $(1, \frac1e)$.
   $f'' = -e^{-x} - (1-x)e^{-x} = (x - 2)e^{-x} = 0 \Rightarrow x = 2$ → inflection $(2, \frac2{e^2})$.
8. Zero $x = 1$. $f' = \dfrac{\frac1x\cdot x - \ln x}{x^2} = \dfrac{1 - \ln x}{x^2} = 0 \Rightarrow x = e$; $f'$ changes from $+$ to $-$ → max $(e, \frac1e)$.

## Level 4
9. $g' = e^{-t/\tau}\left(1 - \frac t\tau\right) = 0 \Rightarrow t = \tau$; peak value $g(\tau) = \tau e^{-1} = \frac\tau e$.
   $g'' = e^{-t/\tau}\left(-\frac1\tau - \frac1\tau + \frac{t}{\tau^2}\right) = \frac{1}{\tau}e^{-t/\tau}\left(\frac t\tau - 2\right) = 0 \Rightarrow t = 2\tau$ → inflection $(2\tau, \frac{2\tau}{e^2})$.
10. $\sigma' = \sigma(1 - \sigma) > 0$ since $0 < \sigma < 1$ → strictly increasing. $x\to-\infty$: $e^{-x}\to\infty$, $\sigma\to0$; $x\to\infty$: $\sigma\to1$.
    $\sigma'' = \sigma'(1 - 2\sigma) = 0 \iff \sigma = \tfrac12 \iff x = 0$; sign of $1 - 2\sigma$ changes there → inflection $(0, \tfrac12)$, where the slope $\sigma'(0) = \tfrac14$ is maximal.
11. $f' = -xe^{-x^2/2} = 0 \Rightarrow x = 0$ → max $(0, 1)$. $f'' = (x^2 - 1)e^{-x^2/2} = 0 \Rightarrow x = \pm1$ → inflection points $(\pm1, e^{-1/2})$ – the curve is steepest there (one standard deviation from the peak).
12. $2a + 2b = 20 \Rightarrow b = 10 - a$. $A(a) = a(10 - a) = 10a - a^2$; $A' = 10 - 2a = 0 \Rightarrow a = 5$, $A'' = -2 < 0$ → max. Square $5\times5$, area 25.
