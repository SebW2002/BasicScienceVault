---
aliases: [Signal Propagation and Cable Theory, Cable Equation, Length Constant, Conduction Velocity, Hodgkin-Huxley, Kabeltheorie]
tags: [physics, cable-theory, conduction, myelin, hodgkin-huxley, type/overview, neuro]
---
# Ph10 Signal Propagation and Cable Theory

> [[MOC-physics|↑ Physics MOC]] · [[Ph10 Signal Propagation and Cable Theory - Worksheet|✏️ Worksheet]] · [[Ph10 Signal Propagation and Cable Theory - Solutions|✅ Solutions]] · [[Mistakes - Physics|⚠️ Mistake log]]

## Why this matters
Neurons are long and thin, so signals have to travel. **Passive** signals (synaptic potentials in dendrites) shrink and slow down as they spread, and cable theory says how much. **Active** signals (action potentials) regenerate themselves and travel without loss. Myelin makes them fast. Cable theory combines the RC membrane ([[Ph05 Capacitance and RC Circuits]]) with the resistance of the cytoplasm ([[Ph04 Circuits and Resistance]]).

## The cable model
A dendrite or axon is a cylinder of radius $a$ (diameter $d = 2a$). Per unit length it has:
- **Axial (internal) resistance** $r_i = \frac{R_i}{\pi a^2}$ (Ω/cm), where $R_i$ ≈ 100–200 Ω·cm is the specific resistivity of the cytoplasm. Thin cables have high $r_i$.
- **Membrane resistance** $r_m = \frac{R_m}{2\pi a}$ (Ω·cm), where $R_m$ is the specific membrane resistance (≈ 10–100 kΩ·cm²).
- **Membrane capacitance** $c_m = C_m\cdot2\pi a$ (F/cm), where $C_m\approx1\,\mu\text{F/cm}^2$.

Picture a ladder: resistors $r_i$ along the core, and at each rung an RC element ($r_m\parallel c_m$) to the outside.

## Passive spread and the length constant λ
In steady state (constant current injected at $x = 0$, infinite cable), the voltage decays exponentially:
$$V(x) = V_0\,e^{-x/\lambda},\qquad \lambda = \sqrt{\frac{r_m}{r_i}} = \sqrt{\frac{R_m}{R_i}\cdot\frac{d}{4}}$$
- After one $\lambda$, 37 % of the voltage remains; after $2\lambda$, 14 %; after $3\lambda$, 5 %.
- $\lambda\propto\sqrt d$: thicker dendrites conduct passively farther. $\lambda\propto\sqrt{R_m}$: a less leaky membrane conducts farther.
- Typical values: 0.2–2 mm for dendrites. Example: $R_m = 20\,\text{k}\Omega\text{·cm}^2$, $R_i = 100\,\Omega\text{·cm}$, $d = 1\,\mu\text{m}$ gives $\lambda = \sqrt{\frac{20\,000}{100}\cdot\frac{10^{-4}\,\text{cm}}{4}} = \sqrt{0.005}\,\text{cm}\approx0.7\,\text{mm}$.
- **Electrotonic length** $L = \ell/\lambda$ (physical length in units of λ) describes how "compact" a neuron is electrically.

## The cable equation and its link to RC circuits
Applying Kirchhoff's current law ([[Ph04 Circuits and Resistance]]) to a short piece of cable gives:
$$\lambda^2\frac{\partial^2V}{\partial x^2} = \tau_m\frac{\partial V}{\partial t} + V$$
- **Without the spatial term** ($\partial^2V/\partial x^2 = 0$, e.g. a small isopotential soma), it reduces to the RC equation $\tau\,dV/dt = -V$ ([[Ph05 Capacitance and RC Circuits]]).
- **Without the time term** (steady state), it gives the exponential decay $V_0e^{-x/\lambda}$.
- It has the same form as the diffusion equation with a leak term: voltage "diffuses" along the cable and leaks out through the membrane ([[Ph07 Diffusion and Transport]]).

**Consequences for dendritic integration:**
- **Attenuation:** distal synaptic inputs arrive at the soma **smaller**.
- **Filtering:** distal inputs arrive **slower and broader** (rise time and half-width increase), because high frequencies are attenuated more ([[Ph09 Waves and Oscillations]]).
- Synapses close together summate more strongly than distant ones (spatial summation, local interaction).
- Neurons compensate for these effects with active dendritic conductances (Na⁺, Ca²⁺, NMDA spikes) and synapse scaling.

## Conduction velocity and myelin
**Unmyelinated axons:** the AP spreads continuously; the speed depends on how fast the next segment is charged to threshold. It scales roughly with $\lambda/\tau$, so
$$v\propto\sqrt d$$
Typical: 0.5–2 m/s for 1 µm fibres. The squid's giant axon (0.5 mm) reaches about 20 m/s, by size alone.

