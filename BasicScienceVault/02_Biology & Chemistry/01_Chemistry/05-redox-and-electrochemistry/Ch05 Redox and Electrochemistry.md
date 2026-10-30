---
aliases: [Electrochemistry, Redox, Nernst Equation, GHK Equation, Electrochemical Gradient, Elektrochemie]
tags: [chemistry, electrochemistry, nernst, redox, type/overview, neuro]
---
# Ch05 Redox and Electrochemistry

> [[MOC-chemistry|↑ Chemistry MOC]] · [[Ch05 Redox and Electrochemistry - Worksheet|✏️ Worksheet]] · [[Ch05 Redox and Electrochemistry - Solutions|✅ Solutions]] · [[Mistakes - Chemistry|⚠️ Mistake log]]

## Why this matters
This is **the** central chemistry topic for neuroscience. Ion gradients and the voltages they produce explain the resting potential, the action potential, synaptic excitation and inhibition. Redox chemistry explains where the energy comes from: about 20 % of the body's oxygen is consumed by an organ that weighs about 2 % of body mass.

## Three forces acting on an ion
1. **Concentration (chemical) gradient:** ions diffuse from high to low concentration ([[Ch06 Solutions and Concentration]]).
2. **Electrical potential:** cations are pulled towards negative potential and anions towards positive potential.
3. The **electrochemical gradient** is the sum of both, and it decides the net direction of flow.

The free energy for moving one mole of an ion with charge $z$ **into** the cell at membrane potential $V_m$ (inside relative to outside) is
$$\Delta G = RT\ln\frac{c_\text{in}}{c_\text{out}} + zFV_m$$
Ions flow spontaneously in the direction that makes $\Delta G < 0$.

## The Nernst equation
At **equilibrium**, the two forces balance exactly ($\Delta G = 0$). Solving for the voltage gives the **equilibrium (reversal) potential** of that ion:
$$\boxed{E_\text{ion} = \frac{RT}{zF}\ln\frac{c_\text{out}}{c_\text{in}} \;\approx\; \frac{61.5\,\text{mV}}{z}\log_{10}\frac{c_\text{out}}{c_\text{in}}\quad(37\,°\text{C})}$$
($R = 8.314\,\text{J/(mol·K)}$, $T = 310\,\text{K}$, $F = 96\,485\,\text{C/mol}$, so $RT/F\approx26.7\,\text{mV}$, and $\times\ln10$ gives 61.5 mV. At room temperature the factor is 58 mV.)

| Ion | $c_\text{in}$ (mM) | $c_\text{out}$ (mM) | $E_\text{ion}$ |
|---|---|---|---|
| K⁺ | 140 | 5 | ≈ −89 mV |
| Na⁺ | 15 | 145 | ≈ +61 mV |
| Cl⁻ ($z = -1$) | 10 | 110 | ≈ −64 mV |
| Ca²⁺ ($z = +2$) | 0.0001 | 1.5 | ≈ +128 mV |

**Interpretation:** $E_\text{K} = -89\,\text{mV}$ means that at −89 mV the electrical pull inward exactly balances the diffusion outward, and there is no net K⁺ flux.

**Driving force and current:** the current through channels for one ion is
$$I_\text{ion} = g_\text{ion}\,(V_m - E_\text{ion})$$
- $V_m > E$: the ion flows so that $V_m$ moves towards $E$.
- By convention, a positive current is an **outward** flow of positive charge.
- At rest ($V_m\approx-70\,\text{mV}$), Na⁺ has a driving force of −130 mV (strongly inward) and K⁺ has +20 mV (weakly outward).

## The Goldman–Hodgkin–Katz (GHK) equation
The membrane is permeable to several ions at once. The **steady-state membrane potential** is weighted by each ion's permeability $P$:
$$V_m = 61.5\,\text{mV}\cdot\log_{10}\frac{P_\text{K}[\text{K}^+]_o + P_\text{Na}[\text{Na}^+]_o + P_\text{Cl}[\text{Cl}^-]_i}{P_\text{K}[\text{K}^+]_i + P_\text{Na}[\text{Na}^+]_i + P_\text{Cl}[\text{Cl}^-]_o}$$
Note that **Cl⁻ is flipped** (inside on top) because of its negative charge.
- **At rest:** $P_\text{K}:P_\text{Na}:P_\text{Cl}\approx1:0.04:0.45$. K⁺ dominates, so $V_m\approx-65$ to $-70$ mV, close to $E_\text{K}$.
- **Action potential peak:** $P_\text{Na}$ rises about 500-fold (≈ 1 : 20 : 0.45), so $V_m$ approaches $E_\text{Na}$ (about +40 mV).
- If one ion dominates, GHK reduces to Nernst.
- The steady state relies on the Na⁺/K⁺-ATPase continuously restoring the gradients ([[Bio02 Membranes and Transport]]).

