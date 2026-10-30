---
aliases: [Organic Chemistry Essentials, Functional Groups, Stereochemistry, Chirality, Organische Chemie]
tags: [chemistry, organic, functional-group, chirality, type/overview, neuro]
---
# Ch07 Organic Chemistry Essentials

> [[MOC-chemistry|↑ Chemistry MOC]] · [[Ch07 Organic Chemistry Essentials - Worksheet|✏️ Worksheet]] · [[Ch07 Organic Chemistry Essentials - Solutions|✅ Solutions]] · [[Mistakes - Chemistry|⚠️ Mistake log]]

## Why this matters
Neurotransmitters, drugs and toxins are small organic molecules. A handful of **functional groups** decides their charge, solubility and how they bind to receptors. **Stereochemistry** decides whether a molecule fits a receptor at all: mirror-image versions of the same drug can have completely different effects.

## Carbon skeletons
- Carbon forms **4 bonds**. Chains, branches and rings are possible.
- **Aliphatic** molecules are chains; **aromatic** molecules contain a benzene-type ring (planar, delocalised π electrons, stable).
- In skeletal formulas, every corner or line end is a C atom, and the H atoms attached to C are not drawn.

## The functional groups to know
| Group | Structure | Properties at pH 7.4 | Neuro examples |
|---|---|---|---|
| **Hydroxyl** | –OH | polar, H-bond donor/acceptor; neutral | serotonin (5-**hydroxy**tryptamine), cholesterol, ethanol, sugars |
| **Carboxyl** | –COOH | acidic (p$K_a$ 2–5), so **–COO⁻** | glutamate, GABA, fatty acids, aspartate |
| **Amine** | –NH₂ / –NHR / –NR₂; quaternary –N⁺R₃ | basic (p$K_a$ 9–10.5), so **–NH₃⁺** | all monoamines; acetylcholine (permanent N⁺(CH₃)₃) |
| **Phosphate** | –O–PO₃²⁻ | strongly negative, very hydrophilic | ATP, DNA backbone, phospholipids, phosphorylated proteins |
| **Thiol (sulfhydryl)** | –SH | can form **disulfide bridges** (–S–S–) by oxidation; binds metals | cysteine, glutathione (antioxidant), coenzyme A |
| Carbonyl | C=O (aldehyde, ketone) | polar, H-bond acceptor | sugars, ketamine, ketone bodies |
| Ester | –COO–R | can be hydrolysed (esterases) | **acetylcholine**, cocaine, heroin, phospholipids |
| Amide | –CO–NH– | planar, stable, H-bonding | **peptide bond**, glutamine, many drugs |
| Catechol | benzene ring with two adjacent –OH | easily oxidised; target of COMT | dopamine, noradrenaline, adrenaline (the catecholamines) |
| Indole | benzene fused to a pyrrole ring | aromatic, flat | tryptophan, serotonin, melatonin, LSD, psilocybin |

**Typical reactions in biology**
- **Condensation:** two molecules join and release H₂O (peptide bonds, ester bonds, glycosidic bonds, phosphodiester bonds).
- **Hydrolysis:** water splits the bond again. Example: acetylcholinesterase hydrolyses the ester bond of ACh into acetate and choline.
- **Phosphorylation** by kinases and **dephosphorylation** by phosphatases. These attach or remove a phosphate on Ser/Thr/Tyr –OH groups, which is the main molecular switch of signalling.
- **Oxidation/reduction:** 2 –SH ⇌ –S–S– (+ 2 H⁺ + 2 e⁻); dopamine oxidation produces quinones and ROS ([[Ch05 Redox and Electrochemistry]]).
- **Methylation** (methyl groups on DNA, histones, catecholamines via COMT); **acetylation** (histones, acetyl-CoA → ACh).

## Stereochemistry
**Isomers** have the same molecular formula but a different structure.
- **Constitutional isomers** have a different connectivity.
- **Stereoisomers** have the same connectivity but a different spatial arrangement:
  - **cis/trans (E/Z)** at double bonds. Retinal in the eye switches from **11-cis to all-trans** when light hits it, the very first step of vision. Natural fatty acids are mostly cis (kinked tails increase membrane fluidity).
  - **Enantiomers** are mirror images that can't be superimposed (like left and right hands).

**Chirality:** a carbon with **four different substituents** is a **stereocentre**.
- Labels: **R/S** (Cahn–Ingold–Prelog rules); for amino acids and sugars, the older **D/L** system.
- Enantiomers have identical physical properties (melting point, solubility) but rotate polarised light in opposite directions and **interact differently with other chiral molecules**.
- Receptors and enzymes are themselves chiral (made of L-amino acids), so they distinguish enantiomers like a glove distinguishes hands (the "three-point attachment" model).
- A 1:1 mixture of both enantiomers is called a **racemate**.

## In neuroscience #neuro
- **Chirality in the brain:**
  - Proteins are built from **L-amino acids** and sugars are **D-sugars**.
  - **D-serine** (not L) is released by neurons and astrocytes and acts as a co-agonist at NMDA receptors.
  - **L-DOPA** (levodopa) treats Parkinson's disease; D-DOPA does not.
  - **Esketamine** (S-ketamine) binds NMDA receptors more strongly than R-ketamine and is approved as a nasal spray for depression.
  - **Dextromethorphan** is a cough suppressant; its mirror image **levomethorphan** is a potent opioid.
  - **Thalidomide:** one enantiomer is a sedative and the other is teratogenic. They interconvert in the body, so even the "safe" one doesn't help.
- **Functional groups decide charge:** glutamate (net −1) and GABA (zwitterion, net 0) at pH 7.4 ([[Ch04 Acids Bases and pH]]). Acetylcholine has a **permanent** positive charge (quaternary ammonium), so it does not cross the BBB.
- **Transmitter synthesis is functional-group chemistry:**
  - tyrosine –(hydroxylation)→ L-DOPA –(decarboxylation, losing CO₂)→ dopamine
  - tryptophan → 5-hydroxytryptophan → serotonin
  - glutamate –(decarboxylation)→ GABA
  - See [[Bio06 Synapses and Neurotransmitters]].
- **Disulfide bridges** stabilise the Cys-loop of nicotinic, GABA_A, glycine and 5-HT₃ receptors and many extracellular domains. Thiol oxidation is part of oxidative stress.
- **Ester drugs are short-acting** because esterases hydrolyse them. Examples are remifentanil and the local anaesthetic procaine, while lidocaine (an amide) lasts longer.

## Math links #math-link
- Enantiomers = mirror images, i.e. a reflection with determinant −1 → [[C2 Determinants]]
- Three-dimensional geometry of a tetrahedral carbon (≈ 109.5° bond angles) → [[D2 Dot and Cross Product]]
- Charge as a function of pH (Henderson–Hasselbalch) → [[A3 Logarithms]]

## Connections
- Bonds and polarity → [[Ch02 Chemical Bonds]]
- Charges and pH → [[Ch04 Acids Bases and pH]]
- Biomolecules built from these groups → [[Ch08 Biomolecules]]
- Neurotransmitters → [[Bio06 Synapses and Neurotransmitters]]
- Receptor binding → [[Bio03 Proteins and Enzymes]]

## Key takeaways
- Hydroxyl, carboxyl (−), amine (+), phosphate (−−), thiol (S–S): recognise them on sight.
- Condensation builds molecules; hydrolysis breaks them.
- A carbon with 4 different substituents is chiral. Chiral receptors distinguish enantiomers, so drugs can differ completely between mirror images.
