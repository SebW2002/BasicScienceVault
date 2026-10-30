---
aliases: [Neural Circuits and Systems, Brain Anatomy, Neurodevelopment, Glia, Neuroanatomie]
tags: [biology, anatomy, development, glia, circuit, type/overview, neuro]
---
# Bio07 Neural Circuits and Systems

> [[MOC-biology|↑ Biology MOC]] · [[Bio07 Neural Circuits and Systems - Worksheet|✏️ Worksheet]] · [[Bio07 Neural Circuits and Systems - Solutions|✅ Solutions]] · [[Mistakes - Biology|⚠️ Mistake log]]

## Why this matters
Single neurons don't think. Circuits do. To read any paper you need a map: where structures are, how they're connected, how they develop, and which non-neuronal cells (glia) keep them working. This note gives a compact anatomical and developmental orientation.

## Orientation vocabulary
| Term | Meaning |
|---|---|
| **Rostral / anterior** vs. **caudal / posterior** | towards the nose vs. towards the tail/back |
| **Dorsal / superior** vs. **ventral / inferior** | towards the top (back) vs. the belly side (bottom) |
| **Medial** vs. **lateral** | towards the midline vs. away from it |
| Ipsilateral / contralateral | same side / opposite side |
| Sections: **sagittal**, **coronal (frontal)**, **horizontal (axial)** | side view / front view / top view |

In humans, the neuraxis bends at the midbrain, so in the forebrain "dorsal" means "superior". In MNI coordinates, $x$ = left→right, $y$ = posterior→anterior, $z$ = inferior→superior ([[D1 Vectors in 2D and 3D]]).

**Grey matter** contains somata, dendrites and synapses. **White matter** contains myelinated axon tracts (corpus callosum, internal capsule).

## Brain structures to know
| Structure | Location / components | Main functions |
|---|---|---|
| **Cerebral cortex** | outer sheet, 2–4 mm thick; **6 layers** in neocortex; lobes: frontal, parietal, temporal, occipital (+ insula) | perception, action, cognition, language |
| **Hippocampus** | medial temporal lobe; dentate gyrus (DG), CA3, CA1, subiculum; input from the entorhinal cortex | **episodic memory**, spatial navigation (**place cells**; grid cells in the entorhinal cortex) |
| **Basal ganglia** | striatum (caudate, putamen, nucleus accumbens), globus pallidus (GPe, GPi), subthalamic nucleus (STN), substantia nigra (SNc, SNr) | action selection, habit and reinforcement learning, motivation |
| **Cerebellum** | posterior, below the occipital lobe; cortex with **Purkinje cells**, granule cells; deep nuclei | motor coordination, timing, motor learning; also cognition |
| Thalamus | diencephalon, centre of the brain | relay and gating of almost all sensory input to cortex (not smell); thalamocortical rhythms |
| Hypothalamus | below the thalamus | homeostasis: temperature, hunger, thirst, circadian rhythm (SCN), hormones |
| Amygdala | anterior medial temporal lobe | emotion, fear learning |
| Brainstem | midbrain, pons, medulla | vital functions, cranial nerves, neuromodulatory nuclei (raphe, locus coeruleus, VTA/SNc) |

### Circuits in detail
**Neocortex:**
- Layer 4 receives thalamic input.
- Layers 2/3 project to other cortical areas.
- Layer 5 projects to subcortical targets (pyramidal tract).
- Layer 6 projects back to the thalamus.
- About 80 % of neurons are excitatory pyramidal cells and about 20 % are inhibitory interneurons (PV, SST, VIP types).
- Functional **columns** (e.g. ocular dominance in V1).

**Hippocampal trisynaptic circuit:** entorhinal cortex → (perforant path) → **DG** → (mossy fibres) → **CA3** → (Schaffer collaterals) → **CA1** → subiculum → entorhinal cortex. Patient **H.M.** (bilateral medial temporal lobe resection, 1953) lost the ability to form new episodic memories.

**Basal ganglia loops** (cortex → striatum → output nuclei → thalamus → cortex):
- **Direct pathway:** striatal D1 neurons inhibit GPi/SNr, which disinhibits the thalamus: **"go"**.
- **Indirect pathway:** striatal D2 neurons inhibit GPe, which disinhibits STN, which excites GPi: **"no-go"**.
- Dopamine from SNc excites the direct pathway (D1) and inhibits the indirect pathway (D2), so dopamine facilitates movement.
- **Parkinson's disease:** loss of SNc dopamine neurons shifts the balance towards "no-go", causing bradykinesia. Deep brain stimulation (DBS) of the STN is a treatment.
- **Huntington's disease:** early loss of indirect-pathway neurons causes excess movement (chorea).

**Cerebellum:**
- Mossy fibres → granule cells → parallel fibres → Purkinje cells.
- **Climbing fibres** from the inferior olive deliver an "error signal".
- Purkinje cells (inhibitory) → deep nuclei.
- The cerebellum contains about **80 %** of all neurons in the brain (mostly granule cells).

