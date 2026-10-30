---
aliases: [Cell Biology, Organelles, Cytoskeleton, Vesicle Trafficking, Zellbiologie]
tags: [biology, cell, organelle, cytoskeleton, vesicle, type/overview, neuro]
---
# Bio01 Cell Biology

> [[MOC-biology|↑ Biology MOC]] · [[Bio01 Cell Biology - Worksheet|✏️ Worksheet]] · [[Bio01 Cell Biology - Solutions|✅ Solutions]] · [[Mistakes - Biology|⚠️ Mistake log]]

## Why this matters
A neuron is an extreme cell. Its axon can be 10,000 times longer than its cell body, it has thousands of synapses that each need proteins and vesicles, and it must survive for a lifetime without dividing. Every general cell-biology mechanism (protein sorting, transport, recycling, energy) is pushed to its limits in neurons, and when one fails, neurodegeneration often follows.

## Prokaryotic vs. eukaryotic cells
| Feature | Prokaryotes (bacteria, archaea) | Eukaryotes (animals, plants, fungi) |
|---|---|---|
| Nucleus | none (DNA in the nucleoid) | membrane-bound nucleus |
| Organelles | none bounded by membranes | ER, Golgi, mitochondria, lysosomes … |
| Size | ~1–10 µm | ~10–100 µm (neurons: soma 5–100 µm, axon up to > 1 m) |
| Ribosomes | 70S | 80S (cytosol); 70S-like in mitochondria |
| DNA | circular, often plasmids | linear chromosomes with histones |
| Cytoskeleton | simple homologues | actin, microtubules, intermediate filaments |

