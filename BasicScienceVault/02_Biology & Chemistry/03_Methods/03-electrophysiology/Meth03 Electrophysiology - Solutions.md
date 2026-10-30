---
tags: [methods, electrophysiology, type/solution]
---
# Meth03 Electrophysiology – Solutions

> Worksheet: [[Meth03 Electrophysiology - Worksheet]] · Theory: [[Meth03 Electrophysiology]] · Wrong? → [[Mistakes - Methods]]

## Level 1
1. Cell-attached: single channels in the intact patch (or spikes). Whole-cell: total currents or the membrane potential of the cell. Inside-out: single channels with the cytosolic face to the bath. Outside-out: single channels with the extracellular face to the bath.
2. Voltage clamp: voltage fixed, **current** measured. Current clamp: current fixed (or injected), **voltage** measured.
3. Synchronous **postsynaptic currents** in parallel-aligned cortical **pyramidal cells** (an open field configuration). APs are too short (~1 ms) and rarely synchronous enough across thousands of cells, so their fields cancel and fall off quickly with distance.
4. Spikes: ~300–6000 Hz (high-pass). LFP: < ~300 Hz (low-pass).

## Level 2
5. Single-channel currents are a few pA. With a poor seal, leak currents around the pipette and their noise would swamp the signal. A > 1 GΩ seal minimises both (current noise ∝ $1/\sqrt R$ for thermal noise).
6. **Inside-out**: the intracellular face of the patch faces the bath, so you can apply defined Ca²⁺ concentrations directly and quickly, without the cell's own signalling.
7. Advantage: control of the intracellular solution (ions, drugs, dyes, blockers). Disadvantage: washout of second messengers and proteins, which can alter responses ("rundown"); Cl⁻ is set artificially. Alternative: **perforated patch** (amphotericin, gramicidin).
8. In a roughly spherical head, the magnetic field of **radial** dipoles (gyral crowns) cancels outside the head, while **tangential** dipoles (sulcal walls) produce measurable fields. EEG measures potentials, which arise from both orientations (although they are smeared by the skull).

## Level 3
9. $R = \frac{\Delta V}{\Delta I} = \frac{10\,\text{mV}}{50\,\text{pA}} = \frac{10^{-2}}{5\times10^{-11}} = 2\times10^8\,\Omega = 200\,\text{M}\Omega$
10. $\tau = RC = 2\times10^8\cdot10^{-10} = 2\times10^{-2}\,\text{s} = 20\,\text{ms}$
11. $I = \frac{V}{R} = \frac{70\times10^{-3}}{2\times10^{9}} = 3.5\times10^{-11}\,\text{A} = 35\,\text{pA}$. That's larger than a single-channel current (2 pA). In practice, leak is a constant offset that can be subtracted, but the noise from it limits resolution. Better seals (10+ GΩ) and smaller holding potentials help.
12. a) > 10 kHz (in practice 20–30 kHz). b) > 200 Hz (in practice 500–1000 Hz, also to allow anti-aliasing filters).
13. Noise in the average $= \frac{20}{\sqrt N} = 1\Rightarrow\sqrt N = 20\Rightarrow N = 400$ trials.

## Level 4
14. a) **ECoG / stereo-EEG** (intracranial; scalp EEG for initial screening). b) **Outside-out** (or cell-attached) **patch clamp** with fast glutamate application. c) **Neuropixels** (multi-shank) in a behaving mouse. d) **EEG or MEG** (ERPs such as the N400). e) **EEG** (polysomnography with EOG and EMG).
15. Amplitude depends mainly on the **distance and orientation** relative to the electrode, not only on cell type. The same neuron type can give large or small spikes. Cell-type identification needs more: spike width, firing pattern, optogenetic tagging, juxtacellular labelling, or ground-truth recordings.
16. $384\cdot30\,000\cdot2\,\text{bytes} = 23.04\,\text{MB/s}$; $\times3600\,\text{s}\approx82.9\,\text{GB/h}$.
