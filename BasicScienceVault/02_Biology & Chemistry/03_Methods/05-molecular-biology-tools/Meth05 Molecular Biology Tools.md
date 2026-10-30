---
aliases: [Molecular Biology Tools, PCR, qPCR, Western Blot, ELISA, Immunohistochemistry, CRISPR, Optogenetics, DREADDs, AAV, Molekularbiologische Methoden]
tags: [methods, pcr, antibody, crispr, optogenetics, aav, type/overview, neuro]
---
# Meth05 Molecular Biology Tools

> [[MOC-methods|↑ Methods MOC]] · [[Meth05 Molecular Biology Tools - Worksheet|✏️ Worksheet]] · [[Meth05 Molecular Biology Tools - Solutions|✅ Solutions]] · [[Mistakes - Methods|⚠️ Mistake log]]

## Why this matters
Modern neuroscience is defined by the ability to **measure** molecules (PCR, blots, ELISA, staining) and to **manipulate** specific genes and cell types (CRISPR, viral vectors, optogenetics, chemogenetics). These tools turned correlation ("region X is active") into causation ("activating cell type Y in region X causes behaviour Z").

## Measuring nucleic acids: PCR and qPCR
**PCR (polymerase chain reaction; Mullis, Nobel 1993)** amplifies a defined DNA segment exponentially. Each cycle has three steps:
1. **Denaturation** (~95 °C): the strands separate (H-bonds break, [[Ch02 Chemical Bonds]]).
2. **Annealing** (~50–65 °C): two **primers** (~18–25 nt) bind the flanking sequences. Their melting temperature depends on GC content.
3. **Extension** (72 °C): a heat-stable **Taq polymerase** synthesises the new strands (5' → 3').

Ideally the amount **doubles** each cycle: after $n$ cycles, $N = N_0\cdot2^n$ ($2^{30}\approx10^9$).
Uses: genotyping (e.g. Cre lines), cloning, sequencing library preparation, diagnostics.

**RT-qPCR** (reverse-transcription quantitative PCR) measures **mRNA levels**:
- RNA → cDNA (reverse transcriptase) → PCR with fluorescent detection (SYBR Green or TaqMan probe) **in real time**.
- **Ct (cycle threshold):** the cycle at which fluorescence crosses a threshold. More starting template gives a **smaller Ct**. A difference of 1 Ct is a factor of 2.
- **ΔΔCt method:**
  - $\Delta\text{Ct} = \text{Ct}_\text{target} - \text{Ct}_\text{reference gene}$ (normalised to a housekeeping gene, e.g. *GAPDH*, *ACTB*)
  - $\Delta\Delta\text{Ct} = \Delta\text{Ct}_\text{treated} - \Delta\text{Ct}_\text{control}$
  - **fold change** $= 2^{-\Delta\Delta\text{Ct}}$ (assuming 100 % efficiency)

