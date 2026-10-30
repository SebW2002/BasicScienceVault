---
aliases: [Mistake Log Analysis, Fehler Analysis]
tags: [analysis, type/mistakes]
---
# ⚠️ Mistakes – Analysis

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[00 Roadmap|Roadmap]] · Template: [[Mistake Entry Template]]

**How to use:** after every worksheet, add each wrong step to *My mistakes* – wrong version, correct version, and a quick check that would have caught it.

## Classic traps (pre-filled)
| ❌ Wrong                                                         | ✅ Right                                             | Quick check                                         | Topic                                  |
| --------------------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | -------------------------------------- |
| $(fg)' = f'g'$                                                  | $f'g + fg'$                                         | $(x\cdot x)' = 2x$, not $1$                         | [[B6 Differentiation Rules]]           |
| $(e^{2x})' = e^{2x}$                                            | $2e^{2x}$ (chain rule)                              | inner derivative!                                   | [[B6 Differentiation Rules]]           |
| $(\sin 3x)' = \cos 3x$                                          | $3\cos 3x$                                          | inner derivative!                                   | [[B6 Differentiation Rules]]           |
| $\left(\frac fg\right)' = \frac{f'g + fg'}{g^2}$                | $\frac{f'g - fg'}{g^2}$                             | "low d-high **minus** high d-low, over low squared" | [[B6 Differentiation Rules]]           |
| $\left(\frac1x\right)' = \ln x$                                 | $-\frac1{x^2}$                                      | power rule with $n = -1$                            | [[B6 Differentiation Rules]]           |
| $(\cos x)' = \sin x$                                            | $-\sin x$                                           | slope of $\cos$ at $\frac\pi2$ is negative          | [[B6 Differentiation Rules]]           |
| $\int fg\,dx = \int f\int g$                                    | substitution / parts                                | differentiate to check                              | [[B7 Antiderivatives and Integration]] |
| forgot $+C$                                                     | $\int f = F + C$                                    | –                                                   | [[B7 Antiderivatives and Integration]] |
| $\int\frac1x dx = \frac{x^0}{0}$                                | $\ln\lvert x\rvert + C$                             | power rule fails for $n=-1$                         | [[B7 Antiderivatives and Integration]] |
| $\int e^{3x}dx = e^{3x}$                                        | $\frac13e^{3x} + C$                                 | differentiate: $3e^{3x}$ ✗                          | [[B7 Antiderivatives and Integration]] |
| substitution: kept old bounds                                   | transform bounds or resubstitute                    | –                                                   | [[B7 Antiderivatives and Integration]] |
| $f'(x_0) = 0 \Rightarrow$ extremum                              | also need sign change / $f''\neq0$                  | $x^3$ at 0                                          | [[B8 Curve Sketching]]                 |
| $\frac00 = 0$ or $=1$                                           | indeterminate → simplify                            | –                                                   | [[B5 Limits and Continuity]]           |
| $\lim(1 + \frac1n)^n = 1$                                       | $= e$                                               | –                                                   | [[B5 Limits and Continuity]]           |
| calculator in degrees for calculus                              | radians!                                            | $\sin(\pi)\neq 0.0548$                              | [[B4 Trigonometric Functions]]         |
| $\sin^{-1}x = \frac{1}{\sin x}$                                 | $\arcsin x$                                         | –                                                   | [[B4 Trigonometric Functions]]         |
| $\sin x = \frac12 \Rightarrow x = \frac\pi6$ only               | also $\frac{5\pi}6$ (+ periods)                     | unit circle                                         | [[B4 Trigonometric Functions]]         |
| $\ln(x)$ for $x \le 0$                                          | not defined                                         | domain first                                        | [[B3 Logarithmic Functions]]           |
| $e^{-t/\tau}$ at $t=\tau$ is 50 %                               | $e^{-1}\approx37\%$; 50 % at $\tau\ln2$             | –                                                   | [[B2 Exponential Functions]]           |
| $f\circ g = g\circ f$                                           | generally not                                       | $x^2$ and $x+1$                                     | [[B1 Properties of Functions]]         |
| Taylor: forgot $k!$                                             | $\frac{f^{(k)}(a)}{k!}$                             | $e^x$ coefficients $1/k!$                           | [[B9 Taylor Series]]                   |
| $\tau\dot x = -(x - x_\infty)$: solution $x_\infty e^{-t/\tau}$ | $x_\infty + (x_0 - x_\infty)e^{-t/\tau}$            | check $x(0) = x_0$                                  | [[B10 Differential Equations]]         |
| forgot the initial condition / integration constant             | ODE solutions are families; fix $C$ with $x(0)$     | –                                                   | [[B10 Differential Equations]]         |
| fixed point stable if $f'(x^*) > 0$                             | stable if $f'(x^*) < 0$                             | phase line arrows                                   | [[B10 Differential Equations]]         |
| Euler with $\Delta t$ ≈ τ or larger                             | $\Delta t\ll\tau$ (unstable for $\Delta t > 2\tau$) | compare with exact                                  | [[B10 Differential Equations]]         |
| partial derivative: other variables differentiated too          | treat other variables as constants                  | $\partial_x(x^2y) = 2xy$                            | [[B11 Multivariable Calculus]]         |
| $\nabla f = 0$ ⇒ minimum                                        | check Hessian: could be max or saddle               | $x^2 - y^2$                                         | [[B11 Multivariable Calculus]]         |
| polar coordinates: $dA = dr\,d\theta$                           | $dA = r\,dr\,d\theta$                               | area of disc $\pi R^2$                              | [[B11 Multivariable Calculus]]         |
| power spectrum ∝ amplitude                                      | ∝ amplitude²                                        | –                                                   | [[B12 Fourier Analysis]]               |
| time shift changes the power spectrum                           | only the phase changes                              | $\lvert e^{-i\phi}\rvert = 1$                       | [[B12 Fourier Analysis]]               |
| frequency resolution set by sampling rate                       | $\Delta f = 1/T_\text{total}$ (length of recording) | –                                                   | [[B12 Fourier Analysis]]               |

## My mistakes
| Date | ❌ What I did | ✅ Correct | Why / quick check | Link |
|---|---|---|---|---|
| | | | | |

## Patterns I notice
- 
