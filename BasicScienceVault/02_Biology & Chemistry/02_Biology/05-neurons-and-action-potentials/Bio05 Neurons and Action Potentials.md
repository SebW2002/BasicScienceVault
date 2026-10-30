---
aliases: [Neurons and Action Potentials, Action Potential, Resting Potential, Saltatory Conduction, Neuron Anatomy, Aktionspotential]
tags: [biology, neuron, action-potential, myelin, type/overview, neuro]
---
# Bio05 Neurons and Action Potentials

> [[MOC-biology|↑ Biology MOC]] · [[Bio05 Neurons and Action Potentials - Worksheet|✏️ Worksheet]] · [[Bio05 Neurons and Action Potentials - Solutions|✅ Solutions]] · [[Mistakes - Biology|⚠️ Mistake log]]

## Why this matters
The action potential (AP) is the universal "digital" signal of the nervous system: an all-or-none voltage pulse of about 100 mV and about 1 ms that travels along the axon without losing amplitude. Understanding it ties together everything from ion gradients ([[Ch05 Redox and Electrochemistry]]) and channels ([[Bio02 Membranes and Transport]]) to the differential equations of Hodgkin and Huxley.

## Neuron anatomy
| Part | Function |
|---|---|
| **Dendrites** (with **spines**) | receive synaptic input; passive and active integration |
| **Soma** (cell body) | nucleus, protein synthesis (Nissl bodies), integration |
| **Axon hillock / axon initial segment (AIS)** | very high density of Nav channels (Nav1.6), so this is where the AP is **initiated**; lowest threshold |
| **Axon** | conducts APs over distances up to > 1 m; diameter ~0.1–20 µm |
| **Myelin** | insulating sheath from **oligodendrocytes** (CNS; one cell myelinates many axons) or **Schwann cells** (PNS; one cell, one segment) |
| **Nodes of Ranvier** | ~1 µm gaps between myelin segments (internodes ~0.2–2 mm), packed with Nav channels |
| **Axon terminals / boutons** | transmitter release ([[Bio06 Synapses and Neurotransmitters]]) |

