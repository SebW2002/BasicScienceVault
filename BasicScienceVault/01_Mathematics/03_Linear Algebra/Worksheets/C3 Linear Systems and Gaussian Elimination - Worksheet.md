---
tags: [linear-algebra, linear-system, type/worksheet]
---
# C3 Linear Systems and Gaussian Elimination – Worksheet

> Theory: [[C3 Linear Systems and Gaussian Elimination]] · Solutions: [[C3 Linear Systems and Gaussian Elimination - Solutions]] · Log mistakes in [[Mistakes - Linear Algebra]]
> No calculator needed. Always check your solution in the original equations.

## Level 1 – 2×2
1. $x + y = 5$, $\;x - y = 1$
2. $2x + 3y = 12$, $\;4x - y = 10$
3. $x + y = 2$, $\;2x + 2y = 5$ – what happens?

## Level 2 – 3×3 with Gauss
4. $\begin{aligned}x + y + z &= 6\\ 2x - y + z &= 3\\ x + 2y - z &= 2\end{aligned}$ (compare with the worked example – try it alone first)
5. $\begin{aligned}2x + y - z &= 8\\ -3x - y + 2z &= -11\\ -2x + y + 2z &= -3\end{aligned}$
6. $\begin{aligned}x + 2y - z &= 3\\ 2x + y + z &= 3\\ 3x + 3y &= 6\end{aligned}$ – give the solution set in parameter form.

## Level 3 – Rank & parameters
7. Determine the rank of $\begin{pmatrix}1&2&3\\2&4&6\\1&0&1\end{pmatrix}$.
8. For which $a$ does $x + ay = 1$, $\;2x + 4y = 2$ have infinitely many solutions? For which exactly one?
9. Find the parabola $y = ax^2 + bx + c$ through $(0, 1)$, $(1, 2)$, $(2, 7)$.

## Level 4 – Neuro
10. **Excitatory network:** steady state $(I - W)\mathbf r = \mathbf h$ with $W = \begin{pmatrix}0&0.5\\0.5&0\end{pmatrix}$, $\mathbf h = \begin{pmatrix}3\\3\end{pmatrix}$. Compute $\mathbf r$.
11. **E–I pair:** $W = \begin{pmatrix}0&-1\\0.5&0\end{pmatrix}$ (neuron 2 inhibits neuron 1, neuron 1 excites neuron 2), $\mathbf h = \begin{pmatrix}4\\1\end{pmatrix}$. Compute the steady state.
12. **Mini-GLM:** fit $y = \beta_0 + \beta_1 x$ to the data $(0, 1)$, $(1, 3)$, $(2, 5)$ via the normal equations $X^TX\boldsymbol\beta = X^T\mathbf y$ with $X = \begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix}$.