**Endosymbiont theory:** mitochondria descend from engulfed bacteria. They still have their **own circular DNA** (mtDNA, inherited from the mother) and bacteria-like ribosomes.
- Mutations in mtDNA cause **mitochondrial diseases** that often affect the brain and muscle (e.g. MELAS, Leber's hereditary optic neuropathy).
- Some antibiotics (e.g. aminoglycosides) can harm mitochondrial ribosomes, which leads to hearing loss.

**Lab relevance:** bacteria (*E. coli*) are used to amplify plasmids, for example for AAV production ([[Meth05 Molecular Biology Tools]]).

## Organelles
| Organelle | Function | In neurons |
|---|---|---|
| **Nucleus** | DNA, transcription, RNA processing | activity-dependent gene expression (c-Fos, CREB) |
| **Rough ER** (with ribosomes) | synthesis of membrane and secreted proteins; folding; start of N-glycosylation | visible as **Nissl bodies** in the soma; also in dendrites |
| **Smooth ER** | lipid synthesis, **Ca²⁺ store** (IP₃ and ryanodine receptors, SERCA pump) | extends into axon and spines; Ca²⁺ signalling |
| **Golgi apparatus** | modification (glycosylation), **sorting** and packaging into vesicles | Golgi outposts in dendrites |
| **Mitochondria** | ATP (oxidative phosphorylation), Ca²⁺ buffering, apoptosis | transported to synapses and nodes; defects → Parkinson's (PINK1/Parkin) |
| **Lysosomes** | degradation (acidic, pH ≈ 4.5–5, hydrolases); autophagy | defects → storage diseases; mostly in the soma |
| Endosomes | sorting of endocytosed material (recycle or degrade) | receptor recycling at synapses (e.g. AMPA receptors) |
| Peroxisomes | fatty acid oxidation, H₂O₂ breakdown, plasmalogen synthesis | myelin lipids; defects → leukodystrophies |

**Secretory pathway:** rough ER → (vesicles) → Golgi (cis → trans) → vesicles → plasma membrane or secretion. Membrane proteins such as channels and receptors take this route.

## The cytoskeleton
| Filament | Subunit | Diameter | Key functions | Neuro |
|---|---|---|---|---|
| **Actin** (microfilaments) | G-actin → F-actin | ~7 nm | cell shape, motility (myosin motors) | **dendritic spines**, growth cones, presynaptic organisation |
| **Microtubules** | α/β-tubulin dimers, GTP-dependent | ~25 nm | tracks for transport, cell division | axon: uniform plus-ends-out polarity; dendrites: mixed. Stabilised by **tau** (axon) and **MAP2** (dendrites) |
| **Intermediate filaments** | **neurofilaments** (NF-L, -M, -H) in neurons; GFAP in astrocytes | ~10 nm | mechanical stability | determine **axon diameter** (and thus conduction speed); **NfL** in blood is a biomarker of axon damage |

**Motor proteins:**
- **Kinesin** moves towards the plus end (anterograde: soma → terminal).
- **Dynein** moves towards the minus end (retrograde: terminal → soma).
- **Myosin** moves along actin.

**Axonal transport:**
- **fast** (≈ 50–400 mm/day): vesicles, mitochondria
- **slow** (≈ 0.2–8 mm/day): cytoskeleton, soluble proteins

Diffusion alone would take years over such distances ([[Ch06 Solutions and Concentration]]).

## Vesicle trafficking, endocytosis and exocytosis
- **Exocytosis:** a vesicle fuses with the plasma membrane and releases its content.
  - At synapses, fusion is driven by **SNARE** proteins: v-SNARE **synaptobrevin/VAMP2** on the vesicle, t-SNAREs **syntaxin-1** and **SNAP-25** on the membrane. They zip into a four-helix bundle and pull the membranes together.
  - **Synaptotagmin** senses Ca²⁺ and triggers fusion within under a millisecond of Ca²⁺ entry.
  - **Constitutive** exocytosis happens continuously (membrane renewal); **regulated** exocytosis is triggered by Ca²⁺ (transmitters, neuropeptides from dense-core vesicles).
- **Endocytosis:** the membrane invaginates and pinches off a vesicle.
  - **Clathrin-mediated**: an adaptor (AP2) binds cargo, clathrin forms a coat, and **dynamin** pinches off the vesicle (it is a GTPase).
  - At synapses there are also faster modes (ultrafast endocytosis, kiss-and-run).
  - Used for vesicle recycling, receptor internalisation (LTD: AMPA receptor endocytosis), and uptake of nutrients (transferrin), viruses and toxins.

## In neuroscience #neuro
- **Polarity:** neurons are strongly polarised (dendrites receive, axons send). The **axon initial segment** acts as a filter: ankyrin-G anchors Na⁺ channels and blocks the free diffusion of dendritic proteins into the axon.
- **Toxins that target SNAREs:**
  - **Botulinum toxins** cleave SNAREs at the neuromuscular junction, preventing ACh release and causing flaccid paralysis. Botox is used therapeutically against spasticity, dystonia and migraine.
  - **Tetanus toxin** is transported retrogradely into the spinal cord and cleaves VAMP2 in **inhibitory** interneurons, causing spastic paralysis.
- **Neurodegeneration and cell biology:**
  - **Tau** detaches from microtubules and aggregates in Alzheimer's disease.
  - Mutations in transport proteins cause hereditary neuropathies.
  - Mitochondrial quality control (PINK1/Parkin mitophagy) fails in Parkinson's disease.
  - Impaired autophagy and lysosomal degradation contribute to many protein-aggregation diseases ([[Bio03 Proteins and Enzymes]]).
- **Local translation:** mRNAs (e.g. *Arc*, *CaMKIIα*) are transported to dendrites and translated locally at active synapses, which is important for long-lasting plasticity ([[Bio06 Synapses and Neurotransmitters]]).
- **Markers in the lab:** Nissl staining (rough ER, labels neuronal somata), MAP2 (dendrites), tau or neurofilament (axons), synaptophysin (vesicles). See [[Meth05 Molecular Biology Tools]].

## Math links #math-link
- Surface-to-volume ratio of cells ($\propto 1/r$) → [[A1 Exponent Rules]], [[A5 Fractions]]
- Transport time = distance / speed; diffusion time ∝ distance² → [[A2 Root Rules]]
- Microtubule length dynamics (growth/shrinkage) as a random process → [[A7 Sums Products and Factorials]]

## Connections
- Biomolecules → [[Ch08 Biomolecules]]
- Membranes → [[Bio02 Membranes and Transport]]
- Protein folding and degradation → [[Bio03 Proteins and Enzymes]]
- Neuron anatomy → [[Bio05 Neurons and Action Potentials]]
- Transmitter release → [[Bio06 Synapses and Neurotransmitters]]
- Imaging organelles → [[Meth01 Microscopy]]

## Key takeaways
- Eukaryotic cells have organelles. Mitochondria are former bacteria with their own DNA.
- Secretory pathway: ER → Golgi → vesicle → membrane.
- Actin for spines, microtubules for transport (kinesin outward, dynein inward), neurofilaments for axon calibre.
- SNAREs and synaptotagmin drive Ca²⁺-triggered exocytosis; clathrin and dynamin drive endocytosis.
