---
aliases: [Circuits and Resistance, Ohm's Law, Kirchhoff's Laws, Conductance, Equivalent Circuit, Stromkreise]
tags: [physics, circuit, resistance, conductance, kirchhoff, type/overview, neuro]
---
# Ph04 Circuits and Resistance

> [[MOC-physics|↑ Physics MOC]] · [[Ph04 Circuits and Resistance - Worksheet|✏️ Worksheet]] · [[Ph04 Circuits and Resistance - Solutions|✅ Solutions]] · [[Mistakes - Physics|⚠️ Mistake log]]

## Why this matters
A neuron can be described as an **electrical circuit**: ion channels are resistors (conductances), ion gradients are batteries, and the membrane is a capacitor. With Ohm's and Kirchhoff's laws you can derive the resting potential, input resistance and synaptic effects. This equivalent circuit is the basis of every neuron model, from integrate-and-fire to Hodgkin–Huxley.

## Ohm's law
$$V = I\cdot R\qquad\Longleftrightarrow\qquad I = G\cdot V,\quad G = \frac1R$$
- **Resistance** $R$ in ohms (Ω = V/A): how strongly a component opposes current.
- **Conductance** $G$ in siemens (S = 1/Ω): how easily current flows. Neurophysiologists prefer conductance because **open channels add conductance**.
- Typical scales:
  - single channel: 1–300 **pS** (e.g. 20 pS = $2\times10^{-11}$ S, i.e. 50 GΩ)
  - neuron input resistance: 10 MΩ – 1 GΩ
  - patch pipette: 2–10 MΩ
  - gigaseal: > 1 GΩ
- **Resistance of a conductor:** $R = \rho\frac{L}{A}$ ($\rho$ = resistivity, $L$ = length, $A$ = cross-section). Thin, long structures such as dendrites and axons have high axial resistance ([[Ph10 Signal Propagation and Cable Theory]]).
- **Electrical power:** $P = V\cdot I = I^2R = V^2/R$, which is dissipated as heat.

## Series and parallel
| | Series (one after the other) | Parallel (side by side) |
|---|---|---|
| Current | the same through all | splits: $I = I_1 + I_2 + \dots$ |
| Voltage | splits: $V = V_1 + V_2 + \dots$ | the same across all |
| Resistance | $R = R_1 + R_2 + \dots$ (adds) | $\frac1R = \frac1{R_1} + \frac1{R_2} + \dots$ |
| Conductance | $\frac1G = \frac1{G_1} + \frac1{G_2} + \dots$ | $G = G_1 + G_2 + \dots$ (adds) |
| Neuro example | pipette (series) resistance + cell; axial resistance along a dendrite | **ion channels in the membrane** are all in parallel |

- Parallel resistance is always smaller than the smallest single resistance. Opening more channels lowers the input resistance.
- **Voltage divider** (two resistors in series): $V_1 = V\cdot\frac{R_1}{R_1 + R_2}$. Example: in voltage clamp, the uncompensated series resistance $R_s$ causes a voltage error $\Delta V = I\cdot R_s$.

## Kirchhoff's laws
1. **Current law (KCL, junction rule):** at every node, the sum of incoming currents equals the sum of outgoing currents, $\sum I = 0$. This is charge conservation.
2. **Voltage law (KVL, loop rule):** around any closed loop, the sum of all voltages is zero, $\sum V = 0$. This is energy conservation.

## The equivalent circuit of a neuron
Each ion species forms one branch: a **conductance** $g_\text{ion}$ (channels) in series with a **battery** $E_\text{ion}$ (the Nernst potential, set by the gradient). All branches and the membrane capacitance $C_m$ lie **in parallel** between inside and outside.
```
  inside ──┬────────┬────────┬────────┬──────
           │        │        │        │
          g_Na     g_K      g_L      C_m
           │        │        │        │
          E_Na     E_K      E_L       │
           │        │        │        │
  outside ─┴────────┴────────┴────────┴──────
```
Current through each branch (Ohm's law with the battery): $I_\text{ion} = g_\text{ion}(V_m - E_\text{ion})$.

**KCL at the inside node** (no injected current, steady state, so no capacitive current):
$$g_\text{Na}(V - E_\text{Na}) + g_\text{K}(V - E_\text{K}) + g_L(V - E_L) = 0$$
$$\Longrightarrow\quad V_\text{rest} = \frac{g_\text{Na}E_\text{Na} + g_\text{K}E_\text{K} + g_LE_L}{g_\text{Na} + g_\text{K} + g_L}$$
The membrane potential is a **conductance-weighted average** of the reversal potentials ([[A4 Factoring and Simplifying]]). The ion with the largest conductance dominates, which is the same message as the GHK equation ([[Ch05 Redox and Electrochemistry]]).

**Input resistance** $R_\text{in} = \frac{\Delta V}{\Delta I}$ (in current clamp). It equals $1/\sum g$ of all open channels. **Specific membrane resistance** $R_m$ (in Ω·cm²) describes the leakiness of a membrane area, typically ~10–100 kΩ·cm².

## In neuroscience #neuro
- **Synaptic input** = adding a conductance branch: $I_\text{syn} = g_\text{syn}(V - E_\text{syn})$. AMPA ($E\approx0$ mV) excites; GABA_A ($E\approx-70$ mV) inhibits or **shunts** (it increases the denominator and divides other inputs).
- **Input resistance and excitability:** small neurons with few channels have a high $R_\text{in}$, so a small current produces a large voltage change (Ohm's law). This is why small motor neurons are recruited first (Henneman's size principle).
- **Recording artefacts:** series resistance in whole-cell voltage clamp (voltage errors, slow clamp); seal resistance (leak currents). See [[Meth03 Electrophysiology]].
- **Gap junctions** are conductances *between* two cells, coupling their voltages.

## Math links #math-link
- Ohm's law as a linear function; I–V curves; reversal potential as the zero crossing → [[B1 Properties of Functions]], [[A8 Solving Equations]]
- Parallel resistances and the weighted average → [[A5 Fractions]], [[A4 Factoring and Simplifying]]
- Networks of resistors → linear systems of equations (Kirchhoff for each node) → [[C3 Linear Systems and Gaussian Elimination]]
- Sums of currents → [[A7 Sums Products and Factorials]]

## Connections
- Current and voltage → [[Ph02 Electricity and Charge]]
- Adding the capacitor → [[Ph05 Capacitance and RC Circuits]]
- Resistances along dendrites → [[Ph10 Signal Propagation and Cable Theory]]
- Ion channels → [[Bio02 Membranes and Transport]]
- Reversal potentials → [[Ch05 Redox and Electrochemistry]]

## Key takeaways
- $V = IR$, $G = 1/R$. Channels are conductances (pS), cells have input resistances in MΩ.
- Series: $R$ adds. Parallel: $G$ adds. Membrane channels are in parallel.
- KCL: currents at a node sum to zero. KVL: voltages around a loop sum to zero.
- Equivalent circuit: battery $E_\text{ion}$ + conductance $g_\text{ion}$ per ion, in parallel with $C_m$. $V_\text{rest}$ is the conductance-weighted average of the $E_\text{ion}$.
