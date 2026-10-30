---
tags: [computer-science, computational-neuroscience, type/worksheet]
---
# CS10 Dynamical and Computational Neuro Models – Worksheet

> Theory: [[CS10 Dynamical and Computational Neuro Models]] · Solutions: [[CS10 Dynamical and Computational Neuro Models - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮. $\ln2\approx0.69$, $\ln3\approx1.1$.

## Level 1 – Dynamical systems
1. Find the fixed points of $\dot x = x - x^3$ and determine their stability.
2. For $\dot x = -2(x - 3)$, find the fixed point, its stability and the time constant of the approach.
3. Perform two Euler steps with $\Delta t = 0.1$ for $\dot x = -x$ from $x_0 = 1$. Compare with the exact solution $e^{-0.2}\approx0.82$.
4. A 2D system has Jacobian eigenvalues $-0.5\pm3i$ at a fixed point. Describe the dynamics nearby.

## Level 2 – Single-neuron models
5. LIF: $\tau = 10$ ms, $V_\text{reset} = 0$, $V_\theta = 10$ mV, $V_\infty = 20$ mV (all relative to rest), $t_\text{ref} = 2$ ms. Compute the firing rate.
6. In task 5, what is the rheobase in terms of $V_\infty$? What is the rate for $V_\infty = 15$ mV? (Use $\ln3\approx1.1$.)
7. What roles do $m$, $h$ and $n$ play in the Hodgkin–Huxley model? Which is fast, which slow?
8. Why are 2D reductions like FitzHugh–Nagumo useful?

## Level 3 – Networks
9. Linear rate model: $\tau\dot{\mathbf r} = -\mathbf r + W\mathbf r + \mathbf h$ with $W = \begin{pmatrix}0.5&0\\0&0.8\end{pmatrix}$, $\mathbf h = (1, 1)$. Compute the steady state. What happens if $W_{22} = 1$?
10. A Hopfield network has 1000 neurons. Roughly how many random patterns can it store? What happens if you store many more?
11. Explain how a ring attractor can maintain the memory of a head direction in the dark.
12. Why does an E–I loop tend to oscillate?

## Level 4 – Reinforcement learning & ANN vs. brain
13. TD learning with $\gamma = 0.9$, $\alpha = 0.5$: $V(s) = 2$, $V(s') = 4$, reward $r = 1$. Compute δ and the updated $V(s)$.
14. Predict the dopamine response (burst / no change / dip) in each case: a) an unexpected juice drop, b) a fully predicted juice drop after a cue, c) the cue itself after learning, d) a cue followed by an omitted reward (at the expected reward time).
15. A cue is always followed by a reward of 1 after one step. With $\gamma = 0.9$, what is the learned value of the cue state? Of a state two steps before the reward?
16. Name three ways in which typical deep networks differ from biological networks.
17. 🧮 Rescorla–Wagner $V\leftarrow V + \alpha(r - V)$ with $\alpha = 0.3$, $r = 1$, $V_0 = 0$. Compute $V_1, V_2, V_3$ and give a closed formula for $V_n$.
