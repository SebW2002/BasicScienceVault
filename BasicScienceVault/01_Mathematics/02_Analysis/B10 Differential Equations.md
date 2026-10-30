---
aliases: [Differential Equations, ODEs, Differentialgleichungen]
tags: [analysis, differential-equation, derivative, type/overview, neuro]
---
# B10 Differential Equations

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B10 Differential Equations - Worksheet|✏️ Worksheet]] · [[B10 Differential Equations - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
Almost every model in neuroscience is a **differential equation**: the membrane equation, Hodgkin–Huxley, channel gating, synaptic currents, firing-rate networks, drug clearance, diffusion and cable theory. A differential equation says how a quantity **changes** depending on its current state. Solving it tells you how the quantity evolves over time. This note collects the techniques you need. It builds on [[B6 Differentiation Rules]], [[B7 Antiderivatives and Integration]] and [[B2 Exponential Functions]].

## What is a differential equation?
An equation that relates an unknown **function** to its **derivatives**.
- **Ordinary** (ODE): one independent variable, usually time: $\frac{dx}{dt} = f(x, t)$.
- **Partial** (PDE): several independent variables, e.g. time and space: $\frac{\partial c}{\partial t} = D\frac{\partial^2c}{\partial x^2}$.
- **Order** = highest derivative. **Linear** = the unknown and its derivatives appear only to the first power and are not multiplied together.
- A solution is a **function**, not a number. To pin it down you need an **initial condition** (e.g. $x(0) = x_0$).
- **Checking a solution** is always possible: insert it and see whether both sides agree.

## The most important ODE: first-order linear with constant coefficients
$$\tau\frac{dx}{dt} = -(x - x_\infty)\qquad\Longrightarrow\qquad x(t) = x_\infty + (x_0 - x_\infty)\,e^{-t/\tau}$$
- $x_\infty$ is the **steady state** (where $dx/dt = 0$); τ is the **time constant**.
- The rate of change is proportional to the distance from the steady state, so the approach is exponential (63 % after τ).
- **Special cases:**
  - pure decay $\frac{dx}{dt} = -kx\Rightarrow x = x_0e^{-kt}$ ($k = 1/\tau$)
  - pure growth $\frac{dx}{dt} = kx\Rightarrow x = x_0e^{kt}$

**Recipe for $\frac{dx}{dt} = a - bx$:**
1. Steady state: $x_\infty = a/b$.
2. Time constant: $\tau = 1/b$.
3. Write down the solution above.

## Separation of variables
For $\frac{dx}{dt} = g(t)\,h(x)$: move all $x$ to one side and all $t$ to the other, then integrate both sides.
$$\int\frac{dx}{h(x)} = \int g(t)\,dt$$
**Example:** $\frac{dx}{dt} = -kx$ gives $\int\frac{dx}{x} = -\int k\,dt$, so $\ln\lvert x\rvert = -kt + C$ and $x = x_0e^{-kt}$ ([[A3 Logarithms]]).

**Example (logistic growth):** $\frac{dN}{dt} = rN\left(1 - \frac NK\right)$ gives an S-shaped curve: exponential growth at first, then saturation at the carrying capacity $K$.

## Linear ODEs with input (driven systems)
$$\tau\frac{dx}{dt} = -x + u(t)$$
- **Constant input** $u$: steady state $x_\infty = u$ (the recipe above).
- **General input:** the solution is the input **convolved** with the exponential kernel,
  $$x(t) = x_0e^{-t/\tau} + \frac1\tau\int_0^te^{-(t-s)/\tau}u(s)\,ds$$
  The system "remembers" past input with exponentially fading weight. This is a **low-pass filter** ([[CS11 Time Series and Signal Processing]]).
- **Solution method (integrating factor):** multiply by $e^{t/\tau}$; the left side becomes the derivative of $x\,e^{t/\tau}$; integrate.

## Stability and equilibria (for non-linear ODEs)
For $\frac{dx}{dt} = f(x)$ we often can't solve explicitly, but we can find out a lot qualitatively:
1. **Fixed points:** solve $f(x^*) = 0$ ([[A8 Solving Equations]]).
2. **Stability:** $f'(x^*) < 0$ means stable (perturbations decay); $f'(x^*) > 0$ means unstable. This is the linearisation $\frac{d(\delta x)}{dt}\approx f'(x^*)\delta x$ from [[B9 Taylor Series]].
3. **Phase line:** draw the $x$ axis with arrows showing where $f > 0$ (x increases) and $f < 0$ (x decreases). The arrows point towards stable fixed points.

**Example:** $\frac{dx}{dt} = x(1 - x)$ has fixed points 0 (unstable, $f'(0) = 1$) and 1 (stable, $f'(1) = -1$).

## Systems of linear ODEs
$$\frac{d\mathbf x}{dt} = A\mathbf x$$
- If $\mathbf v$ is an eigenvector of $A$ with eigenvalue λ, then $\mathbf x(t) = e^{\lambda t}\mathbf v$ is a solution. The general solution is a combination $\sum_ic_ie^{\lambda_it}\mathbf v_i$ ([[C4 Eigenvalues and Eigenvectors]]).

| Eigenvalues | Behaviour |
|---|---|
| all real, negative | stable node: decay without oscillation |
| real, mixed signs | saddle: unstable |
| complex $a\pm bi$, $a < 0$ | stable spiral: **damped oscillation** with angular frequency $b$ |
| complex, $a > 0$ | unstable spiral: growing oscillation |
| purely imaginary | centre: undamped oscillation |

- For a non-linear system $\dot{\mathbf x} = \mathbf f(\mathbf x)$, use the **Jacobian** at the fixed point ([[B11 Multivariable Calculus]]).
- **Second-order equations** can be written as first-order systems. The **harmonic oscillator** $\ddot x = -\omega^2x$ becomes $\dot x = v$, $\dot v = -\omega^2x$, with eigenvalues $\pm i\omega$ and solutions $\sin$ and $\cos$ ([[B4 Trigonometric Functions]], [[E2 Complex Numbers]]).

## Numerical solution: Euler's method
$$x(t + \Delta t)\approx x(t) + \Delta t\cdot f(x(t))$$
- It is the first-order Taylor step ([[B9 Taylor Series]]). It is simple, but needs small $\Delta t$; too large steps become inaccurate or unstable (for $\dot x = -x/\tau$, you need $\Delta t < 2\tau$ for stability, and much smaller for accuracy).
- Better methods: Runge–Kutta (RK4), adaptive step size, exponential Euler (exact for linear parts). Simulators (NEURON, Brian2, NEST) handle this for you.

## A glimpse at PDEs
- **Diffusion equation** $\frac{\partial c}{\partial t} = D\frac{\partial^2c}{\partial x^2}$: concentration spreads, and peaks flatten into Gaussians ([[Ph07 Diffusion and Transport]]).
- **Cable equation** $\lambda^2\frac{\partial^2V}{\partial x^2} = \tau\frac{\partial V}{\partial t} + V$: voltage spreads and leaks along dendrites ([[Ph10 Signal Propagation and Cable Theory]]).
- **Steady states** of PDEs ($\partial/\partial t = 0$) are ODEs in space, e.g. $\lambda^2V'' = V$ gives $V = V_0e^{-x/\lambda}$.

## In neuroscience #neuro
- **Membrane equation:** $\tau_m\frac{dV}{dt} = -(V - E_L) + R_mI$, the recipe above with $V_\infty = E_L + R_mI$ ([[Ph05 Capacitance and RC Circuits]]).
- **Channel gating:** $\frac{dn}{dt} = \alpha(1 - n) - \beta n$, which is first-order linear at fixed voltage, with $n_\infty = \frac{\alpha}{\alpha + \beta}$ and $\tau_n = \frac{1}{\alpha + \beta}$ (Hodgkin–Huxley; [[Bio05 Neurons and Action Potentials]]).
- **Synaptic currents** after a spike decay as $e^{-t/\tau_\text{syn}}$; two time constants give the difference of exponentials ([[B8 Curve Sketching]]).
- **Pharmacokinetics:** drug concentration after a bolus, $\dot c = -kc$; with constant infusion, it approaches a plateau.
- **Rate models and E–I networks:** $\tau\dot{\mathbf r} = -\mathbf r + W\mathbf r + \mathbf h$, whose stability is decided by eigenvalues ([[CS10 Dynamical and Computational Neuro Models]]).
- **Gene expression:** mRNA production and degradation, $\dot m = k - \gamma m$ ([[Bio04 Nucleic Acids and Gene Expression]]).

## Connections
- Derivatives and integrals → [[B6 Differentiation Rules]], [[B7 Antiderivatives and Integration]]
- Exponential solutions → [[B2 Exponential Functions]]
- Linearisation → [[B9 Taylor Series]]; eigenvalues → [[C4 Eigenvalues and Eigenvectors]]
- Multivariable systems → [[B11 Multivariable Calculus]]
- Oscillations → [[B12 Fourier Analysis]], [[E2 Complex Numbers]]

## Where this is used in the vault
**Most important applications:** Membrane equation and LIF ([[Ph05 Capacitance and RC Circuits]]), Hodgkin–Huxley and gating ([[Bio05 Neurons and Action Potentials]]), diffusion and cable PDEs ([[Ph07 Diffusion and Transport]], [[Ph10 Signal Propagation and Cable Theory]]), rate networks and attractors ([[CS10 Dynamical and Computational Neuro Models]]).

**All notes that build on this topic:**
- *Physics:* [[Ph05 Capacitance and RC Circuits]] · [[Ph07 Diffusion and Transport]] · [[Ph10 Signal Propagation and Cable Theory]]
- *Chemistry:* [[Ch05 Redox and Electrochemistry]]
- *Biology:* [[Bio04 Nucleic Acids and Gene Expression]] · [[Bio05 Neurons and Action Potentials]] · [[Bio06 Synapses and Neurotransmitters]]
- *Computer Science:* [[CS09 Probabilistic and Bayesian Models]] · [[CS10 Dynamical and Computational Neuro Models]]
- *Programming:* [[Prog00 Shared Programming Concepts]] · [[Py03 Python Control Flow and Functions]] · [[Py08 SciPy Scientific Computing]] · [[Py10 Python Neuroscience Packages]] · [[Py12 Python Object-Oriented Programming]] · [[Py13 Python Reproducible Projects and Testing]] · [[MAT03 MATLAB Control Flow and Functions]] · [[MAT11 MATLAB Live Scripts and Reports]] · [[MAT12 MATLAB Reproducible Projects]] · [[Doc06 LaTeX Math]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- $\tau\dot x = -(x - x_\infty)$ gives $x = x_\infty + (x_0 - x_\infty)e^{-t/\tau}$: the most-used formula in neuroscience.
- Separation of variables: $\int dx/h(x) = \int g(t)\,dt$.
- Non-linear 1D: fixed points where $f = 0$, stable if $f' < 0$.
- Linear systems: solutions $e^{\lambda t}\mathbf v$; eigenvalues decide decay, growth or oscillation.
- Euler: $x\leftarrow x + \Delta t\,f(x)$; keep $\Delta t\ll\tau$.
