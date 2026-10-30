---
tags: [linear-algebra, matrix, type/solution]
---
# C1 Matrices – Solutions

> Worksheet: [[C1 Matrices - Worksheet]] · Theory: [[C1 Matrices]] · Wrong? → [[Mistakes - Linear Algebra]]

## Level 1
1. $A + B = \begin{pmatrix}1&3\\2&6\end{pmatrix}$; $\;2A - B = \begin{pmatrix}2&4\\6&8\end{pmatrix} - \begin{pmatrix}0&1\\-1&2\end{pmatrix} = \begin{pmatrix}2&3\\7&6\end{pmatrix}$
2. $A^T = \begin{pmatrix}1&3\\2&4\end{pmatrix}$
3. a) $2\times4$ b) not defined ($2\neq3$) c) $1\times1$ (a number – the dot product!) d) $3\times3$ (outer product)

## Level 2
4. $AB = \begin{pmatrix}-2&5\\-4&11\end{pmatrix}$ (see theory note)
5. $BA = \begin{pmatrix}0\cdot1 + 1\cdot3 & 0\cdot2 + 1\cdot4\\ -1\cdot1 + 2\cdot3 & -1\cdot2 + 2\cdot4\end{pmatrix} = \begin{pmatrix}3&4\\5&6\end{pmatrix} \neq AB$
6. $\begin{pmatrix}2 + 0 - 2\\ -2 + 3 - 1\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}$
7. $C^2 = \begin{pmatrix}2&0&2\\0&4&0\\2&0&2\end{pmatrix}$
8. $(AB)^T = \begin{pmatrix}-2&-4\\5&11\end{pmatrix}$. $B^T A^T = \begin{pmatrix}0&-1\\1&2\end{pmatrix}\begin{pmatrix}1&3\\2&4\end{pmatrix} = \begin{pmatrix}-2&-4\\5&11\end{pmatrix}$ ✓

## Level 3
9. $\det A = 4 - 6 = -2$ → $A^{-1} = -\frac12\begin{pmatrix}4&-2\\-3&1\end{pmatrix} = \begin{pmatrix}-2&1\\ \tfrac32&-\tfrac12\end{pmatrix}$.
   Check: $\begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}-2&1\\1.5&-0.5\end{pmatrix} = \begin{pmatrix}-2 + 3 & 1 - 1\\ -6 + 6 & 3 - 2\end{pmatrix} = I$ ✓
10. $D^{-1} = \begin{pmatrix}\tfrac12&0\\0&\tfrac15\end{pmatrix}$ (diagonal: invert each entry)
11. $X = A^{-1}B = \begin{pmatrix}-2&1\\1.5&-0.5\end{pmatrix}\begin{pmatrix}0&1\\-1&2\end{pmatrix} = \begin{pmatrix}-1&0\\ \tfrac12&\tfrac12\end{pmatrix}$. Check: $AX = \begin{pmatrix}-1 + 1 & 0 + 1\\ -3 + 2 & 0 + 2\end{pmatrix} = B$ ✓
12. $\det = 4 - 4 = 0$ → no inverse. (The rows are multiples of each other.)

## Level 4
13. a) $\mathbf u = \begin{pmatrix}0.5\cdot4\\ 1\cdot10 - 1\cdot2\\ 2\cdot4\end{pmatrix} = \begin{pmatrix}2\\8\\8\end{pmatrix}$
    b) $W_{23} = -1 < 0$: neuron 3 inhibits neuron 2 (row = target, column = source).
    c) All diagonal entries are 0 → no neuron has a self-connection (autapse).
14. $XX^T = \begin{pmatrix}1+4+9 & 3+4+3\\ 3+4+3 & 9+4+1\end{pmatrix} = \begin{pmatrix}14&10\\10&14\end{pmatrix}$ – symmetric ✓ (in general $(XX^T)^T = (X^T)^TX^T = XX^T$).
