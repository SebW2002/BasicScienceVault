---
aliases: [Microscopy, Confocal, Two-photon, Super-resolution, Electron Microscopy, Cryo-EM, Cryo-ET, Mikroskopie]
tags: [methods, microscopy, super-resolution, electron-microscopy, cryo-em, type/overview, neuro]
---
# Meth01 Microscopy

> [[MOC-methods|↑ Methods MOC]] · [[Meth01 Microscopy - Worksheet|✏️ Worksheet]] · [[Meth01 Microscopy - Solutions|✅ Solutions]] · [[Mistakes - Methods|⚠️ Mistake log]]

## Why this matters
Neuroscience began with microscopy: Golgi's silver stain and Cajal's drawings established the neuron doctrine. Today microscopy spans scales from whole cortical columns in living animals (two-photon imaging) through single synapses (super-resolution) to the atomic structure of receptors (cryo-EM). Choosing a method means trading off **resolution, depth, speed, field of view, live vs. fixed, and labelling**.

## The resolution limit (light)
Light is diffracted, so a point source appears as a blurred spot (the **point spread function**, PSF). Two points can be separated only if they are farther apart than about the
$$\text{Abbe limit:}\quad d = \frac{\lambda}{2\,\text{NA}},\qquad \text{NA} = n\sin\theta$$
- $\lambda$ = wavelength; NA = numerical aperture of the objective; $n$ = refractive index of the immersion medium (air 1.0, water 1.33, oil 1.52); $\theta$ = half-angle of the light cone.
- With visible light (≈ 500 nm) and NA 1.4: **lateral ≈ 200 nm**, axial ≈ 500–800 nm.
- Synaptic vesicles (~40 nm), the synaptic cleft (~20 nm) and receptors (~10 nm) are **below** this limit.

## Light microscopy
| Method | Principle | Strengths | Limitations | Neuro use |
|---|---|---|---|---|
| **Widefield (epifluorescence)** | whole field illuminated, camera detects | fast, simple, cheap, sensitive | out-of-focus blur; no optical sectioning | cultured neurons, slices, quick imaging |
| **Confocal** (point scanning) | laser focused to a point; a **pinhole** before the detector rejects out-of-focus light | **optical sectioning**, 3D stacks, multiple colours | slower; photobleaching; limited depth (≈ 100 µm in scattering tissue) | fixed tissue, immunofluorescence, morphology, colocalisation |
| Spinning disk confocal | many pinholes on a rotating disk | fast, gentle sectioning | less flexible | live imaging of cells |
| **Two-photon** | two infrared photons (e.g. 920 nm) absorbed **simultaneously**; excitation ∝ intensity², so it happens **only at the focal point** | intrinsic sectioning (no pinhole), **deep in scattering tissue** (~0.5–1 mm), less phototoxicity out of focus | expensive pulsed lasers; slower than widefield | **in vivo** calcium imaging of neuron populations and spines in awake animals |
| Light-sheet | thin sheet of light illuminates one plane; camera from the side | very fast, gentle, large volumes | needs transparent (cleared) or small samples | whole cleared brains (CLARITY, iDISCO), zebrafish larvae |

**Fluorescence basics:** a fluorophore absorbs a photon at a shorter wavelength and emits one at a longer wavelength (**Stokes shift**). Filters separate excitation and emission light. Labels include antibodies with dyes (immunofluorescence, [[Meth05 Molecular Biology Tools]]), fluorescent proteins (GFP and relatives, Nobel 2008) and indicators (GCaMP, [[Meth04 In Vivo Imaging]]).

## Super-resolution microscopy (Nobel 2014: Betzig, Hell, Moerner)
| Method | Trick | Resolution (lateral) | Notes |
|---|---|---|---|
| **SIM** (structured illumination) | patterned illumination creates moiré fringes; high spatial frequencies are recovered computationally | ~100–120 nm (2× better) | fast, works with normal dyes, live imaging possible |
| **STED** (stimulated emission depletion) | a donut-shaped depletion beam switches off fluorescence around the focus, leaving a tiny effective spot: $d\approx\frac{\lambda}{2\text{NA}\sqrt{1 + I/I_\text{sat}}}$ | ~30–80 nm | point scanning; high laser power; used for spines and synaptic proteins in living tissue |
| **PALM / STORM** (single-molecule localisation) | only a sparse subset of fluorophores is "on" at a time; each spot's **centre** is fitted much more precisely than its width; repeat thousands of times | ~10–30 nm | precision $\approx\frac{\sigma_\text{PSF}}{\sqrt N}$ ($N$ = photons); slow (minutes); mostly fixed cells |
| Expansion microscopy | the tissue is physically swollen in a hydrogel (~4×, or more) | effective ~70 nm with a normal confocal | cheap; needs anchoring and careful validation |
| MINFLUX | combines localisation with a donut beam | ~1–5 nm | newest, very slow |

**Neuro discoveries:** a periodic actin–spectrin ring lattice (~190 nm spacing) in axons (STORM); nanocolumns aligning presynaptic release sites with postsynaptic receptors; spine dynamics in vivo (STED).

