---
aliases: [Atomic Structure, Atombau, Ions and Charge]
tags: [chemistry, atom, ion, type/overview, neuro]
---
# Ch01 Atomic Structure

> [[MOC-chemistry|↑ Chemistry MOC]] · [[Ch01 Atomic Structure - Worksheet|✏️ Worksheet]] · [[Ch01 Atomic Structure - Solutions|✅ Solutions]] · [[Mistakes - Chemistry|⚠️ Mistake log]]

## Why this matters
Every electrical signal in the nervous system is carried by **ions** – atoms that have gained or lost electrons. Which ions exist, how strongly they hold their electrons and how big they are decides which channels let them through and in which direction they move. Neuroscience starts here.

## Building blocks of an atom
| Particle | Charge | Mass (u) | Where |
|---|---|---|---|
| Proton (p⁺) | +1 | ≈ 1 | nucleus |
| Neutron (n) | 0 | ≈ 1 | nucleus |
| Electron (e⁻) | −1 | ≈ 1/1836 | shells around the nucleus |

- **Atomic number $Z$** = number of protons, which defines the element (Na: $Z = 11$).
- **Mass number $A$** = protons + neutrons. **Isotopes** have the same $Z$ but a different $A$ (¹²C, ¹³C, ¹⁴C).
- A neutral atom has as many electrons as protons.

## Electron shells and valence electrons
Electrons occupy shells $n = 1, 2, 3, \dots$, and shell $n$ holds at most $2n^2$ electrons (2, 8, 18, …). For the light elements that matter in biology, a simplified rule is enough: **first shell 2, then 8 per shell** (the octet rule).

| Element | $Z$ | Configuration | Valence e⁻ | Typical ion |
|---|---|---|---|---|
| H | 1 | 1 | 1 | H⁺ |
| C | 6 | 2, 4 | 4 | – (forms 4 bonds) |
| N | 7 | 2, 5 | 5 | – (3 bonds; NH₄⁺) |
| O | 8 | 2, 6 | 6 | – (2 bonds) |
| Na | 11 | 2, 8, 1 | 1 | **Na⁺** |
| Mg | 12 | 2, 8, 2 | 2 | **Mg²⁺** |
| Cl | 17 | 2, 8, 7 | 7 | **Cl⁻** |
| K | 19 | 2, 8, 8, 1 | 1 | **K⁺** |
| Ca | 20 | 2, 8, 8, 2 | 2 | **Ca²⁺** |

**Valence electrons** are the electrons in the outermost shell. They decide the chemistry: atoms gain, lose or share electrons until they reach a noble-gas configuration (full outer shell).

The **periodic table** groups elements with the same number of valence electrons:
- Group 1, the alkali metals (Li, Na, K), lose 1 e⁻ and become **+1**.
- Group 2, the alkaline earth metals (Mg, Ca), lose 2 e⁻ and become **+2**.
- Group 17, the halogens (F, Cl), gain 1 e⁻ and become **−1**.

## Electronegativity (EN)
Electronegativity is the tendency of an atom to pull shared electrons towards itself (Pauling scale). It rises **to the right** of the periodic table and **upwards**.

| Atom | K | Na | H | C | S | N | Cl | O | F |
|---|---|---|---|---|---|---|---|---|---|
| EN | 0.82 | 0.93 | 2.20 | 2.55 | 2.58 | 3.04 | 3.16 | 3.44 | 3.98 |

The EN difference $\Delta EN$ decides the bond type ([[Ch02 Chemical Bonds]]):
- $< 0.4$: nonpolar covalent
- $0.4$–$1.7$: polar covalent
- $> 1.7$: mostly ionic

## Ions and charge
- **Cation:** has lost electrons and is positively charged (Na⁺, K⁺, Ca²⁺, Mg²⁺, H⁺).
- **Anion:** has gained electrons and is negatively charged (Cl⁻, HCO₃⁻, phosphate, and negatively charged proteins).
- The **charge number $z$** (+1, +2, −1) appears in the [[Ch05 Redox and Electrochemistry|Nernst equation]].

**Ionic radius:** a cation is smaller than its atom (it lost a whole shell or electrons); an anion is larger. In water, ions are surrounded by a **hydration shell** ([[Ch03 Intermolecular Forces and Solubility]]). Na⁺ is *smaller* than K⁺ as a bare ion but holds its water more tightly. This difference is what potassium channels exploit for selectivity.

**Charge is quantised:** one ion with charge $z$ carries $z\cdot e$, with $e = 1.602\times10^{-19}\,\text{C}$. One mole of single charges carries the **Faraday constant** $F = N_A\cdot e \approx 96\,485\,\text{C/mol}$.

## In neuroscience #neuro
- **The four key ions:** K⁺ (high inside the cell), Na⁺ and Cl⁻ (high outside), Ca²⁺ (very high outside, about $10^4$ times lower inside). Their unequal distribution across the membrane produces the resting and action potentials ([[Bio05 Neurons and Action Potentials]]).

  | Ion | inside (mM) | outside (mM) |
  |---|---|---|
  | K⁺ | ~140 | ~5 |
  | Na⁺ | ~10–15 | ~145 |
  | Cl⁻ | ~5–10 | ~110 |
  | Ca²⁺ | ~0.0001 | ~1–2 |

- **Divalent ions matter differently:** Mg²⁺ blocks the NMDA receptor pore at rest ([[Bio06 Synapses and Neurotransmitters]]). Ca²⁺ is a second messenger: it triggers transmitter release and plasticity.
- **Selectivity filter of K⁺ channels:** carbonyl oxygens mimic the water shell of K⁺ exactly but fit Na⁺ badly. As a result, K⁺ passes about 1000 times more easily, even though Na⁺ is smaller.
- **Isotopes as tools:** radioactive ¹¹C, ¹⁸F and ¹⁵O are used in PET ([[Meth04 In Vivo Imaging]]); ¹³C and ¹H are used in NMR and MRI.
- **Lithium (Li⁺)**, the lightest alkali metal, is a mood stabiliser. Its similarity to Na⁺ and Mg²⁺ explains some of its targets.

## Math links #math-link
- Charges, concentrations and constants in scientific notation → [[A1 Exponent Rules]]
- Ratios of concentrations ($10^4$ for Ca²⁺) → [[A3 Logarithms]]
- Charge number $z$ in $E = \frac{RT}{zF}\ln\frac{c_o}{c_i}$ → [[A8 Solving Equations]]

## Connections
- How atoms bond → [[Ch02 Chemical Bonds]]
- Ions in water → [[Ch03 Intermolecular Forces and Solubility]]
- Ion gradients and potentials → [[Ch05 Redox and Electrochemistry]]
- Ion channels → [[Bio02 Membranes and Transport]]

## Key takeaways
- The number of valence electrons sets the typical ion charge: group 1 gives +1, group 2 gives +2, halogens give −1.
- Electronegativity grows to the right and upwards, and $\Delta EN$ sets the bond type.
- Inside the neuron, K⁺ is high; outside, Na⁺, Cl⁻ and Ca²⁺ are high. These gradients are the battery of the brain.
