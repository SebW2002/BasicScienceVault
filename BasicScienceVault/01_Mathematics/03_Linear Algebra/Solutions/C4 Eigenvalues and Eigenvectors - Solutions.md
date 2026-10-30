---
tags: [linear-algebra, eigenvalue, type/solution]
---
# C4 Eigenvalues and Eigenvectors – Solutions

> Worksheet: [[C4 Eigenvalues and Eigenvectors - Worksheet]] · Theory: [[C4 Eigenvalues and Eigenvectors]] · Wrong? → [[Mistakes - Linear Algebra]]

## Level 1
1. $A\mathbf v = \begin{pmatrix}3\\3\end{pmatrix} = 3\mathbf v$ → yes, $\lambda = 3$.
2. $3, -1$ and $1, 2, 3$ – diagonal/triangular matrices have their eigenvalues on the diagonal ($\det(A - \lambda I)$ is the product of $(a_{ii} - \lambda)$).
3. $\mathbf 0$: no (by definition – otherwise every $\lambda$ would work). $\lambda = 0$: yes, exactly when $A$ is singular ($\det A = 0$).

## Level 2
4. $\lambda^2 - 7\lambda + 10 = 0 \Rightarrow \lambda\in\{5, 2\}$; $\mathbf v_5 = (1, 1)^T$, $\mathbf v_2 = (1, -2)^T$ (see theory note). Check: $5 + 2 = 7 = \operatorname{tr}A$ ✓, $5\cdot2 = 10 = 12 - 2 = \det A$ ✓
5. $\lambda^2 - 4\lambda + 3 = 0\Rightarrow\lambda\in\{3, 1\}$.
   $\lambda = 3$: $\begin{pmatrix}-1&1\\1&-1\end{pmatrix}\mathbf v = 0 \Rightarrow (1, 1)^T$; $\;\lambda = 1$: $\begin{pmatrix}1&1\\1&1\end{pmatrix}\mathbf v = 0\Rightarrow(1, -1)^T$.
   $(1,1)\cdot(1,-1) = 0$ ✓ orthogonal (symmetric matrix).
6. $\lambda^2 + 1 = 0\Rightarrow\lambda = \pm i$. No real eigenvector – the matrix is a rotation by 90°, no direction stays fixed.
7. Block structure: $\lambda = 2$ from the first entry; the block $\begin{pmatrix}3&4\\4&-3\end{pmatrix}$ gives $\lambda^2 - 0\cdot\lambda + (-9 - 16) = \lambda^2 - 25 = 0 \Rightarrow \lambda = \pm5$. Eigenvalues $2, 5, -5$.

## Level 3
8. $V = \begin{pmatrix}1&1\\1&-2\end{pmatrix}$, $\Lambda = \begin{pmatrix}5&0\\0&2\end{pmatrix}$, $V^{-1} = \frac{1}{-3}\begin{pmatrix}-2&-1\\-1&1\end{pmatrix} = \begin{pmatrix}\tfrac23&\tfrac13\\ \tfrac13&-\tfrac13\end{pmatrix}$.
   $A^3 = V\begin{pmatrix}125&0\\0&8\end{pmatrix}V^{-1} = \begin{pmatrix}125&8\\125&-16\end{pmatrix}\begin{pmatrix}\tfrac23&\tfrac13\\ \tfrac13&-\tfrac13\end{pmatrix} = \begin{pmatrix}86&39\\78&47\end{pmatrix}$
   Direct: $A^2 = \begin{pmatrix}18&7\\14&11\end{pmatrix}$, $A^3 = A^2A = \begin{pmatrix}72 + 14 & 18 + 21\\ 56 + 22 & 14 + 33\end{pmatrix} = \begin{pmatrix}86&39\\78&47\end{pmatrix}$ ✓

## Level 4
9. $\lambda^2 + 4\lambda + 3 = 0\Rightarrow\lambda\in\{-1, -3\}$, both negative → stable (activity decays to 0).
10. $\operatorname{tr} = -2$, $\det = 1 + 4 = 5$ → $\lambda^2 + 2\lambda + 5 = 0\Rightarrow\lambda = -1\pm\sqrt{1 - 5} = -1\pm2i$.
    Real part $-1 < 0$ → decaying; imaginary part $\pm2$ → oscillation with angular frequency 2. Trajectory: inward **spiral** (damped oscillation) – the typical E–I rhythm.
11. Triangular → $\lambda\in\{0.5, 0.9\}$, both $\lvert\lambda\rvert < 1$ → activity dies out. For large $t$, $0.9^t$ decays more slowly than $0.5^t$ → $\lambda = 0.9$ dominates.
12. Eigenvalues $3, 1$ (task 5). First PC: $\frac{1}{\sqrt2}(1, 1)^T$ – both neurons co-vary. Explained variance $\frac{3}{3+1} = 75\%$.
13. a) $\lambda_W = \pm2$ → $\lambda_{W-I} = 1, -3$. A positive eigenvalue → **unstable** (runaway excitation along $(1,1)$).
    b) $\lambda_W = \pm0.5$ → $\lambda_{W-I} = -0.5, -1.5$ → stable.