## Electron microscopy (EM)
Electrons have a tiny wavelength (de Broglie: about 2–4 **pm** at 100–300 kV), so the resolution is limited by the optics and the sample, not by diffraction. It reaches nm in biological samples. Requirements: vacuum, fixed or frozen samples, heavy-metal staining (osmium, uranyl, lead) for contrast in conventional EM.

| Method | Principle | Output | Neuro use |
|---|---|---|---|
| **TEM** (transmission) | electrons pass through an **ultrathin section** (~50–100 nm) | 2D projection image, nm detail | synaptic vesicles, PSD, myelin layers, the definition of chemical vs. electrical synapses |
| **SEM** (scanning) | focused beam scans the **surface**; secondary or backscattered electrons are detected | surface topography; with serial block-face SEM or FIB-SEM: 3D volumes | **connectomics**: dense 3D reconstruction of neural circuits ([[Meth06 Omics and Sequencing]]) |

**Immuno-EM:** antibodies coupled to gold nanoparticles localise proteins at nm precision.
**Correlative light–electron microscopy (CLEM):** find a fluorescent cell, then image the same spot with EM.

## Cryo-EM and cryo-ET
- **Cryo-electron microscopy:** samples are **flash-frozen** so fast that water forms **vitreous (glass-like) ice** instead of crystals. Molecules are preserved in a near-native, hydrated state without stain or fixation.
  - **Single-particle analysis (SPA):** images of many thousands to millions of copies of a purified protein in random orientations are classified, aligned and averaged into a 3D map. Resolution routinely reaches **2–4 Å** and in the best cases nearly atomic (~1.2 Å) ([[Meth02 Structural Biology]]).
  - Nobel prize 2017 (Dubochet, Frank, Henderson). The "resolution revolution" since ~2013 came from direct electron detectors and better software.
  - Neuro: structures of AMPA, NMDA and GABA_A receptors, TRPV1, Nav and Cav channels, the SNARE–synaptotagmin complex, and amyloid fibrils of tau and α-synuclein extracted from patient brains, which showed **disease-specific folds**.
- **Cryo-electron tomography (cryo-ET):** a frozen cell or tissue slice (often thinned by focused-ion-beam milling into a ~100–200 nm lamella) is **tilted** stepwise (e.g. −60° to +60°) and imaged at each angle. The images are computationally combined into a **3D tomogram** of molecules *in situ*.
  - Subtomogram averaging improves the resolution of repeated structures.
  - Limitation: the "**missing wedge**" of unreachable tilt angles distorts the 3D reconstruction slightly.
  - Neuro: synaptic vesicles tethered at the active zone, receptor arrangements in synapses, and aggregates inside neurons.

## Choosing a method
| Question | Method |
|---|---|
| Activity of 1000 neurons in an awake mouse | two-photon calcium imaging |
| Colocalisation of two proteins in fixed tissue | confocal (or super-resolution if < 200 nm matters) |
| Nanoscale arrangement of synaptic proteins | STORM/PALM, STED, expansion microscopy |
| Wiring diagram of a circuit | serial-section EM (connectomics) |
| Atomic structure of a receptor | cryo-EM single-particle analysis |
| Molecular architecture inside an intact synapse | cryo-ET |
| Whole-brain anatomy at cellular resolution | tissue clearing + light-sheet |

## Math links #math-link
- Fourier series and transforms (spectra, convolution theorem, k-space) → [[B12 Fourier Analysis]]
- $\text{NA} = n\sin\theta$ and the light cone → [[D4 Unit Circle Trigonometry]]
- Resolution formulas, square roots in STED and localisation precision → [[A2 Root Rules]], [[A5 Fractions]]
- Two-photon excitation ∝ $I^2$: a power law → [[A1 Exponent Rules]]
- Light attenuation in tissue $I(z) = I_0e^{-z/\ell}$ (scattering length) → [[B2 Exponential Functions]]
- Image formation as **convolution** with the PSF; SIM, cryo-EM and tomography reconstructions work in **Fourier space** → [[B7 Antiderivatives and Integration]], [[E2 Complex Numbers]]
- Tomography: rotations of the sample (rotation matrices) → [[C1 Matrices]]

## Connections
- Labelling: antibodies and IF → [[Meth05 Molecular Biology Tools]]
- Functional imaging (GCaMP, voltage) → [[Meth04 In Vivo Imaging]]
- Structural biology with cryo-EM → [[Meth02 Structural Biology]]
- EM connectomics → [[Meth06 Omics and Sequencing]]
- What you're looking at: [[Bio01 Cell Biology]], [[Bio06 Synapses and Neurotransmitters]]

## Key takeaways
- Light is diffraction-limited to $d = \lambda/(2\text{NA})\approx200$ nm.
- Confocal uses a pinhole for sectioning; two-photon uses $I^2$ excitation for depth in vivo.
- Super-resolution (SIM ×2, STED, PALM/STORM down to ~10–30 nm) beats the limit by controlling which fluorophores emit.
- EM gives nm resolution (TEM for sections, SEM for surfaces and volumes). Cryo-EM gives atomic protein structures; cryo-ET gives 3D molecular architecture in situ.
