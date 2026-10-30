---
aliases: [Thermodynamics and Statistics, Boltzmann Distribution, Free Energy, Entropy, kT, Thermodynamik]
tags: [physics, thermodynamics, boltzmann, free-energy, entropy, type/overview, neuro]
---
# Ph08 Thermodynamics and Statistics

> [[MOC-physics|↑ Physics MOC]] · [[Ph08 Thermodynamics and Statistics - Worksheet|✏️ Worksheet]] · [[Ph08 Thermodynamics and Statistics - Solutions|✅ Solutions]] · [[Mistakes - Physics|⚠️ Mistake log]]

## Why this matters
Molecules in the brain are constantly shaken by thermal motion. Whether a channel opens, a transmitter binds or an ion moves across a membrane is a matter of **probability** set by energy differences compared to **thermal energy $kT$**. Thermodynamics tells us which processes can happen spontaneously ($\Delta G < 0$), and statistical physics (Boltzmann) tells us how likely each state is. The Nernst equation, channel gating curves and equilibrium constants all follow from this.

## Temperature and thermal energy
- **Temperature** measures the **average kinetic energy** of molecules. For translation in 3D:
  $$\langle E_\text{kin}\rangle = \tfrac32kT$$
  Each degree of freedom gets $\tfrac12kT$ (equipartition).
- **Boltzmann constant:** $k = 1.381\times10^{-23}$ J/K. **Gas constant:** $R = N_Ak = 8.314$ J/(mol·K). Absolute temperature in kelvin: $T = \theta_{°C} + 273.15$.

| Thermal energy at 37 °C (310 K) | Value |
|---|---|
| $kT$ per molecule | $4.3\times10^{-21}$ J = **4.3 pN·nm** = **26.7 meV** |
| $RT$ per mole | **2.58 kJ/mol** (≈ 0.62 kcal/mol) |
| "Thermal voltage" $kT/e = RT/F$ | **26.7 mV** |

**Energy scale comparison** (in units of $kT$):
- van der Waals contact: < 1
- hydrogen bond: ~2–8
- ATP hydrolysis in the cell: ~20
- covalent C–C bond: ~140
- a visible photon: ~100 ([[Ph12 Quantum Basics for Biophysics]])

**Role of $kT$:** processes with energy barriers of a few $kT$ happen spontaneously all the time (channel flickering, conformational fluctuations, unbinding). Barriers of many $kT$ need energy input (ATP, photons, voltage).

## Boltzmann distribution
At thermal equilibrium, the probability of a state with energy $E_i$ is
$$p_i = \frac{e^{-E_i/kT}}{Z},\qquad Z = \sum_j e^{-E_j/kT}$$
($Z$ = partition function, which normalises the probabilities.) For two states:
$$\frac{p_2}{p_1} = e^{-(E_2 - E_1)/kT} = e^{-\Delta E/kT}$$
- $\Delta E = 0$: 1 : 1. $\Delta E = 1\,kT$: 1 : 2.7. $\Delta E = 2.3\,kT$: 1 : 10. $\Delta E = 10\,kT$: 1 : 22,000.
- Higher temperature makes the distribution more even.

**Rates over energy barriers (Arrhenius):** $k_\text{rate}\propto e^{-E_a/kT}$. Small changes in the barrier height change rates exponentially. Channel kinetics have a **Q₁₀** of about 2–4 (rate change per 10 °C), which is why experiments at room temperature vs. 37 °C give different time courses.

### Boltzmann and channel gating
A two-state channel (closed ⇌ open) with gating charge $z_g$ (number of elementary charges moved by the voltage sensor across the field): the energy difference between open and closed depends linearly on voltage, $\Delta E(V) = \Delta E_0 - z_geV$. The Boltzmann distribution gives
$$P_\text{open}(V) = \frac{1}{1 + e^{-z_ge(V - V_{1/2})/kT}} = \frac{1}{1 + e^{-(V - V_{1/2})/s}},\qquad s = \frac{kT}{z_ge} = \frac{26.7\,\text{mV}}{z_g}$$
- $V_{1/2}$: the voltage at which half the channels are open.
- **Slope factor** $s$: more gating charge means a smaller $s$ and a **steeper** curve. Kv channels move ~12–13 $e$ in total, which makes their activation very steep.
- This sigmoid is exactly the "Boltzmann fit" used for activation and inactivation curves in patch clamp ([[Meth03 Electrophysiology]]).

**Synaptic release probability** follows the same logic. Vesicle fusion must overcome an energy barrier. Ca²⁺ binding to synaptotagmin (several sites, cooperative) lowers this barrier, and because rates depend exponentially on barrier height, release probability rises steeply with Ca²⁺ (≈ [Ca²⁺]⁴, [[Bio06 Synapses and Neurotransmitters]]). Release is **probabilistic** (with $p$ per site), a consequence of thermal fluctuations.

## Free energy as the driving force
**Gibbs free energy** $G = H - TS$ (enthalpy minus temperature times entropy). For a process at constant $T$ and pressure:
$$\Delta G = \Delta H - T\Delta S$$
- $\Delta G < 0$: the process runs **spontaneously** (exergonic).
- $\Delta G > 0$: it needs energy input (endergonic), e.g. coupling to ATP hydrolysis.
- $\Delta G = 0$: equilibrium.
- $\Delta G$ says **whether** a process can run, not **how fast** (that is set by the barrier; enzymes and channels lower barriers without changing $\Delta G$).

