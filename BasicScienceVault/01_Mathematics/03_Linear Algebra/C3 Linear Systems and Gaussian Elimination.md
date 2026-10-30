---
aliases: [Linear Systems, Gaussian Elimination, Lineare Gleichungssysteme, Gauss]
tags: [linear-algebra, linear-system, matrix, type/overview, neuro]
---
# C3 Linear Systems and Gaussian Elimination

> [[C0 Linear Algebra MOC|↑ Linear Algebra MOC]] · [[C3 Linear Systems and Gaussian Elimination - Worksheet|✏️ Worksheet]] · [[C3 Linear Systems and Gaussian Elimination - Solutions|✅ Solutions]] · [[Mistakes - Linear Algebra|⚠️ Mistake log]]

## Why this matters
Many unknowns, many linear equations: fitting a GLM, finding the steady state of a linear network, solving circuit equations of a multi-compartment neuron. Gaussian elimination is the systematic algorithm that always works – and it is what software does under the hood.

## Matrix form
$$\begin{aligned} a_{11}x_1 + a_{12}x_2 + a_{13}x_3 &= b_1\\ a_{21}x_1 + a_{22}x_2 + a_{23}x_3 &= b_2\\ a_{31}x_1 + a_{32}x_2 + a_{33}x_3 &= b_3\end{aligned} \quad\iff\quad A\mathbf x = \mathbf b \quad\iff\quad \left(\begin{array}{ccc|c} a_{11}&a_{12}&a_{13}&b_1\\ a_{21}&a_{22}&a_{23}&b_2\\ a_{31}&a_{32}&a_{33}&b_3\end{array}\right)$$

## Gaussian elimination
**Allowed row operations** (they don't change the solution set):
1. Swap two rows.
2. Multiply a row by a number $\neq 0$.
3. Add a multiple of one row to another row.

**Algorithm**
1. Write the augmented matrix $(A\mid\mathbf b)$.
2. Use row 1 to create zeros below the first entry in column 1, then row 2 for column 2, … → **row echelon form** (staircase, zeros below the diagonal).
3. **Back substitution:** solve the last equation, insert upwards.
(Gauss–Jordan: also clear entries above the pivots → read off the solution directly.)

**Example**
$$\left(\begin{array}{ccc|c}1&1&1&6\\2&-1&1&3\\1&2&-1&2\end{array}\right)\xrightarrow[R_3 - R_1]{R_2 - 2R_1}\left(\begin{array}{ccc|c}1&1&1&6\\0&-3&-1&-9\\0&1&-2&-4\end{array}\right)\xrightarrow{3R_3 + R_2}\left(\begin{array}{ccc|c}1&1&1&6\\0&-3&-1&-9\\0&0&-7&-21\end{array}\right)$$
Back substitution: $z = 3$; $-3y - 3 = -9\Rightarrow y = 2$; $x + 2 + 3 = 6\Rightarrow x = 1$.

## Types of solutions
| Echelon form shows … | Solutions | Rank condition |
|---|---|---|
| a pivot in every column | **exactly one** | $\operatorname{rank}A = \operatorname{rank}(A\mid\mathbf b) = n$ |
| a row $(0\ 0\ 0 \mid c)$ with $c\neq0$ | **none** (contradiction $0 = c$) | $\operatorname{rank}A < \operatorname{rank}(A\mid\mathbf b)$ |
| a zero row $(0\ 0\ 0\mid0)$, fewer pivots than unknowns | **infinitely many** (free parameters) | $\operatorname{rank}A = \operatorname{rank}(A\mid\mathbf b) < n$ |

**Rank** = number of non-zero rows in echelon form = number of linearly independent rows.
For square $A$: unique solution $\iff\det A\neq0$ ([[C2 Determinants]]) $\iff A^{-1}$ exists, and then $\mathbf x = A^{-1}\mathbf b$ ([[C1 Matrices]]).

With infinitely many solutions, set a free variable $= t$ and express the others in terms of $t$ → solution is a line (or plane) ([[D3 Lines and Planes]]).

## In neuroscience #neuro
- **Steady state of a linear rate network:** $\tau\frac{d\mathbf r}{dt} = -\mathbf r + W\mathbf r + \mathbf h$. At steady state: $(I - W)\mathbf r = \mathbf h$ – a linear system. If $I - W$ is singular, there's no unique steady state (e.g. line attractors for working memory or eye-position integration!).
- **GLM normal equations:** least squares $\min\lVert\mathbf y - X\boldsymbol\beta\rVert^2$ leads to $X^TX\boldsymbol\beta = X^T\mathbf y$ – a linear system with as many equations as regressors.
- **Compartmental models / Kirchhoff's laws:** currents into each node sum to zero → one linear equation per compartment.
- **Source mixing:** EEG electrodes record linear mixtures of sources, $\mathbf x = A\mathbf s$. Unmixing (ICA, beamforming, source localisation) means solving or approximately inverting such systems – usually with more unknowns than equations, hence infinitely many solutions and the need for constraints.

## Connections
- Matrix form, inverse → [[C1 Matrices]]
- Unique solution $\iff\det\neq0$ → [[C2 Determinants]]
- Eigenvectors are solutions of $(A - \lambda I)\mathbf v = \mathbf 0$ → [[C4 Eigenvalues and Eigenvectors]]
- Intersections of lines and planes → [[D3 Lines and Planes]]
- Single equations → [[A8 Solving Equations]]

## Where this is used in the vault
**Most important applications:** Normal equations of least squares ([[CS07 Machine Learning Fundamentals]]), Kirchhoff networks ([[Ph04 Circuits and Resistance]]), EEG/MEG inverse problem ([[CS12 Neuroimaging Data Analysis]], [[Meth03 Electrophysiology]]), compartment models ([[Ph10 Signal Propagation and Cable Theory]]).

**All notes that build on this topic:**
- *Physics:* [[Ph04 Circuits and Resistance]] · [[Ph06 Magnetism and Induction]] · [[Ph10 Signal Propagation and Cable Theory]]
- *Methods:* [[Meth03 Electrophysiology]] · [[Meth04 In Vivo Imaging]]
- *Computer Science:* [[CS01 Mathematical Foundations]] · [[CS07 Machine Learning Fundamentals]] · [[CS10 Dynamical and Computational Neuro Models]] · [[CS12 Neuroimaging Data Analysis]]
- *Programming:* [[Py05 NumPy and Arrays]] · [[R02 R Data Structures and Vectorization]] · [[R06 ggplot2 Visualization]] · [[R07 R Statistical Modelling]] · [[MAT02 MATLAB Matrices and Vectorization]] · [[MAT07 MATLAB Statistics Toolbox]] · [[MAT09 EEGLAB]] · [[MAT10 MATLAB Neuroscience Toolboxes]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Three allowed row operations; aim for a staircase.
- Contradiction row → no solution; zero row + free variable → infinitely many.
- Always substitute your solution back into the **original** equations.
