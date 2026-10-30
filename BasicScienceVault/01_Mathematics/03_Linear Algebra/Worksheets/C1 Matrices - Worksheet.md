---
tags: [linear-algebra, matrix, type/worksheet]
---
# C1 Matrices – Worksheet

> Theory: [[C1 Matrices]] · Solutions: [[C1 Matrices - Solutions]] · Log mistakes in [[Mistakes - Linear Algebra]]
> No calculator needed. Throughout:
> $$A = \begin{pmatrix}1&2\\3&4\end{pmatrix},\qquad B = \begin{pmatrix}0&1\\-1&2\end{pmatrix}$$

## Level 1 – Basic operations
1. Compute $A + B$ and $2A - B$.
2. Compute $A^T$.
3. Which products are defined, and what size are they? a) $(2\times3)(3\times4)$ b) $(3\times2)(3\times2)$ c) $(1\times3)(3\times1)$ d) $(3\times1)(1\times3)$

## Level 2 – Products
4. Compute $AB$.
5. Compute $BA$. Compare with 4.
6. Compute $M\mathbf v$ for $M = \begin{pmatrix}1&0&2\\-1&3&1\end{pmatrix}$, $\mathbf v = \begin{pmatrix}2\\1\\-1\end{pmatrix}$.
7. Compute $C^2$ for $C = \begin{pmatrix}1&0&1\\0&2&0\\1&0&1\end{pmatrix}$.
8. Verify $(AB)^T = B^TA^T$ with the matrices above.

## Level 3 – Inverse
9. Compute $A^{-1}$ and verify $AA^{-1} = I$.
10. Compute the inverse of $D = \begin{pmatrix}2&0\\0&5\end{pmatrix}$.
11. Solve $AX = B$ for the matrix $X$.
12. Does $\begin{pmatrix}2&4\\1&2\end{pmatrix}$ have an inverse? Why (not)?

## Level 4 – Neuro
13. **Connectivity:** three neurons with
    $$W = \begin{pmatrix}0&0.5&0\\1&0&-1\\0&2&0\end{pmatrix},\qquad \mathbf r = \begin{pmatrix}10\\4\\2\end{pmatrix}\text{ Hz}$$
    a) Compute the total input $\mathbf u = W\mathbf r$. b) Which neuron inhibits which? c) Which neuron receives no input from itself?
14. **Covariance:** a data matrix of 2 neurons × 3 time points is $X = \begin{pmatrix}1&2&3\\3&2&1\end{pmatrix}$. Compute $XX^T$ and check that it is symmetric.
