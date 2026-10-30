---
aliases: [Vectors, Vectors in 2D and 3D, Vektoren]
tags: [geometry, vector, type/overview, neuro]
---
# D1 Vectors in 2D and 3D

> [[D0 Geometry and Vectors MOC|↑ Geometry MOC]] · [[D1 Vectors in 2D and 3D - Worksheet|✏️ Worksheet]] · [[D1 Vectors in 2D and 3D - Solutions|✅ Solutions]] · [[Mistakes - Geometry and Vectors|⚠️ Mistake log]]

## Why this matters
A vector is a list of numbers with geometric meaning: a position in the brain, a direction of movement, or the activity of a whole neural population at one moment ("state vector"). Population coding, neural trajectories and brain coordinates all need vector arithmetic.

## Basics
$$\mathbf a = \begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix}\in\mathbb R^3$$
- **Position vector** $\vec{OP}$: points from the origin to point $P$.
- **Direction / connecting vector** $\vec{PQ} = \mathbf q - \mathbf p$ ("tip minus tail").

| Operation | Formula | Geometry |
|---|---|---|
| Addition | $\mathbf a + \mathbf b = (a_1 + b_1,\ a_2 + b_2,\ a_3 + b_3)$ | put arrows tip to tail |
| Scalar multiple | $c\,\mathbf a = (ca_1, ca_2, ca_3)$ | stretch / flip |
| Length (norm) | $\lVert\mathbf a\rVert = \sqrt{a_1^2 + a_2^2 + a_3^2}$ | Pythagoras ([[A2 Root Rules]]) |
| Unit vector | $\hat{\mathbf a} = \frac{\mathbf a}{\lVert\mathbf a\rVert}$ | same direction, length 1 |
| Distance | $d(P, Q) = \lVert\mathbf q - \mathbf p\rVert$ | – |
| Midpoint | $\mathbf m = \frac12(\mathbf p + \mathbf q)$ | – |

> [!warning] $\lVert\mathbf a + \mathbf b\rVert\neq\lVert\mathbf a\rVert + \lVert\mathbf b\rVert$ in general (only if they point the same way). Triangle inequality: $\lVert\mathbf a + \mathbf b\rVert\le\lVert\mathbf a\rVert + \lVert\mathbf b\rVert$.

## Linear combinations and independence
A **linear combination** of $\mathbf v_1,\dots,\mathbf v_k$ is $c_1\mathbf v_1 + \dots + c_k\mathbf v_k$.
Vectors are **linearly independent** if $c_1\mathbf v_1 + \dots + c_k\mathbf v_k = \mathbf 0$ only for $c_1 = \dots = c_k = 0$ – none of them can be built from the others.
- 2 vectors: dependent ⟺ one is a multiple of the other (collinear).
- 3 vectors in $\mathbb R^3$: independent ⟺ $\det(\mathbf v_1\ \mathbf v_2\ \mathbf v_3)\neq0$ ([[C2 Determinants]]).
- At most $n$ independent vectors in $\mathbb R^n$; $n$ independent vectors form a **basis**.

Finding coefficients of a linear combination = solving a linear system ([[C3 Linear Systems and Gaussian Elimination]]).

## Vectors and matrices
A matrix maps vectors to vectors: $\mathbf y = A\mathbf x$ – a **linear map** (preserves sums and scalar multiples). Its columns are the images of the basis vectors ([[C1 Matrices]]). Rotations, reflections, scalings and projections are all matrices.

## In neuroscience #neuro
- **Brain coordinates:** MNI/Talairach coordinates $(x, y, z)$ in mm: $x$ left→right, $y$ posterior→anterior, $z$ inferior→superior. Distances between electrodes, sources or activation peaks are vector norms.
- **Population vector** (Georgopoulos): each motor cortex neuron $i$ has a preferred direction $\mathbf c_i$ (unit vector). The movement direction is decoded as
  $$\mathbf P = \sum_i r_i\,\mathbf c_i$$
  a linear combination of preferred directions weighted by firing rates.
- **State space:** the activity of $N$ neurons at time $t$ is a vector $\mathbf r(t)\in\mathbb R^N$. Over time it traces a **neural trajectory**; similar stimuli → nearby points. Dimensionality reduction (PCA, [[C4 Eigenvalues and Eigenvectors]]) projects this onto a few axes.
- **Current dipoles** in EEG/MEG are vectors (position + orientation + strength).

## Connections
- Lengths and roots → [[A2 Root Rules]]
- Angles, projections, normals → [[D2 Dot and Cross Product]]
- Lines and planes → [[D3 Lines and Planes]]
- Vectors ↔ matrices (linear maps) → [[C1 Matrices]], independence ↔ determinant → [[C2 Determinants]]
- Polar coordinates of 2D vectors → [[D4 Unit Circle Trigonometry]]

## Where this is used in the vault
**Most important applications:** Brain coordinates (MNI) ([[Bio07 Neural Circuits and Systems]]), forces and fields as vectors ([[Ph01 Mechanics and Energy]], [[Ph03 Electric Fields and Potential]]), dipole sums ([[Ch03 Intermolecular Forces and Solubility]]), population vectors and feature spaces ([[CS01 Mathematical Foundations]]).

**All notes that build on this topic:**
- *Physics:* [[Ph01 Mechanics and Energy]] · [[Ph02 Electricity and Charge]] · [[Ph03 Electric Fields and Potential]]
- *Chemistry:* [[Ch03 Intermolecular Forces and Solubility]]
- *Biology:* [[Bio07 Neural Circuits and Systems]]
- *Methods:* [[Meth04 In Vivo Imaging]] · [[Meth06 Omics and Sequencing]]
- *Computer Science:* [[CS01 Mathematical Foundations]] · [[CS05 Data Formats and Representation]] · [[CS12 Neuroimaging Data Analysis]]
- *Programming:* [[Prog00 Shared Programming Concepts]] · [[Py02 Python Data Structures]] · [[Py10 Python Neuroscience Packages]] · [[MAT01 MATLAB Basics and Syntax]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Connecting vector = tip minus tail.
- Length via Pythagoras, unit vector = vector / length.
- Independence ⟺ no redundant vector ⟺ $\det\neq0$ (for $n$ vectors in $\mathbb R^n$).
