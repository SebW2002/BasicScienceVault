---
aliases: [Electric Fields and Potential, Electric Field, Membrane Potential, Equilibrium Potential, Elektrisches Feld]
tags: [physics, electric-field, potential, membrane-potential, type/overview, neuro]
---
# Ph03 Electric Fields and Potential

> [[MOC-physics|↑ Physics MOC]] · [[Ph03 Electric Fields and Potential - Worksheet|✏️ Worksheet]] · [[Ph03 Electric Fields and Potential - Solutions|✅ Solutions]] · [[Mistakes - Physics|⚠️ Mistake log]]

## Why this matters
The membrane potential is the central variable of neurophysiology. It is a **potential difference** across a 5 nm thin lipid bilayer, and it creates an enormous electric field that moves the voltage sensors of ion channels. The equilibrium potential of an ion is the voltage at which electrical and diffusive forces cancel.

## Electric field
The **electric field** $\vec E$ is the force per unit charge that a test charge $q$ would feel:
$$\vec E = \frac{\vec F}{q}\qquad[\text{N/C} = \text{V/m}]$$
- Field of a point charge: $E = \frac{1}{4\pi\varepsilon_0\varepsilon_r}\frac{Q}{r^2}$, pointing radially away from positive charges.
- **Uniform field** between two parallel charged plates (a capacitor; the membrane):
  $$E = \frac{V}{d}$$
- **Field lines** run from + to −. Their density shows field strength. Fields from several charges add as vectors (superposition).

## Electric potential and potential difference
The **potential** $\varphi$ (or $V$) at a point is the potential energy per charge there. Only **differences** are measurable:
$$\Delta V = V_B - V_A = \frac{W_{A\to B}}{q},\qquad E = -\frac{dV}{dx}$$
- The field points "downhill" from high to low potential. Positive charges move with the field (towards lower potential); negative charges move against it.
- **Energy to move a charge** through a potential difference: $W = q\Delta V$. For one elementary charge, 1 V corresponds to 1 eV $= 1.6\times10^{-19}$ J. For one mole of $z$-valent ions, $W = zF\Delta V$.
- **Equipotential surfaces** are perpendicular to field lines. No work is done moving along them.

## The membrane potential
$$V_m = V_\text{inside} - V_\text{outside}\approx-70\,\text{mV at rest}$$
- The lipid bilayer is a thin **insulator** (≈ 5 nm) between two conducting salt solutions, i.e. a capacitor ([[Ph05 Capacitance and RC Circuits]]).
- **The field across the membrane is huge:** $E = \frac{0.07\,\text{V}}{5\times10^{-9}\,\text{m}} = 1.4\times10^7\,\text{V/m}$ = 14 MV/m. For comparison, air breaks down (lightning) at about 3 MV/m. This field acts directly on charged parts of membrane proteins, such as the **S4 voltage sensors** of channels, which move a few elementary charges across part of the field when the membrane depolarises.
- **Where is the excess charge?** Only in a very thin layer right at the two membrane surfaces (on the order of 1 nm, the Debye length in physiological saline). The bulk cytoplasm and extracellular fluid are electrically neutral: the number of positive and negative charges is equal to better than 1 part in 10⁵ ([[Ch01 Atomic Structure]]).
- **Energy scale:** moving one Na⁺ across 70 mV costs or releases $e\cdot0.07\,\text{V} = 1.1\times10^{-20}$ J ≈ $2.6\,kT$. Per mole that is $F\cdot0.07\,\text{V}\approx6.8$ kJ/mol, the same order as the chemical energy stored in the concentration gradients.

## Equilibrium potential: when diffusion and electrical forces balance
Take a membrane permeable only to K⁺, with $[\text{K}^+]_\text{in} > [\text{K}^+]_\text{out}$.
1. K⁺ diffuses out, down its concentration gradient.
2. Each K⁺ that leaves carries positive charge, so the inside becomes negative.
3. The resulting electric field pulls K⁺ back in.
4. At a specific voltage, the electrical pull equals the diffusive push. There is no **net** flux, although ions still cross in both directions.

This voltage is the **equilibrium (Nernst) potential**. Setting the electrical energy equal to the concentration ("chemical") energy per mole gives
$$zFE_\text{ion} = RT\ln\frac{c_\text{out}}{c_\text{in}}\quad\Longrightarrow\quad E_\text{ion} = \frac{RT}{zF}\ln\frac{c_\text{out}}{c_\text{in}}$$
See [[Ch05 Redox and Electrochemistry]] for numbers and [[Ph08 Thermodynamics and Statistics]] for the derivation from $\Delta G$.

**Key insight:** only a **tiny** number of ions has to cross to build up this voltage, because the membrane capacitance is small. The concentrations barely change.

## In neuroscience #neuro
- **Extracellular potentials and EEG:** currents flowing through the extracellular space produce small potential differences (µV–mV) between points in the tissue or on the scalp. Synchronous pyramidal cells act like **current dipoles**, and their fields superimpose ([[Meth03 Electrophysiology]]).
- **Brain stimulation with fields:**
  - Transcranial direct/alternating current stimulation (tDCS/tACS) creates weak fields (≈ 0.2–1 V/m) in the cortex, which shift membrane potentials by fractions of a mV.
  - Deep brain stimulation and TMS ([[Ph06 Magnetism and Induction]]) create much stronger fields that can trigger APs.
- **Ephaptic coupling:** endogenous fields from strong synchronous activity (e.g. hippocampal sharp-wave ripples) can feed back on neighbouring neurons.
- **Surface charge screening:** extracellular Ca²⁺ screens negative charges on the membrane surface. Low Ca²⁺ changes the field the voltage sensors experience, making Na⁺ channels open more easily, which is why hypocalcaemia causes tetany.

## Math links #math-link
- Partial derivatives, gradients, Jacobians, multiple integrals → [[B11 Multivariable Calculus]]
- Field as the negative derivative of potential, $E = -dV/dx$; potential as an integral of the field → [[B6 Differentiation Rules]], [[B7 Antiderivatives and Integration]]
- Superposition of field vectors → [[D1 Vectors in 2D and 3D]]
- Nernst equation: logarithm of a ratio → [[A3 Logarithms]]
- $E = V/d$ with tiny $d$: scientific notation → [[A1 Exponent Rules]]

## Connections
- Charges, Coulomb's law → [[Ph02 Electricity and Charge]]
- The membrane as a capacitor → [[Ph05 Capacitance and RC Circuits]]
- Electrodiffusion → [[Ph07 Diffusion and Transport]]
- ΔG and the Nernst equation → [[Ph08 Thermodynamics and Statistics]], [[Ch05 Redox and Electrochemistry]]
- Resting potential and voltage-gated channels → [[Bio05 Neurons and Action Potentials]], [[Bio02 Membranes and Transport]]

## Key takeaways
- Field = force per charge (V/m). Potential = energy per charge. Only differences are measurable.
- $V_m = V_\text{in} - V_\text{out}\approx-70$ mV across 5 nm gives a field of about 14 MV/m, strong enough to move voltage sensors.
- Excess charge sits only at the membrane surfaces; the bulk solutions stay neutral.
- Equilibrium potential: $zFE = RT\ln(c_o/c_i)$, where electrical and diffusive forces balance and there is no net flux.
