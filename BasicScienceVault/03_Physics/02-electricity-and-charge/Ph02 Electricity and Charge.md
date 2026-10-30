---
aliases: [Electricity and Charge, Coulomb's Law, Current and Voltage, Elektrizität und Ladung]
tags: [physics, charge, current, voltage, coulomb, type/overview, neuro]
---
# Ph02 Electricity and Charge

> [[MOC-physics|↑ Physics MOC]] · [[Ph02 Electricity and Charge - Worksheet|✏️ Worksheet]] · [[Ph02 Electricity and Charge - Solutions|✅ Solutions]] · [[Mistakes - Physics|⚠️ Mistake log]]

## Why this matters
Neurons are electrical devices, but unlike copper wires their charge carriers are **ions**, not electrons. Charge, current and voltage are the three basic quantities of every electrophysiology recording, and confusing current with voltage is the most common conceptual error in neurophysiology.

## Charge
- Electric charge $Q$ is measured in **coulombs (C)**. There are positive and negative charges; like charges repel, opposite charges attract.
- **Quantisation:** every charge is an integer multiple of the **elementary charge**
  $$e = 1.602\times10^{-19}\,\text{C}$$
  An electron has $-e$, a proton $+e$, Na⁺ and K⁺ carry $+e$, Ca²⁺ carries $+2e$, Cl⁻ carries $-e$.
- **Conservation:** charge is never created or destroyed, only moved.
- **Per mole:** the **Faraday constant** is $F = N_A\cdot e\approx96\,485\,\text{C/mol}$, the charge of one mole of single charges ([[Ch01 Atomic Structure]]).

## Coulomb's law
The force between two point charges $q_1$ and $q_2$ at distance $r$:
$$F = \frac{1}{4\pi\varepsilon_0\varepsilon_r}\cdot\frac{q_1q_2}{r^2},\qquad \frac{1}{4\pi\varepsilon_0}\approx8.99\times10^9\,\frac{\text{N·m}^2}{\text{C}^2}$$
- $F > 0$ means repulsion (like charges); $F < 0$ means attraction.
- Inverse-square law: twice the distance gives a quarter of the force.
- $\varepsilon_r$ is the **relative permittivity (dielectric constant)** of the medium: vacuum 1, lipid membrane interior ≈ 2, protein interior ≈ 2–10, **water ≈ 80**. Water weakens electrostatic forces about 80-fold, which is why salts dissolve ([[Ch02 Chemical Bonds]], [[Ch03 Intermolecular Forces and Solubility]]).
- Potential energy of two charges: $U = \frac{1}{4\pi\varepsilon_0\varepsilon_r}\frac{q_1q_2}{r}$ (falls off as $1/r$).

**Worked example:** Na⁺ and Cl⁻ at $r = 0.5\,\text{nm}$.
- In vacuum: $U = 8.99\times10^9\cdot\frac{(1.6\times10^{-19})^2}{0.5\times10^{-9}}\approx4.6\times10^{-19}\,\text{J}\approx110\,kT$, so the ions stay bound.
- In water: divide by 80, giving $\approx5.8\times10^{-21}\,\text{J}\approx1.3\,kT$. Thermal motion separates them, so the salt dissociates.

## Current and voltage, and the difference between them
| | **Current $I$** | **Voltage $V$** (potential difference) |
|---|---|---|
| What it is | amount of charge flowing **through** a cross-section per time: $I = \frac{dQ}{dt}$ | energy per charge **between** two points: $V = \frac{\Delta E}{q}$ |
| Unit | ampere: A = C/s | volt: V = J/C |
| Measured | **in series**, through the path | **in parallel**, across two points |
| Water analogy | flow rate (litres per second) | pressure difference |
| In neurons | pA–nA (channel currents, synaptic currents) | mV (membrane potential, PSPs) |

- Voltage is the **cause** (driving force); current is the **effect**. Their relationship depends on the resistance (Ohm's law, [[Ph04 Circuits and Resistance]]).
- Voltage always refers to **two** points. "The membrane potential is −70 mV" means inside relative to outside.
- A voltage can exist without current (an open switch, or an ion at its equilibrium potential). A current needs both a driving force and a conducting path.

**Sign conventions in neurophysiology:**
- **Membrane potential** $V_m = V_\text{in} - V_\text{out}$.
- **Current** direction is defined as the flow of **positive** charge.
- **Outward current** (positive charge leaving the cell, e.g. K⁺ efflux, or Cl⁻ influx) is **positive** and hyperpolarises.
- **Inward current** (positive charge entering, e.g. Na⁺ or Ca²⁺ influx) is **negative** and depolarises.
- Cl⁻ influx is therefore an **outward** current, because negative charge entering is equivalent to positive charge leaving.

## Ions as charge carriers in neurons
| Ion | Charge | Gradient (in/out) | Typical role |
|---|---|---|---|
| **Na⁺** | +1 | low / high | depolarisation, AP upstroke |
| **K⁺** | +1 | high / low | resting potential, repolarisation |
| **Ca²⁺** | +2 | very low / high | transmitter release, plasticity, second messenger |
| **Cl⁻** | −1 | low / high (mature) | inhibition (GABA_A, GlyR) |

**Electrons vs. ions:** in metal wires and electrodes, electrons carry current. In tissue, ions do. At the electrode surface, chemistry (e.g. Ag/AgCl: AgCl + e⁻ ⇌ Ag + Cl⁻) converts between the two. Ions move much more slowly than electrons in metals, but there are so many of them that the currents are large enough.

**How many ions is a current?** 1 pA $= 10^{-12}\,\text{C/s}\div1.6\times10^{-19}\,\text{C}\approx6.2$ million monovalent ions per second.

## In neuroscience #neuro
- **Single-channel currents** are ~1–10 pA; **synaptic currents** are ~10–1000 pA; **whole-cell AP currents** reach nA ([[Meth03 Electrophysiology]]).
- **Voltage sensors** of channels are charged α-helices (S4) that move in the membrane's electric field ([[Bio02 Membranes and Transport]]).
- **Electrolyte disturbances** change excitability: hypokalaemia causes muscle weakness and arrhythmias; hypocalcaemia causes tetany (low Ca²⁺ screens fewer surface charges, so Na⁺ channels open more easily).

## Math links #math-link
- Coulomb's law: inverse-square law, scientific notation → [[A1 Exponent Rules]]
- Current as a derivative $I = dQ/dt$; charge as an integral $Q = \int I\,dt$ → [[B6 Differentiation Rules]], [[B7 Antiderivatives and Integration]]
- Forces as vectors (superposition of Coulomb forces) → [[D1 Vectors in 2D and 3D]]

## Connections
- Ions and their charges → [[Ch01 Atomic Structure]]
- Ionic bonds and solubility → [[Ch02 Chemical Bonds]], [[Ch03 Intermolecular Forces and Solubility]]
- Field and potential → [[Ph03 Electric Fields and Potential]]
- Circuits and Ohm's law → [[Ph04 Circuits and Resistance]]
- Electrochemistry → [[Ch05 Redox and Electrochemistry]]

## Key takeaways
- Charge is quantised in units of $e = 1.6\times10^{-19}$ C; per mole, $F\approx96\,500$ C.
- Coulomb: $F\propto\frac{q_1q_2}{\varepsilon_rr^2}$. Water ($\varepsilon_r = 80$) weakens it strongly.
- Current = charge per time **through** something; voltage = energy per charge **between** two points.
- In neurons, ions carry current. Inward (cation influx) is negative and depolarising; outward is positive.
