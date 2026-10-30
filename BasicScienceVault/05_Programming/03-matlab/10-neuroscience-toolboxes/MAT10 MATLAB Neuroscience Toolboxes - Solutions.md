---
tags: [programming, matlab, neuro-packages, type/solution]
---
# MAT10 MATLAB Neuroscience Toolboxes – Solutions

> Worksheet: [[MAT10 MATLAB Neuroscience Toolboxes - Worksheet]] · Theory: [[MAT10 MATLAB Neuroscience Toolboxes]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. a) FieldTrip b) SPM c) CONN d) ERPLAB e) Brainstorm f) Chronux (or FieldTrip) g) Psychtoolbox h) MATLAB's `niftiread` (Image Processing Toolbox, R2017b+) – or the free NIfTI tools from File Exchange if that toolbox isn't available.
2. CONN needs SPM. Brainstorm's compiled stand-alone version runs without MATLAB (Psychtoolbox also runs in GNU Octave).
3. A struct holding all options for one FieldTrip function. It is stored in the output (`data.cfg`, including the previous steps), so the full analysis history is documented and can be re-run.

## Level 2
4. They ship copies of the same helper functions (sometimes different versions) and may shadow MATLAB built-ins; the one found first on the path wins, causing subtle errors. Add only the toolbox needed by a script, use its own setup function (`ft_defaults`, `eeglab nogui`), and `restoredefaultpath` between projects.
5. `ver` lists installed toolboxes; `license("test", "Signal_Toolbox")` checks the licence. Some toolbox functions call `butter`, `filtfilt`, `pwelch` etc.; without the licence they fail or fall back to their own (possibly different) implementations – results may differ.
6. Cogent is legacy software and may not run on current systems. Port the experiment to Psychtoolbox or PsychoPy, keeping the timing and conditions identical, and verify the new timing with a photodiode.
7. Defaults, algorithms and bug fixes change between versions; the exact version is needed to reproduce the analysis.

## Level 3
8. Each trial starts 0.2 s before and ends 0.8 s after the trigger event. `data.trial{3}` is a channels × time matrix of the third trial (with `data.time{3}` the corresponding time axis in s).
9. A list (cell array via `cellstr`) of all volumes ("file,1", "file,2", …) of the matching 4-D NIfTI file(s) – SPM needs one entry per volume. A saved batch documents all parameters and can be looped over subjects → reproducible.

## Level 4
10. SPM: DICOM → NIfTI (or BIDS), realign (+ unwarp), slice timing (optional), coregister the T1, segment and normalise to MNI, smooth; first-level GLM for the localiser (task regressors convolved with the HRF, motion regressors), contrasts; second-level group analysis. Resting state: CONN (denoising with CompCor, motion, band-pass; seed/ROI connectivity; group statistics). Scripts via SPM batch / CONN batch.
11. Save the EEGLAB dataset (`.set`) and read it in FieldTrip with `ft_preprocessing` (`cfg.dataset = "x.set"`) or convert with `eeglab2fieldtrip(EEG, "preprocessing", "none")`. Check that channel names, sampling rate, trial definitions and units match.
12. `ver` prints MATLAB's version and each toolbox (e.g. "Signal Processing Toolbox Version 24.x"); third-party toolboxes appear only if they provide a `Contents.m`. `license("test", "Statistics_Toolbox")` returns 1 if the licence is available.
