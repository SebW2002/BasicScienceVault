---
tags: [linear-algebra, linear-system, type/solution]
---
# C3 Linear Systems and Gaussian Elimination – Solutions

> Worksheet: [[C3 Linear Systems and Gaussian Elimination - Worksheet]] · Theory: [[C3 Linear Systems and Gaussian Elimination]] · Wrong? → [[Mistakes - Linear Algebra]]

## Level 1
1. Add: $2x = 6\Rightarrow x = 3$, $y = 2$
2. From eq. 2: $y = 4x - 10$ → $2x + 12x - 30 = 12 \Rightarrow x = 3$, $y = 2$
3. $2\cdot$eq. 1: $2x + 2y = 4$, but eq. 2 says $= 5$ → contradiction $0 = 1$ → **no solution** (parallel lines).

## Level 2
4. See theory note: $(x, y, z) = (1, 2, 3)$
5. $\left(\begin{array}{ccc|c}2&1&-1&8\\-3&-1&2&-11\\-2&1&2&-3\end{array}\right)$
   $R_2 + \tfrac32R_1$: $(0,\ \tfrac12,\ \tfrac12 \mid 1)$; $\;R_3 + R_1$: $(0,\ 2,\ 1\mid5)$
   $R_3 - 4R_2$: $(0,\ 0,\ -1\mid1)$ → $z = -1$
   $\tfrac12y - \tfrac12 = 1\Rightarrow y = 3$; $\;2x + 3 + 1 = 8\Rightarrow x = 2$ → $(2, 3, -1)$
   Check eq. 3: $-4 + 3 - 2 = -3$ ✓
6. $R_2 - 2R_1$: $(0, -3, 3\mid-3)$; $R_3 - 3R_1$: $(0, -3, 3\mid-3)$; $R_3 - R_2$: zero row → infinitely many.
   $z = t$: $-3y + 3t = -3\Rightarrow y = 1 + t$; $x = 3 - 2(1+t) + t = 1 - t$.
   $$\mathbf x = \begin{pmatrix}1\\1\\0\end{pmatrix} + t\begin{pmatrix}-1\\1\\1\end{pmatrix},\quad t\in\mathbb R$$ (a line in 3D)

## Level 3
7. $R_2 - 2R_1 = \mathbf 0$; $R_3 - R_1 = (0, -2, -2)$ → two non-zero rows → rank 2.
8. Eq. 2 $= 2\cdot$eq. 1 exactly when $2a = 4$, i.e. $a = 2$ → infinitely many. For $a\neq2$: $\det = 4 - 2a\neq0$ → exactly one. (No case without solution, since $b$ is consistent.)
9. $c = 1$; $a + b + 1 = 2$; $4a + 2b + 1 = 7$ → $a + b = 1$, $2a + b = 3$ → $a = 2$, $b = -1$ → $y = 2x^2 - x + 1$

## Level 4
10. $r_1 - 0.5r_2 = 3$, $-0.5r_1 + r_2 = 3$. By symmetry $r_1 = r_2 = r$: $0.5r = 3\Rightarrow r = 6$ → $\mathbf r = (6, 6)$. Recurrent excitation doubles the response to the input of 3.
11. $I - W = \begin{pmatrix}1&1\\-0.5&1\end{pmatrix}$: $r_1 + r_2 = 4$, $-0.5r_1 + r_2 = 1$ → subtract: $1.5r_1 = 3\Rightarrow r_1 = 2$, $r_2 = 2$. Check eq. 1: $2 + 2 = 4$ ✓
12. $X^TX = \begin{pmatrix}3&3\\3&5\end{pmatrix}$, $X^T\mathbf y = \begin{pmatrix}1+3+5\\0+3+10\end{pmatrix} = \begin{pmatrix}9\\13\end{pmatrix}$.
    $3\beta_0 + 3\beta_1 = 9$, $3\beta_0 + 5\beta_1 = 13$ → $2\beta_1 = 4$ → $\beta_1 = 2$, $\beta_0 = 1$ → $y = 1 + 2x$ (fits the data exactly).
