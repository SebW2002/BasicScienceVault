---
aliases: [Electrophysiology, Patch Clamp, Extracellular Recording, EEG, ECoG, MEG, Elektrophysiologie]
tags: [methods, electrophysiology, patch-clamp, eeg, type/overview, neuro]
---
# Meth03 Electrophysiology

> [[MOC-methods|↑ Methods MOC]] · [[Meth03 Electrophysiology - Worksheet|✏️ Worksheet]] · [[Meth03 Electrophysiology - Solutions|✅ Solutions]] · [[Mistakes - Methods|⚠️ Mistake log]]

## Why this matters
Electrophysiology measures what neurons actually do: electrical signals with **millisecond** precision. It ranges from the opening of a single ion channel (picoamperes) to the summed activity of millions of neurons measured on the scalp (microvolts). It is the reference method against which all indirect measures (fMRI, calcium imaging) are compared.

## Overview by scale
| Method | Measures | Spatial scale | Signal size | Invasiveness |
|---|---|---|---|---|
| Patch clamp | single channels, whole-cell currents and voltages | one channel / one cell | pA–nA, mV | in vitro / in vivo, invasive |
| Sharp intracellular electrode | membrane potential | one cell | mV | invasive |
| Extracellular single-unit / MEA / Neuropixels | spikes (APs) of individual neurons, LFP | ~50–100 µm around the electrode | spikes ~50–500 µV | invasive (implant) |
| ECoG | cortical field potentials from the surface | mm | ~100 µV–mV | semi-invasive (subdural, e.g. epilepsy surgery) |
| EEG | summed postsynaptic currents on the scalp | cm | ~10–100 µV | non-invasive |
| MEG | magnetic fields of those currents | cm (better than EEG for tangential sources) | ~10–1000 fT | non-invasive |

## Patch clamp (Neher & Sakmann, Nobel 1991)
A glass pipette (tip ~1 µm) filled with salt solution is pressed against the membrane. Gentle suction forms a **gigaseal** (> 1 GΩ). This high resistance means almost no current leaks around the pipette, so tiny currents become measurable with low noise.

| Configuration | How | What you measure | Notes |
|---|---|---|---|
| **Cell-attached** (on-cell) | seal formed, membrane intact | single channels in the patch (or spikes, non-invasively) | cell interior undisturbed |
| **Whole-cell** | rupture the patch with suction | **sum of all currents** of the cell (voltage clamp) or membrane potential (current clamp) | pipette solution **dialyses** the cell; low access resistance |
| **Inside-out** | pull the patch away from the cell (excised) | single channels; **intracellular face** exposed to the bath | test cytosolic modulators (Ca²⁺, ATP, G proteins) |
| Outside-out | pull away after whole-cell; membrane reseals | single channels; **extracellular face** to the bath | fast application of transmitters and drugs |
| Perforated patch | antibiotics (amphotericin, gramicidin) form pores in the patch | whole-cell without dialysis | keeps intracellular signalling (and Cl⁻ with gramicidin) intact |

**Recording modes**
- **Voltage clamp:** the amplifier holds $V$ constant and measures the **current** needed. Used for I–V curves, reversal potentials, synaptic currents (EPSCs/IPSCs) and channel kinetics. Hodgkin & Huxley used a voltage clamp on the squid axon.
- **Current clamp:** inject a defined current and measure the **voltage**. Used for firing patterns, EPSPs, input resistance and the membrane time constant.