**Concentration dependence:**
$$\Delta G = \Delta G^\circ + RT\ln Q$$
($Q$ = reaction quotient, the current ratio of products to reactants)

## ΔG, equilibrium constants and the Nernst equation
- At equilibrium, $\Delta G = 0$ and $Q = K$, so
  $$\boxed{\Delta G^\circ = -RT\ln K}\qquad\Longleftrightarrow\qquad K = e^{-\Delta G^\circ/RT}$$
  At 37 °C, each factor of 10 in $K$ corresponds to $RT\ln10\approx5.9$ kJ/mol.
- Binding: $K_d = e^{\Delta G_\text{bind}^\circ/RT}$. A binding energy of −50 kJ/mol gives $K_d$ in the nM range.
- **Ion transport:** moving one mole of ions with charge $z$ from outside to inside at membrane potential $V_m$:
  $$\Delta G = \underbrace{RT\ln\frac{c_\text{in}}{c_\text{out}}}_\text{chemical} + \underbrace{zFV_m}_\text{electrical}$$
  At equilibrium ($\Delta G = 0$), $V_m = E_\text{ion} = \frac{RT}{zF}\ln\frac{c_\text{out}}{c_\text{in}}$, which is the **Nernst equation** ([[Ch05 Redox and Electrochemistry]]).
- **Pumps** couple uphill ion transport to ATP hydrolysis. The total $\Delta G$ of the coupled process must be negative.
- **Redox:** $\Delta G = -nF\Delta E$ (the same structure: energy = charge × voltage).

## Entropy: why diffusion happens spontaneously
- **Entropy** $S$ measures the number of microscopic arrangements (microstates) $W$ compatible with a macroscopic state: $S = k\ln W$.
- **Second law:** in an isolated system, entropy never decreases. Systems evolve towards the most probable macrostate.
- **Diffusion:** a solute concentrated in one corner can be arranged in far fewer ways than one spread evenly. Mixing is overwhelmingly more probable, so it happens spontaneously, without any force pushing the molecules. Concentration gradients are "low entropy" states and therefore **stores of free energy**.
- Living systems maintain low-entropy states (gradients, ordered structures) by continuously consuming free energy (glucose, ATP) and exporting entropy (heat, CO₂). If the Na⁺/K⁺ pump stops, gradients run down towards equilibrium.
- The **hydrophobic effect** is entropy-driven (water ordering, [[Ch02 Chemical Bonds]]).

## In neuroscience #neuro
- **Channel noise:** single channels open and close stochastically (Boltzmann). In small structures (thin axons, spines), these random fluctuations can cause spontaneous spikes and limit how thin axons can be (≈ 0.1 µm).
- **Temperature dependence:** hypothermia slows neuronal kinetics (used for neuroprotection). Fever can trigger seizures in children (febrile seizures), partly through temperature-dependent channel properties.
- **Ligand binding and drug potency:** $K_d$, $\text{EC}_{50}$ and $\Delta G_\text{bind}$ are directly related ([[Bio03 Proteins and Enzymes]]).
- **Energy budget:** maintaining gradients costs the brain most of its ~20 W.

## Math links #math-link
- Boltzmann factor $e^{-E/kT}$ and Arrhenius rates → [[B2 Exponential Functions]]
- $\Delta G^\circ = -RT\ln K$ and Nernst: logarithms → [[A3 Logarithms]]
- Gating curves: sigmoid, slope at $V_{1/2}$ is $1/(4s)$ → [[B8 Curve Sketching]], [[B6 Differentiation Rules]]
- Partition function as a sum, probabilities normalise to 1 → [[A7 Sums Products and Factorials]]
- Counting microstates (binomial coefficients) for entropy → [[A6 Binomial Formulas and Theorem]]

## Connections
- Energy conservation (first law) → [[Ph01 Mechanics and Energy]]
- Diffusion and random walks → [[Ph07 Diffusion and Transport]]
- Nernst, GHK, redox → [[Ch05 Redox and Electrochemistry]]
- pH and $K_a$ → [[Ch04 Acids Bases and pH]]
- Channel gating → [[Bio02 Membranes and Transport]], [[Bio05 Neurons and Action Potentials]]
- Release probability → [[Bio06 Synapses and Neurotransmitters]]

## Key takeaways
- $kT\approx4.3$ pN·nm = 26.7 meV; $RT\approx2.6$ kJ/mol; $kT/e\approx26.7$ mV at 37 °C.
- Boltzmann: $p\propto e^{-E/kT}$. Two-state channels give sigmoid $P_\text{open}(V)$ with slope $26.7\,\text{mV}/z_g$.
- $\Delta G < 0$ means spontaneous; $\Delta G^\circ = -RT\ln K$; ion $\Delta G = RT\ln(c_i/c_o) + zFV$, which equals 0 at the Nernst potential.
- Entropy: diffusion happens because mixed states are overwhelmingly more probable. Gradients store free energy.
