---
aliases: [Proteins and Enzymes, Protein Structure, Enzyme Kinetics, GPCR, Receptors, Protein Misfolding, Proteine und Enzyme]
tags: [biology, protein, enzyme, gpcr, misfolding, type/overview, neuro]
---
# Bio03 Proteins and Enzymes

> [[MOC-biology|↑ Biology MOC]] · [[Bio03 Proteins and Enzymes - Worksheet|✏️ Worksheet]] · [[Bio03 Proteins and Enzymes - Solutions|✅ Solutions]] · [[Mistakes - Biology|⚠️ Mistake log]]

## Why this matters
Channels, receptors, transporters, enzymes, motors, scaffolds: almost everything that *does* something in a neuron is a protein. Its function follows from its 3D structure. Pharmacology is quantitative protein–ligand binding. Many neurodegenerative diseases are diseases of protein misfolding.

## Structure levels
| Level | What | Held together by | Example |
|---|---|---|---|
| **Primary** | amino acid sequence (N → C) | peptide bonds (covalent) | the sequence of the Nav1.7 gene product |
| **Secondary** | local folding patterns: **α-helix** (3.6 residues/turn, 0.15 nm rise per residue), **β-sheet** (parallel/antiparallel strands), loops | **backbone** H-bonds (C=O···H–N) | transmembrane helices (~20 hydrophobic residues ≈ 3 nm ≈ membrane thickness) |
| **Tertiary** | overall 3D fold of one chain; domains | side-chain interactions: hydrophobic core, H-bonds, salt bridges, **disulfide bridges** | the voltage-sensor domain |
| **Quaternary** | assembly of several chains (subunits) | same as tertiary | AMPA receptor (tetramer), nAChR and GABA_A (pentamers, e.g. 2α 2β 1γ), haemoglobin (α₂β₂) |

**Sequence determines structure (Anfinsen):** a denatured protein can refold spontaneously into its native state. AlphaFold now predicts structures from sequence with high accuracy ([[Meth02 Structural Biology]]).

## Folding and misfolding
- Folding is driven mainly by the **hydrophobic effect** (nonpolar residues hide in the core) plus many weak interactions ([[Ch02 Chemical Bonds]]).
- **Chaperones** (Hsp70, Hsp90, chaperonins) help folding and prevent aggregation.
- Proteins that fail quality control are degraded by the **ubiquitin–proteasome system** or by **autophagy/lysosomes** ([[Bio01 Cell Biology]]).
- **Misfolding and aggregation:** proteins form **amyloid**, insoluble fibrils with a **cross-β** structure (β-strands perpendicular to the fibre axis). Small soluble **oligomers** are often considered the most toxic species.

| Disease | Protein | Aggregate |
|---|---|---|
| Alzheimer's | **amyloid-β** (cleaved from APP by β- and γ-secretase); **tau** (hyperphosphorylated) | extracellular plaques; intracellular neurofibrillary tangles |
| Parkinson's, Lewy body dementia | **α-synuclein** | Lewy bodies |
| Prion diseases (CJD, kuru, BSE) | **PrP**: PrP^C → PrP^Sc | infectious template: misfolded PrP converts normal PrP |
| Huntington's | **huntingtin** with polyglutamine (CAG repeat > ~36) | nuclear inclusions |
| ALS / FTD | **TDP-43**, SOD1, FUS | cytoplasmic inclusions |

Many of these aggregates spread from cell to cell in a **prion-like** fashion (templated seeding), which may explain stereotyped disease progression (Braak stages).

## Enzymes and enzyme kinetics
Enzymes are catalysts. They lower the **activation energy**, but they do not change the equilibrium or $\Delta G$. They bind substrates in the **active site** (induced fit) and are specific and regulatable.

**Michaelis–Menten kinetics**
$$v = \frac{V_\text{max}\,[S]}{K_m + [S]}$$
- $V_\text{max}$ is the maximal rate at saturation ($= k_\text{cat}[E]_\text{total}$).
- $K_m$ is the substrate concentration giving **half-maximal rate**. A small $K_m$ means high affinity.
- At $[S]\ll K_m$, the rate is approximately linear in [S]; at $[S]\gg K_m$, it saturates.
- **Lineweaver–Burk** (double reciprocal) plot: $\frac1v = \frac{K_m}{V_\text{max}}\frac{1}{[S]} + \frac{1}{V_\text{max}}$ is a straight line.

**Inhibition**
| Type | Mechanism | Effect |
|---|---|---|
| **Competitive** | inhibitor binds the active site | apparent $K_m$ ↑ ($K_m(1 + [I]/K_i)$), $V_\text{max}$ unchanged; overcome by more substrate |
| **Non-competitive** | binds elsewhere (allosteric) | $V_\text{max}$ ↓, $K_m$ unchanged |
| **Irreversible** | covalent modification | enzyme destroyed (organophosphates on AChE, aspirin on COX) |