**Typical analyses:**
- input resistance $R_\text{in} = \Delta V/\Delta I$ (Ohm's law)
- membrane time constant from an exponential fit
- reversal potential where $I = 0$
- quantal analysis of miniature EPSCs (minis)

## Extracellular recordings
An electrode in tissue picks up voltage changes caused by currents flowing in the extracellular space.
- **Spikes (single-unit activity):** brief (~1 ms) deflections of about 50–500 µV from neurons within ~50–100 µm. Recordings are high-pass filtered at about 300–6000 Hz.
- **Spike sorting:** separates the waveforms of several neurons recorded on one electrode (by shape, amplitude across channels and clustering). **Tetrodes** (four close wires) help triangulate.
- **Local field potential (LFP):** the low-frequency part (< ~300 Hz), mainly summed **synaptic** currents near the electrode, which shows oscillations (theta, gamma, sharp-wave ripples).
- **Multi-electrode arrays (MEAs):** planar arrays for cultures and slices; Utah arrays (100 electrodes) in humans for brain–computer interfaces.
- **Neuropixels probes:** silicon shanks with ~1000 recording sites (384 recorded simultaneously per shank in version 1.0), giving hundreds of neurons across many brain areas at once.
- **Juxtacellular recording** can label the recorded cell afterwards and identify its type.

## EEG, ECoG and MEG
**Where the signal comes from:** mainly **postsynaptic currents in cortical pyramidal cells**, which are aligned in parallel (an "open field"). When thousands of them are **synchronously** active, their dipoles add up. Action potentials contribute little because they are too brief and not synchronised enough.

| | EEG | ECoG | MEG |
|---|---|---|---|
| Sensors | electrodes on the scalp (10–20 system, up to 256) | electrode grids or strips on the cortex | SQUIDs (cooled with liquid helium) or new **OPMs** (optically pumped magnetometers, wearable) |
| Measures | electric potential differences | potentials directly at the cortex | magnetic field (~10⁻¹⁵ T) |
| Temporal resolution | ms | ms | ms |
| Spatial resolution | poor (cm); skull smears potentials | good (mm); high-gamma activity visible | better than EEG (magnetic fields are not distorted by the skull) |
| Sensitive to | radial **and** tangential sources | local cortex | mainly **tangential** sources (sulcal walls) |
| Practical | cheap, mobile, clinical standard | only with clinical indication (epilepsy, tumour surgery) | expensive, shielded room |

**Analysis:**
- **ERPs** (event-related potentials) are averaged over trials; noise falls with $\sqrt N$. Examples: P300, N400, mismatch negativity.
- **Frequency analysis** (spectra; delta, theta, alpha, beta, gamma), time–frequency analysis, phase locking, connectivity.
- **Source localisation** solves an ill-posed **inverse problem**.

**Clinical uses:** epilepsy diagnosis (spikes, seizures), sleep staging (polysomnography), anaesthesia monitoring, coma and brain death assessment; ECoG to map seizure foci and eloquent cortex.

## In neuroscience #neuro
- **Classic discoveries:** the ionic basis of the AP (voltage clamp), single-channel currents (patch clamp), place cells (single units, O'Keefe 1971), orientation tuning (Hubel & Wiesel), the alpha rhythm (Berger 1929, EEG).
- **Combining methods:** patch clamp + optogenetics (identify connections), Patch-seq (patch clamp + RNA-seq + morphology of the same cell), Neuropixels + behaviour.
- **Brain–computer interfaces:** Utah arrays and ECoG decode movement or speech intentions in paralysed patients.

## Math links #math-link
- Fourier series and transforms (spectra, convolution theorem, k-space) → [[B12 Fourier Analysis]]
- Ohm's law $V = IR$, input resistance; seal resistance in GΩ → [[A1 Exponent Rules]], [[A8 Solving Equations]]
- Exponential fits for $\tau$; charging curves → [[B2 Exponential Functions]], [[B3 Logarithmic Functions]]
- **Sampling:** the Nyquist theorem says to sample at more than twice the highest frequency in the signal (spikes: ≥ 20–30 kHz; EEG: ≥ 250–1000 Hz) → [[B4 Trigonometric Functions]]
- Filtering and spectra via the Fourier transform → [[E2 Complex Numbers]]
- Averaging ERPs: SNR improves with $\sqrt N$ → [[A2 Root Rules]]
- Source localisation: $\mathbf x = L\mathbf s$ (lead field matrix), an underdetermined linear system → [[C3 Linear Systems and Gaussian Elimination]]
- Spike sorting: PCA of waveforms + clustering → [[C4 Eigenvalues and Eigenvectors]]
- MEG blindness to radial dipoles: cross product → [[D2 Dot and Cross Product]]

## Connections
- In code → [[Py10 Python Neuroscience Packages]] (MNE, SpikeInterface, Neo), [[MAT09 EEGLAB]], [[MAT10 MATLAB Neuroscience Toolboxes]] (FieldTrip), [[Py11 PsychoPy Experiment Control]] / [[MAT08 Psychtoolbox]] (triggers)
- What is being measured → [[Bio05 Neurons and Action Potentials]], [[Bio06 Synapses and Neurotransmitters]]
- Channels and currents → [[Bio02 Membranes and Transport]]
- Solutions for pipettes and baths → [[Ch06 Solutions and Concentration]]
- Optical alternatives (Ca²⁺ and voltage imaging) → [[Meth04 In Vivo Imaging]]

## Key takeaways
- Patch clamp: a gigaseal; cell-attached, whole-cell, inside-out and outside-out configurations; voltage clamp measures current, current clamp measures voltage.
- Extracellular: spikes (high-pass, single units) + LFP (low-pass, synaptic); Neuropixels records hundreds of neurons at once.
- EEG, ECoG and MEG measure synchronised postsynaptic currents of pyramidal cells with ms resolution. MEG sees tangential sources; ECoG has the best spatial resolution.
