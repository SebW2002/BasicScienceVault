---
aliases: [Methods MOC, Methods Overview, Methoden]
tags: [methods, type/moc]
---
# MOC – Methods in Neuroscience

> [[MOC-neuroscience-foundations|↑ Neuroscience Foundations]] · ⚠️ [[Mistakes - Methods]] · Biology: [[MOC-biology]]

## What this field is about
Every claim in a neuroscience paper rests on a method. Each method has a **scale**, a **proxy** (what it actually measures) and **limits**. Reading papers critically means asking: *what exactly was measured, at which resolution, and does it support a causal claim?*

## The methods landscape
| Spatial scale ↓ / Temporal scale → | **ms** (fast) | **s** | **min–h** / static |
|---|---|---|---|
| **Å–nm** (molecules) | – | – | X-ray, NMR, cryo-EM, cryo-ET, MS |
| **nm–µm** (synapses, cells) | patch clamp, voltage imaging | calcium imaging, two-photon | EM, super-resolution, IHC/IF |
| **µm–mm** (populations) | Neuropixels, MEAs, LFP, ECoG | calcium imaging (populations), fibre photometry | scRNA-seq, connectomics, spatial omics |
| **cm** (whole brain) | EEG, MEG | fMRI | PET, structural MRI, DTI |

*(Rough placement. Static methods such as EM and sequencing give snapshots of fixed tissue, not dynamics.)*

| # | Topic | Covers | Practice |
|---|---|---|---|
| Meth01 | [[Meth01 Microscopy]] | widefield, confocal, two-photon, SIM/STED/PALM/STORM, TEM/SEM, cryo-EM, cryo-ET | [[Meth01 Microscopy - Worksheet\|✏️]] · [[Meth01 Microscopy - Solutions\|✅]] |
| Meth02 | [[Meth02 Structural Biology]] | X-ray, NMR, cryo-EM SPA, mass spectrometry, AlphaFold | [[Meth02 Structural Biology - Worksheet\|✏️]] · [[Meth02 Structural Biology - Solutions\|✅]] |
| Meth03 | [[Meth03 Electrophysiology]] | patch clamp, extracellular, Neuropixels, EEG/ECoG/MEG | [[Meth03 Electrophysiology - Worksheet\|✏️]] · [[Meth03 Electrophysiology - Solutions\|✅]] |
| Meth04 | [[Meth04 In Vivo Imaging]] | fMRI/BOLD, PET, calcium imaging, voltage imaging | [[Meth04 In Vivo Imaging - Worksheet\|✏️]] · [[Meth04 In Vivo Imaging - Solutions\|✅]] |
| Meth05 | [[Meth05 Molecular Biology Tools]] | PCR/qPCR, Western, ELISA, IHC/IF, CRISPR, optogenetics, DREADDs, AAV | [[Meth05 Molecular Biology Tools - Worksheet\|✏️]] · [[Meth05 Molecular Biology Tools - Solutions\|✅]] |
| Meth06 | [[Meth06 Omics and Sequencing]] | RNA-seq, scRNA-seq, proteomics, connectomics | [[Meth06 Omics and Sequencing - Worksheet\|✏️]] · [[Meth06 Omics and Sequencing - Solutions\|✅]] |

**Suggested order:** Meth03 (electrophysiology, closest to [[Bio05 Neurons and Action Potentials]]) → Meth01 → Meth04 → Meth05 → Meth02 → Meth06. Do the methods after the matching biology notes.

## Three questions to ask about any method
1. **Proxy:** what does it actually measure? BOLD measures oxygenation, not spikes. GCaMP measures Ca²⁺, not voltage. An antibody band means "something binds the antibody", not necessarily the protein you want.
2. **Resolution:** in space, in time, and in which cell types?
3. **Inference:** correlation (recording, imaging) or causation (lesion, opto/chemogenetics)? Necessity (loss-of-function) or sufficiency (gain-of-function)? See [[E1 Sets Logic and Quantifiers]].

## Bridges
- **To computer science (data analysis):** formats → [[CS05 Data Formats and Representation]]; spike sorting & spectra → [[CS11 Time Series and Signal Processing]]; fMRI/EEG/MEG analysis → [[CS12 Neuroimaging Data Analysis]]; scRNA-seq clustering → [[CS07 Machine Learning Fundamentals]]
- **To physics:**
  - Fourier, filters, sampling → [[Ph09 Waves and Oscillations]]
  - TMS, MEG, MRI → [[Ph06 Magnetism and Induction]]
  - optics, diffraction, fluorescence → [[Ph11 Optics and Fluorescence]]
  - photon energy, two-photon, opsins → [[Ph12 Quantum Basics for Biophysics]]
- **To math:**
  - Fourier transforms (microscopy, crystallography, EEG) → [[E2 Complex Numbers]]
  - GLM and linear systems (fMRI, source localisation) → [[C1 Matrices]], [[C3 Linear Systems and Gaussian Elimination]]
  - PCA (spike sorting, scRNA-seq, population activity) → [[C4 Eigenvalues and Eigenvectors]]
  - exponential growth and decay (PCR, PET, indicators) → [[B2 Exponential Functions]]
  - logs (qPCR Ct, fold changes) → [[A3 Logarithms]]
  - $\sqrt N$ averaging → [[A2 Root Rules]]
- **To chemistry:**
  - isotopes → [[Ch01 Atomic Structure]]
  - detergents → [[Ch03 Intermolecular Forces and Solubility]]
  - pH indicators → [[Ch04 Acids Bases and pH]]
  - recording solutions → [[Ch06 Solutions and Concentration]]

## Progress
- [ ] Meth03 Electrophysiology
- [ ] Meth01 Microscopy
- [ ] Meth04 In Vivo Imaging
- [ ] Meth05 Molecular Biology Tools
- [ ] Meth02 Structural Biology
- [ ] Meth06 Omics and Sequencing