## Redox reactions
**Oxidation = loss of electrons; reduction = gain of electrons** ("OIL RIG"). The two always occur together.
- Redox potential $E^{\circ\prime}$ (V): a more positive value means the substance pulls electrons more strongly.
- Free energy: $\Delta G = -nF\Delta E$ ($n$ = number of electrons transferred).

### ATP production and mitochondrial electron transport
1. **Glycolysis** (cytosol): glucose → 2 pyruvate, producing **2 ATP** and 2 NADH.
2. **Citric acid (TCA) cycle** (matrix): this oxidises acetyl-CoA to CO₂ and produces NADH and FADH₂.
3. **Electron transport chain** (inner mitochondrial membrane):
   NADH → complex I → ubiquinone (Q) → complex III → cytochrome c → complex IV → **O₂** (the final electron acceptor, reduced to H₂O).
   - $E^{\circ\prime}$: NAD⁺/NADH = −0.32 V, O₂/H₂O = +0.82 V, so $\Delta E = 1.14\,\text{V}$ and $\Delta G = -2\cdot96\,485\cdot1.14\approx-220\,\text{kJ/mol}$.
   - Complexes I, III and IV pump H⁺ out of the matrix, creating the **proton-motive force** (≈ −150 to −180 mV across the membrane plus a pH difference).
4. **ATP synthase** (complex V): H⁺ flows back down its electrochemical gradient and drives the rotary synthesis of ATP (**chemiosmosis**, Mitchell).
5. Total yield: **≈ 30–32 ATP per glucose** with O₂, compared with only 2 without it.

## In neuroscience #neuro
- **Resting potential:** set mainly by K⁺ leak channels, so it lies close to $E_\text{K}$. Raising extracellular K⁺ (e.g. in ischaemia or after intense activity) depolarises neurons; astrocytes buffer K⁺.
- **Excitation vs. inhibition by reversal potential:**
  - glutamate receptors (AMPA): $E_\text{rev}\approx0\,\text{mV}$, so they depolarise
  - GABA_A (Cl⁻): $E_\text{Cl}\approx-65$ to $-75$ mV, so they inhibit
  - In **immature neurons**, intracellular Cl⁻ is high (because of NKCC1), $E_\text{Cl}$ is more positive, and GABA can be **depolarising**. The switch to KCC2 makes GABA inhibitory.
- **Energy budget:** the Na⁺/K⁺-ATPase that restores gradients after action potentials and synaptic currents consumes a large share of the brain's ATP. Neurons and astrocytes rely heavily on oxidative phosphorylation, which is why the brain is so sensitive to hypoxia (unconsciousness within seconds, damage within minutes).
- **Mitochondria and disease:** the Complex I inhibitors MPP⁺ (from the street-drug contaminant MPTP) and rotenone selectively kill dopaminergic neurons and cause **parkinsonism**. Reactive oxygen species (ROS) from leaking electrons damage proteins, lipids and DNA (oxidative stress).
- **Measuring metabolism:** FDG-PET maps glucose uptake ([[Meth04 In Vivo Imaging]]), and the BOLD signal arises from the mismatch between O₂ consumption and blood flow.

## Math links #math-link
- Differential equations (steady state, time constant, stability, Euler steps) → [[B10 Differential Equations]]
- Nernst and GHK are **logarithms** of concentration ratios → [[A3 Logarithms]]
- GHK as a weighted ratio; conductance-weighted average $V = \frac{\sum g_iE_i}{\sum g_i}$ → [[A4 Factoring and Simplifying]], [[A5 Fractions]]
- $I = g(V - E)$ is a linear function; the membrane equation $C\frac{dV}{dt} = -\sum g_i(V - E_i)$ → [[B6 Differentiation Rules]], [[B2 Exponential Functions]]
- Unit conversions (mV, nA, nS) → [[A1 Exponent Rules]]

## Connections
- Ions, charge $z$, Faraday constant → [[Ch01 Atomic Structure]]
- Concentrations, diffusion → [[Ch06 Solutions and Concentration]]
- Pumps and channels → [[Bio02 Membranes and Transport]]
- Action potential → [[Bio05 Neurons and Action Potentials]]
- Synaptic reversal potentials → [[Bio06 Synapses and Neurotransmitters]]
- Mitochondria → [[Bio01 Cell Biology]]

## Key takeaways
- Nernst: $E = \frac{61.5}{z}\log\frac{c_o}{c_i}$ mV, where every factor of 10 gives 61.5 mV / $z$.
- Current $= g(V - E)$: ions always push $V$ towards their own $E$.
- GHK: the ion with the highest permeability sets $V_m$. K⁺ dominates at rest; Na⁺ dominates at the AP peak.
- Redox: electrons flow from NADH to O₂; the energy is stored as an H⁺ gradient, and ATP synthase converts it into ATP.
