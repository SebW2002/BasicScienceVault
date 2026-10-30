---
tags: [computer-science, linear-algebra, type/worksheet]
---
# CS01 Mathematical Foundations – Worksheet

> Theory: [[CS01 Mathematical Foundations]] · Solutions: [[CS01 Mathematical Foundations - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮.

## Level 1 – Data containers & linear maps
1. A calcium imaging experiment has 40 trials, 120 neurons and 300 frames per trial. What is the tensor shape? How many numbers is that? If you want PCA over neurons using all time points of all trials, what matrix shape do you need?
2. Compute $\mathbf y = W\mathbf x + \mathbf b$ for $W = \begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}$, $\mathbf x = \begin{pmatrix}2\\1\end{pmatrix}$, $\mathbf b = \begin{pmatrix}0\\1\\-1\end{pmatrix}$. What are the shapes?
3. Show that two linear layers $W_2(W_1\mathbf x)$ can be replaced by a single matrix. Compute it for $W_1 = \begin{pmatrix}1&0\\1&1\end{pmatrix}$, $W_2 = \begin{pmatrix}2&1\end{pmatrix}$.

## Level 2 – Norms and distances
4. For $\mathbf x = (3, -4)$: compute $\lVert\mathbf x\rVert_1$, $\lVert\mathbf x\rVert_2$, $\lVert\mathbf x\rVert_\infty$.
5. Two population vectors are $\mathbf a = (2, 0, 2)$ and $\mathbf b = (4, 0, 4)$. Compute the Euclidean distance and the cosine similarity. Interpret.
6. $\mathbf a = (1, 2, 3)$, $\mathbf b = (3, 2, 1)$. Compute the correlation distance $1 - r$. (Hint: centre both vectors first.)

## Level 3 – SVD and PCA
7. Find the singular values of $A = \begin{pmatrix}3&0\\0&-2\end{pmatrix}$. What are $U$ and $V$? (Hint: a sign can be moved into $U$.)
8. Find the singular values and rank of $A = \begin{pmatrix}1&1\\1&1\end{pmatrix}$ via the eigenvalues of $A^TA$.
9. A centred dataset of two neurons has covariance $C = \begin{pmatrix}2&1\\1&2\end{pmatrix}$. Give the principal components, their variances, and the explained variance ratio of PC1.
10. A matrix has singular values 10, 3, 1, 0.1. What fraction of the total "energy" ($\sum\sigma_i^2$) does the rank-1 approximation keep? The rank-2 approximation?

## Level 4 – Gradients and Jacobians
11. Compute the gradient of $f(x, y) = x^2y + 3y$ at $(1, 2)$. In which direction should you step to decrease $f$ fastest?
12. Compute the Jacobian of $\mathbf f(x, y) = (xy,\ x + y,\ x^2)$ at $(2, 1)$.
13. For $L(\mathbf w) = \lVert X\mathbf w - \mathbf y\rVert^2$, the gradient is $2X^T(X\mathbf w - \mathbf y)$. Set it to zero and derive the normal equations. Where did you see them before?
14. Chain rule: $z = wx + b$, $a = \sigma(z)$ with $\sigma' = \sigma(1-\sigma)$, $L = (a - t)^2$. Write $\frac{\partial L}{\partial w}$ as a product of three factors.
15. 🧮 Compute the cosine similarity between $(1, 2, 3, 4)$ and $(2, 1, 4, 3)$.
