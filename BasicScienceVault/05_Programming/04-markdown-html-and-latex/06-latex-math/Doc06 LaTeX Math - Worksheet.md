---
tags: [programming, latex, math-typesetting, type/worksheet]
---
# Doc06 LaTeX Math – Worksheet

> Theory: [[Doc06 LaTeX Math]] · Solutions: [[Doc06 LaTeX Math - Solutions]] · Log mistakes in [[Mistakes - Markdown HTML LaTeX]]
> Write on paper or in a text editor; compile only for tasks marked 💻.

## Level 1 – Typeset
1. Inline: the length constant $\lambda = \sqrt{\frac{r_m}{r_i}}$.
2. Numbered equation with label `eq:ohm`: $V = IR$, and a sentence referring to it with parentheses.
3. The SD $s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar x)^2}$ as an unnumbered display.
4. The 3 × 3 identity matrix in square brackets.

## Level 2 – Fix
5. `$20 ms$` – what's wrong (two things)? Correct it with siunitx.
6. `\begin{align} a = b \\ c = d \end{align}` compiles but looks misaligned. Why?
7. `$sin(\omega t)$` – what's wrong?
8. `\ref{eq:nernst}` prints "1" but you want "(1)". Which command? Why doesn't `\label` before `\begin{equation}` work?

## Level 3 – Multi-line
9. Write the Hodgkin–Huxley gating equation for $m$ and its steady state in an `align` environment, numbering only the first line: $\frac{dm}{dt} = \alpha_m(V)(1 - m) - \beta_m(V)m$, $m_\infty = \frac{\alpha_m}{\alpha_m + \beta_m}$.
10. Write the piecewise ReLU $f(x) = \max(0, x)$ with `cases`.
11. Define a command `\E` for the expectation symbol $\mathbb{E}$ and an auto-sized absolute value `\abs{}` with mathtools; use both to write $\mathbb{E}\left[\lvert X - \mu\rvert\right]$.

## Level 4 – Neuro transfer
12. Write the Poisson log-likelihood of spike counts $k_1, \dots, k_n$ with rate $\lambda$ in an `align*` with two lines (product form, then sum form).
13. 💻 Put tasks 1–12 into one document (`amsmath`, `amssymb`, `mathtools`, `siunitx`), compile with `latexmk -pdf` and check that the reference from task 2 shows "(1)".
