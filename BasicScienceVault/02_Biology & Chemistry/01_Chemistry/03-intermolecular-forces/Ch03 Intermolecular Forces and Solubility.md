---
aliases: [Intermolecular Forces, Solubility, Water, Hydrophobic, Amphiphilic]
tags: [chemistry, water, solubility, type/overview, neuro]
---
# Ch03 Intermolecular Forces and Solubility

> [[MOC-chemistry|↑ Chemistry MOC]] · [[Ch03 Intermolecular Forces and Solubility - Worksheet|✏️ Worksheet]] · [[Ch03 Intermolecular Forces and Solubility - Solutions|✅ Solutions]] · [[Mistakes - Chemistry|⚠️ Mistake log]]

## Why this matters
The brain is about 75–80 % water. Whether a molecule dissolves in water or in lipid decides whether it stays in the blood or crosses the blood–brain barrier, whether it diffuses through membranes or needs a transporter, and why membranes form spontaneously at all.

## Water as a polar solvent
- H₂O is **bent** (≈ 104.5°) and has strongly polar O–H bonds, so it carries a permanent dipole: O is $\delta^-$ and the H atoms are $\delta^+$.
- Each molecule can form up to **4 hydrogen bonds**. This gives water its high boiling point, high heat capacity and surface tension.
- Its **high dielectric constant** ($\varepsilon\approx80$) shields charges, which is why salts dissociate into free ions.
- Rule of thumb: **"like dissolves like"**. Polar and charged substances dissolve in water; nonpolar substances dissolve in nonpolar solvents (oil, membrane interior).

## Hydration shells
Ions in water are surrounded by oriented water molecules.
- Around **cations** (Na⁺, K⁺), the water molecules point their O atoms ($\delta^-$) towards the ion.
- Around **anions** (Cl⁻), they point their H atoms ($\delta^+$) towards the ion.
- **Smaller ions with higher charge** bind their water more tightly: Mg²⁺ > Ca²⁺ > Li⁺ > Na⁺ > K⁺. A hydrated Na⁺ is effectively *larger* than a hydrated K⁺.
- To pass through a narrow channel pore, an ion must (partially) **shed** its hydration shell. The energetic cost of this is the key to channel **selectivity** ([[Ch01 Atomic Structure]], [[Bio02 Membranes and Transport]]).

## Hydrophilic, hydrophobic, amphiphilic
| Type | Features | Examples |
|---|---|---|
| **Hydrophilic** ("water-loving") | charged or polar groups: –OH, –COO⁻, –NH₃⁺, phosphate | glucose, amino acids, ions, ATP, glutamate |
| **Hydrophobic** ("water-fearing") | mainly C–H, nonpolar | fatty acid tails, cholesterol ring system, O₂, steroid hormones, many anaesthetics |
| **Amphiphilic** | polar head **and** nonpolar tail | phospholipids, detergents (SDS), bile acids |

**Self-assembly of amphiphiles:** in water, amphiphilic molecules arrange themselves so that the tails are hidden from water (the hydrophobic effect, [[Ch02 Chemical Bonds]]):
- **Micelles** (single-tailed molecules such as detergents) are spheres with the tails inside.
- **Bilayers** (double-tailed phospholipids) form two leaflets with the tails facing each other, which close into **vesicles/liposomes**. This is the basis of every cell membrane and every synaptic vesicle.

**Partition coefficient** $P = \frac{[\text{X}]_\text{octanol}}{[\text{X}]_\text{water}}$, often given as $\log P$. A higher $\log P$ means the substance is more lipophilic and crosses membranes more easily, though if it is *too* lipophilic it sticks in membranes and binds plasma proteins.

## In neuroscience #neuro
- **Blood–brain barrier (BBB):** endothelial cells joined by tight junctions block passage between cells. Molecules must go *through* the cells.
  - Small lipophilic molecules (O₂, CO₂, ethanol, nicotine, caffeine, many anaesthetics, diazepam) diffuse through the membranes.
  - Polar molecules need **transporters**: glucose uses GLUT1 and amino acids use LAT1.
  - Rules of thumb for CNS drugs: molecular weight under about 400–500 Da, moderate $\log P$ (about 1–3), few hydrogen-bond donors.
- **Heroin vs. morphine:** heroin is diacetylmorphine. The two acetyl groups mask polar –OH groups, so it crosses the BBB faster and has a stronger "rush". In the brain it is converted back to morphine.
- **L-DOPA vs. dopamine:** dopamine itself does not cross the BBB. Its precursor L-DOPA is carried by LAT1 and converted into dopamine in the brain, which is the basis of Parkinson's therapy.
- **Detergents in the lab:** SDS denatures proteins and gives them a uniform negative charge for Western blots ([[Meth05 Molecular Biology Tools]]). Triton X-100 permeabilises membranes so antibodies can enter cells for immunofluorescence.
- **Myelin** is very lipid-rich (≈ 70–80 % lipid by dry weight). The many hydrophobic layers make it an excellent electrical insulator ([[Bio05 Neurons and Action Potentials]]).
- **General anaesthetics:** the old Meyer–Overton rule says potency correlates with lipid solubility. Today we know they act on specific proteins (GABA_A receptors, K2P channels), but lipophilicity is still needed to reach them.

## Math links #math-link
- $\log P$ is a decadic logarithm: $\log P = 2$ means 100 times more in octanol → [[A3 Logarithms]]
- Vector sum of bond dipoles → [[D1 Vectors in 2D and 3D]]
- Diffusion through membranes ∝ partition coefficient (Fick's law) → [[Ch06 Solutions and Concentration]]

## Connections
- Bond types, hydrophobic effect → [[Ch02 Chemical Bonds]]
- Lipids → [[Ch08 Biomolecules]]
- Membrane structure and transport → [[Bio02 Membranes and Transport]]

## Key takeaways
- Water is a polar, hydrogen-bonding solvent with high $\varepsilon$. "Like dissolves like."
- Ions carry hydration shells; shedding them is what makes channels selective.
- Amphiphiles self-assemble into micelles and bilayers, driven by the hydrophobic effect.
- Lipophilic and small molecules cross the BBB; polar ones need transporters.
