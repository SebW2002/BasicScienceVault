---
aliases: [Mathematical Foundations for CS, Tensors, SVD, PCA, Norms, Jacobian]
tags: [computer-science, linear-algebra, svd, pca, gradient, type/overview, neuro]
---
# CS01 Mathematical Foundations

> [[MOC-computer-science|↑ CS MOC]] · [[CS01 Mathematical Foundations - Worksheet|✏️ Worksheet]] · [[CS01 Mathematical Foundations - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
Every dataset in neuroscience is an array of numbers, and every model is a function of these arrays. Linear algebra and multivariate calculus are the **operating system** of data science and machine learning: data live in vectors, matrices and tensors; models apply linear maps; PCA and SVD find structure; gradients tell optimisers which way to go. This note builds on [[C1 Matrices]], [[C4 Eigenvalues and Eigenvectors]] and [[B6 Differentiation Rules]] and takes them to the multivariate, data-driven setting.

## Vectors, matrices and tensors as data containers
| Object | Shape | Neuro example |
|---|---|---|
| Scalar | () | one firing rate |
| Vector $\mathbf x\in\mathbb R^n$ | (n,) | population activity of $n$ neurons in one time bin |
| Matrix $X\in\mathbb R^{m\times n}$ | (m, n) | time bins × neurons; trials × features; voxels × time |
| **Tensor** (order 3+) | (a, b, c, …) | trials × neurons × time; x × y × z × time (fMRI); height × width × channels × frames (video) |

- **Convention matters:** most ML libraries expect **samples in rows, features in columns** ($X\in\mathbb R^{N\times d}$). Check every time; a transposed matrix silently gives wrong results.
- **Reshaping / flattening:** a tensor (trials × neurons × time) = (100 × 50 × 200) can be reshaped into a matrix of (100·200) × 50 = 20,000 × 50 to run PCA over neurons. Which axes you merge decides the question you ask.
- **Broadcasting:** operations between arrays of compatible shapes (e.g. subtracting a mean per neuron from all time bins).

## Matrix multiplication as a linear transformation: y = Wx + b
$$\mathbf y = W\mathbf x + \mathbf b,\qquad W\in\mathbb R^{m\times n},\ \mathbf x\in\mathbb R^n,\ \mathbf b,\mathbf y\in\mathbb R^m$$
- $W\mathbf x$ is a **linear** map: rotations, scalings, projections, mixing ([[C1 Matrices]]). Adding $\mathbf b$ makes it **affine** (a shift).
- Each output $y_i = \sum_j W_{ij}x_j + b_i$ is a **weighted sum** (dot product of row $i$ with $\mathbf x$, [[D2 Dot and Cross Product]]), exactly what a model neuron computes.
- **Composition:** two linear layers $W_2(W_1\mathbf x)$ = one linear layer $(W_2W_1)\mathbf x$. Without a nonlinearity, stacking layers adds no expressive power ([[CS08 Deep Neural Networks]]).
- **Cost:** multiplying $(m\times n)$ by $(n\times p)$ needs about $2mnp$ floating-point operations ([[CS14 Hardware Essentials]]).

## Eigendecomposition and singular value decomposition (SVD)
**Eigendecomposition** (square $A$ with $n$ independent eigenvectors):
$$A = Q\Lambda Q^{-1};\quad\text{for symmetric }A:\ A = Q\Lambda Q^T\ \ (Q\text{ orthogonal})$$
Only for square matrices; eigenvalues may be complex ([[C4 Eigenvalues and Eigenvectors]]).

**Singular value decomposition** (**any** $m\times n$ matrix):
$$A = U\Sigma V^T$$
- $U$ ($m\times m$, orthogonal): **left singular vectors**, an orthonormal basis of the output space.
- $\Sigma$ ($m\times n$, diagonal, $\sigma_1\ge\sigma_2\ge\dots\ge0$): **singular values**, which are the scaling factors.
- $V$ ($n\times n$, orthogonal): **right singular vectors**, an orthonormal basis of the input space.
- **Geometry:** every linear map = rotation ($V^T$) → axis-aligned stretch ($\Sigma$) → rotation ($U$).
- **Link to eigenvalues:** $A^TA = V\Sigma^2V^T$, so the singular values are the square roots of the eigenvalues of $A^TA$.
- **Rank** = number of non-zero singular values.
- **Low-rank approximation (Eckart–Young):** keeping the $k$ largest singular values gives the best rank-$k$ approximation $A_k = \sum_{i=1}^k\sigma_i\mathbf u_i\mathbf v_i^T$ in least-squares error. This is the basis of compression and denoising.

## PCA as SVD-based dimensionality reduction
**Goal:** find orthogonal directions of maximal variance.
1. **Centre** the data: subtract each feature's mean, giving $X_c$ ($N$ samples × $d$ features).
2. Compute the SVD $X_c = U\Sigma V^T$ (or equivalently the eigendecomposition of the covariance $C = \frac{1}{N-1}X_c^TX_c = V\frac{\Sigma^2}{N-1}V^T$).
3. **Principal components** (directions) = columns of $V$. **Variance** along PC $i$ is $\lambda_i = \frac{\sigma_i^2}{N-1}$.
4. **Scores** (the data in the new coordinates) = $X_cV = U\Sigma$. Keep the first $k$ columns.
5. **Explained variance ratio** $= \lambda_i/\sum_j\lambda_j$. Choose $k$ with a scree plot or a cumulative threshold (e.g. 90 %).

**Notes:**
- Standardise features first (z-score) if they have different units or scales; otherwise high-variance features dominate.
- PCA is **linear** and finds variance, not necessarily meaning. A direction with large variance can be noise or motion.
- **Neuro:** neural population activity often lies on a **low-dimensional manifold**. A few PCs capture most of the variance, and trajectories in PC space reveal dynamics (e.g. rotations during reaching, Churchland et al. 2012). PCA is also used in spike sorting (waveform features), fMRI denoising (CompCor) and scRNA-seq ([[Meth06 Omics and Sequencing]]).

## Norms and distances
| Norm | Formula | Unit ball (2D) |
|---|---|---|
| $L_1$ (Manhattan) | $\lVert\mathbf x\rVert_1 = \sum_i\lvert x_i\rvert$ | diamond |
| $L_2$ (Euclidean) | $\lVert\mathbf x\rVert_2 = \sqrt{\sum_ix_i^2}$ | circle |
| $L_\infty$ (max) | $\lVert\mathbf x\rVert_\infty = \max_i\lvert x_i\rvert$ | square |

| Distance / similarity | Formula | Use |
|---|---|---|
| Euclidean | $\lVert\mathbf x - \mathbf y\rVert_2$ | general; sensitive to scale |
| Manhattan | $\lVert\mathbf x - \mathbf y\rVert_1$ | robust to single large deviations; grid-like data |
| **Cosine similarity** | $\frac{\mathbf x\cdot\mathbf y}{\lVert\mathbf x\rVert\lVert\mathbf y\rVert}$ | pattern similarity independent of overall magnitude (population vectors, embeddings) |
| Correlation distance | $1 - r(\mathbf x,\mathbf y)$ | cosine of **mean-centred** vectors; RSA ([[CS12 Neuroimaging Data Analysis]]) |
| Mahalanobis | $\sqrt{(\mathbf x - \mathbf y)^TC^{-1}(\mathbf x - \mathbf y)}$ | accounts for correlations and noise covariance (crossnobis in RSA) |

**Curse of dimensionality:** in high dimensions, random points become almost equidistant and nearly orthogonal. Distances lose contrast, which is why dimensionality reduction and regularisation matter.

## Gradients, Jacobians and the multivariate chain rule
- **Partial derivative** $\frac{\partial f}{\partial x_i}$: change one input, hold the others fixed.
- **Gradient** of a scalar function $f:\mathbb R^n\to\mathbb R$: $\nabla f = \left(\frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n}\right)^T$. It points in the direction of **steepest ascent**, and its length is the slope in that direction. Gradient descent steps along $-\nabla f$ ([[CS04 Optimization]]).
- **Jacobian** of a vector function $\mathbf f:\mathbb R^n\to\mathbb R^m$: the $m\times n$ matrix $J_{ij} = \frac{\partial f_i}{\partial x_j}$, the best linear approximation of $\mathbf f$ near a point ([[B9 Taylor Series]]).
- **Hessian** $H_{ij} = \frac{\partial^2f}{\partial x_i\partial x_j}$: curvature, symmetric. Its eigenvalues tell minima (all > 0), maxima (all < 0) and saddles (mixed signs).
- **Multivariate chain rule:** for $\mathbf z = \mathbf g(\mathbf x)$ and $L = f(\mathbf z)$,
  $$\frac{\partial L}{\partial x_j} = \sum_i\frac{\partial L}{\partial z_i}\frac{\partial z_i}{\partial x_j}\qquad\Longleftrightarrow\qquad\nabla_\mathbf xL = J_\mathbf g^T\,\nabla_\mathbf zL$$
  Jacobians of compositions multiply: $J_{f\circ g} = J_f\cdot J_g$. **Backpropagation** is exactly this, applied layer by layer from the output backwards ([[CS08 Deep Neural Networks]]).
- **Useful gradients:**
  - $\nabla_\mathbf w(\mathbf w^T\mathbf x) = \mathbf x$
  - $\nabla_\mathbf w\lVert\mathbf w\rVert^2 = 2\mathbf w$
  - $\nabla_\mathbf w\lVert X\mathbf w - \mathbf y\rVert^2 = 2X^T(X\mathbf w - \mathbf y)$. Setting this to 0 gives the normal equations $X^TX\mathbf w = X^T\mathbf y$ ([[C3 Linear Systems and Gaussian Elimination]]).

## In neuroscience #neuro
- **Population analysis:** PCA/SVD on trial-averaged activity → neural trajectories and low-dimensional dynamics.
- **Encoding and decoding models** are linear maps (receptive fields $\mathbf k^T\mathbf x$, linear decoders $\mathbf w^T\mathbf r$).
- **Jacobians of dynamical systems** decide the stability of fixed points ([[CS10 Dynamical and Computational Neuro Models]]).
- **Connectivity matrices** and their SVD reveal dominant input–output modes of circuits.

## Math links #math-link
- Partial derivatives, gradients, Jacobians, multiple integrals → [[B11 Multivariable Calculus]]
- Matrices, transpose, inverse → [[C1 Matrices]]
- Eigenvalues, symmetric matrices, PCA → [[C4 Eigenvalues and Eigenvectors]]
- Vectors, norms, dot product, cosine → [[D1 Vectors in 2D and 3D]], [[D2 Dot and Cross Product]]
- Derivatives and chain rule (1D) → [[B6 Differentiation Rules]]
- Linearisation → [[B9 Taylor Series]]
- Linear systems, normal equations → [[C3 Linear Systems and Gaussian Elimination]]

## Connections
- In code → [[Py05 NumPy and Arrays]] (`linalg.svd`, PCA), [[MAT02 MATLAB Matrices and Vectorization]], [[R02 R Data Structures and Vectorization]]
- Optimisation with gradients → [[CS04 Optimization]]
- Backpropagation → [[CS08 Deep Neural Networks]]
- PCA for population activity → [[CS11 Time Series and Signal Processing]]
- Covariance → [[CS02 Probability and Statistics]]

## Key takeaways
- Data are tensors; know your axes (samples × features).
- $\mathbf y = W\mathbf x + \mathbf b$: every output is a weighted sum. Stacked linear maps stay linear.
- SVD $A = U\Sigma V^T$ works for any matrix: rotate, stretch, rotate. Truncating it gives the best low-rank approximation.
- PCA = SVD of centred data. PCs are the columns of $V$; variances are $\sigma_i^2/(N-1)$.
- Gradient = direction of steepest ascent; Jacobian = local linear map; chain rule = multiplying Jacobians, which is backprop.
