---
aliases: [Chemical Bonds, Chemische Bindungen]
tags: [chemistry, bond, type/overview, neuro]
---
# Ch02 Chemical Bonds

> [[MOC-chemistry|↑ Chemistry MOC]] · [[Ch02 Chemical Bonds - Worksheet|✏️ Worksheet]] · [[Ch02 Chemical Bonds - Solutions|✅ Solutions]] · [[Mistakes - Chemistry|⚠️ Mistake log]]

## Why this matters
Strong bonds hold molecules together (a neurotransmitter, a protein backbone). Weak interactions decide how molecules **recognise** each other: a ligand in its receptor, base pairing in DNA, a folded ion channel. Biology runs on weak, reversible interactions that thermal motion can break and re-form.

## Overview by strength
| Interaction | Typical energy (kJ/mol) | Example in the brain |
|---|---|---|
| Covalent bond | ~150–1000 (C–C ≈ 350) | backbone of every biomolecule |
| Ionic bond / salt bridge (in water) | ~5–20 | Lys⁺–Asp⁻ in proteins, ligand–receptor |
| Coordinate (dative) bond | ~50–300 | Zn²⁺ in enzymes, Mg²⁺–ATP |
| Hydrogen bond | ~5–30 | DNA base pairs, α-helices |
| Hydrophobic effect | entropic, a few kJ/mol per CH₂ | membrane bilayer, protein cores |
| Van der Waals | ~0.5–4 | close packing of lipid tails |

For comparison, thermal energy at body temperature is $RT\approx2.6\,\text{kJ/mol}$. Weak interactions are only a few multiples of $RT$, so they can break and form constantly.

## Covalent bonds
Atoms **share** electron pairs to complete their octets.
- **Single bond** (σ): C–C, C–H. Free rotation is possible.
- **Double bond** (σ + π): C=O, C=C. It is shorter and stronger, and **rotation is blocked**, which gives cis/trans isomers.
- **Triple bond**: N≡N, C≡N (cyanide). It is the shortest and strongest.
- **Nonpolar** ($\Delta EN < 0.4$): C–C, C–H. Electrons are shared equally.
- **Polar** ($0.4 < \Delta EN < 1.7$): O–H, N–H, C=O. They create partial charges $\delta^+$ and $\delta^-$ and a **dipole**.

Whether a molecule is polar depends on both the bond polarity and the **geometry**. CO₂ is linear, so its dipoles cancel and the molecule is nonpolar. H₂O is bent (≈ 104.5°), so it is polar ([[Ch03 Intermolecular Forces and Solubility]]).

**Resonance / delocalisation:** in the peptide bond, the C–N bond has partial double-bond character. It is therefore planar and rigid, which strongly constrains protein folding ([[Ch08 Biomolecules]]).

