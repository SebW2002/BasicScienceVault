---
tags: [programming, python, neuro-packages, type/solution]
---
# Py10 Python Neuroscience Packages – Solutions

> Worksheet: [[Py10 Python Neuroscience Packages - Worksheet]] · Theory: [[Py10 Python Neuroscience Packages]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. a) NiBabel b) SpikeInterface (`run_sorter("kilosort4", ...)`) c) MNE-Python d) dandi-cli e) Brian2 (or NEST) f) NEURON g) fMRIPrep h) Elephant (`cv(isi(st))`).
2. `Raw`, `Epochs`, `Evoked`.
3. Volts; 50 µV = `5e-5`.

## Level 2
4. It wraps many non-Python tools (FSL, ANTs, FreeSurfer, AFNI) in fixed versions. A container ships all of them, identical on every machine → reproducible preprocessing ([[CS13 Reproducibility and Research Software]]).
5. The mapping from voxel indices to world coordinates (mm, scanner or template space): voxel size, orientation, origin. Without it you don't know which voxel corresponds to which brain location, so you can't align images or compare subjects (after normalisation to MNI space).
6. To avoid unit errors: e.g. passing spike times in ms to a function expecting s (rates off by 1000), or mixing mV and V in an equation; Brian2 refuses dimensionally inconsistent equations.
7. 300 time points (volumes) × 45,000 voxels (inside the mask). Next: scikit-learn (decoding) or Nilearn's connectivity/GLM tools.

## Level 3
8. Each epoch runs from 200 ms before to 800 ms after the event; the mean of the pre-stimulus interval (start to 0) is subtracted per channel. At 500 Hz: 1.0 s × 500 + 1 = **501 samples** (both ends included).
9. Epochs in which any EEG channel has a peak-to-peak amplitude above 150 µV.
10. Voxels 3 × 3 × 3.5 mm, TR = 2.0 s; 300 × 2 s = 600 s = 10 min.

## Level 4
11. PsychoPy (stimuli, triggers) → BIDS conversion (`mne-bids`) → MNE: filter 0.1–30 Hz, re-reference, ICA for blinks, epochs around targets/standards, baseline, rejection → per subject: mean amplitude 300–500 ms at Pz for each condition → group: paired t-test or mixed model ([[R08 R Mixed-Effects Models]]), or cluster-based permutation test over channels × time in MNE.
12. Neo (`neo.io.PlexonIO`) to read → (SpikeInterface for sorting/curation if raw) → PyNWB (or NeuroConv, which wraps these) to write NWB with metadata → `nwbinspector` to validate → `dandi upload`.
13. ```python
    import mne
    path = mne.datasets.sample.data_path()
    raw = mne.io.read_raw_fif(path / "MEG" / "sample" / "sample_audvis_raw.fif")
    print(raw.info["sfreq"], len(mne.pick_types(raw.info, meg=False, eeg=True)))
    # ≈ 600.6 Hz, 60 EEG channels
    # without download:
    import numpy as np
    info = mne.create_info(["Fz", "Cz", "Pz", "Oz"], sfreq=250, ch_types="eeg")
    raw = mne.io.RawArray(np.random.default_rng(0).standard_normal((4, 2500)) * 1e-5, info)
    print(raw)
    ```
