---
tags: [programming, markdown, latex, type/solution]
---
# Doc02 Math in Markdown – Solutions

> Worksheet: [[Doc02 Math in Markdown - Worksheet]] · Theory: [[Doc02 Math in Markdown]] · Wrong? → [[Mistakes - Markdown HTML LaTeX]]

## Level 1
1. `The time constant is $\tau = RC$.`
2. ```latex
   $$
   E_\text{K} = \frac{RT}{F}\ln\frac{[\text{K}^+]_o}{[\text{K}^+]_i}
   $$
   ```
3. `$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$` and `$\frac{s}{\sqrt{n}}$`
4. `$Q = \int_{0}^{T} I(t)\,dt$`

## Level 2
5. Without braces only the `-` is raised. Write `$e^{-t/\tau}$`.
6. Many renderers (Pandoc, GitHub) require that inline math has no space right after the opening and before the closing `$` (to avoid confusion with prices). Write `$x = 5$`.
7. Multi-letter names in italics look like products of letters ($S\cdot N\cdot R$), and subscripts with several letters need braces (`P_signal` → only "s" is a subscript). Correct: `$\text{SNR} = P_\text{signal} / P_\text{noise}$` (or `\frac{P_\text{signal}}{P_\text{noise}}`).
8. The `|` is interpreted as a table column separator. Write `$\lvert x\rvert$` (or escape: `$\|x\|$` – note that `\|` means a double bar in LaTeX outside tables, so `\lvert…\rvert` is the clean solution).

## Level 3
9. ```latex
   $$
   W = \begin{pmatrix} w_{11} & w_{12} \\ w_{21} & w_{22} \end{pmatrix}, \qquad
   \dot{\mathbf{r}} = -\mathbf{r} + W\mathbf{r} + \mathbf{I}
   $$
   ```
10. ```latex
    $$
    \begin{aligned}
    \tau \frac{dV}{dt} &= -(V - E_L) + RI \\
    V &\to \begin{cases} V_\text{reset} & \text{if } V \ge V_\text{th} \\ V & \text{otherwise} \end{cases}
    \end{aligned}
    $$
    ```
11. ```latex
    $$
    P(K = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \qquad
    X(f) = \int_{-\infty}^{\infty} x(t)\, e^{-2\pi i f t}\, dt
    $$
    ```

## Level 4
12. Quarto (or R Markdown with bookdown): `$$ y = X\beta + \varepsilon $$ {#eq-glm}` and refer with `@eq-glm` → "Equation 1" in both HTML and PDF. (In pure LaTeX: `equation` + `\label`/`\eqref`, [[Doc06 LaTeX Math]].)
13. E.g. GitHub's parser interpreted `_` or `*` inside inline math as emphasis; inline math next to punctuation/backticks isn't recognised; Obsidian-only features such as math inside callouts or macros defined elsewhere; a `$` with a space after it.
14. Check that fractions, subscripts, matrices, aligned rows and cases render; fix any missing braces.