## Measuring proteins: Western blot and ELISA
**Western blot:**
1. Lyse the tissue and denature proteins with **SDS** (negative charge, unfolded, [[Ch03 Intermolecular Forces and Solubility]]).
2. **SDS-PAGE:** separate by **size** in a gel (small proteins migrate farther).
3. **Transfer** to a membrane (nitrocellulose/PVDF).
4. **Block**, then incubate with a **primary antibody** (specific to the target), then a **secondary antibody** (against the primary's species, coupled to HRP or a fluorophore).
5. Detect (chemiluminescence or fluorescence); quantify bands relative to a **loading control** (β-actin, GAPDH, total protein stain).

Information: presence, approximate **size** (kDa; cleavage products, isoforms) and **semi-quantitative** amount; with phospho-specific antibodies, the **activation state** (e.g. p-CREB/CREB).

**ELISA (enzyme-linked immunosorbent assay):** in a multi-well plate, usually as a **sandwich ELISA** (capture antibody → antigen → detection antibody → enzyme → colour). Concentration is read off a **standard curve**. It is **quantitative**, high-throughput and sensitive (pg/mL).
Neuro: CSF Aβ42, total tau and p-tau for Alzheimer's diagnosis; cytokines; BDNF. Ultrasensitive variants (Simoa) measure NfL and p-tau in **blood**.

## Seeing proteins in tissue: immunohistochemistry (IHC) and immunofluorescence (IF)
1. **Fix** the tissue (e.g. 4 % paraformaldehyde, which cross-links proteins) and section it.
2. Permeabilise (Triton X-100) and block (serum/BSA).
3. Apply the primary antibody, then the secondary antibody with an **enzyme** (IHC, e.g. HRP + DAB gives a brown precipitate; viewed with brightfield) or a **fluorophore** (IF, multiple colours; confocal, [[Meth01 Microscopy]]).

**Common neuro markers**
| Marker | Labels |
|---|---|
| NeuN | neuronal nuclei |
| MAP2 / Tau | dendrites / axons |
| GFAP | astrocytes |
| Iba1 | microglia |
| Olig2, MBP | oligodendrocyte lineage / myelin |
| Parvalbumin, somatostatin, VIP | interneuron subtypes |
| c-Fos | recently active neurons |
| Synaptophysin, PSD-95 | pre- / postsynapses |
| TH | catecholaminergic (dopamine) neurons |

**Controls:** no-primary control, knockout tissue (the gold standard for antibody specificity), pre-absorption, and consistent imaging settings.

## Editing genes: CRISPR–Cas9 (Charpentier & Doudna, Nobel 2020)
- **Cas9** nuclease + **guide RNA** (~20 nt complementary to the target). It requires a **PAM** sequence next to the target (NGG for SpCas9) and cuts both strands (a double-strand break, DSB).
- **Repair:**
  - **NHEJ** (non-homologous end joining) is error-prone and produces small insertions or deletions, often frameshifts, so the result is a **knockout**. This works even in postmitotic neurons.
  - **HDR** (homology-directed repair) uses a donor template for precise **knock-in** (e.g. adding a tag or a point mutation). It is inefficient in non-dividing cells.
- **Variants:** base editors (single-base changes without DSBs), prime editors, **CRISPRi/CRISPRa** (catalytically dead dCas9 fused to repressors or activators that turn genes down or up without cutting).
- **Neuro:** fast generation of mouse models, knockouts in specific cell types (Cas9 driven by Cre), genetic screens, and correction of disease mutations in iPSC-derived neurons. Clinical trials are under way (the first CRISPR therapy approved, for sickle cell disease, is not neurological).

## Controlling neurons: optogenetics and chemogenetics
**Optogenetics** (Boyden, Deisseroth et al. 2005): neurons express **light-sensitive microbial opsins**, and light delivered through optical fibres controls their activity with **millisecond** precision.
| Tool | Type | Light | Effect |
|---|---|---|---|
| **ChR2** (channelrhodopsin-2) | cation channel | blue (~470 nm) | **depolarises** → spikes |
| ChRmine, Chrimson | cation channels | red-shifted | activation, deeper tissue |
| **NpHR** (halorhodopsin) | Cl⁻ pump | yellow (~590 nm) | hyperpolarises → silencing |
| ArchT | H⁺ pump | green-yellow | silencing |
| GtACR | anion channel | blue | strong silencing (caution: depolarising at axon terminals with high Cl⁻) |

**Chemogenetics (DREADDs):** designer GPCRs that respond only to an otherwise inert ligand ([[Bio03 Proteins and Enzymes]]).
- **hM3Dq** (Gq) increases excitability; **hM4Di** (Gi) silences (GIRK activation, less release).
- Ligands: CNO (but it is back-converted to clozapine, so controls are needed), **deschloroclozapine (DCZ)**, compound 21.
- Timescale: **minutes to hours**, with no implant needed (injection), which makes them good for chronic or brain-wide modulation but not for temporal precision.

## Delivering genes: viral vectors
| Vector | Capacity | Integration | Notes |
|---|---|---|---|
| **AAV** (adeno-associated virus) | **~4.7 kb** | mostly episomal (stays as a separate DNA circle in the nucleus) | low immunogenicity, long-lasting expression in neurons; **serotypes** set the tropism (AAV1/2/5/8/9; AAV-PHP.eB crosses the BBB in some mouse strains; AAVretro for retrograde access) |
| Lentivirus | ~8 kb | integrates | larger cargo; also for dividing cells |
| Rabies (ΔG, pseudotyped) | – | – | **monosynaptic retrograde tracing** of inputs onto starter cells |
| HSV, CAV-2 | large / – | – | retrograde, large cargo |

**Specificity comes from:**
1. **Promoters:** hSyn (pan-neuronal), CaMKIIα (excitatory neurons), GFAP (astrocytes), mDlx (interneurons).
2. **Cre-lox:** Cre-driver mice (PV-Cre, SST-Cre, DAT-Cre, …) combined with **Cre-dependent (DIO/FLEX) AAVs**. The transgene is inverted and only turned the right way by Cre.
3. Injection site and serotype; intersectional strategies (Cre + Flp).

**Gene therapy:** AAV9-*SMN1* (onasemnogene, Zolgensma) for spinal muscular atrophy; AAV therapies in trials for other monogenic brain diseases.

## In neuroscience #neuro
**A typical modern circuit experiment:**
1. A Cre-driver mouse (e.g. DAT-Cre).
2. Inject a Cre-dependent AAV with ChR2 into the VTA.
3. Implant an optical fibre.
4. Stimulate during behaviour, which shows that **activating dopamine neurons is sufficient** to reinforce actions.
5. Confirm expression afterwards by IF (TH + ChR2-eYFP colocalisation) and quantify c-Fos.

Add photometry or calcium imaging ([[Meth04 In Vivo Imaging]]) to measure natural activity, and silencing (NpHR/hM4Di) to test **necessity**.

## Math links #math-link
- PCR: $N = N_0\cdot2^n$, efficiency $E$: $N = N_0(1 + E)^n$ → [[A1 Exponent Rules]], [[B2 Exponential Functions]]
- ΔΔCt: fold change $= 2^{-\Delta\Delta\text{Ct}}$, i.e. Ct is a $\log_2$ scale → [[A3 Logarithms]]
- ELISA standard curves: 4-parameter logistic (sigmoid on a log axis) → [[B1 Properties of Functions]], [[B3 Logarithmic Functions]]
- Light attenuation in tissue for optogenetics → [[B2 Exponential Functions]]
- Necessity vs. sufficiency (loss- vs. gain-of-function) → [[E1 Sets Logic and Quantifiers]]
- CRISPR off-target probability: a 20-nt guide matches by chance once in $4^{20}\approx10^{12}$ bases → [[A1 Exponent Rules]]

## Connections
- DNA, RNA, expression → [[Bio04 Nucleic Acids and Gene Expression]]
- Proteins and GPCRs (DREADDs) → [[Bio03 Proteins and Enzymes]]
- Opsins as ion channels/pumps → [[Bio02 Membranes and Transport]]
- Imaging stained tissue → [[Meth01 Microscopy]]
- Indicators delivered by AAV → [[Meth04 In Vivo Imaging]]
- Sequencing-based readouts → [[Meth06 Omics and Sequencing]]

## Key takeaways
- PCR doubles DNA per cycle (denature–anneal–extend). In qPCR, ΔCt = 1 is a factor of 2 and fold change $= 2^{-\Delta\Delta\text{Ct}}$.
- Western blot gives size and relative amount; ELISA gives quantitative concentration; IHC/IF gives location in tissue. Always use proper controls.
- CRISPR–Cas9: guide RNA + PAM, DSB → NHEJ knockout or HDR knock-in.
- Optogenetics (ms, light, opsins) vs. DREADDs (minutes–hours, ligand, GPCRs). AAVs + promoters + Cre-lox give cell-type specificity.
