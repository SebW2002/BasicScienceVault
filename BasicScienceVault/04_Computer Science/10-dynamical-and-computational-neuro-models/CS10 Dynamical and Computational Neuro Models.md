---
aliases: [Dynamical and Computational Neuro Models, Computational Neuroscience, Attractor Networks, Firing Rate Models, Temporal Difference Learning, Reward Prediction Error]
tags: [computer-science, computational-neuroscience, dynamical-systems, reinforcement-learning, type/overview, neuro]
---
# CS10 Dynamical and Computational Neuroscience Models

> [[MOC-computer-science|↑ CS MOC]] · [[CS10 Dynamical and Computational Neuro Models - Worksheet|✏️ Worksheet]] · [[CS10 Dynamical and Computational Neuro Models - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
Computational neuroscience asks **how** neurons and circuits compute, using mathematical models whose behaviour can be simulated and analysed. Models range from single neurons (integrate-and-fire, Hodgkin–Huxley) through populations (firing-rate and attractor networks) to learning algorithms (reinforcement learning). They connect the physics of [[Ph05 Capacitance and RC Circuits]] and [[Ph10 Signal Propagation and Cable Theory]] with the machine learning of [[CS08 Deep Neural Networks]].

## Dynamical systems toolkit
A model is a set of differential equations $\frac{d\mathbf x}{dt} = \mathbf f(\mathbf x)$.
- **Fixed points:** $\mathbf f(\mathbf x^*) = 0$, where nothing changes.
- **Stability (1D):** a fixed point is stable if $f'(x^*) < 0$ (perturbations decay) and unstable if $f'(x^*) > 0$.
- **Stability (nD):** look at the eigenvalues of the **Jacobian** at $\mathbf x^*$ ([[C4 Eigenvalues and Eigenvectors]], [[CS01 Mathematical Foundations]]). All real parts < 0 means stable; complex eigenvalues mean spiralling (oscillations).
- **Phase plane** (2D): plot **nullclines** ($\dot x = 0$, $\dot y = 0$). Fixed points sit at their intersections. Arrows show the flow.
- **Limit cycle:** a closed trajectory, i.e. sustained oscillation (repetitive spiking, rhythms).
- **Bifurcation:** a qualitative change as a parameter varies, e.g. from rest to repetitive firing when the input current crosses rheobase (saddle-node or Hopf bifurcation, which explain type I vs. type II excitability).
- **Numerical simulation:** Euler $\mathbf x_{t+\Delta t} = \mathbf x_t + \Delta t\,\mathbf f(\mathbf x_t)$ ([[B9 Taylor Series]]); better methods are Runge–Kutta or exponential integrators.

## Leaky integrate-and-fire (LIF) neuron
$$\tau_m\frac{dV}{dt} = -(V - E_L) + R_mI(t);\qquad\text{if }V\ge V_\theta:\ \text{spike},\ V\to V_\text{reset}$$
- The RC membrane plus a threshold ([[Ph05 Capacitance and RC Circuits]]).
- With constant input, $V_\infty = E_L + RI$. The interspike interval is $T = \tau\ln\frac{V_\infty - V_\text{reset}}{V_\infty - V_\theta}$ (if $V_\infty > V_\theta$), and the **f–I curve** is $f = \frac{1}{t_\text{ref} + T}$: zero below rheobase, rising steeply, then roughly linear.
- **Extensions:** adaptive exponential IF (AdEx, adaptation and a realistic spike onset), Izhikevich model (many firing patterns with two variables). Networks of 10⁵–10⁶ LIF neurons are simulated routinely (Brian2, NEST).

## Hodgkin–Huxley as a system of ODEs (conceptual)
Four coupled nonlinear ODEs: $V$ plus the gating variables $m, h, n$.
$$C\dot V = -\bar g_\text{Na}m^3h(V - E_\text{Na}) - \bar g_\text{K}n^4(V - E_\text{K}) - g_L(V - E_L) + I$$
$$\dot x = \alpha_x(V)(1 - x) - \beta_x(V)x\quad(x = m, h, n)$$
- Each gate relaxes towards a voltage-dependent steady state $x_\infty(V)$ with time constant $\tau_x(V)$.
- Fast $m$ gives the positive feedback; slow $h$ and $n$ give recovery. Biophysically precise but expensive.
- **2D reductions** (FitzHugh–Nagumo, Morris–Lecar) keep the essence (a fast excitatory variable plus a slow recovery variable) and can be analysed in the phase plane.
- See [[Bio05 Neurons and Action Potentials]] and [[Ph10 Signal Propagation and Cable Theory]].

## Firing-rate models and population dynamics
Instead of spikes, model the **average rate** $r$ of a population:
$$\tau\frac{d\mathbf r}{dt} = -\mathbf r + \phi(W\mathbf r + \mathbf h)$$
($\phi$ = nonlinear f–I function, e.g. a sigmoid or rectified linear function; $W$ = connectivity; $\mathbf h$ = external input)
- **Linear case** ($\phi$ = identity): $\tau\dot{\mathbf r} = (W - I)\mathbf r + \mathbf h$. The steady state is $\mathbf r^* = (I - W)^{-1}\mathbf h$, and it is stable if all eigenvalues of $W$ have real part < 1 ([[C3 Linear Systems and Gaussian Elimination]], [[C4 Eigenvalues and Eigenvectors]]).
- **Wilson–Cowan model:** coupled excitatory (E) and inhibitory (I) populations. Depending on parameters: stable activity, bistability, or **oscillations** (E excites I, I inhibits E, with a delay). This is the basis of gamma rhythms and inhibition-stabilised networks.
- **Balanced networks:** large excitation and inhibition cancel on average, which explains irregular, Poisson-like cortical firing (van Vreeswijk & Sompolinsky 1996).

## Attractor networks and recurrent dynamics
An **attractor** is a state (or set of states) that the dynamics converge to and stay in.
| Type | Structure | Function |
|---|---|---|
| **Point attractors (Hopfield network)** | symmetric weights $w_{ij} = \frac1N\sum_\mu\xi_i^\mu\xi_j^\mu$ (Hebbian storage of patterns $\boldsymbol\xi^\mu$); energy $E = -\tfrac12\sum_{ij}w_{ij}s_is_j$ decreases with each update | **associative memory, pattern completion**: a partial cue converges to the stored memory; capacity ≈ 0.14 N patterns |
| **Ring (continuous) attractor** | neurons arranged on a ring, local excitation + broad inhibition | a bump of activity can sit at any angle: **head-direction cells** (fly ellipsoid body, rodent ADN), visuospatial working memory |
| **Line attractor** | an eigenvalue exactly at the stability limit (eigenvalue 1 of $W$ in the linear rate model) | **integration and persistent activity**: oculomotor neural integrator (eye position), evidence accumulation |
| Chaotic / transient dynamics | strong random recurrent connections | rich dynamics for timing and motor patterns (reservoir computing) |

**Hippocampal CA3**, with its dense recurrent collaterals, is the classic candidate for a point-attractor memory network. Grid cells may come from 2D continuous attractors.

## Reinforcement learning: reward prediction error and TD learning
- **Setting:** an agent in state $s$ chooses an action $a$, receives a reward $r$ and moves to state $s'$. Goal: maximise the expected discounted future reward $G_t = r_{t+1} + \gamma r_{t+2} + \gamma^2r_{t+3} + \dots$ (discount $0\le\gamma<1$).
- **Value function** $V(s) = \mathbb E[G_t\mid s_t = s]$; action-value $Q(s, a)$.
- **Temporal-difference (TD) learning:**
  $$\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t),\qquad V(s_t)\leftarrow V(s_t) + \alpha\,\delta_t$$
  The **TD error** δ is the **reward prediction error** (RPE): "better than expected" (δ > 0) or "worse than expected" (δ < 0). The simplest version (Rescorla–Wagner) is $V\leftarrow V + \alpha(r - V)$.
- **Dopamine = RPE** (Schultz, Dayan & Montague 1997). Midbrain dopamine neurons:
  - burst for an **unexpected reward** (δ > 0)
  - don't change for a **fully predicted reward** (δ = 0); after learning, the burst moves to the **predictive cue**
  - **dip below baseline** when a predicted reward is **omitted** (δ < 0)
- **Basal ganglia as actor–critic:** the ventral striatum learns values (critic), and the dorsal striatum selects actions (actor). Dopamine-dependent plasticity on D1 ("go") and D2 ("no-go") pathways implements learning from positive and negative RPEs ([[Bio07 Neural Circuits and Systems]]).
- **Extensions:** Q-learning, model-based RL (planning; prefrontal cortex and hippocampus), distributional RL (dopamine neurons encode different parts of the reward distribution, Dabney et al. 2020).

## Artificial vs. biological neural networks: where the analogy holds and breaks
| Shared ideas | Where the analogy breaks |
|---|---|
| units summing weighted inputs and passing them through a nonlinearity | real neurons **spike**, with rich dynamics, dendritic computation and many cell types |
| learned connection weights (synaptic plasticity) | **Dale's law**: a neuron is either excitatory or inhibitory; ANN weights flip sign freely |
| hierarchical processing (CNN ↔ ventral stream) | the brain is massively **recurrent** with feedback at every level |
| distributed representations; population codes | **backprop** needs symmetric feedback weights (weight transport) and separate forward and backward phases; biological plausibility is debated (feedback alignment, predictive coding, dendritic error signals) |
| gradient-based learning as an abstraction of plasticity | the brain learns from few examples, continually (without catastrophic forgetting), mostly without labels, guided by neuromodulators (dopamine, ACh, NE) |
| ANNs as testable models of brain areas | **energy**: the brain uses ~20 W; training large models uses megawatts; development and genetics pre-structure brain circuits |

**Productive view:** ANNs are useful **normative and hypothesis-generating models**. Compare them with the brain at the level of representations (RSA, encoding models) and behaviour, not neuron by neuron.

## Math links #math-link
- Partial derivatives, gradients, Jacobians, multiple integrals → [[B11 Multivariable Calculus]]
- Differential equations (steady state, time constant, stability, Euler steps) → [[B10 Differential Equations]]
- ODEs, Euler method, exponential solutions → [[B6 Differentiation Rules]], [[B9 Taylor Series]], [[B2 Exponential Functions]]
- Fixed points and stability, Jacobian eigenvalues → [[C4 Eigenvalues and Eigenvectors]], [[B8 Curve Sketching]]
- Steady state of linear networks $(I - W)^{-1}\mathbf h$ → [[C3 Linear Systems and Gaussian Elimination]]
- Geometric series for discounted return, $\sum\gamma^k = \frac{1}{1-\gamma}$ → [[A7 Sums Products and Factorials]]
- Time to threshold (log) → [[A3 Logarithms]]

## Connections
- In code → [[Py08 SciPy Scientific Computing]] (`solve_ivp`), [[Py10 Python Neuroscience Packages]] (Brian2, NEURON), [[Py12 Python Object-Oriented Programming]] (neuron classes), [[MAT03 MATLAB Control Flow and Functions]] (Euler loops)
- RC membrane and LIF → [[Ph05 Capacitance and RC Circuits]]
- AP biophysics → [[Bio05 Neurons and Action Potentials]], [[Ph10 Signal Propagation and Cable Theory]]
- Dopamine and basal ganglia → [[Bio06 Synapses and Neurotransmitters]], [[Bio07 Neural Circuits and Systems]]
- Trained RNNs, ANN architectures → [[CS08 Deep Neural Networks]]
- Plasticity as optimisation → [[CS04 Optimization]]

## Key takeaways
- Dynamical systems: fixed points, stability via $f'$ or Jacobian eigenvalues, limit cycles, bifurcations.
- LIF = RC + threshold + reset, with an analytic f–I curve. HH = 4D nonlinear ODE system; FitzHugh–Nagumo is its 2D essence.
- Rate models $\tau\dot{\mathbf r} = -\mathbf r + \phi(W\mathbf r + \mathbf h)$; E–I loops produce oscillations.
- Attractors: Hopfield (memory), ring (head direction), line (integration).
- TD error $\delta = r + \gamma V(s') - V(s)$ = reward prediction error, which matches the dopamine burst/no change/dip pattern.
- ANNs are useful models, but spikes, Dale's law, recurrence, local learning and energy efficiency differ.
