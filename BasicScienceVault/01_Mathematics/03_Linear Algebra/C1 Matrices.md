---
aliases: [Matrices, Matrix Rules, Matrizen]
tags: [linear-algebra, matrix, type/overview, neuro]
---
# C1 Matrices

> [[C0 Linear Algebra MOC|↑ Linear Algebra MOC]] · [[C1 Matrices - Worksheet|✏️ Worksheet]] · [[C1 Matrices - Solutions|✅ Solutions]] · [[Mistakes - Linear Algebra|⚠️ Mistake log]]

## Why this matters
A matrix is a table of numbers – and also a **linear map** that transforms vectors. Neuroscience data are matrices (neurons × time, voxels × scans, trials × features), networks are matrices (connectivity $W$), and the general linear model for fMRI is a matrix equation.

## Notation
An $m\times n$ matrix has $m$ **rows** and $n$ **columns**; $a_{ij}$ is the entry in row $i$, column $j$ ("**r**ow before **c**olumn").
$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{pmatrix} \in \mathbb R^{2\times3}$$
Special matrices: square ($m = n$), **identity** $I$ (1s on the diagonal), diagonal, zero matrix, **symmetric** ($A^T = A$).

## Operations
| Operation | Rule | Condition |
|---|---|---|
| Sum $A + B$ | entrywise | same size |
| Scalar $cA$ | multiply every entry | – |
| Product $AB$ | $(AB)_{ij} = \sum_k a_{ik}b_{kj}$ ("row × column") | columns of $A$ = rows of $B$ |
| Transpose $A^T$ | rows ↔ columns: $(A^T)_{ij} = a_{ji}$ | – |

**Dimension check:** $(m\times n)\cdot(n\times p) = (m\times p)$ – inner numbers must match, outer numbers give the size.

**Example:**
$$\begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}0&1\\-1&2\end{pmatrix} = \begin{pmatrix}1\cdot0 + 2\cdot(-1) & 1\cdot1 + 2\cdot2\\ 3\cdot0 + 4\cdot(-1) & 3\cdot1 + 4\cdot2\end{pmatrix} = \begin{pmatrix}-2&5\\-4&11\end{pmatrix}$$

## Rules
| ✅ True | ❌ Generally false |
|---|---|
| $(AB)C = A(BC)$ (associative) | $AB = BA$ (**not commutative!**) |
| $A(B + C) = AB + AC$ | $AB = 0 \Rightarrow A = 0$ or $B = 0$ |
| $AI = IA = A$ | $AB = AC \Rightarrow B = C$ |
| $(A^T)^T = A$, $\;(A + B)^T = A^T + B^T$ | |
| $(AB)^T = B^T A^T$ (order reverses!) | $(AB)^T = A^TB^T$ |

## Inverse matrix
$A^{-1}$ is the matrix with $AA^{-1} = A^{-1}A = I$. It exists only for square matrices with $\det A \neq 0$ ([[C2 Determinants]]).

**2×2 formula:**
$$\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$$
("swap the diagonal, negate the off-diagonal, divide by the determinant")

Larger matrices: Gauss–Jordan on $(A \mid I) \to (I \mid A^{-1})$ ([[C3 Linear Systems and Gaussian Elimination]]).
Rules: $(AB)^{-1} = B^{-1}A^{-1}$, $\;(A^T)^{-1} = (A^{-1})^T$, $\;(A^{-1})^{-1} = A$. There is **no division** by matrices: $AX = B \Rightarrow X = A^{-1}B$ (multiply from the left!).

## Matrix × vector = linear combination of columns
$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix} = x\begin{pmatrix}a\\c\end{pmatrix} + y\begin{pmatrix}b\\d\end{pmatrix}$$
The columns show where the basis vectors go. E.g. a rotation by $\theta$: $R_\theta = \begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}$ ([[D4 Unit Circle Trigonometry]]).

## In neuroscience #neuro
- **Connectivity matrix:** $W_{ij}$ = weight of the synapse **from neuron $j$ to neuron $i$**. The input to all neurons at once is $\mathbf u = W\mathbf r$ (each row = one neuron's weighted sum, [[A7 Sums Products and Factorials]]). Negative entries = inhibition.
- **Data matrix:** $X\in\mathbb R^{N\times T}$ (neurons × time bins). After centring, $C = \frac1T XX^T$ is the $N\times N$ **covariance matrix** (always symmetric) – input to PCA ([[C4 Eigenvalues and Eigenvectors]]).
- **General linear model (fMRI):** $\mathbf y = X\boldsymbol\beta + \boldsymbol\varepsilon$, with design matrix $X$ (scans × regressors). Least-squares estimate:
  $$\hat{\boldsymbol\beta} = (X^TX)^{-1}X^T\mathbf y$$
  Uses product, transpose and inverse in one formula.
- **Coordinate transforms:** registering a brain to MNI space uses affine transformation matrices (rotation, scaling, shear + translation).

## Connections
- Invertibility ↔ determinant → [[C2 Determinants]]
- $A\mathbf x = \mathbf b$ → [[C3 Linear Systems and Gaussian Elimination]]
- Directions that are only scaled → [[C4 Eigenvalues and Eigenvectors]]
- Vectors as $n\times1$ matrices, linear maps & rotations → [[D1 Vectors in 2D and 3D]], [[D2 Dot and Cross Product]]

## Where this is used in the vault
**Most important applications:** Connectivity matrices ([[Bio07 Neural Circuits and Systems]]), data matrices and $Wx+b$ ([[CS01 Mathematical Foundations]]), the GLM ([[CS12 Neuroimaging Data Analysis]]), affine transforms in NIfTI ([[CS05 Data Formats and Representation]]), connectomes ([[Meth06 Omics and Sequencing]]).

**All notes that build on this topic:**
- *Physics:* [[Ph10 Signal Propagation and Cable Theory]]
- *Biology:* [[Bio06 Synapses and Neurotransmitters]] · [[Bio07 Neural Circuits and Systems]]
- *Methods:* [[Meth01 Microscopy]] · [[Meth02 Structural Biology]] · [[Meth04 In Vivo Imaging]] · [[Meth06 Omics and Sequencing]]
- *Computer Science:* [[CS01 Mathematical Foundations]] · [[CS04 Optimization]] · [[CS05 Data Formats and Representation]] · [[CS07 Machine Learning Fundamentals]] · [[CS09 Probabilistic and Bayesian Models]] · [[CS12 Neuroimaging Data Analysis]] · [[CS14 Hardware Essentials]]
- *Programming:* [[Prog00 Shared Programming Concepts]] · [[Py04 Python Files and Data Formats]] · [[Py05 NumPy and Arrays]] · [[Py09 Python Machine Learning Libraries]] · [[Py10 Python Neuroscience Packages]] · [[R02 R Data Structures and Vectorization]] · [[R07 R Statistical Modelling]] · [[R08 R Mixed-Effects Models]] · [[R09 R Neuroscience Packages]] · [[MAT01 MATLAB Basics and Syntax]] · [[MAT02 MATLAB Matrices and Vectorization]] · [[MAT04 MATLAB Data Import and Files]] · [[MAT09 EEGLAB]] · [[Doc02 Math in Markdown]] · [[Doc06 LaTeX Math]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Row × column; inner dimensions must match.
- $AB\neq BA$; transpose and inverse of a product reverse the order.
- 2×2 inverse: swap, negate, divide by $\det$.
