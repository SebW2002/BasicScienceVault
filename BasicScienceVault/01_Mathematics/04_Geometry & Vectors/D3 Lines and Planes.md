---
aliases: [Lines and Planes, Geraden und Ebenen, Hyperplane]
tags: [geometry, vector, plane, type/overview, neuro]
---
# D3 Lines and Planes

> [[D0 Geometry and Vectors MOC|↑ Geometry MOC]] · [[D3 Lines and Planes - Worksheet|✏️ Worksheet]] · [[D3 Lines and Planes - Solutions|✅ Solutions]] · [[Mistakes - Geometry and Vectors|⚠️ Mistake log]]

## Why this matters
Lines and planes are the simplest geometric objects in space: the trajectory of an electrode, an MRI slice, and – in higher dimensions – the **decision boundary** of a linear classifier that decodes stimuli from brain activity.

## Lines
**2D, explicit:** $y = mx + b$ (slope $m = \frac{\Delta y}{\Delta x}$, intercept $b$).

**Parametric form (2D or 3D):**
$$\mathbf x = \mathbf p + t\,\mathbf v,\quad t\in\mathbb R$$
$\mathbf p$ = support (position) vector of a point on the line, $\mathbf v$ = direction vector. Line through $P$ and $Q$: $\mathbf v = \mathbf q - \mathbf p$; $t\in[0, 1]$ gives the segment from $P$ to $Q$.

**Point on line?** Solve $\mathbf p + t\mathbf v = \mathbf x_0$ for $t$ – the same $t$ must work in every component.

**Two lines in 3D** can be: identical, parallel (directions are multiples), intersecting, or **skew** (neither parallel nor intersecting – only in 3D).

## Planes
| Form | Formula |
|---|---|
| Parametric | $\mathbf x = \mathbf p + s\,\mathbf u + t\,\mathbf v$ ($\mathbf u, \mathbf v$ not parallel) |
| Normal form | $\mathbf n\cdot(\mathbf x - \mathbf p) = 0$ |
| Coordinate form | $ax + by + cz = d$ with normal vector $\mathbf n = (a, b, c)$ |

**Converting parametric → coordinate form:** $\mathbf n = \mathbf u\times\mathbf v$ ([[D2 Dot and Cross Product]]), then $d = \mathbf n\cdot\mathbf p$.

## Standard problems
| Problem | Method |
|---|---|
| Line ∩ plane | insert $\mathbf p + t\mathbf v$ into $ax + by + cz = d$, solve for $t$ |
| Plane ∩ plane | solve the 2×3 linear system ([[C3 Linear Systems and Gaussian Elimination]]) → a line |
| Distance point $X_0$ → plane | $\dfrac{\lvert\mathbf n\cdot\mathbf x_0 - d\rvert}{\lVert\mathbf n\rVert}$ |
| Angle between planes | angle between their normal vectors |
| Line ∥ plane | $\mathbf v\cdot\mathbf n = 0$ |
| Line ⟂ plane | $\mathbf v$ parallel to $\mathbf n$ |

## Hyperplanes – the general idea
In $\mathbb R^n$, the set $\{\mathbf x : \mathbf w\cdot\mathbf x + b = 0\}$ is a **hyperplane** (a line in 2D, a plane in 3D). It splits space into two halves: $\mathbf w\cdot\mathbf x + b > 0$ and $< 0$. The signed distance of a point to it is $\frac{\mathbf w\cdot\mathbf x + b}{\lVert\mathbf w\rVert}$.

## In neuroscience #neuro
- **Linear decoders / classifiers** (LDA, linear SVM, logistic regression, perceptron): population activity $\mathbf r\in\mathbb R^N$ is classified as "stimulus A" if $\mathbf w\cdot\mathbf r + b > 0$. The decision boundary is a hyperplane; the distance to it is the classifier's confidence (SVMs maximise this **margin**). A threshold neuron ([[A7 Sums Products and Factorials]]) implements exactly such a hyperplane.
- **MRI slices:** axial ($z = \text{const}$), coronal ($y = \text{const}$), sagittal ($x = \text{const}$) are planes in scanner/MNI coordinates; oblique slices have general normal vectors. Intersection of two orthogonal slices is a line.
- **Electrode / DBS trajectory planning:** a straight line from the entry point on the skull to the target (e.g. subthalamic nucleus), $\mathbf x(t) = \mathbf E + t(\mathbf T - \mathbf E)$. Planning software checks the distance of this line to blood vessels and ventricles.
- **Regression:** a linear model $y = \beta_0 + \beta_1x_1 + \beta_2x_2$ is a plane fitted through a point cloud.

## Connections
- Vectors, direction vectors → [[D1 Vectors in 2D and 3D]]
- Normal via cross product, distances via dot product → [[D2 Dot and Cross Product]]
- Intersections = linear systems → [[C3 Linear Systems and Gaussian Elimination]]
- Linear functions $y = mx + b$ → [[B1 Properties of Functions]]

## Where this is used in the vault
**Most important applications:** Decision boundaries of linear classifiers ([[CS07 Machine Learning Fundamentals]]), anatomical section planes ([[Bio07 Neural Circuits and Systems]]).

**All notes that build on this topic:**
- *Biology:* [[Bio07 Neural Circuits and Systems]]
- *Computer Science:* [[CS07 Machine Learning Fundamentals]]
- *Programming:* [[Py10 Python Neuroscience Packages]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Line: point + $t\cdot$direction. Plane: point + two directions, or $\mathbf n\cdot\mathbf x = d$.
- Normal vector = cross product of the two direction vectors.
- A linear classifier's boundary is a hyperplane $\mathbf w\cdot\mathbf x + b = 0$.
