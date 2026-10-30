---
tags: [computer-science, computational-neuroscience, type/solution]
---
# CS10 Dynamical and Computational Neuro Models – Solutions

> Worksheet: [[CS10 Dynamical and Computational Neuro Models - Worksheet]] · Theory: [[CS10 Dynamical and Computational Neuro Models]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. $x(1 - x^2) = 0$ gives $x^*\in\{-1, 0, 1\}$. $f'(x) = 1 - 3x^2$: $f'(0) = 1 > 0$, so 0 is **unstable**; $f'(\pm1) = -2 < 0$, so $\pm1$ are **stable**. This is a bistable system, like a memory switch.
2. $x^* = 3$; $f' = -2 < 0$, so it is stable. Solution $x(t) = 3 + (x_0 - 3)e^{-2t}$, time constant $\tau = 0.5$.
3. $x_1 = 1 - 0.1\cdot1 = 0.9$; $x_2 = 0.9 - 0.09 = 0.81$. Exact: 0.8187. Euler slightly underestimates; the error shrinks with smaller $\Delta t$.
4. Negative real part means stable; imaginary part ±3 means oscillation. Trajectories **spiral** into the fixed point: damped oscillations with angular frequency 3 and decay rate 0.5.

## Level 2
5. $T = 10\ln\frac{20 - 0}{20 - 10} = 10\ln2\approx6.9$ ms; $f = \frac{1}{2 + 6.9}\,\text{ms}^{-1}\approx112$ Hz.
6. Rheobase: $V_\infty = V_\theta = 10$ mV (below it the neuron never fires). For $V_\infty = 15$: $T = 10\ln\frac{15}{5} = 10\ln3\approx11$ ms, so $f\approx\frac{1}{13\,\text{ms}}\approx77$ Hz.
7. $m$: Na⁺ activation (**fast**; positive feedback). $h$: Na⁺ inactivation (slow; ends the Na⁺ current). $n$: K⁺ activation (slow; repolarisation). $V$ and $m$ form the fast subsystem; $h$ and $n$ the slow recovery.
8. Two variables can be analysed **graphically** in the phase plane (nullclines, fixed points, limit cycles, bifurcations). This explains threshold, excitability types and repetitive firing intuitively, while keeping the essential fast–slow structure of HH.

## Level 3
9. $\mathbf r^* = (I - W)^{-1}\mathbf h$: $r_1 = \frac{1}{0.5} = 2$, $r_2 = \frac{1}{0.2} = 5$. With $W_{22} = 1$: $1 - W_{22} = 0$, so there is no steady state. $r_2$ integrates its input ($\tau\dot r_2 = h_2$) and grows linearly: a **line attractor/integrator**. Without input, it holds any value (persistent activity).
10. About $0.14\cdot1000 = 140$ patterns. Storing many more causes **interference**: spurious mixture states appear and retrieval fails ("catastrophic" breakdown of memory).
11. Local recurrent excitation between neurons with similar preferred directions plus broad inhibition creates a stable **activity bump** that sustains itself at any position on the ring (a continuum of fixed points). Without input, the bump stays where it is, so the direction is remembered. Angular-velocity inputs shift the bump (path integration); landmarks correct drift.
12. Excitation drives the I population, which then (with a delay set by synaptic and membrane time constants) suppresses E. With less E activity, I drops, so E recovers, and so on. In linear terms, the Jacobian of the E–I system has complex eigenvalues (as in [[C4 Eigenvalues and Eigenvectors - Solutions]], task 10). This is the basis of gamma rhythms (PING).

## Level 4
13. $\delta = 1 + 0.9\cdot4 - 2 = 2.6$; $V(s)\leftarrow2 + 0.5\cdot2.6 = 3.3$.
14. a) burst (δ > 0) b) no change (δ = 0) c) burst (the cue now unexpectedly predicts reward) d) **dip** at the expected reward time (δ < 0).
15. Cue state: $V = r = 1$ (reward one step later; with the convention $\delta = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$ and a terminal state of value 0). One step earlier: $V = \gamma\cdot1 = 0.9$. Values discount with distance to the reward.
16. Any three: (1) continuous activations vs. spikes; (2) weights can change sign vs. **Dale's law**; (3) mostly feedforward vs. massively recurrent; (4) backprop with non-local gradient information vs. local plasticity + neuromodulators; (5) need for huge labelled datasets vs. few-shot and unsupervised learning; (6) catastrophic forgetting vs. continual learning; (7) energy consumption; (8) uniform units vs. diverse cell types and dendrites.
17. $V_1 = 0.3$; $V_2 = 0.3 + 0.3\cdot0.7 = 0.51$; $V_3 = 0.51 + 0.3\cdot0.49 = 0.657$. The error shrinks by a factor 0.7 each step, so $V_n = 1 - 0.7^n$, an exponential learning curve.
