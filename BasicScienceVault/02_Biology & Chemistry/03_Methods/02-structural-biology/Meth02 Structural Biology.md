---
aliases: [Structural Biology, X-ray Crystallography, NMR Spectroscopy, Mass Spectrometry, Cryo-EM SPA, Strukturbiologie]
tags: [methods, structural-biology, cryo-em, mass-spec, type/overview, neuro]
---
# Meth02 Structural Biology

> [[MOC-methods|↑ Methods MOC]] · [[Meth02 Structural Biology - Worksheet|✏️ Worksheet]] · [[Meth02 Structural Biology - Solutions|✅ Solutions]] · [[Mistakes - Methods|⚠️ Mistake log]]

## Why this matters
How does a K⁺ channel select K⁺ over Na⁺? Where exactly does a benzodiazepine bind on the GABA_A receptor? Why do tau fibrils from different dementias look different? Answering such questions requires **atomic structures**. Structural biology also enables rational drug design, and mass spectrometry tells us *which* proteins are present and how they are modified.

## Resolution in Å (1 Å = 0.1 nm)
| Resolution | What you can see |
|---|---|
| > 8 Å | overall shape, domains |
| 4–8 Å | α-helices as rods, β-sheets |
| ~3–4 Å | backbone trace, big side chains, ligand density |
| < 2.5 Å | individual side chains, water molecules, ions in the filter |

A C–C bond is about 1.5 Å long, and a protein is roughly 30–100 Å across.

## X-ray crystallography
1. Purify the protein and grow a **crystal** (the hardest step, especially for membrane proteins).
2. Shine X-rays (λ ≈ 1 Å) on it. The ordered lattice **diffracts** them into a pattern of spots.
3. **Bragg's law** gives where constructive interference occurs:
   $$n\lambda = 2d\sin\theta$$
   ($d$ = spacing of lattice planes, $\theta$ = angle of incidence, $n$ = integer order). Smaller $d$ means larger angles and higher resolution.
4. **Phase problem:** the detector measures only spot **intensities** (amplitude²), not their **phases**. Phases come from heavy-atom derivatives, anomalous scattering or molecular replacement with a similar known structure.
5. An **electron density map** is computed (inverse Fourier transform), and an atomic model is built and refined.

- **Strengths:** often very high resolution (1–3 Å); mature, well-established method; most entries in the Protein Data Bank (PDB).
- **Limitations:** needs crystals; gives a static snapshot; crystal packing can distort flexible parts.
- **Neuro milestone:** **KcsA** K⁺ channel (MacKinnon 1998, Nobel 2003) revealed the selectivity filter: carbonyl oxygens that mimic K⁺'s hydration shell ([[Ch01 Atomic Structure]]). Also Kv1.2, the AChBP (a homologue of the nicotinic receptor binding site), and GluA2 AMPA receptor domains.

## NMR spectroscopy
- Atomic nuclei with spin (¹H, ¹³C, ¹⁵N) behave like tiny magnets in a strong magnetic field $B_0$. They absorb radio waves at their **Larmor frequency**
  $$f = \frac{\gamma}{2\pi}B_0\qquad(\text{¹H: }42.58\,\text{MHz/T})$$
- The **chemical shift** (in ppm) shows each nucleus's chemical environment. Couplings and the nuclear Overhauser effect (NOE, for distances < ~5–6 Å) give distance and angle restraints, from which a structure ensemble is calculated.
- **Strengths:** proteins **in solution**, near physiological conditions; **dynamics** on ps–s timescales; binding and folding studies; intrinsically disordered proteins (e.g. α-synuclein, tau).
- **Limitations:** size limit of roughly 30–50 kDa for full structures; needs isotope labelling (¹⁵N, ¹³C) and high concentrations.
- **Same physics as MRI:** MRI images the ¹H signal of water in the body ([[Meth04 In Vivo Imaging]]). MR spectroscopy (MRS) measures metabolites in the living brain (NAA, glutamate, GABA, lactate).

## Cryo-EM single-particle analysis
(See [[Meth01 Microscopy]] for vitrification.)
1. Purified protein (often a membrane protein in detergent or nanodiscs) is applied to a grid and vitrified.
2. Thousands of micrographs are collected, and ~10⁵–10⁶ particle images are picked.
3. **2D classification** removes junk and sorts views; **3D reconstruction** combines views from different orientations; refinement improves the map.
4. **3D classification** separates **different conformational states** from the same sample (e.g. open, closed and desensitised channels).
5. An atomic model is built into the map.

