---
aliases: [MATLAB Neuroscience Toolboxes, FieldTrip, SPM, ERPLAB, Brainstorm, CONN, Chronux]
tags: [programming, matlab, neuro-packages, eeg, meg, fmri, type/overview, neuro]
---
# MAT10 MATLAB Neuroscience Toolboxes

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT10 MATLAB Neuroscience Toolboxes - Worksheet|✏️ Worksheet]] · [[MAT10 MATLAB Neuroscience Toolboxes - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
Much of today's standard methodology in EEG, MEG and fMRI was developed – and is still distributed – as MATLAB toolboxes: SPM's GLM and normalisation, FieldTrip's cluster-based permutation tests, EEGLAB's ICA, Brainstorm's source imaging. Knowing what each one does, what data structure it uses and what it needs (licences, other toolboxes) is essential for reading methods sections and choosing tools.

## The landscape
| Toolbox | What it does | Where to find it | Notes |
|---|---|---|---|
| **Psychtoolbox-3** | stimulus presentation, precise timing, input | psychtoolbox.org, GitHub `Psychtoolbox-3` | also runs in GNU Octave → [[MAT08 Psychtoolbox]] |
| **EEGLAB** | EEG analysis: ICA, ERPs, time–frequency, STUDY | sccn.ucsd.edu/eeglab | huge plug-in ecosystem → [[MAT09 EEGLAB]] |
| **ERPLAB** | ERP analysis as an EEGLAB plug-in: event lists, bins, artefact detection, amplitude/latency measures | erpinfo.org/erplab | developed with the ERP Boot Camp (Luck) |
| **FieldTrip** | MEG/EEG/iEEG/LFP: preprocessing, time–frequency (multitapers, wavelets), connectivity, source reconstruction, **cluster-based permutation statistics** | fieldtriptoolbox.org | no GUI; scripts with `cfg` structs |
| **SPM** | fMRI/PET/structural MRI: realignment, normalisation, segmentation, smoothing, **mass-univariate GLM**, random-field theory; also M/EEG and DCM | fil.ion.ucl.ac.uk/spm | SPM12 has been the standard release for years; batch system (`spm_jobman`) |
| **CONN** | functional connectivity of fMRI (seed-based, ROI-to-ROI, ICA, graph measures), denoising | web.conn-toolbox.org | needs SPM; GUI + batch |
| **Brainstorm** | MEG/EEG with a full GUI: import, preprocessing, source imaging, statistics | neuroimage.usc.edu/brainstorm | also as a compiled stand-alone version without a MATLAB licence |
| **NIfTI tools** ("Tools for NIfTI and ANALYZE image", J. Shen) | read/write NIfTI | MathWorks File Exchange | MATLAB itself has `niftiread`/`niftiinfo`/`niftiwrite` since R2017b (Image Processing Toolbox) |
| **Chronux** | multitaper spectral analysis of continuous data and spike trains, coherence | chronux.org | classic; no longer actively developed |
| **Cogent 2000** | experiment presentation (older) | vislab.ucl.ac.uk | legacy, Windows only; largely replaced by Psychtoolbox/PsychoPy |
| **BCILAB** | brain–computer interface design and evaluation | sccn.ucsd.edu/bcilab | development has largely stopped; check compatibility with current MATLAB |
| **SPM extensions** | e.g. CAT12 (voxel-based morphometry), MarsBaR (ROI analysis), xjView (viewing) | SPM extensions page, File Exchange | install into `spm/toolbox` |
| **BrainVoyager** (MATLAB access) | commercial fMRI/anatomy software (Brain Innovation); MATLAB access e.g. via NeuroElf/BVQXtools to read its file formats | brainvoyager.com | BrainVoyager itself is not a MATLAB toolbox |

> [!info] Licences
> Most of these toolboxes are free and open source, but they need **MATLAB itself** and partly the **Signal Processing** or **Statistics and Machine Learning Toolbox** (e.g. some FieldTrip and EEGLAB functions). Check your institute's MATLAB licence: `ver` lists installed toolboxes, `license("test", "Signal_Toolbox")` checks availability. Brainstorm's compiled version and the Octave-compatible parts of Psychtoolbox work without a MATLAB licence.

## FieldTrip in five lines
```matlab
addpath("toolboxes/fieldtrip"); ft_defaults            % sets up FieldTrip's path correctly
cfg = []; cfg.dataset = "sub-01_task-oddball_eeg.vhdr";
cfg.trialdef.eventtype = "Stimulus"; cfg.trialdef.eventvalue = {"S  1", "S  2"};
cfg.trialdef.prestim = 0.2; cfg.trialdef.poststim = 0.8;
cfg = ft_definetrial(cfg);
cfg.bpfilter = "yes"; cfg.bpfreq = [0.1 30]; cfg.reref = "yes"; cfg.refchannel = "all";
data = ft_preprocessing(cfg);                          % data.trial{k}: channels × time
cfg = []; cfg.trials = find(data.trialinfo == 2);
erp = ft_timelockanalysis(cfg, data);                  % erp.avg: channels × time
```
- Every function takes a **`cfg` struct** with options plus data, returns new data – easy to log (`cfg` is stored in `data.cfg`, the analysis history).
- Statistics: `ft_timelockstatistics` / `ft_freqstatistics` with `cfg.method = "montecarlo"; cfg.correctm = "cluster";` ([[MAT07 MATLAB Statistics Toolbox]]).

## SPM batch in brief
```matlab
spm("defaults", "fmri"); spm_jobman("initcfg");
matlabbatch{1}.spm.spatial.realign.estwrite.data = {cellstr(spm_select("ExtFPList", funcdir, "^sub-01.*bold\.nii$", Inf))};
spm_jobman("run", matlabbatch);
```
Build the batch in the GUI (*Batch editor*), save it as a `.m` file, and loop over subjects – the SPM equivalent of EEGLAB's history.

## Choosing a tool
| Data / question | Typical choice (MATLAB) | Python alternative |
|---|---|---|
| EEG preprocessing, ICA, ERPs | EEGLAB (+ ERPLAB) | MNE-Python |
| MEG, source imaging, cluster stats | FieldTrip, Brainstorm | MNE-Python |
| fMRI GLM, normalisation | SPM | fMRIPrep + Nilearn |
| fMRI connectivity | CONN | Nilearn |
| spike trains, multitapers | Chronux, FieldTrip | Elephant, SpikeInterface |
| experiments | Psychtoolbox | PsychoPy |
→ [[Py10 Python Neuroscience Packages]], [[R09 R Neuroscience Packages]]

## In neuroscience #neuro
- **Methods sections** name the toolbox **and version** (e.g. "FieldTrip version 2024-xx-xx", "SPM12 r7771") – versions change defaults.
- **Mixing toolboxes** on the path causes function-name clashes (EEGLAB, FieldTrip and SPM all include some versions of the same external functions); add only what a script needs ([[MAT01 MATLAB Basics and Syntax]]).
- **Data exchange:** FieldTrip ↔ EEGLAB (`eeglab2fieldtrip`, `ft_read_data` of `.set`), MNE reads `.set`/FieldTrip `.mat`; BIDS as common ground ([[CS05 Data Formats and Representation]]).

## Math links #math-link
- GLM and design matrices (SPM) → [[C3 Linear Systems and Gaussian Elimination]], [[CS12 Neuroimaging Data Analysis]]
- Multitaper/wavelet spectral estimates (FieldTrip, Chronux) → [[B12 Fourier Analysis]]
- Inverse problems in source imaging → [[CS12 Neuroimaging Data Analysis]], [[Ph06 Magnetism and Induction]]
- Permutation and cluster statistics → [[CS02 Probability and Statistics]]

## Connections
- EEGLAB in detail → [[MAT09 EEGLAB]]; Psychtoolbox → [[MAT08 Psychtoolbox]]
- Statistics → [[MAT07 MATLAB Statistics Toolbox]]
- Methods → [[Meth03 Electrophysiology]], [[Meth04 In Vivo Imaging]]
- Analysis concepts → [[CS11 Time Series and Signal Processing]], [[CS12 Neuroimaging Data Analysis]]

## Key takeaways
- EEG → EEGLAB/ERPLAB; MEG/EEG source & cluster stats → FieldTrip/Brainstorm; fMRI → SPM (+ CONN for connectivity); experiments → Psychtoolbox.
- FieldTrip: `ft_defaults`, `cfg` structs; SPM: batch system; both scriptable for reproducibility.
- Free toolboxes still need MATLAB (and sometimes paid toolboxes); several older tools (Cogent, BCILAB, Chronux) are no longer actively developed.
- Record toolbox versions; avoid path clashes.