**Morphological types:** multipolar (most CNS neurons, e.g. **pyramidal cells**, **Purkinje cells**), bipolar (retina, olfactory epithelium), pseudounipolar (sensory neurons in the dorsal root ganglia).
**Functional flow** (Cajal's "dynamic polarisation"): dendrites → soma → AIS → axon → terminals.
The human brain has about **86 billion** neurons and about as many glial cells.

## Resting potential
$V_\text{rest}\approx-60$ to $-75$ mV (inside negative).
1. The **Na⁺/K⁺-ATPase** creates gradients: high K⁺ inside, high Na⁺ outside.
2. At rest, the membrane is mostly permeable to **K⁺** (leak channels, K2P, Kir). K⁺ flows out until the inside is negative enough to hold it back, which brings $V_m$ close to $E_\text{K}$.
3. A small Na⁺ permeability pulls $V_m$ a bit above $E_\text{K}$ (GHK equation, [[Ch05 Redox and Electrochemistry]]).

## The action potential, phase by phase
| Phase | What happens | Channels |
|---|---|---|
| 1. **Depolarisation to threshold** (≈ −55 mV) | synaptic input or current depolarises the AIS | some Nav open |
| 2. **Rising phase** (to about +30 to +40 mV) | **positive feedback**: depolarisation opens Nav, Na⁺ flows in, depolarising further (Hodgkin cycle); $V_m$ approaches $E_\text{Na}$ | Nav open |
| 3. **Repolarisation** | Nav **inactivate** (within ~1 ms) and delayed-rectifier **Kv** open, so K⁺ flows out | Nav inactivated, Kv open |
| 4. **Afterhyperpolarisation (AHP)** | Kv still open, $V_m$ approaches $E_\text{K}$ (below rest) | Kv, Ca²⁺-activated K⁺ (SK, BK) |
| 5. Return to rest | Kv close | leak |

**All-or-none:** once threshold is crossed, the AP has a stereotyped shape and size. Information is coded in **AP rate and timing**, not amplitude.

**Refractory period**
- **Absolute** (~1–2 ms): Nav channels are inactivated and no new AP is possible, whatever the stimulus. This limits the maximum firing rate (to below ~500–1000 Hz) and makes **propagation one-directional**.
- **Relative** (a few ms): some Nav channels have recovered but K⁺ conductance is still high. A stronger stimulus is needed.

**Hodgkin–Huxley model** (1952, Nobel 1963):
$$C_m\frac{dV}{dt} = -\bar g_\text{Na}m^3h(V - E_\text{Na}) - \bar g_\text{K}n^4(V - E_\text{K}) - g_L(V - E_L) + I_\text{ext}$$
Gating variables $m$ (Na⁺ activation), $h$ (Na⁺ inactivation) and $n$ (K⁺ activation) each follow first-order kinetics with voltage-dependent rates.

**Pharmacology:** TTX blocks Nav, so there is no AP. TEA blocks Kv, so the AP is broadened. Local anaesthetics block Nav from the inside.

## Propagation and saltatory conduction
**Unmyelinated axons:** the AP spreads continuously. The local current from the active region depolarises the neighbouring membrane to threshold. Speed $\propto\sqrt{d}$ (axon diameter), typically 0.5–2 m/s (C fibres). The squid giant axon (~0.5 mm) is fast through sheer size.

**Passive spread** is set by the **length constant**
$$\lambda = \sqrt{\frac{r_m}{r_i}}$$
($r_m$: membrane resistance × length; $r_i$: axial resistance per length). The voltage decays as $V(x) = V_0e^{-x/\lambda}$.

**Myelinated axons:**
- Myelin raises $r_m$ (less leak) and lowers $c_m$ (less charge needed), so current flows effectively from node to node.
- The AP "jumps" (Latin *saltare*) between **nodes of Ranvier**, where Nav channels are concentrated.
- Speed $\propto d$, roughly **6 m/s per µm** of fibre diameter, up to about 120 m/s (Aα fibres).
- It saves energy (only the nodes exchange ions) and space (thin fast axons).

| Fibre | Diameter (µm) | Myelin | Speed (m/s) | Function |
|---|---|---|---|---|
| Aα | 12–20 | yes | 70–120 | motor, proprioception |
| Aβ | 6–12 | yes | 35–75 | touch |
| Aδ | 1–5 | thin | 5–30 | fast pain, cold |
| C | 0.2–1.5 | no | 0.5–2 | slow pain, temperature |

## In neuroscience #neuro
- **Demyelinating diseases:** in **multiple sclerosis** (CNS, autoimmune against oligodendrocyte myelin) and Guillain–Barré syndrome (PNS), conduction slows or is blocked. In clinical tests, visual evoked potentials show delayed latencies.
- **Firing patterns** (regular spiking, fast spiking, bursting) are shaped by the mix of channels a neuron expresses: HCN, T-type Cav, Kv3 for fast spiking in PV interneurons, and others.
- **Dendrites are active:** back-propagating APs and dendritic Ca²⁺ and NMDA spikes support coincidence detection and plasticity.
- **Computational models:** leaky integrate-and-fire (simple), Hodgkin–Huxley (biophysical), FitzHugh–Nagumo (2D reduction for phase-plane analysis).

## Math links #math-link
- Differential equations (steady state, time constant, stability, Euler steps) → [[B10 Differential Equations]]
- Membrane equation $\tau\frac{dV}{dt} = -(V - E_L) + RI$, with exponential charging $V(t) = V_\infty(1 - e^{-t/\tau})$ → [[B2 Exponential Functions]], [[B6 Differentiation Rules]], [[A8 Solving Equations]]
- Time to threshold, $t = -\tau\ln(1 - V_\theta/V_\infty)$ → [[A3 Logarithms]]
- Length constant $\lambda = \sqrt{r_m/r_i}$ and $V(x) = V_0e^{-x/\lambda}$ → [[A2 Root Rules]], [[B2 Exponential Functions]]
- Conduction velocity scaling ($\sqrt d$ vs. $d$) → [[A1 Exponent Rules]]
- Gating variables as sigmoids of $V$; stability of the resting state (eigenvalues of the Jacobian) → [[B8 Curve Sketching]], [[C4 Eigenvalues and Eigenvectors]]
- Spike trains as Poisson processes → [[A7 Sums Products and Factorials]]

## Connections
- Ion gradients, Nernst, GHK → [[Ch05 Redox and Electrochemistry]]
- Channels and pumps → [[Bio02 Membranes and Transport]]
- Myelin lipids → [[Ch08 Biomolecules]]; oligodendrocytes → [[Bio07 Neural Circuits and Systems]]
- Synaptic transmission → [[Bio06 Synapses and Neurotransmitters]]
- Measuring APs → [[Meth03 Electrophysiology]]

## Key takeaways
- The resting potential is close to $E_\text{K}$ (K⁺ leak), sustained by Na⁺/K⁺-ATPase gradients.
- AP: threshold → Nav positive feedback → Nav inactivation + Kv opening → AHP. It is all-or-none.
- Refractoriness (Nav inactivation) limits rate and makes propagation one-way.
- Myelin + nodes give saltatory conduction: faster (∝ d) and cheaper.
