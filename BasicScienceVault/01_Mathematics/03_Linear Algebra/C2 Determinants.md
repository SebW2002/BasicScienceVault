---
aliases: [Determinants, Determinante]
tags: [linear-algebra, determinant, matrix, type/overview, neuro]
---
# C2 Determinants

> [[C0 Linear Algebra MOC|↑ Linear Algebra MOC]] · [[C2 Determinants - Worksheet|✏️ Worksheet]] · [[C2 Determinants - Solutions|✅ Solutions]] · [[Mistakes - Linear Algebra|⚠️ Mistake log]]

## Why this matters
The determinant is a single number that tells you whether a square matrix is invertible (≠ 0), whether a linear system has a unique solution, and by how much a transformation scales areas/volumes. It is the gateway to eigenvalues.

## Computing determinants
**2×2:**
$$\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = \begin{vmatrix}a&b\\c&d\end{vmatrix} = ad - bc$$

**3×3 – rule of Sarrus:** copy the first two columns to the right; add the three "down-right" diagonal products, subtract the three "up-right" ones:
$$\det\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix} = aei + bfg + cdh - ceg - afh - bdi$$
(Sarrus only works for 3×3!)

**Laplace (cofactor) expansion** – along any row or column, with checkerboard signs $\begin{smallmatrix}+&-&+\\-&+&-\\+&-&+\end{smallmatrix}$:
$$\det A = a_{11}\begin{vmatrix}e&f\\h&i\end{vmatrix} - a_{12}\begin{vmatrix}d&f\\g&i\end{vmatrix} + a_{13}\begin{vmatrix}d&e\\g&h\end{vmatrix}$$
Tip: expand along the row/column with the most zeros.

**Triangular matrices:** $\det$ = product of the diagonal entries. Gaussian elimination brings any matrix into triangular form ([[C3 Linear Systems and Gaussian Elimination]]) – track how the row operations change the determinant:

| Row operation | Effect on $\det$ |
|---|---|
| Swap two rows | sign flips |
| Multiply a row by $c$ | $\det$ multiplied by $c$ |
| Add a multiple of one row to another | **no change** |

## Properties ($A, B$ are $n\times n$)
| Property | Formula |
|---|---|
| Invertibility | $A$ invertible $\iff \det A \neq 0$ |
| Product | $\det(AB) = \det A\cdot\det B$ |
| Transpose | $\det(A^T) = \det A$ |
| Inverse | $\det(A^{-1}) = \frac1{\det A}$ |
| Scalar | $\det(cA) = c^n\det A$ (not $c\det A$!) |
| Linear dependence | rows/columns linearly dependent $\iff \det A = 0$ |
| Eigenvalues | $\det A = \lambda_1\cdot\lambda_2\cdots\lambda_n$ ([[C4 Eigenvalues and Eigenvectors]]) |
| ❌ | $\det(A + B)\neq\det A + \det B$ |

## Geometric meaning
$\lvert\det A\rvert$ = factor by which $A$ scales areas (2D) or volumes (3D). The sign tells whether orientation is preserved ($+$) or mirrored ($-$).
- Parallelogram spanned by $\mathbf u, \mathbf v$: area $= \lvert\det(\mathbf u\ \mathbf v)\rvert$.
- Parallelepiped spanned by $\mathbf u, \mathbf v, \mathbf w$: volume $= \lvert\det(\mathbf u\ \mathbf v\ \mathbf w)\rvert = \lvert\mathbf u\cdot(\mathbf v\times\mathbf w)\rvert$ ([[D2 Dot and Cross Product]]).
- $\det = 0$: the map squashes space into a lower dimension – information is lost, so it can't be undone.

## In neuroscience #neuro
- **Multicollinearity in the GLM:** if two regressors in the fMRI design matrix are (nearly) linearly dependent, $\det(X^TX)\approx0$ and $(X^TX)^{-1}$ doesn't exist or is numerically unstable → the betas can't be separated. Classic case: two conditions that always occur together.
- **Voxel-/tensor-based morphometry:** normalising a brain to a template uses a nonlinear warp. The **Jacobian determinant** at each voxel says how much local volume was stretched (> 1) or compressed (< 1) – used to measure atrophy or regional growth.
- **Stability of 2D dynamical systems** (e.g. Wilson–Cowan E–I model): for the Jacobian $J$, $\det J$ and $\operatorname{tr}J$ classify the fixed point – $\det J < 0$ means a saddle (unstable).
- **Change of variables in probability densities:** transforming random variables scales densities by $1/\lvert\det\rvert$ – used in normalising flows and ICA.

## Connections
- Invertibility of matrices → [[C1 Matrices]]
- Unique solvability of $A\mathbf x = \mathbf b$ → [[C3 Linear Systems and Gaussian Elimination]]
- Characteristic polynomial $\det(A - \lambda I) = 0$ → [[C4 Eigenvalues and Eigenvectors]]
- Area/volume, triple product, cross product formula → [[D2 Dot and Cross Product]]
- Linear independence → [[D1 Vectors in 2D and 3D]]

## Where this is used in the vault
**Most important applications:** Collinearity in GLMs ([[Meth04 In Vivo Imaging]], [[CS12 Neuroimaging Data Analysis]]), Jacobian determinants in morphometry, invertibility for ridge ([[CS04 Optimization]]), mirror images/chirality ([[Ch07 Organic Chemistry Essentials]]).

**All notes that build on this topic:**
- *Chemistry:* [[Ch07 Organic Chemistry Essentials]]
- *Methods:* [[Meth04 In Vivo Imaging]]
- *Computer Science:* [[CS04 Optimization]] · [[CS12 Neuroimaging Data Analysis]]
- *Programming:* [[Py05 NumPy and Arrays]] · [[MAT02 MATLAB Matrices and Vectorization]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- $\det\neq0$ ⟺ invertible ⟺ unique solution ⟺ columns independent.
- 2×2: $ad - bc$; 3×3: Sarrus or expansion; triangular: product of diagonal.
- $\det(cA) = c^n\det A$; $\det$ is multiplicative but not additive.
