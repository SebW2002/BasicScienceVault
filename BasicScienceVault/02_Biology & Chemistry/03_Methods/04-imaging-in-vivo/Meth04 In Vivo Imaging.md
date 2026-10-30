---
aliases: [In Vivo Imaging, fMRI, BOLD, PET, Calcium Imaging, GCaMP, Voltage Imaging, Bildgebung]
tags: [methods, fmri, pet, calcium-imaging, imaging, type/overview, neuro]
---
# Meth04 In Vivo Imaging

> [[MOC-methods|↑ Methods MOC]] · [[Meth04 In Vivo Imaging - Worksheet|✏️ Worksheet]] · [[Meth04 In Vivo Imaging - Solutions|✅ Solutions]] · [[Mistakes - Methods|⚠️ Mistake log]]

## Why this matters
Imaging lets us watch the living brain at work: whole-brain activity in humans (fMRI), molecules such as dopamine receptors or amyloid plaques (PET), and the activity of thousands of identified neurons in behaving animals (calcium and voltage imaging). Each method measures a **proxy** of neural activity, and interpreting it correctly requires knowing what that proxy is.

## Overview
| Method | What it measures | Spatial res. | Temporal res. | Species |
|---|---|---|---|---|
| **fMRI (BOLD)** | blood oxygenation changes (indirect) | ~1–3 mm (sub-mm at 7 T) | seconds (HRF ~5 s to peak) | humans, animals |
| **PET** | distribution of a radiotracer | ~2–5 mm | minutes | humans, animals |
| **Calcium imaging** | intracellular Ca²⁺ (≈ spiking) | single cells/spines | ~10–100 ms (indicator-limited) | mainly animals |
| **Voltage imaging** | membrane potential directly | single cells | ~1 ms | mainly animals |
| (EEG/MEG for comparison) | electrical/magnetic fields | cm | ms | humans |

## fMRI and the BOLD signal
**MRI physics in brief:** hydrogen nuclei in water align in the strong field (3 T clinical, 7 T research). A radio-frequency pulse tips them over, and as they relax they emit a signal (the same physics as NMR, [[Meth02 Structural Biology]]). Magnetic field gradients encode spatial position. Contrast comes from relaxation times (T1, T2, T2*).

**BOLD (blood-oxygen-level-dependent) contrast:**
1. **Deoxyhaemoglobin is paramagnetic.** It distorts the local field and shortens T2*, so the signal is lower. Oxyhaemoglobin is diamagnetic (little effect).
2. Neural activity, mainly **synaptic** activity, raises energy use.
3. **Neurovascular coupling** (astrocytes, NO, prostaglandins, pericytes) dilates arterioles. **Blood flow increases far more than O₂ consumption**.
4. Locally, deoxyhaemoglobin is "washed out" and the BOLD signal **increases**.

**Haemodynamic response function (HRF):** after a brief stimulus, there is sometimes an initial dip, then a peak at about **4–6 s**, an undershoot, and a return to baseline after ~15–20 s.

**Implications:**
- BOLD is **indirect** and **slow**. It reflects input and local processing (LFP) more than spiking output (Logothetis et al. 2001).
- It can't directly distinguish excitation from inhibition.
- Statistics: the **general linear model (GLM)** models each voxel's time series as the stimulus convolved with the HRF, plus nuisance regressors. Many voxels mean **multiple comparisons** (FWE, FDR, cluster-level correction).

**Other MRI modalities:**
- structural (T1, T2) for anatomy and volumetry
- **diffusion MRI/DTI** for white-matter tracts ([[Ch06 Solutions and Concentration]])
- resting-state fMRI for functional connectivity
- ASL for perfusion
- MRS for metabolites (glutamate, GABA, lactate)

## PET (positron emission tomography)
1. A **radiotracer** (a molecule labelled with a positron emitter) is injected.
2. A positron is emitted, travels ~1 mm and **annihilates** with an electron, producing **two 511 keV gamma photons** in opposite directions (~180°).
3. A detector ring registers **coincidences**. Reconstruction gives the 3D tracer distribution, and kinetic modelling gives quantitative parameters.

| Isotope | Half-life | Consequence |
|---|---|---|
| ¹⁵O | ~2 min | blood flow (H₂¹⁵O); on-site cyclotron needed |
| ¹¹C | ~20 min | receptor ligands (raclopride, PiB); on-site cyclotron needed |
| ¹⁸F | ~110 min | can be shipped; clinical tracers |

| Tracer | Target | Use |
|---|---|---|
| **[¹⁸F]FDG** | glucose uptake (hexokinase traps FDG-6-P) | metabolism; tumour and epilepsy focus; dementia patterns |
| **[¹¹C]raclopride** | D2/D3 receptors | competition with endogenous dopamine: **lower binding when dopamine release rises** (reward, amphetamine) |
| [¹⁸F]FDOPA | dopamine synthesis capacity (AADC) | Parkinson's, schizophrenia research |
| DAT tracers ([¹²³I]FP-CIT SPECT, "DaTscan") | dopamine transporter | Parkinson's vs. essential tremor |
| **Amyloid**: [¹¹C]PiB, [¹⁸F]florbetapir, flutemetamol, florbetaben | amyloid-β plaques | Alzheimer's diagnosis and eligibility for anti-amyloid antibodies |
| **Tau**: [¹⁸F]flortaucipir and others | tau tangles | Braak staging in vivo |
| [¹¹C]PBR28, TSPO tracers | activated microglia/astrocytes | neuroinflammation |

**Strengths:** molecular specificity, absolute quantification. **Limitations:** radiation dose, slow time resolution, cost, cyclotron logistics.