**Neuro enzymes:**
- acetylcholinesterase (AChE, one of the fastest enzymes, $k_\text{cat}\sim10^4\,\text{s}^{-1}$); AChE inhibitors such as donepezil treat Alzheimer's
- monoamine oxidase (MAO-A/B; MAO inhibitors as antidepressants or in Parkinson's)
- COMT
- tyrosine hydroxylase (rate-limiting for catecholamines)
- kinases (PKA, PKC, CaMKII) and phosphatases (calcineurin, PP1)

## Receptors and pharmacology
- **Binding:** at equilibrium, fractional occupancy is $\theta = \frac{[L]}{[L] + K_d}$ (the same shape as Michaelis–Menten). $K_d$ is the concentration giving 50 % occupancy.
- **Hill equation** for cooperative binding (several ligands needed): $\theta = \frac{[L]^n}{[L]^n + K^n}$, where $n > 1$ makes the curve steeper (a switch-like response).
- **Dose–response:** $\text{EC}_{50}$ (potency) and $E_\text{max}$ (efficacy).
  - **Agonist**: activates the receptor.
  - **Partial agonist**: lower $E_\text{max}$ (e.g. buprenorphine at µ-opioid, varenicline at α4β2 nAChR).
  - **Antagonist**: binds without activating; blocks agonists (naloxone, haloperidol at D2).
  - **Inverse agonist**: reduces constitutive activity.
  - **Allosteric modulator**: binds a separate site and changes the response (benzodiazepines at GABA_A).

### G-protein-coupled receptors (GPCRs)
- Structure: **7 transmembrane helices**. They are the largest receptor family and the target of about a third of approved drugs.
- **Cycle:**
  1. Ligand binds and the receptor changes conformation.
  2. It acts as a GEF for the heterotrimeric G protein (α, β, γ): Gα releases GDP and binds **GTP**.
  3. Gα-GTP and Gβγ dissociate and act on effectors.
  4. Gα hydrolyses GTP and the system switches off.
  5. **β-arrestin** binding after phosphorylation by GRKs desensitises and internalises the receptor.

| G protein | Effector | Second messenger | Example receptors |
|---|---|---|---|
| **Gs** | adenylyl cyclase ↑ | cAMP ↑ → PKA | D1, β-adrenergic, 5-HT₄/₆/₇ |
| **Gi/o** | adenylyl cyclase ↓; Gβγ opens **GIRK** K⁺ channels, closes Cav | cAMP ↓ | D2, µ-opioid, CB1, GABA_B, mGluR2/3, α2, M2/M4 |
| **Gq** | phospholipase C ↑ | **IP₃** (Ca²⁺ release from ER) + **DAG** (→ PKC) | mGluR1/5, M1/M3, α1, 5-HT₂A, H1 |

**Amplification:** one receptor activates many G proteins, and each adenylyl cyclase makes many cAMP molecules. Signalling is slow (100 ms to minutes) but strong and long-lasting.

## In neuroscience #neuro
- **Ionotropic vs. metabotropic:** fast receptor-channels vs. slow modulatory GPCRs ([[Bio06 Synapses and Neurotransmitters]]).
- **Psychiatric drugs act on GPCRs:**
  - antipsychotics are D2 antagonists
  - psychedelics are 5-HT₂A agonists (Gq)
  - opioids are µ-opioid agonists (Gi/o)
  - cannabinoids act on CB1 (Gi/o)
- **Chemogenetic tools are designer GPCRs:** DREADDs hM3Dq (Gq, excitatory) and hM4Di (Gi, inhibitory) ([[Meth05 Molecular Biology Tools]]).
- **CaMKII**, a dodecameric kinase, autophosphorylates and stays active after a Ca²⁺ signal, a molecular memory switch in LTP.

## Math links #math-link
- Michaelis–Menten, occupancy and Hill are all **saturating fractions** → [[A5 Fractions]], [[B1 Properties of Functions]]
- Lineweaver–Burk linearises by taking reciprocals; dose–response curves are sigmoids on a **log** concentration axis → [[A3 Logarithms]], [[B3 Logarithmic Functions]]
- Steepness at EC50 and the sensitivity of a switch → [[B6 Differentiation Rules]], [[B8 Curve Sketching]]
- Signal amplification cascades multiply → [[A7 Sums Products and Factorials]]
- Aggregation kinetics (lag phase, then exponential seeding) → [[B2 Exponential Functions]]

## Connections
- Amino acids, peptide bond → [[Ch08 Biomolecules]]
- Bond types → [[Ch02 Chemical Bonds]]
- Translation and splicing → [[Bio04 Nucleic Acids and Gene Expression]]
- Receptors at synapses → [[Bio06 Synapses and Neurotransmitters]]
- Structure determination → [[Meth02 Structural Biology]]

## Key takeaways
- Primary sequence → secondary (H-bonds) → tertiary (side chains) → quaternary (subunits).
- Misfolding into cross-β amyloid underlies Alzheimer's, Parkinson's, prion diseases, Huntington's and ALS.
- $v = V_\text{max}[S]/(K_m + [S])$; competitive inhibition raises $K_m$, non-competitive lowers $V_\text{max}$.
- GPCRs: 7TM; Gs raises cAMP, Gi lowers cAMP (and opens GIRK), Gq triggers IP₃/Ca²⁺ and DAG.
