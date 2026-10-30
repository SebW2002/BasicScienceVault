---
aliases: [Synapses and Neurotransmitters, Synapse, Neurotransmitters, Synaptic Plasticity, LTP, LTD, Synapsen]
tags: [biology, synapse, neurotransmitter, receptor, plasticity, type/overview, neuro]
---
# Bio06 Synapses and Neurotransmitters

> [[MOC-biology|↑ Biology MOC]] · [[Bio06 Synapses and Neurotransmitters - Worksheet|✏️ Worksheet]] · [[Bio06 Synapses and Neurotransmitters - Solutions|✅ Solutions]] · [[Mistakes - Biology|⚠️ Mistake log]]

## Why this matters
Synapses are where neurons compute and where the brain **learns**. They convert electrical signals into chemical ones and back, they can be strengthened or weakened, and they are the target of most psychoactive drugs. The human brain has on the order of $10^{14}$ synapses.

## Chemical vs. electrical synapses
| | Chemical synapse | Electrical synapse |
|---|---|---|
| Structure | presynaptic terminal, **cleft ~20–40 nm**, postsynaptic density | **gap junctions** (connexins, e.g. Cx36 in neurons); gap ~3.5 nm |
| Transmission | transmitter release → receptors | direct ion flow between cytoplasms |
| Speed | **synaptic delay ~0.5–1 ms** | practically instantaneous |
| Direction | mostly one-way | usually **bidirectional** |
| Sign / gain | excitatory or inhibitory; can **amplify** | same sign; attenuated (low-pass filtering) |
| Plasticity | rich (LTP, LTD, short-term) | limited |
| Examples | most CNS synapses, neuromuscular junction | inhibitory interneuron networks, inferior olive, retina: **synchronisation** |

## Chemical transmission step by step
1. An AP arrives at the terminal.
2. Voltage-gated **Ca²⁺ channels** (Cav2.1 P/Q-type, Cav2.2 N-type) open, and Ca²⁺ rises locally to ~10–100 µM within nanodomains.
3. Ca²⁺ binds **synaptotagmin**, the **SNARE** complex zips, and the vesicle fuses (exocytosis) ([[Bio01 Cell Biology]]). Release depends steeply on Ca²⁺ (≈ [Ca²⁺]⁴).
4. Transmitter diffuses across the cleft (< 1 µs over 20 nm) and binds postsynaptic receptors.
5. A postsynaptic potential results: an **EPSP** (excitatory, depolarising) or an **IPSP** (inhibitory, usually hyperpolarising or shunting).
6. Termination by **reuptake** (transporters), **enzymatic breakdown** (AChE) or diffusion away.
7. Vesicles are recycled by endocytosis.

**Quantal release** (Katz): transmitter is released in packets (one vesicle = one **quantum**). The mean number of quanta = $n\cdot p$ (release sites × release probability), a binomial model ([[A6 Binomial Formulas and Theorem]]).

**Integration:** EPSPs and IPSPs **sum** in space (from different synapses) and time (repeated input). If the AIS reaches threshold, the neuron fires.

**Short-term plasticity:** **facilitation** (residual Ca²⁺, typical for low-$p$ synapses) or **depression** (vesicle depletion, typical for high-$p$ synapses) over milliseconds to seconds.