## Calcium imaging
**Why Ca²⁺?** Each action potential opens voltage-gated Ca²⁺ channels, so intracellular Ca²⁺ rises briefly from about 50–100 nM. Ca²⁺ is a good optical **proxy for spiking**.

**Indicators:**
- Synthetic dyes: Fura-2 (ratiometric), Oregon Green BAPTA, Cal-520.
- **Genetically encoded calcium indicators (GECIs)**, above all **GCaMP**: circularly permuted GFP + calmodulin + the M13 peptide. Ca²⁺ binding changes the conformation and increases fluorescence.
  - Variants trade speed for brightness: GCaMP6s (slow, bright), GCaMP6f (fast), jGCaMP7, **jGCaMP8** (faster rise, single-AP detection).
  - Red indicators (jRGECO, jRCaMP) allow two colours.
  - Expressed cell-type-specifically via AAVs or transgenic lines ([[Meth05 Molecular Biology Tools]]).

**Signal:**
$$\frac{\Delta F}{F} = \frac{F - F_0}{F_0}$$
A single AP gives a fast rise and a slow decay (hundreds of ms to > 1 s, set by indicator kinetics and Ca²⁺ buffering). Spike trains summate. **Deconvolution** estimates the underlying spikes.

**Microscopes:** **two-photon** (cellular resolution, deep, head-fixed animals, [[Meth01 Microscopy]]); **miniscopes** (head-mounted one-photon via GRIN lenses in freely moving animals); fibre photometry (bulk signal from a population); widefield (cortex-wide mesoscale).

**Limitations:** indirect and slow relative to spikes; poorly reflects subthreshold activity and inhibition; non-linear (saturation); Ca²⁺ buffering by the indicator itself; motion artefacts; neuropil contamination.

## Voltage imaging
Directly reports **membrane potential** with ms resolution, including subthreshold potentials, spikes and hyperpolarisation.
- **Voltage-sensitive dyes (VSDs):** fast and suited to mesoscale population signals, but not cell-specific.
- **Genetically encoded voltage indicators (GEVIs):** e.g. ASAP family, Voltron (chemigenetic), Archon, QuasAr (rhodopsin-based).
- **Challenges:** signals are small (a few % to a few tens of % $\Delta F/F$ per AP), and the indicator sits only in the thin membrane (few molecules). Kilohertz imaging is needed (fewer photons per frame), so there is a **photon budget** problem and photobleaching. Field of view is still more limited than with calcium imaging.
- **All-optical electrophysiology:** voltage imaging plus optogenetic stimulation (e.g. Optopatch).

## In neuroscience #neuro
- **Human cognition:** fMRI maps the fusiform face area, default mode network, and reward signals in the ventral striatum. Combined with EEG it gives both where and when.
- **Clinical:** amyloid and tau PET for Alzheimer's diagnosis and treatment trials; FDG-PET in epilepsy and dementia; DaTscan in parkinsonism; presurgical fMRI to map language and motor areas.
- **Animal systems neuroscience:** two-photon imaging of place cells, of plasticity of spines and activity over weeks, and of the same neurons across learning (chronic imaging).

## Math links #math-link
- Fourier series and transforms (spectra, convolution theorem, k-space) → [[B12 Fourier Analysis]]
- BOLD: the measured signal is the stimulus **convolved** with the HRF, $y(t) = \int h(s)\,x(t - s)\,ds$; GLM $\mathbf y = X\boldsymbol\beta + \boldsymbol\varepsilon$, $\hat{\boldsymbol\beta} = (X^TX)^{-1}X^T\mathbf y$ → [[B7 Antiderivatives and Integration]], [[C1 Matrices]], [[C3 Linear Systems and Gaussian Elimination]]
- Multicollinear regressors make $\det(X^TX)\approx0$ → [[C2 Determinants]]
- PET: radioactive decay $N(t) = N_0e^{-t\ln2/t_{1/2}}$ → [[B2 Exponential Functions]], [[A3 Logarithms]]
- $\Delta F/F$ is a ratio; Ca²⁺ indicator saturation follows the Hill equation → [[A5 Fractions]]
- Ca²⁺ transients as sums of exponential kernels; deconvolution → [[B2 Exponential Functions]], [[A7 Sums Products and Factorials]]
- Population activity → PCA, neural trajectories → [[C4 Eigenvalues and Eigenvectors]], [[D1 Vectors in 2D and 3D]]

## Connections
- In code → [[Py10 Python Neuroscience Packages]] (NiBabel, Nilearn, fMRIPrep), [[MAT10 MATLAB Neuroscience Toolboxes]] (SPM, CONN), [[R09 R Neuroscience Packages]] (oro.nifti)
- Microscope technology → [[Meth01 Microscopy]]
- Electrical ground truth → [[Meth03 Electrophysiology]]
- Expressing indicators → [[Meth05 Molecular Biology Tools]]
- What's measured: [[Bio05 Neurons and Action Potentials]], [[Bio06 Synapses and Neurotransmitters]], [[Bio07 Neural Circuits and Systems]]
- Isotopes → [[Ch01 Atomic Structure]]

## Key takeaways
- fMRI BOLD comes from deoxyhaemoglobin being paramagnetic plus neurovascular coupling (flow ≫ O₂ use). It is indirect, slow (HRF peak at 4–6 s) and mm-scale.
- PET: positron annihilation produces two 511 keV photons. Tracers target receptors, transporters, metabolism, amyloid or tau. Half-lives decide logistics.
- Calcium imaging (GCaMP, ΔF/F) is a proxy for spikes, slow but cellular. Voltage imaging is direct and fast but photon-limited.