## Neurodevelopment
1. **Neurulation** (weeks 3–4 in humans): the neural plate folds into the **neural tube**. Failure to close causes neural tube defects (spina bifida, anencephaly), which **folic acid** helps prevent.
2. **Regionalisation:** gradients of morphogens (Shh ventrally, BMP/Wnt dorsally) and transcription factors define the forebrain, midbrain, hindbrain and spinal cord.
3. **Neurogenesis:** radial glia in the ventricular zone divide and produce neurons (and later glia).
4. **Migration:** cortical neurons climb along radial glial fibres in an **inside-out** order (deep layers first, then upper layers). Interneurons migrate tangentially from the ganglionic eminences. Defects cause lissencephaly (*LIS1*, *reelin*).
5. **Axon guidance:** **growth cones** follow attractive and repulsive cues: netrins, slits (with Robo receptors), semaphorins, ephrins.
6. **Synaptogenesis and pruning:** synapses are overproduced, then pruned depending on activity (microglia and complement tag weak synapses). Many neurons die by **apoptosis** (dependence on neurotrophic factors: NGF, BDNF).
7. **Critical periods:** experience shapes circuits in windows of high plasticity. Example: monocular deprivation in kittens causes a permanent shift of ocular dominance (Hubel & Wiesel). PV interneuron maturation and perineuronal nets close these windows.
8. **Myelination** continues into early adulthood (prefrontal cortex is the last); white matter changes throughout life.

**Adult neurogenesis** is well established in the rodent dentate gyrus and olfactory bulb; in adult humans it is debated.

## Glia
| Cell | Origin | Main functions | Disease links |
|---|---|---|---|
| **Astrocytes** | neural (radial glia) | K⁺ buffering (Kir4.1, gap junctions), **glutamate uptake** (EAAT1/2) and the glutamate–glutamine cycle; **BBB** endfeet (AQP4); metabolic support (glycogen, lactate); **tripartite synapse** (release gliotransmitters such as D-serine, ATP); synapse formation | reactive astrogliosis (GFAP ↑), glioma, neuromyelitis optica (antibodies against AQP4) |
| **Oligodendrocytes** | neural (via OPCs/NG2 cells) | **CNS myelin**; one cell myelinates up to ~50 internodes; metabolic support of axons | multiple sclerosis, leukodystrophies |
| Schwann cells | neural crest | PNS myelin (one internode each); regeneration | Charcot–Marie–Tooth, Guillain–Barré |
| **Microglia** | **yolk-sac macrophages** (not neural!) | immune surveillance, phagocytosis, **synaptic pruning** (complement C1q/C3), injury responses | neuroinflammation; Alzheimer's risk genes (*TREM2*) |
| Ependymal cells, choroid plexus | neural | line the ventricles; produce **CSF** | hydrocephalus |

The **glia-to-neuron ratio** in the human brain is roughly 1:1, not 10:1 as long claimed (isotropic fractionator counts).

## In neuroscience #neuro
- **Systems questions** are circuit questions. For example: how does dopamine teach the striatum (reward prediction error)? How does the hippocampus replay sequences during sleep?
- **Lesion and stimulation logic:** a lesion shows necessity, stimulation shows sufficiency ([[E1 Sets Logic and Quantifiers]]).
- Neurodevelopmental disorders (autism, schizophrenia risk, epilepsies) are often disorders of migration, synaptogenesis, pruning or the excitation/inhibition balance.

## Math links #math-link
- Partial derivatives, gradients, Jacobians, multiple integrals → [[B11 Multivariable Calculus]]
- Coordinates and planes for anatomy (MNI, sections) → [[D1 Vectors in 2D and 3D]], [[D3 Lines and Planes]]
- Circuits as connectivity matrices; signs (excitatory/inhibitory), disinhibition as a product of two negative signs → [[C1 Matrices]]
- Recurrent E–I networks, stability and oscillations → [[C4 Eigenvalues and Eigenvectors]]
- Morphogen gradients decay exponentially; cells read thresholds → [[B2 Exponential Functions]]
- Place-cell tuning as a Gaussian, head-direction tuning as a cosine → [[B1 Properties of Functions]], [[B4 Trigonometric Functions]]

## Connections
- Single neurons → [[Bio05 Neurons and Action Potentials]]
- Synapses and transmitters in circuits → [[Bio06 Synapses and Neurotransmitters]]
- Imaging brain systems → [[Meth04 In Vivo Imaging]]
- Mapping circuits → [[Meth06 Omics and Sequencing]] (connectomics), [[Meth05 Molecular Biology Tools]] (tracing, optogenetics)

## Key takeaways
- Know directional terms and the main structures: cortex, hippocampus, basal ganglia, cerebellum, thalamus.
- Hippocampus: EC → DG → CA3 → CA1. Basal ganglia: direct "go" (D1) vs. indirect "no-go" (D2).
- Development: neural tube → neurogenesis → inside-out migration → axon guidance → synapse overproduction and pruning → critical periods → myelination.
- Astrocytes support and regulate, oligodendrocytes and Schwann cells myelinate, and microglia are immune cells that prune.
