---
tags: [linear-algebra, eigenvalue, type/worksheet]
---
# C4 Eigenvalues and Eigenvectors – Worksheet

> Theory: [[C4 Eigenvalues and Eigenvectors]] · Solutions: [[C4 Eigenvalues and Eigenvectors - Solutions]] · Log mistakes in [[Mistakes - Linear Algebra]]
> No calculator needed.

## Level 1 – Concept
1. Is $\mathbf v = \begin{pmatrix}1\\1\end{pmatrix}$ an eigenvector of $A = \begin{pmatrix}2&1\\1&2\end{pmatrix}$? If yes, with which eigenvalue?
2. Eigenvalues of $\begin{pmatrix}3&0\\0&-1\end{pmatrix}$ and of $\begin{pmatrix}1&4&5\\0&2&6\\0&0&3\end{pmatrix}$ (no calculation needed – why?)
3. Can $\mathbf 0$ be an eigenvector? Can $0$ be an eigenvalue?

## Level 2 – Compute
4. Eigenvalues and eigenvectors of $\begin{pmatrix}4&1\\2&3\end{pmatrix}$. Check with trace and determinant.
5. Eigenvalues and eigenvectors of $\begin{pmatrix}2&1\\1&2\end{pmatrix}$. Show that the eigenvectors are orthogonal.
6. Eigenvalues of $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$. Interpret geometrically.
7. Eigenvalues of $\begin{pmatrix}2&0&0\\0&3&4\\0&4&-3\end{pmatrix}$.

## Level 3 – Diagonalisation
8. Using task 4, write $A = V\Lambda V^{-1}$ and compute $A^3$. Check by computing $A^2$ and $A^3$ directly.

## Level 4 – Dynamics & neuro
9. **Stability:** $\frac{d\mathbf x}{dt} = A\mathbf x$ with $A = \begin{pmatrix}-2&1\\1&-2\end{pmatrix}$. Stable?
10. **E–I oscillation:** $A = \begin{pmatrix}-1&-4\\1&-1\end{pmatrix}$. Compute the eigenvalues. What does the trajectory look like?
11. **Discrete system:** $\mathbf x_{t+1} = \begin{pmatrix}0.5&0.2\\0&0.9\end{pmatrix}\mathbf x_t$. Does activity die out? Which eigenvalue dominates for large $t$?
12. **PCA:** two neurons have covariance matrix $C = \begin{pmatrix}2&1\\1&2\end{pmatrix}$. Give the first principal component (normalised) and the fraction of variance it explains.
13. **Recurrent network:** $\tau\frac{d\mathbf r}{dt} = (W - I)\mathbf r$. Stable for a) $W = \begin{pmatrix}0&2\\2&0\end{pmatrix}$, b) $W = \begin{pmatrix}0&0.5\\0.5&0\end{pmatrix}$? (Hint: eigenvalues of $W - I$ are $\lambda_W - 1$.)