- **Strengths:** no crystals; large, flexible and membrane proteins; several states from one dataset; little material.
- **Limitations:** small proteins (< ~50 kDa) are hard; preferred orientations and denaturation at the air–water interface; expensive microscopes.
- **Neuro:** full-length AMPA, NMDA and GABA_A receptors with drugs bound (benzodiazepines, anaesthetics, neurosteroids); Nav/Cav channels with toxins; TRPV1 (2013, an early landmark); tau and α-synuclein filaments from patient brains with **disease-specific folds** (Alzheimer's vs. Pick's vs. CTE tau folds differ).

## Mass spectrometry (MS)
Molecules are **ionised**, separated by their **mass-to-charge ratio $m/z$**, and detected.
- **Ionisation:** **ESI** (electrospray; gentle; many charges per molecule; coupled to liquid chromatography, LC-MS) or **MALDI** (laser plus matrix; mostly singly charged ions; used for tissue imaging, MALDI-MSI).
- **Mass analysers:** time-of-flight (TOF; lighter ions fly faster), quadrupole, Orbitrap (very high resolution and accuracy).
- **Tandem MS (MS/MS):** a peptide is selected, **fragmented**, and the fragment masses reveal its **sequence**. Database search then identifies the protein.

**Proteomics workflow (bottom-up):**
1. Extract proteins.
2. Digest with **trypsin**, which cuts after Lys or Arg.
3. Separate peptides by LC.
4. MS/MS.
5. Identify peptides and infer proteins.
6. Quantify (label-free, SILAC, or TMT isotope tags).

See [[Meth06 Omics and Sequencing]] for proteomics at scale.

- **Post-translational modifications:** MS detects mass shifts, e.g. +80 Da for phosphorylation, +42 Da for acetylation, which are hard to see any other way.
- **Neuro:**
  - synaptic proteome (thousands of PSD proteins)
  - phosphoproteomics after learning
  - CSF and blood biomarkers (amyloid-β42/40 ratio, phospho-tau isoforms such as p-tau217 measured by MS-based assays)
  - neurotransmitter measurement in microdialysates (LC-MS)
  - cross-linking MS and native MS for protein complexes

## Prediction: AlphaFold and friends
Deep-learning methods (AlphaFold2 in 2021; Nobel 2024 to Hassabis, Jumper and Baker) predict protein structures from sequence with accuracy often comparable to experiments for well-folded domains. They are excellent for hypotheses and for fitting into cryo-EM maps, but they are less reliable for conformational changes, ligand binding, disordered regions and complexes. Experiments are still needed to show the states that matter for function.

## Comparison
| | X-ray | NMR | Cryo-EM SPA | MS |
|---|---|---|---|---|
| Sample | crystal | solution, labelled | vitrified solution | ionised peptides/proteins |
| Size | any (if it crystallises) | small (< ~50 kDa) | large (> ~50 kDa) | any (as peptides) |
| Output | atomic model | structure ensemble + dynamics | map + model, several states | identity, mass, modifications, abundance |
| Typical resolution | 1–3 Å | – (restraints) | 2–4 Å | mass accuracy in ppm |

## Math links #math-link
- Fourier series and transforms (spectra, convolution theorem, k-space) → [[B12 Fourier Analysis]]
- Bragg's law $n\lambda = 2d\sin\theta$ → [[D4 Unit Circle Trigonometry]], [[A8 Solving Equations]]
- Diffraction pattern = Fourier transform of the electron density; phases are complex arguments → [[E2 Complex Numbers]]
- Cryo-EM: projections and rotations in 3D (rotation matrices, Euler angles); averaging improves SNR ∝ $\sqrt N$ → [[C1 Matrices]], [[A2 Root Rules]]
- NMR: $f = \frac{\gamma}{2\pi}B_0$ is linear; ppm = parts per $10^6$ → [[A1 Exponent Rules]]
- MS: $m/z$ calculations, charge states $(M + zH)/z$ → [[A5 Fractions]]

## Connections
- Vitrification, EM physics → [[Meth01 Microscopy]]
- What the structures show → [[Bio02 Membranes and Transport]], [[Bio03 Proteins and Enzymes]]
- Proteomics at scale → [[Meth06 Omics and Sequencing]]
- MRI/MRS → [[Meth04 In Vivo Imaging]]

## Key takeaways
- X-ray: crystals + Bragg diffraction + the phase problem; high resolution, static.
- NMR: proteins in solution and their dynamics, limited to small proteins; the same physics as MRI.
- Cryo-EM SPA: no crystals, large membrane proteins, several conformations.
- MS: $m/z$ → identity, sequence (MS/MS), modifications and quantities (proteomics).