## Neurotransmitter classes
| Transmitter | Synthesis (precursor → enzyme) | Main receptors | Termination | Key systems / clinical |
|---|---|---|---|---|
| **Glutamate** | glutamine → glutaminase | AMPA, NMDA, kainate (ionotropic); mGluR1–8 | EAATs (mainly astrocytes) | main **excitatory** transmitter; excitotoxicity in stroke; ketamine blocks NMDA |
| **GABA** | glutamate → **GAD** | GABA_A (Cl⁻ channel), GABA_B (Gi/o GPCR) | GAT transporters | main **inhibitory** transmitter in the brain; benzodiazepines, barbiturates, alcohol enhance GABA_A |
| Glycine | serine → SHMT | GlyR (Cl⁻) | GlyT | inhibitory in spinal cord/brainstem; strychnine blocks GlyR |
| **Dopamine** | tyrosine → **tyrosine hydroxylase** (rate-limiting) → L-DOPA → AADC → DA | D1-like (Gs), D2-like (Gi) | DAT; MAO, COMT | substantia nigra (movement; **Parkinson's**), VTA (reward, **reward prediction error**); antipsychotics block D2 |
| Noradrenaline | DA → dopamine β-hydroxylase | α1 (Gq), α2 (Gi), β (Gs) | NET; MAO, COMT | **locus coeruleus**: arousal, attention |
| **Serotonin (5-HT)** | tryptophan → tryptophan hydroxylase → 5-HTP → AADC | 5-HT₁–₇ (GPCRs), **5-HT₃** (ionotropic) | SERT; MAO | **raphe nuclei**: mood, sleep, appetite; SSRIs, psychedelics (5-HT₂A) |
| **Acetylcholine** | choline + acetyl-CoA → **ChAT** | **nicotinic** (ionotropic), **muscarinic** M1–M5 (GPCRs) | **AChE** (hydrolysis) | neuromuscular junction; basal forebrain (attention, memory; loss in Alzheimer's); myasthenia gravis (antibodies against nAChR) |
| Neuropeptides | synthesised as large precursors in the soma, cleaved | mostly GPCRs | peptidases | opioids, substance P, oxytocin, NPY; released from dense-core vesicles at high firing rates |
| Others | – | – | – | histamine, ATP/adenosine, endocannabinoids (retrograde), NO (gaseous, retrograde) |

**Dale's principle (modernised):** a neuron releases the same set of transmitters at all its synapses, which often includes co-transmitters (e.g. GABA + a neuropeptide).

## Receptor types
| | Ionotropic | Metabotropic |
|---|---|---|
| Structure | ligand-gated ion channel (tetramer: glutamate receptors; pentamer: Cys-loop family nAChR, GABA_A, GlyR, 5-HT₃) | GPCR with 7 TM helices ([[Bio03 Proteins and Enzymes]]) |
| Mechanism | binding opens the pore directly | G protein → second messengers → channels/enzymes |
| Speed | **fast** (ms) | **slow** (100 ms – min) |
| Effect | brief EPSP/IPSP | modulation of excitability, release, plasticity, gene expression |

**AMPA vs. NMDA receptors:**
- **AMPA:** fast Na⁺/K⁺ current; carries most of the EPSP.
- **NMDA:** needs (1) glutamate, (2) the co-agonist **glycine or D-serine**, and (3) **depolarisation** to expel the **Mg²⁺ block**. It lets in **Ca²⁺**.
- The NMDA receptor is therefore a **coincidence detector**: it opens only when presynaptic release (glutamate) coincides with postsynaptic activity (depolarisation), which is Hebb's rule at the molecular level.

## Synaptic plasticity: LTP and LTD
**Hebb (1949):** "Cells that fire together wire together." **Bliss & Lømo (1973)** first described LTP in the rabbit hippocampus.

**NMDA-dependent LTP** (e.g. CA3 → CA1 Schaffer collaterals):
1. High-frequency stimulation (e.g. 100 Hz) or pairing pre- with postsynaptic activity.
2. NMDA receptors are unblocked and a **large, fast Ca²⁺ influx** follows.
3. **CaMKII** is activated (and autophosphorylates), and PKC is activated.
4. AMPA receptors are phosphorylated and **more AMPA receptors are inserted** into the synapse.
5. **Late LTP** (hours and beyond) needs new **gene expression and protein synthesis** (CREB, [[Bio04 Nucleic Acids and Gene Expression]]) and structural growth of spines.

**LTD:** low-frequency stimulation (e.g. 1 Hz for 15 min) produces a **modest, prolonged Ca²⁺** rise, which activates **phosphatases** (calcineurin, PP1). AMPA receptors are dephosphorylated and **endocytosed**.
**Rule of thumb:** high Ca²⁺ gives LTP; moderate Ca²⁺ gives LTD; low Ca²⁺ gives no change (the basis of the BCM theory).

**Properties of LTP:**
- **input specificity**: only the active synapses change
- **cooperativity**: several inputs are needed
- **associativity**: a weak input paired with a strong one is potentiated

**Spike-timing-dependent plasticity (STDP):** pre before post (within ~10–20 ms) gives LTP; post before pre gives LTD.

Other forms include cerebellar LTD at Purkinje cells (motor learning), presynaptic LTP at mossy fibres (cAMP-dependent), homeostatic synaptic scaling, and endocannabinoid-mediated LTD.

## In neuroscience #neuro
- **Drugs by mechanism:**
  - release: amphetamine
  - reuptake: SSRIs, cocaine
  - degradation: MAO inhibitors, AChE inhibitors
  - receptors: benzodiazepines, antipsychotics, opioids, ketamine, nicotine
  - vesicle filling: reserpine
- **Excitotoxicity:** too much glutamate leads to excessive NMDA receptor activation and Ca²⁺ overload, which activates proteases and damages mitochondria, killing the cell (stroke, trauma). The NMDA antagonist **memantine** is used in Alzheimer's disease.
- **Learning and memory:** blocking NMDA receptors in the hippocampus (AP5) impairs spatial learning (Morris water maze, Morris et al. 1986). Optogenetically inducing LTD or LTP can erase or restore fear memories in rodents.

## Math links #math-link
- Differential equations (steady state, time constant, stability, Euler steps) → [[B10 Differential Equations]]
- Quantal release (binomial), mean $np$, variance $np(1-p)$; spontaneous minis as a Poisson process → [[A6 Binomial Formulas and Theorem]], [[A7 Sums Products and Factorials]]
- Release ∝ [Ca²⁺]⁴: a power law that becomes a straight line with slope 4 on log–log axes → [[A1 Exponent Rules]], [[B3 Logarithmic Functions]]
- Synaptic conductance as an alpha function or difference of exponentials; time to peak by $f' = 0$ → [[B8 Curve Sketching]], [[B2 Exponential Functions]]
- Driving force $I_\text{syn} = g_\text{syn}(V - E_\text{syn})$ and shunting inhibition → [[A4 Factoring and Simplifying]]
- STDP window $\Delta w = A_\pm e^{-\lvert\Delta t\rvert/\tau}$; learning rules $\Delta w = \eta\,x\,y$ → [[B2 Exponential Functions]], [[B6 Differentiation Rules]]
- Synaptic weight matrices → [[C1 Matrices]]

## Connections
- Vesicle fusion machinery → [[Bio01 Cell Biology]]
- Receptors and GPCRs → [[Bio03 Proteins and Enzymes]]
- Reversal potentials, chloride and GABA → [[Ch05 Redox and Electrochemistry]]
- Transmitter chemistry → [[Ch07 Organic Chemistry Essentials]], [[Ch08 Biomolecules]]
- Circuits that use these synapses → [[Bio07 Neural Circuits and Systems]]
- Methods: patch clamp → [[Meth03 Electrophysiology]]; optogenetics → [[Meth05 Molecular Biology Tools]]

## Key takeaways
- Chemical synapses are slower, one-way, amplifiable and plastic. Electrical synapses are fast, two-way and synchronising.
- AP → Ca²⁺ → SNAREs/synaptotagmin → release → receptors → termination (reuptake or degradation).
- Glutamate excites, GABA inhibits, and the modulators (DA, 5-HT, NA, ACh) mostly act through GPCRs.
- NMDA receptor = coincidence detector. High Ca²⁺ gives LTP (CaMKII, AMPA insertion); moderate Ca²⁺ gives LTD (phosphatases, AMPA removal).
