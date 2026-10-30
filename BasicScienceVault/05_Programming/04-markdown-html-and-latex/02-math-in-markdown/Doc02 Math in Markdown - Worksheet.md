---
tags: [programming, markdown, latex, type/worksheet]
---
# Doc02 Math in Markdown – Worksheet

> Theory: [[Doc02 Math in Markdown]] · Solutions: [[Doc02 Math in Markdown - Solutions]] · Log mistakes in [[Mistakes - Markdown HTML LaTeX]]
> Write on paper or in a text editor; check rendering in Obsidian only for tasks marked 💻.

## Level 1 – Write the LaTeX
1. Inline: the time constant τ equals R times C.
2. Display: $E_\text{K} = \frac{RT}{F}\ln\frac{[\text{K}^+]_o}{[\text{K}^+]_i}$
3. The sample mean $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$ and SEM $\frac{s}{\sqrt{n}}$.
4. The charge $Q = \int_{0}^{T} I(t)\,dt$.

## Level 2 – Find the error
5. `$e^-t/\tau$` renders as $e^-t/\tau$. What's wrong? Correct it.
6. `$ x = 5 $` doesn't render in some tools. Why?
7. `$SNR = P_signal / P_noise$` looks odd. Two problems; correct it.
8. In an Obsidian table, `$|x|$` breaks the table. Why? Fix.

## Level 3 – Environments
9. Write the 2 × 2 matrix $W = \begin{pmatrix} w_{11} & w_{12} \\ w_{21} & w_{22} \end{pmatrix}$ and the system $\dot{\mathbf{r}} = -\mathbf{r} + W\mathbf{r} + \mathbf{I}$.
10. Write the LIF neuron as an aligned system: $\tau\frac{dV}{dt} = -(V - E_L) + RI$, and "if $V \ge V_\text{th}$: $V \to V_\text{reset}$" as a `cases` expression for the reset.
11. Write the Poisson probability $P(K = k) = \frac{\lambda^k e^{-\lambda}}{k!}$ and the Fourier transform $X(f) = \int_{-\infty}^{\infty} x(t)\,e^{-2\pi i f t}\,dt$.

## Level 4 – Platforms
12. You want to write a numbered equation and refer to it as "Equation (1)" in a report that will be HTML and PDF. Which tool and syntax?
13. A formula renders in Obsidian but shows raw code on GitHub. Name two possible reasons.
14. 💻 Write tasks 2, 9, 10 and 11 in an Obsidian note and check the rendering.
