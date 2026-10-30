---
tags: [linear-algebra, determinant, type/worksheet]
---
# C2 Determinants – Worksheet

> Theory: [[C2 Determinants]] · Solutions: [[C2 Determinants - Solutions]] · Log mistakes in [[Mistakes - Linear Algebra]]
> No calculator needed.

## Level 1 – 2×2 and triangular
1. $\det\begin{pmatrix}3&1\\2&4\end{pmatrix}$
2. $\det\begin{pmatrix}2&-1\\4&-2\end{pmatrix}$ – what does the result mean?
3. $\det\begin{pmatrix}1&2&3\\0&4&5\\0&0&6\end{pmatrix}$
4. For which $k$ is $\begin{pmatrix}k&2\\3&k-1\end{pmatrix}$ **not** invertible?

## Level 2 – 3×3
5. $\det\begin{pmatrix}2&0&1\\1&3&2\\1&1&2\end{pmatrix}$ (Sarrus **and** Laplace – do both to check yourself)
6. $\det\begin{pmatrix}1&2&0\\3&-1&4\\0&2&1\end{pmatrix}$
7. Compute $\det\begin{pmatrix}2&4&2\\1&3&1\\3&1&4\end{pmatrix}$ by reducing to triangular form.

## Level 3 – Properties
8. $A$ is a $3\times3$ matrix with $\det A = 5$. Compute $\det(2A)$, $\det(A^T)$, $\det(A^{-1})$, $\det(A^2)$.
9. What happens to the determinant if you swap two rows? If one row is a multiple of another?
10. Show with $A = B = I_2$ that $\det(A + B)\neq\det A + \det B$.

## Level 4 – Geometry & neuro
11. Area of the parallelogram spanned by $(3, 1)$ and $(1, 2)$.
12. Volume of the parallelepiped spanned by $(1,0,0)$, $(0,2,0)$, $(1,1,3)$.
13. **GLM:** a design matrix has columns (intercept, regressor $x$) with $X = \begin{pmatrix}1&1\\1&2\\1&3\end{pmatrix}$.
    a) Compute $X^TX$ and its determinant.
    b) Now the columns are $x = (1,2,3)^T$ and $z = 2x$. Compute $\det(X^TX)$. What's the problem?
14. **Morphometry:** a warp maps $(x, y, z)\mapsto(2x,\ y,\ 1.5z)$. By what factor does it change local volume? Does this region look enlarged or shrunk relative to the template?
