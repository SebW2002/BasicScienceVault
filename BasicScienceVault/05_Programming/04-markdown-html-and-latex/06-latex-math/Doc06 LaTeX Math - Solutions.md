---
tags: [programming, latex, math-typesetting, type/solution]
---
# Doc06 LaTeX Math – Solutions

> Worksheet: [[Doc06 LaTeX Math - Worksheet]] · Theory: [[Doc06 LaTeX Math]] · Wrong? → [[Mistakes - Markdown HTML LaTeX]]

## Level 1
1. `$\lambda = \sqrt{\frac{r_m}{r_i}}$`
2. ```latex
   \begin{equation}
     V = IR
     \label{eq:ohm}
   \end{equation}
   Ohm's law \eqref{eq:ohm} relates voltage and current.
   ```
3. `\[ s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2} \]`
4. `\[ I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \]`

## Level 2
5. In math mode "ms" is set as the italic product $m\cdot s$, and the space is ignored. Use `\qty{20}{\milli\second}` (siunitx) – or in text `20~ms`.
6. No `&` alignment points: each line is right-aligned at its end. Write `a &= b \\ c &= d`.
7. `sin` is set as italic $s\cdot i\cdot n$. Use `$\sin(\omega t)$`.
8. `\eqref{eq:nernst}`. `\label` refers to the last numbered object; before `\begin{equation}` that is the current section (or nothing), so the reference points to the wrong number. Put `\label` inside the equation.

## Level 3
9. ```latex
   \begin{align}
     \frac{dm}{dt} &= \alpha_m(V)\,(1 - m) - \beta_m(V)\, m \label{eq:gate} \\
     m_\infty &= \frac{\alpha_m}{\alpha_m + \beta_m} \nonumber
   \end{align}
   ```
10. `\[ f(x) = \begin{cases} 0 & x < 0 \\ x & x \ge 0 \end{cases} \]`
11. ```latex
    % preamble
    \usepackage{amssymb, mathtools}
    \newcommand{\E}{\mathbb{E}}
    \DeclarePairedDelimiter{\abs}{\lvert}{\rvert}
    % body
    $\E\left[\abs{X - \mu}\right]$   % or \E\bigl[\abs*{X - \mu}\bigr]
    ```

## Level 4
12. ```latex
    \begin{align*}
      \mathcal{L}(\lambda) &= \prod_{i=1}^{n} \frac{\lambda^{k_i} e^{-\lambda}}{k_i!} \\
      \log \mathcal{L}(\lambda) &= \sum_{i=1}^{n} \bigl( k_i \log\lambda - \lambda - \log k_i! \bigr)
    \end{align*}
    ```
13. After two passes (latexmk does this automatically) the sentence reads "Ohm's law (1) relates …"; after one pass it would show "(??)".
