---
tags: [programming, matlab, neuro-packages, type/worksheet]
---
# MAT10 MATLAB Neuroscience Toolboxes – Worksheet

> Theory: [[MAT10 MATLAB Neuroscience Toolboxes]] · Solutions: [[MAT10 MATLAB Neuroscience Toolboxes - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper. Run code only for tasks marked 💻.

## Level 1 – Which toolbox?
1. Match: a) cluster-based permutation test on MEG data b) first-level fMRI GLM c) seed-based resting-state connectivity d) ERP amplitude measurement with bins e) MEG source imaging with a GUI f) multitaper spectra of spike trains g) presenting Gabor patches with precise timing h) read a NIfTI file without extra toolboxes.
2. Which toolbox needs SPM to be installed? Which one runs without a MATLAB licence?
3. What is a FieldTrip `cfg`? Why is it useful for reproducibility?

## Level 2 – Understanding
4. Why might adding EEGLAB, FieldTrip and SPM to the path at the same time cause problems? How do you avoid it?
5. Your institute has MATLAB but not the Signal Processing Toolbox. Which commands tell you this, and why does it matter for some toolboxes?
6. A 2012 script uses Cogent 2000 for stimulus presentation. What do you do if you need to run the experiment on a new Windows 11 PC?
7. Why should a methods section state "FieldTrip version 20xx-xx-xx" rather than just "FieldTrip"?

## Level 3 – Read code
8. In the FieldTrip example, what do `cfg.trialdef.prestim = 0.2` and `poststim = 0.8` mean? What does `data.trial{3}` contain?
9. In the SPM batch example, what does `spm_select("ExtFPList", ...)` return, and why is a batch saved as `.m` file useful?

## Level 4 – Neuro transfer
10. Sketch a MATLAB-only pipeline for an fMRI study with a localiser task and a resting-state scan (toolboxes, main steps).
11. You want to compare an EEGLAB-preprocessed dataset with a FieldTrip-based statistics pipeline. How do you move data between them?
12. 💻 Run `ver` in MATLAB and list which of the toolboxes from the note (and which MathWorks toolboxes) are installed; check `license("test", "Statistics_Toolbox")`.
