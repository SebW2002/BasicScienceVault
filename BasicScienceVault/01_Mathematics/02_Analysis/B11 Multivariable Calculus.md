---
aliases: [Multivariable Calculus, Partial Derivatives, Gradient, Hessian, Double Integrals, Mehrdimensionale Analysis]
tags: [analysis, multivariable, derivative, integral, gradient, type/overview, neuro]
---
# B11 Multivariable Calculus

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B11 Multivariable Calculus - Worksheet|✏️ Worksheet]] · [[B11 Multivariable Calculus - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
Real quantities depend on **several** variables: a place cell's firing rate depends on $x$ and $y$; a model's loss on thousands of weights; a probability density on several random variables; the membrane potential along a dendrite on position **and** time. Multivariable calculus extends derivatives and integrals to these cases. It is the mathematical basis of gradient descent ([[CS04 Optimization]]), backpropagation ([[CS08 Deep Neural Networks]]), Jacobian stability analysis ([[CS10 Dynamical and Computational Neuro Models]]) and probability densities ([[CS02 Probability and Statistics]]).

## Functions of several variables
- $f:\mathbb R^n\to\mathbb R$, e.g. $f(x, y) = x^2 + y^2$, a bowl. Its graph is a surface; its **level sets** ($f = c$, **contour lines**) are curves, like on a map.
- **Vector-valued** functions $\mathbf f:\mathbb R^n\to\mathbb R^m$, e.g. the right-hand side of a dynamical system $\dot{\mathbf x} = \mathbf f(\mathbf x)$.

## Partial derivatives
$$\frac{\partial f}{\partial x} = \lim_{h\to0}\frac{f(x + h, y) - f(x, y)}{h}$$
Differentiate with respect to one variable and **treat all others as constants**. All rules from [[B6 Differentiation Rules]] apply.
- **Example:** $f(x, y) = x^2y + \sin y$ gives $\frac{\partial f}{\partial x} = 2xy$ and $\frac{\partial f}{\partial y} = x^2 + \cos y$.
- **Second derivatives:** $f_{xx}$, $f_{yy}$ and mixed $f_{xy} = f_{yx}$ (Schwarz's theorem, for smooth functions).

## Gradient and directional derivative
$$\nabla f = \begin{pmatrix}\partial f/\partial x_1\\\vdots\\\partial f/\partial x_n\end{pmatrix}$$
- The gradient points in the direction of **steepest ascent**. Its length is the slope in that direction.
- It is **perpendicular to the contour lines** ([[D2 Dot and Cross Product]]).
- **Directional derivative** in the direction of a unit vector $\mathbf u$: $D_\mathbf uf = \nabla f\cdot\mathbf u$. It is maximal for $\mathbf u\parallel\nabla f$ and zero along the contour.
- **Gradient descent:** $\mathbf x\leftarrow\mathbf x - \eta\nabla f$ walks downhill ([[CS04 Optimization]]).

## Jacobian and Hessian
- **Jacobian** of $\mathbf f:\mathbb R^n\to\mathbb R^m$: the $m\times n$ matrix $J_{ij} = \frac{\partial f_i}{\partial x_j}$. It is the best **linear approximation** near a point: $\mathbf f(\mathbf x + \boldsymbol\delta)\approx\mathbf f(\mathbf x) + J\boldsymbol\delta$ ([[B9 Taylor Series]]). Its eigenvalues at a fixed point decide stability ([[C4 Eigenvalues and Eigenvectors]], [[B10 Differential Equations]]).
- **Hessian** of a scalar $f$: $H_{ij} = \frac{\partial^2f}{\partial x_i\partial x_j}$ (symmetric). It describes **curvature**. Second-order Taylor: $f(\mathbf x + \boldsymbol\delta)\approx f + \nabla f^T\boldsymbol\delta + \frac12\boldsymbol\delta^TH\boldsymbol\delta$.

## Critical points and optimisation
1. Set $\nabla f = \mathbf 0$ (all partial derivatives zero) and solve ([[C3 Linear Systems and Gaussian Elimination]] if the result is linear).
2. Classify with the eigenvalues of $H$:
   - all > 0: local **minimum**
   - all < 0: local **maximum**
   - mixed signs: **saddle point**

   In 2D: $\det H > 0$ and $f_{xx} > 0$ means minimum; $\det H < 0$ means saddle ([[C2 Determinants]]).
- **Constraints:** Lagrange multipliers, $\nabla f = \mu\nabla g$ ([[CS04 Optimization]]).

**Example:** $f(x, y) = x^2 + xy + y^2 - 3x$. $\nabla f = (2x + y - 3,\ x + 2y) = 0$ gives $x = 2$, $y = -1$. $H = \begin{pmatrix}2&1\\1&2\end{pmatrix}$ has eigenvalues 3 and 1 (both > 0), so it is a minimum.

## Multivariable chain rule
For $f(x(t), y(t))$:
$$\frac{df}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} = \nabla f\cdot\dot{\mathbf x}$$
Generally, Jacobians multiply: $J_{f\circ g} = J_f\,J_g$. This is the mathematical core of **backpropagation** ([[CS08 Deep Neural Networks]]).

**Example:** along a trajectory of a system, the change of an energy function is $\dot E = \nabla E\cdot\dot{\mathbf x}$. If $\dot{\mathbf x} = -\nabla E$ (gradient flow), then $\dot E = -\lVert\nabla E\rVert^2\le0$: the energy always decreases (the idea behind Hopfield networks).

## Multiple integrals
- **Double integral** over a rectangle (Fubini): integrate one variable at a time,
  $$\iint_Rf(x, y)\,dA = \int_a^b\left(\int_c^df(x, y)\,dy\right)dx$$
- **Meaning:** the volume under the surface; the total mass, charge or probability over a region.
- **Polar coordinates:** $dA = r\,dr\,d\theta$ ([[D4 Unit Circle Trigonometry]]). For radially symmetric functions this is often much easier.
- **The Gaussian integral:** $\int_{-\infty}^\infty e^{-x^2}dx = \sqrt\pi$. It is proved by squaring and switching to polar coordinates: $\iint e^{-(x^2 + y^2)}dA = \int_0^{2\pi}\int_0^\infty e^{-r^2}r\,dr\,d\theta = \pi$. This is why the normal density has the factor $\frac{1}{\sqrt{2\pi\sigma^2}}$.
- **Probability:** for a joint density $p(x, y)$: $P((X, Y)\in R) = \iint_Rp\,dA$; marginal $p(x) = \int p(x, y)\,dy$; expectation $\mathbb E[g] = \iint g\,p\,dA$.

## In neuroscience #neuro
- **2D place fields:** $r(x, y) = r_\text{max}\exp\left(-\frac{(x - x_0)^2 + (y - y_0)^2}{2\sigma^2}\right)$. The gradient points towards the field centre; the expected spike count during a run is an integral along the path.
- **Loss landscapes** of models with thousands of parameters: gradients, saddles and curvature govern training ([[CS04 Optimization]]).
- **Stability of 2D neuron models** (FitzHugh–Nagumo, Wilson–Cowan) via Jacobians ([[CS10 Dynamical and Computational Neuro Models]]).
- **PDEs** in space and time: diffusion and cable equations use partial derivatives ([[Ph07 Diffusion and Transport]], [[Ph10 Signal Propagation and Cable Theory]]).
- **Electric fields:** $\mathbf E = -\nabla V$, the field is the negative gradient of the potential ([[Ph03 Electric Fields and Potential]]).
- **fMRI smoothing** with a 3D Gaussian kernel: a triple integral (convolution) normalised to 1.

## Connections
- 1D derivatives and integrals → [[B6 Differentiation Rules]], [[B7 Antiderivatives and Integration]]
- Linearisation → [[B9 Taylor Series]]; ODE systems → [[B10 Differential Equations]]
- Vectors, dot product → [[D1 Vectors in 2D and 3D]], [[D2 Dot and Cross Product]]
- Matrices, eigenvalues, determinants → [[C1 Matrices]], [[C4 Eigenvalues and Eigenvectors]], [[C2 Determinants]]

## Where this is used in the vault
**Most important applications:** Gradient descent and loss landscapes ([[CS04 Optimization]]), backprop ([[CS08 Deep Neural Networks]]), Jacobian stability ([[CS10 Dynamical and Computational Neuro Models]]), $\mathbf E=-\nabla V$ ([[Ph03 Electric Fields and Potential]]), joint densities ([[CS02 Probability and Statistics]]).

**All notes that build on this topic:**
- *Physics:* [[Ph03 Electric Fields and Potential]] · [[Ph07 Diffusion and Transport]] · [[Ph10 Signal Propagation and Cable Theory]]
- *Biology:* [[Bio07 Neural Circuits and Systems]]
- *Computer Science:* [[CS01 Mathematical Foundations]] · [[CS02 Probability and Statistics]] · [[CS04 Optimization]] · [[CS08 Deep Neural Networks]] · [[CS10 Dynamical and Computational Neuro Models]]
- *Programming:* [[Py08 SciPy Scientific Computing]] · [[Py09 Python Machine Learning Libraries]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Partial derivative: differentiate in one variable, treat the others as constants.
- $\nabla f$ points uphill, perpendicular to contours; the directional derivative is $\nabla f\cdot\mathbf u$.
- Jacobian = local linear map (stability); Hessian = curvature (min, max, saddle via eigenvalues).
- Chain rule: $\frac{df}{dt} = \nabla f\cdot\dot{\mathbf x}$; Jacobians multiply, which is backprop.
- Double integrals one variable at a time; polar coordinates $dA = r\,dr\,d\theta$; $\int e^{-x^2}dx = \sqrt\pi$.
