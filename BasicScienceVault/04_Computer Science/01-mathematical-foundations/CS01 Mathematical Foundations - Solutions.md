---
tags: [computer-science, linear-algebra, type/solution]
---
# CS01 Mathematical Foundations – Solutions

> Worksheet: [[CS01 Mathematical Foundations - Worksheet]] · Theory: [[CS01 Mathematical Foundations]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. Shape (40, 120, 300), i.e. 1,440,000 numbers. For PCA over neurons: merge trials and time into samples, giving a matrix of $(40\cdot300)\times120 = 12{,}000\times120$ (samples × features).
2. $W\mathbf x = (2 + 2,\ 0 - 1,\ 6 + 1) = (4, -1, 7)$; $+\mathbf b = (4, 0, 6)$. Shapes: $W$ (3×2), $\mathbf x$ (2), $\mathbf b,\mathbf y$ (3).
3. Matrix multiplication is associative: $W_2(W_1\mathbf x) = (W_2W_1)\mathbf x$. $W_2W_1 = (2\cdot1 + 1\cdot1,\ 2\cdot0 + 1\cdot1) = (3, 1)$.

## Level 2
4. $L_1 = 7$, $L_2 = 5$, $L_\infty = 4$.
5. Euclidean: $\lVert(2, 0, 2)\rVert = \sqrt8\approx2.83$. Cosine: $\frac{8 + 0 + 8}{\sqrt8\cdot\sqrt{32}} = \frac{16}{16} = 1$. Same **pattern** (direction), different **gain**. Cosine says identical, Euclidean says different. Which one you want depends on the question.
6. Centred: $\mathbf a' = (-1, 0, 1)$, $\mathbf b' = (1, 0, -1)$, so $r = \frac{-1 + 0 - 1}{\sqrt2\sqrt2} = -1$ and the correlation distance is $1 - (-1) = 2$ (the maximum: perfectly anti-correlated patterns).

## Level 3
7. Singular values are non-negative: $\sigma_1 = 3$, $\sigma_2 = 2$. One valid SVD: $V = I$, $\Sigma = \operatorname{diag}(3, 2)$, $U = \operatorname{diag}(1, -1)$ (the sign moves into $U$). Check: $U\Sigma V^T = \operatorname{diag}(3, -2)$ ✓.
8. $A^TA = \begin{pmatrix}2&2\\2&2\end{pmatrix}$: $\lambda^2 - 4\lambda = 0$, so $\lambda\in\{4, 0\}$ and $\sigma\in\{2, 0\}$. **Rank 1** (the columns are identical).
9. Eigenvalues 3 and 1 ([[C4 Eigenvalues and Eigenvectors - Solutions]], task 12). PC1 $= \frac{1}{\sqrt2}(1, 1)$ with variance 3; PC2 $= \frac{1}{\sqrt2}(1, -1)$ with variance 1. Explained ratio of PC1 $= 3/4 = 75\%$.
10. Energies: 100, 9, 1, 0.01, total 110.01. Rank 1: $100/110.01\approx90.9\%$. Rank 2: $109/110.01\approx99.1\%$.

## Level 4
11. $\nabla f = (2xy,\ x^2 + 3)$, so at $(1, 2)$: $(4, 4)$. The steepest descent is along $-\nabla f = (-4, -4)$, i.e. direction $\frac{1}{\sqrt2}(-1, -1)$.
12. $J = \begin{pmatrix}y&x\\1&1\\2x&0\end{pmatrix}$, so at $(2, 1)$: $\begin{pmatrix}1&2\\1&1\\4&0\end{pmatrix}$ (3×2).
13. $2X^T(X\mathbf w - \mathbf y) = 0\Rightarrow X^TX\mathbf w = X^T\mathbf y$, the **normal equations** of least squares, seen in the GLM ([[C3 Linear Systems and Gaussian Elimination]], [[Meth04 In Vivo Imaging]]).
14. $\frac{\partial L}{\partial w} = \underbrace{2(a - t)}_{\partial L/\partial a}\cdot\underbrace{\sigma(z)(1 - \sigma(z))}_{\partial a/\partial z}\cdot\underbrace{x}_{\partial z/\partial w}$. This is backprop for a single neuron.
15. Dot product $= 2 + 2 + 12 + 12 = 28$; both norms $= \sqrt{30}$; cosine $= 28/30\approx0.933$.