**Myelinated axons (saltatory conduction):**
- The myelin sheath (many membrane layers in series) **increases $R_m$** (much less leak) and **decreases $C_m$** (much less charge needed, [[Ph05 Capacitance and RC Circuits]]).
- The internode is charged quickly and almost without loss; the AP is regenerated only at the **nodes of Ranvier** (≈ 1 µm, dense Nav channels), spaced every ~0.2–2 mm (~100× the fibre diameter).
- Speed is **proportional to diameter**, $v\approx6\,\text{m/s per µm}$ (Hursh's rule), up to about 120 m/s.
- Above about 1 µm diameter, myelinated axons are faster than unmyelinated ones; below that, myelination isn't worth it, which is why the thinnest fibres (C fibres) are unmyelinated.
- Further benefits: less energy (ions flow only at the nodes, so less pump work) and less space (a thin myelinated fibre is as fast as a much thicker unmyelinated one).

## Active propagation: the Hodgkin–Huxley model (conceptual)
An action potential is a **nonlinear, regenerative** wave. The cable equation gets an additional current from voltage-gated channels:
$$C_m\frac{\partial V}{\partial t} = \frac{d}{4R_i}\frac{\partial^2V}{\partial x^2} - \underbrace{\left[\bar g_\text{Na}m^3h(V - E_\text{Na}) + \bar g_\text{K}n^4(V - E_\text{K}) + g_L(V - E_L)\right]}_\text{ionic currents (per membrane area)}$$
- Each gating variable ($m$, $h$, $n$) follows its own first-order differential equation with voltage-dependent rates (Boltzmann-like, [[Ph08 Thermodynamics and Statistics]]).
- **Positive feedback:** depolarisation opens Na⁺ channels (m↑), more Na⁺ flows in, and the cell depolarises further. **Negative feedback** arrives with a delay: h↓ (Na⁺ inactivation) and n↑ (K⁺ activation).
- **Nonlinearity** makes the AP all-or-none and lets it travel at **constant amplitude and speed**. A passive cable can't do this: signals there inevitably decay.
- Hodgkin and Huxley (1952) **predicted the conduction velocity** of the squid axon from voltage-clamp data alone. It was a triumph of quantitative biology.

## In neuroscience #neuro
- **Multiple sclerosis:** demyelinated segments conduct slowly or block (lower $R_m$, higher $C_m$, so not enough current reaches the next node).
- **Dendritic location matters:** distal inputs on pyramidal cells (tuft) are strongly attenuated at the soma, so they rely on dendritic spikes. Inputs close to the soma have more direct influence.
- **Compartmental models** (NEURON simulator) divide neurons into many coupled RC compartments, which is a discretised cable equation.
- **Rall's 3/2 power rule:** a dendritic tree whose branches satisfy $d_\text{parent}^{3/2} = \sum d_\text{daughter}^{3/2}$ behaves like a single equivalent cylinder.

## Math links #math-link
- Partial derivatives, gradients, Jacobians, multiple integrals → [[B11 Multivariable Calculus]]
- Differential equations (steady state, time constant, stability, Euler steps) → [[B10 Differential Equations]]
- $\lambda = \sqrt{r_m/r_i}$; velocity ∝ $\sqrt d$ vs. ∝ $d$ → [[A2 Root Rules]], [[A1 Exponent Rules]]
- $V(x) = V_0e^{-x/\lambda}$ → [[B2 Exponential Functions]]
- Cable equation: a partial differential equation with first and second derivatives; analogous to the diffusion equation → [[B6 Differentiation Rules]]
- Discretised into compartments: a matrix (tridiagonal linear system) → [[C1 Matrices]], [[C3 Linear Systems and Gaussian Elimination]]
- Hodgkin–Huxley: nonlinear ODEs; linear stability around rest → [[B9 Taylor Series]], [[C4 Eigenvalues and Eigenvectors]]

## Connections
- RC membrane → [[Ph05 Capacitance and RC Circuits]]
- Resistances → [[Ph04 Circuits and Resistance]]
- Filtering → [[Ph09 Waves and Oscillations]]
- Biology of the AP and myelin → [[Bio05 Neurons and Action Potentials]]
- Myelinating glia → [[Bio07 Neural Circuits and Systems]]
- Voltage clamp → [[Meth03 Electrophysiology]]

## Key takeaways
- Passive cable: $V(x) = V_0e^{-x/\lambda}$, $\lambda = \sqrt{r_m/r_i}\propto\sqrt d$ (~0.2–2 mm). Distal inputs arrive smaller and slower.
- Cable equation: $\lambda^2V'' = \tau\dot V + V$. It combines RC (time) and resistive spread (space).
- Unmyelinated: $v\propto\sqrt d$. Myelinated: $v\propto d$ (~6 m/s per µm), thanks to higher $R_m$, lower $C_m$ and saltatory jumps between nodes.
- The AP is a nonlinear regenerative wave (Hodgkin–Huxley): positive Na⁺ feedback, delayed negative feedback, so it propagates without loss.