## Ionic bonds
One atom transfers electrons to another, and the resulting cation and anion attract each other electrostatically (Coulomb's law):
$$F\propto\frac{q_1q_2}{\varepsilon\,r^2}$$
- In a **crystal** (table salt), the Na⁺/Cl⁻ attraction is very strong.
- In **water**, the dielectric constant $\varepsilon\approx80$ weakens the attraction about 80-fold. The ions dissolve and move independently. This is why the extracellular fluid is a solution of free Na⁺ and Cl⁻ ions.
- Inside proteins (low $\varepsilon$), oppositely charged side chains form **salt bridges**.

## Hydrogen bonds
A hydrogen bond is an attraction between an H atom bound to an electronegative atom (N–H, O–H; the **donor**) and a lone pair on another N or O (the **acceptor**). It is roughly 10–20 times weaker than a covalent bond and works best when the three atoms are in a straight line.
- **DNA:** A–T has 2 hydrogen bonds, G–C has 3. GC-rich DNA is therefore more stable and melts at a higher temperature (relevant for PCR primer design → [[Meth05 Molecular Biology Tools]]).
- **Proteins:** α-helices and β-sheets are held together by backbone C=O···H–N hydrogen bonds ([[Bio03 Proteins and Enzymes]]).
- **Water:** each water molecule forms up to 4 hydrogen bonds, which explains its high boiling point and its role as a solvent.

## Van der Waals and hydrophobic interactions
- **Van der Waals forces:** temporary fluctuating dipoles induce dipoles in neighbouring atoms. They are very weak individually but add up over large contact areas. They only act at very short distances (they scale with $r^{-6}$).
- **Hydrophobic effect:** nonpolar molecules in water force the water around them into ordered "cages", which lowers entropy. When the nonpolar parts **cluster together**, they release this water and entropy increases. This is not an attraction between the nonpolar molecules themselves but a consequence of how water behaves. It drives **membrane formation**, **protein folding** (hydrophobic core) and the burial of the transmembrane helices of ion channels in the lipid bilayer.

## Coordinate (dative) bonds
In a coordinate bond, **both** electrons of the shared pair come from the same atom, the ligand (e.g. O, N or S with a lone pair). The partner is usually a **metal ion**, which accepts the pair.
- **Zn²⁺** in metalloproteases (e.g. matrix metalloproteinases) and in zinc-finger transcription factors (coordinated by Cys/His).
- **Mg²⁺–ATP:** the real substrate of most ATPases, including the Na⁺/K⁺-ATPase, is the Mg·ATP complex.
- **Fe²⁺ in haemoglobin** binds O₂. The magnetic difference between oxy- and deoxyhaemoglobin is the basis of the BOLD fMRI signal ([[Meth04 In Vivo Imaging]]).
- **Cu²⁺/Cu⁺** in cytochrome c oxidase ([[Ch05 Redox and Electrochemistry]]) and in dopamine β-hydroxylase.
- **Ca²⁺** is coordinated by oxygens in calmodulin's EF-hands and in synaptotagmin's C2 domains, the Ca²⁺ sensor for transmitter release.
- **Gadolinium (Gd³⁺)** in MRI contrast agents is bound by chelators because free Gd³⁺ is toxic.

## In neuroscience #neuro
- **Ligand–receptor binding** combines several weak interactions: hydrogen bonds, salt bridges, hydrophobic contacts and π-interactions. Example: in the nicotinic receptor, the positively charged nitrogen of ACh sits in a "box" of aromatic rings (a cation–π interaction). The combination of several weak bonds gives both **specificity** and **reversibility**: the transmitter can unbind within milliseconds.
- **Covalent drugs/toxins** bind irreversibly. Organophosphates (sarin, some pesticides) covalently modify acetylcholinesterase, so ACh accumulates. Aspirin acetylates COX.
- **Disulfide bonds** (covalent S–S between cysteines) stabilise extracellular domains of receptors and the Cys-loop of nicotinic and GABA_A receptors ([[Ch07 Organic Chemistry Essentials]]).

## Math links #math-link
- Coulomb's law $\propto 1/r^2$, van der Waals $\propto 1/r^6$: power laws → [[A1 Exponent Rules]]
- Bond energy vs. $RT$, and Boltzmann factor $e^{-E/RT}$ → [[B2 Exponential Functions]]
- Geometry of bond angles and dipole vectors → [[D2 Dot and Cross Product]]

## Connections
- Electronegativity, ions → [[Ch01 Atomic Structure]]
- Water, hydrophobic effect, membranes → [[Ch03 Intermolecular Forces and Solubility]]
- Folding → [[Bio03 Proteins and Enzymes]]; DNA → [[Bio04 Nucleic Acids and Gene Expression]]

## Key takeaways
- The strength order is covalent > ionic (in water much weaker) ≈ hydrogen bonds > van der Waals.
- Biology relies on many weak, reversible bonds for specific recognition.
- The hydrophobic effect is driven by the entropy of water, not by an attraction between oily molecules.
