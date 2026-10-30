---
tags: [programming, python, neuro-packages, type/worksheet]
---
# Py10 Python Neuroscience Packages – Worksheet

> Theory: [[Py10 Python Neuroscience Packages]] · Solutions: [[Py10 Python Neuroscience Packages - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper. Run code only for tasks marked 💻.

## Level 1 – Which package?
1. Match each task to a package: a) read a `.nii.gz` file b) sort spikes from a Neuropixels probe with Kilosort c) compute ERPs from BrainVision EEG d) download an NWB dataset from an open archive e) simulate 10,000 LIF neurons f) simulate a pyramidal cell with its dendritic tree g) preprocess 50 fMRI datasets in a standardised way h) compute the CV of ISIs.
2. Which three main objects does MNE use for continuous data, trials and averages?
3. In which unit does MNE store EEG amplitudes? What value does 50 µV have in `epochs.get_data()`?

## Level 2 – Understanding
4. Why is fMRIPrep distributed as a container rather than a pip package?
5. What does the `affine` of a NIfTI image encode? Why do you need it to compare two subjects?
6. Why do Neo and Brian2 use quantities with units? Give an error it prevents.
7. `NiftiMasker.fit_transform(img)` returns an array of shape (300, 45000). What are the two dimensions, and which library would you hand it to next?

## Level 3 – Read code
8. In the MNE example, what do `tmin=-0.2, tmax=0.8, baseline=(None, 0)` mean? How many samples does one epoch have at 500 Hz?
9. `reject=dict(eeg=150e-6)`: which epochs are dropped?
10. A NIfTI header says zooms `(3.0, 3.0, 3.5, 2.0)`. What are the voxel size and the TR? How long is a run of 300 volumes?

## Level 4 – Neuro transfer
11. Sketch a complete pipeline (packages and steps) from an oddball EEG experiment to a group-level P300 result.
12. You get a dataset from a collaborator as Plexon `.plx` files and want to upload it to DANDI. Which packages do you use, in which order?
13. 💻 Install MNE and load its sample data (`mne.datasets.sample.data_path()`, ~1.5 GB). Read the raw file `MEG/sample/sample_audvis_raw.fif`, print `raw.info["sfreq"]` and the number of EEG channels. (Optional: skip the download and instead create a fake `RawArray` with 4 channels at 250 Hz.)
