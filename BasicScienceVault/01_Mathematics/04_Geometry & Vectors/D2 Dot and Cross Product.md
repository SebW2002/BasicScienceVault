---
aliases: [Dot Product, Cross Product, Scalar Product, Skalarprodukt, Kreuzprodukt]
tags: [geometry, vector, dot-product, cross-product, type/overview, neuro]
---
# D2 Dot and Cross Product

> [[D0 Geometry and Vectors MOC|↑ Geometry MOC]] · [[D2 Dot and Cross Product - Worksheet|✏️ Worksheet]] · [[D2 Dot and Cross Product - Solutions|✅ Solutions]] · [[Mistakes - Geometry and Vectors|⚠️ Mistake log]]

## Why this matters
The **dot product** measures how much two vectors point in the same direction – it is the weighted sum that every model neuron computes, and the basis of similarity measures between neural patterns. The **cross product** produces a vector perpendicular to two others – surface normals of the cortex and the magnetic fields measured by MEG.

## Dot product (scalar product)
$$\mathbf a\cdot\mathbf b = a_1b_1 + a_2b_2 + a_3b_3 = \sum_i a_ib_i = \lVert\mathbf a\rVert\,\lVert\mathbf b\rVert\cos\theta$$
The result is a **number** (scalar).

| Fact | Formula |
|---|---|
| Angle | $\cos\theta = \dfrac{\mathbf a\cdot\mathbf b}{\lVert\mathbf a\rVert\lVert\mathbf b\rVert}$ |
| Orthogonal | $\mathbf a\perp\mathbf b\iff\mathbf a\cdot\mathbf b = 0$ |
| Sign | $> 0$: angle < 90°; $< 0$: angle > 90° |
| Length | $\mathbf a\cdot\mathbf a = \lVert\mathbf a\rVert^2$ |
| Projection of $\mathbf a$ onto $\mathbf b$ | $\operatorname{proj}_{\mathbf b}\mathbf a = \dfrac{\mathbf a\cdot\mathbf b}{\mathbf b\cdot\mathbf b}\,\mathbf b$ |
| Rules | commutative, distributive, $(c\mathbf a)\cdot\mathbf b = c(\mathbf a\cdot\mathbf b)$ |
| Matrix form | $\mathbf a\cdot\mathbf b = \mathbf a^T\mathbf b$ ([[C1 Matrices]]) |

Works in any dimension $\mathbb R^n$.

## Cross product (only in $\mathbb R^3$)
$$\mathbf a\times\mathbf b = \begin{pmatrix}a_2b_3 - a_3b_2\\ a_3b_1 - a_1b_3\\ a_1b_2 - a_2b_1\end{pmatrix}$$
Memory aid: for component 1 cover row 1 and compute the 2×2 "determinant" of the rest; component 2 has a minus sign (or use the cyclic order 2-3, 3-1, 1-2).

| Fact | Formula |
|---|---|
| Direction | perpendicular to both $\mathbf a$ and $\mathbf b$; right-hand rule |
| Length | $\lVert\mathbf a\times\mathbf b\rVert = \lVert\mathbf a\rVert\lVert\mathbf b\rVert\sin\theta$ = area of the parallelogram |
| Triangle area | $\tfrac12\lVert\vec{AB}\times\vec{AC}\rVert$ |
| Parallel vectors | $\mathbf a\times\mathbf b = \mathbf 0$ |
| **Anticommutative** | $\mathbf b\times\mathbf a = -\,\mathbf a\times\mathbf b$ |
| Triple product | $\mathbf a\cdot(\mathbf b\times\mathbf c) = \det(\mathbf a\ \mathbf b\ \mathbf c)$ = signed volume ([[C2 Determinants]]) |

Standard basis: $\mathbf e_x\times\mathbf e_y = \mathbf e_z$, $\;\mathbf e_y\times\mathbf e_z = \mathbf e_x$, $\;\mathbf e_z\times\mathbf e_x = \mathbf e_y$.

## In neuroscience #neuro
- **Neuron as dot product:** a linear neuron's input is $u = \mathbf w\cdot\mathbf x$ (weights · inputs, [[A7 Sums Products and Factorials]]). It responds most strongly when the input pattern points in the same direction as the weight vector – the neuron is a **template matcher**. The same holds for receptive fields: response ≈ receptive field · stimulus.
- **Cosine similarity / RSA:** the similarity of two population responses is often measured as $\cos\theta = \frac{\mathbf r_A\cdot\mathbf r_B}{\lVert\mathbf r_A\rVert\lVert\mathbf r_B\rVert}$ (independent of overall firing level). Correlation = cosine similarity of mean-centred vectors.
- **Projection onto an axis:** PCA scores, "coding directions" and decoder outputs are projections of population activity onto a direction vector.
- **MEG and the cross product:** the magnetic field of a current dipole $\mathbf Q$ at position $\mathbf r_0$ involves $\mathbf Q\times(\mathbf r - \mathbf r_0)$ (Biot–Savart). In a spherical head model, **radially oriented dipoles produce no external magnetic field** – MEG is mostly blind to activity on gyral crowns and sees mainly tangential sources in sulci, whereas EEG sees both.
- **Cortical surface normals:** meshes from FreeSurfer consist of triangles; the normal of each triangle ($\vec{AB}\times\vec{AC}$) gives the orientation of the cortical columns and thus the dipole orientation for source modelling.

## Connections
- Dot product = weighted sum → [[A7 Sums Products and Factorials]], matrix product rows → [[C1 Matrices]]
- Angles, $\cos$ → [[D4 Unit Circle Trigonometry]]
- Normal vectors of planes → [[D3 Lines and Planes]]
- Volume & triple product → [[C2 Determinants]]
- Orthogonal eigenvectors → [[C4 Eigenvalues and Eigenvectors]]

## Where this is used in the vault
**Most important applications:** Weighted sums and attention ([[CS08 Deep Neural Networks]]), cosine similarity and RSA ([[CS01 Mathematical Foundations]], [[CS12 Neuroimaging Data Analysis]]), Lorentz force and MEG ([[Ph06 Magnetism and Induction]]), work $\vec F\cdot\vec s$ ([[Ph01 Mechanics and Energy]]).

**All notes that build on this topic:**
- *Physics:* [[Ph01 Mechanics and Energy]] · [[Ph06 Magnetism and Induction]]
- *Chemistry:* [[Ch02 Chemical Bonds]] · [[Ch07 Organic Chemistry Essentials]]
- *Methods:* [[Meth03 Electrophysiology]] · [[Meth06 Omics and Sequencing]]
- *Computer Science:* [[CS01 Mathematical Foundations]] · [[CS08 Deep Neural Networks]] · [[CS12 Neuroimaging Data Analysis]]
- *Programming:* [[Py05 NumPy and Arrays]] · [[MAT02 MATLAB Matrices and Vectorization]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Dot product → number; $0$ ⟺ orthogonal; gives angles and projections.
- Cross product → vector ⊥ both; only 3D; length = area; order matters.
