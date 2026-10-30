---
tags: [linear-algebra, determinant, type/solution]
---
# C2 Determinants – Solutions

> Worksheet: [[C2 Determinants - Worksheet]] · Theory: [[C2 Determinants]] · Wrong? → [[Mistakes - Linear Algebra]]

## Level 1
1. $12 - 2 = 10$
2. $-4 - (-4) = 0$ → singular; the second row is twice the first.
3. Triangular: $1\cdot4\cdot6 = 24$
4. $k(k-1) - 6 = 0 \Rightarrow k^2 - k - 6 = (k-3)(k+2) = 0 \Rightarrow k = 3$ or $k = -2$

## Level 2
5. Sarrus: $2\cdot3\cdot2 + 0\cdot2\cdot1 + 1\cdot1\cdot1 - 1\cdot3\cdot1 - 2\cdot2\cdot1 - 0\cdot1\cdot2 = 12 + 0 + 1 - 3 - 4 - 0 = 6$
   Laplace (row 1): $2\begin{vmatrix}3&2\\1&2\end{vmatrix} - 0 + 1\begin{vmatrix}1&3\\1&1\end{vmatrix} = 2(6 - 2) + (1 - 3) = 8 - 2 = 6$ ✓
6. Row 1: $1\begin{vmatrix}-1&4\\2&1\end{vmatrix} - 2\begin{vmatrix}3&4\\0&1\end{vmatrix} + 0 = 1(-1 - 8) - 2(3 - 0) = -9 - 6 = -15$
7. $R_2 - \tfrac12R_1 \to (0, 1, 0)$; $\;R_3 - \tfrac32R_1 \to (0, -5, 1)$; $\;R_3 + 5R_2 \to (0, 0, 1)$.
   Triangular $\begin{pmatrix}2&4&2\\0&1&0\\0&0&1\end{pmatrix}$, only "add multiple" operations used → $\det = 2\cdot1\cdot1 = 2$.

## Level 3
8. $\det(2A) = 2^3\cdot5 = 40$; $\;\det A^T = 5$; $\;\det A^{-1} = \tfrac15$; $\;\det A^2 = 25$
9. Swap → sign flips. Multiple row → $\det = 0$ (rows dependent).
10. $\det(2I) = 4$, but $\det I + \det I = 2$.

## Level 4
11. $\lvert 3\cdot2 - 1\cdot1\rvert = 5$
12. $\det\begin{pmatrix}1&0&1\\0&2&1\\0&0&3\end{pmatrix}$ (vectors as columns, triangular) $= 6$
13. a) $X^TX = \begin{pmatrix}3&6\\6&14\end{pmatrix}$, $\det = 42 - 36 = 6\neq0$ ✓ invertible.
    b) $X = \begin{pmatrix}1&2\\2&4\\3&6\end{pmatrix}$, $X^TX = \begin{pmatrix}14&28\\28&56\end{pmatrix}$, $\det = 784 - 784 = 0$ → not invertible; the two regressors are perfectly collinear, their effects can't be separated (no unique $\hat\beta$).
14. Jacobian matrix $= \operatorname{diag}(2, 1, 1.5)$, $\det = 2\cdot1\cdot1.5 = 3$ → local volume is tripled.
    If this warp maps subject → template, the subject's region had to be stretched to fit, i.e. it was **smaller** than in the template (e.g. atrophy). Toolboxes differ in which direction they report, so always check the warp direction.
