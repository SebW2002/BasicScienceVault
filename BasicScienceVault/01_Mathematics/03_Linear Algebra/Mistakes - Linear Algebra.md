---
aliases: [Mistake Log Linear Algebra, Fehler Lineare Algebra]
tags: [linear-algebra, type/mistakes]
---
# ⚠️ Mistakes – Linear Algebra

> [[C0 Linear Algebra MOC|↑ Linear Algebra MOC]] · [[00 Roadmap|Roadmap]] · Template: [[Mistake Entry Template]]

## Classic traps (pre-filled)
| ❌ Wrong | ✅ Right | Quick check | Topic |
|---|---|---|---|
| $AB = BA$ | generally not | try two 2×2 matrices | [[C1 Matrices]] |
| $(AB)^T = A^TB^T$ | $B^TA^T$ | dimensions often don't even fit | [[C1 Matrices]] |
| $(AB)^{-1} = A^{-1}B^{-1}$ | $B^{-1}A^{-1}$ | "socks and shoes" | [[C1 Matrices]] |
| $X = \frac BA$ | $X = A^{-1}B$ (or $BA^{-1}$ for $XA = B$) | no matrix division | [[C1 Matrices]] |
| multiplied entrywise | row × column | – | [[C1 Matrices]] |
| 2×2 inverse: forgot to swap $a, d$ | $\frac1{\det}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ | check $AA^{-1} = I$ | [[C1 Matrices]] |
| $W_{ij}$ = from $i$ to $j$ | usually **to $i$ from $j$** | check the paper's convention | [[C1 Matrices]] |
| $\det(cA) = c\det A$ | $c^n\det A$ | $\det(2I_2) = 4$ | [[C2 Determinants]] |
| $\det(A + B) = \det A + \det B$ | no rule | $A = B = I$ | [[C2 Determinants]] |
| Sarrus for 4×4 | only 3×3 | – | [[C2 Determinants]] |
| Laplace: forgot checkerboard signs | $+ - +$ | – | [[C2 Determinants]] |
| row swap without sign change | swap flips sign | – | [[C2 Determinants]] |
| Gauss: sign error in row operation | write the operation next to the row | substitute solution back | [[C3 Linear Systems and Gaussian Elimination]] |
| zero row ⇒ "no solution" | zero row $(0\mid0)$ ⇒ free parameter; $(0\mid c\neq0)$ ⇒ no solution | – | [[C3 Linear Systems and Gaussian Elimination]] |
| eigenvector $\mathbf 0$ | eigenvectors are non-zero | – | [[C4 Eigenvalues and Eigenvectors]] |
| "my eigenvector differs from the solution" | any non-zero multiple is fine | check $A\mathbf v = \lambda\mathbf v$ | [[C4 Eigenvalues and Eigenvectors]] |
| $\det(A - \lambda)$ | $\det(A - \lambda I)$ – subtract only on the diagonal | – | [[C4 Eigenvalues and Eigenvectors]] |
| stable if $\lambda < 1$ (continuous) | continuous: $\operatorname{Re}\lambda < 0$; discrete: $\lvert\lambda\rvert < 1$ | – | [[C4 Eigenvalues and Eigenvectors]] |

## My mistakes
| Date | ❌ What I did | ✅ Correct | Why / quick check | Link |
|---|---|---|---|---|
| | | | | |

## Patterns I notice
- 
