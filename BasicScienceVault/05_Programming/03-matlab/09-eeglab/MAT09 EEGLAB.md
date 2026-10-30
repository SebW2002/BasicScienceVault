---
aliases: [EEGLAB, pop_loadset, pop_runica, pop_epoch, ICLabel, Clean Rawdata, ERPLAB]
tags: [programming, matlab, eeglab, eeg, ica, type/overview, neuro]
---
# MAT09 EEGLAB

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT09 EEGLAB - Worksheet|✏️ Worksheet]] · [[MAT09 EEGLAB - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
**EEGLAB** (Swartz Center for Computational Neuroscience, UC San Diego) is the most widely used open-source MATLAB toolbox for EEG: import, filtering, re-referencing, **ICA**-based artefact removal, epoching, ERPs, time–frequency analysis and a large plug-in ecosystem. It has a GUI for exploring and a function interface for scripting – and the GUI writes the scripts for you. Concepts of the signals → [[Meth03 Electrophysiology]], [[CS11 Time Series and Signal Processing]].

## GUI and scripting
```matlab
addpath("toolboxes/eeglab2025.0");     % example folder name – use your installed version
[ALLEEG, EEG, CURRENTSET, ALLCOM] = eeglab;   % starts the GUI and adds sub-folders/plug-ins to the path
% or, for scripts on a cluster:
eeglab nogui
```
- Every GUI action calls a **`pop_` function** (`pop_` = "pop-up": with fewer arguments it opens a dialog; with all arguments it runs silently). The core computations are in non-pop functions (`runica`, `epoch`, `newtimef`).
- **History:** `EEG.history` stores the commands applied to a dataset; `eegh` prints the session's commands. Explore in the GUI, then copy the history into a script → reproducible ([[Prog00 Shared Programming Concepts]]).
- `ALLEEG` holds all loaded datasets, `EEG` the current one; in scripts you can mostly work with `EEG` alone.

## The EEG structure
| Field | Content |
|---|---|
| `EEG.data` | channels × points (× trials once epoched), in µV |
| `EEG.srate` | sampling rate (Hz) |
| `EEG.nbchan`, `EEG.pnts`, `EEG.trials` | sizes |
| `EEG.times` | time of each sample in **ms** (epochs: e.g. −200 … 798) |
| `EEG.xmin`, `EEG.xmax` | epoch limits in **s** |
| `EEG.chanlocs` | struct array: `labels`, coordinates (for topoplots) |
| `EEG.event` | struct array: `type`, `latency` (in **samples**, 1-based), `epoch` |
| `EEG.icaweights`, `EEG.icasphere`, `EEG.icawinv`, `EEG.icaact` | ICA unmixing, sphering, mixing (scalp maps), component activations |
| `EEG.etc` | extra info (e.g. ICLabel classifications, clean_rawdata masks) |
After changing `EEG` by hand, run `EEG = eeg_checkset(EEG);` to keep the structure consistent.

## Loading and importing data
```matlab
EEG = pop_loadset("filename", "sub-01_task-oddball_eeg.set", "filepath", fullfile(root, "derived"));
EEG = pop_loadbv(fullfile(raw, "sub-01", "eeg"), "sub-01_task-oddball_eeg.vhdr");  % BrainVision (bva-io plug-in)
EEG = pop_biosig(fullfile(raw, "sub-01.edf"));                                     % EDF/BDF (BIOSIG plug-in)
[STUDY, ALLEEG] = pop_importbids(bidsroot, "outputdir", outdir);                   % whole BIDS dataset (bids-matlab-tools plug-in)
EEG = pop_chanedit(EEG, "lookup", "standard_1005.elc");                             % channel locations
EEG = pop_saveset(EEG, "filename", "sub-01_clean.set", "filepath", outdir);
```
`.set` files contain the structure (and optionally the data; large data go into a matching `.fdt` file – keep both together).

## Filtering, re-referencing, artefact removal (ICA)
```matlab
EEG = pop_eegfiltnew(EEG, "locutoff", 1, "hicutoff", 40);   % windowed-sinc FIR, zero-phase
EEG = pop_reref(EEG, []);                                    % average reference ([] = average)
EEG = pop_clean_rawdata(EEG, "FlatlineCriterion", 5, "ChannelCriterion", 0.8, ...
        "LineNoiseCriterion", 4, "Highpass", "off", "BurstCriterion", 20, ...
        "WindowCriterion", 0.25, "BurstRejection", "on");    % bad channels + ASR (Clean Rawdata plug-in)
EEG = pop_runica(EEG, "icatype", "runica", "extended", 1);  % ICA (Infomax)
EEG = pop_iclabel(EEG, "default");                           % classify components (ICLabel plug-in)
EEG = pop_icflag(EEG, [NaN NaN; 0.9 1; 0.9 1; NaN NaN; NaN NaN; NaN NaN; NaN NaN]);  % flag muscle/eye ≥ 90 %
EEG = pop_subcomp(EEG, find(EEG.reject.gcompreject), 0);    % remove flagged components
EEG = pop_interp(EEG, origChanlocs, "spherical");            % interpolate removed channels
```
- **ICA** decomposes the data into maximally independent sources: $\mathbf x = A\mathbf s$, unmixing $W = A^{-1}$ (`icaweights * icasphere`). Eye blinks, eye movements, muscle and heartbeat appear as separate components with typical scalp maps and time courses; removing them and back-projecting cleans the EEG ([[C4 Eigenvalues and Eigenvectors]], [[CS01 Mathematical Foundations]]).
- **Practical rules:** high-pass ≥ 1 Hz before ICA (slow drifts hurt the decomposition; you can compute ICA on a 1-Hz copy and apply the weights to a 0.1-Hz-filtered copy); remove bad channels/segments first; enough data (rule of thumb: ≥ 20–30 × channels² samples); the data rank decreases after average referencing or interpolation – reduce dimensions (`"pca", rank`) accordingly.
- Filter **order** and cut-offs, the reference, ICA algorithm and rejection criteria all belong in the methods section.

## Epochs, ERPs, time–frequency
```matlab
EEG = pop_epoch(EEG, {"S  1", "S  2"}, [-0.2 0.8]);   % event types, limits in seconds
EEG = pop_rmbase(EEG, [-200 0]);                      % baseline in milliseconds!
erp_oddball = mean(EEG.data(:, :, strcmp({EEG.epoch.eventtype}, "S  2")), 3);  % simplified selection
figure; pop_timtopo(EEG, [-200 800], [300 400]);      % butterfly + topographies
figure; pop_erpimage(EEG, 1, find(strcmp({EEG.chanlocs.labels}, "Pz")));      % trials sorted as an image
[ersp, itc, ~, times, freqs] = newtimef(EEG.data(chan, :, :), EEG.pnts, ...
        [EEG.xmin EEG.xmax] * 1000, EEG.srate, [3 0.5], "baseline", [-200 0], "plotitc", "off");
```
- `pop_epoch` limits are in **seconds**, `pop_rmbase` in **milliseconds** – a classic mix-up.
- Event type strings of BrainVision files contain spaces (`"S  1"`), so check `unique({EEG.event.type})`.
- **ERSP** (event-related spectral perturbation) = power change from baseline in dB; **ITC** (inter-trial coherence) = phase consistency across trials ([[E2 Complex Numbers]]). `[3 0.5]` = wavelets with 3 cycles at the lowest frequency, increasing with frequency.
- Group analyses: **STUDY** framework (`std_precomp`, `std_erpplot`) or export to MATLAB/R statistics ([[MAT07 MATLAB Statistics Toolbox]], [[R08 R Mixed-Effects Models]]).
- When epoching, `EEG.epoch(k).eventtype` can be a **cell array** if several events fall into one epoch – robust selection uses the time-locking event (`eventlatency == 0`).

## Plug-ins
Installed via *File → Manage EEGLAB extensions* (or downloaded into `eeglab/plugins/`):
| Plug-in | Use |
|---|---|
| **ICLabel** | automatic classification of ICA components (brain, muscle, eye, heart, line noise, channel noise, other) |
| **Clean Rawdata** (+ ASR) | detection of flat/noisy channels, artifact subspace reconstruction of bursts |
| **ERPLAB** | ERP analysis: event lists, bins, artefact detection, ERPsets, measurement (amplitudes, latencies) → [[MAT10 MATLAB Neuroscience Toolboxes]] |
| **bva-io**, **BIOSIG**, **bids-matlab-tools** | import BrainVision, EDF/BDF, BIDS |
| **firfilt** | the FIR filter behind `pop_eegfiltnew` (included) |
| **dipfit** | dipole fitting of ICA components |
| **PREP pipeline**, **Zapline-plus**, **AMICA** | robust referencing, line-noise removal, alternative ICA |

## Same idea in Python
MNE-Python covers the same pipeline (`raw.filter`, `ICA`, `mne_icalabel`, `Epochs`, `tfr_morlet`) and can read EEGLAB `.set` files (`mne.io.read_raw_eeglab`, `read_epochs_eeglab`) ([[Py10 Python Neuroscience Packages]]). FieldTrip is the main MATLAB alternative ([[MAT10 MATLAB Neuroscience Toolboxes]]).

## In neuroscience #neuro
- **Standard ERP pipeline:** import → channel locations → filter (0.1–30 Hz for ERPs; ICA on a 1 Hz copy) → bad channels → average reference → ICA + ICLabel → epoch → baseline → reject remaining artefacts → average per condition → measure mean amplitudes in time windows (e.g. P300 300–500 ms at Pz) → statistics.
- **Oscillations:** ERSP/ITC for event-related synchronisation/desynchronisation (e.g. alpha decrease, theta increase).
- **Source-level:** dipfit of ICA components; MEG/EEG source imaging is more common in FieldTrip/Brainstorm/MNE.

## Math links #math-link
- ICA as unmixing matrices, $\mathbf x = A\mathbf s$ → [[C1 Matrices]], [[C3 Linear Systems and Gaussian Elimination]]
- PCA/rank reduction before ICA → [[C4 Eigenvalues and Eigenvectors]]
- ERSP in dB, wavelets → [[B12 Fourier Analysis]], [[A3 Logarithms]]
- ITC as mean resultant vector length → [[E2 Complex Numbers]], [[D4 Unit Circle Trigonometry]]

## Connections
- Data structures (structs, cells) → [[MAT04 MATLAB Data Import and Files]]
- Filters and spectra → [[MAT06 MATLAB Signal Processing Toolbox]]
- Triggers from experiments → [[MAT08 Psychtoolbox]]
- Other toolboxes → [[MAT10 MATLAB Neuroscience Toolboxes]]
- EEG physics and recording → [[Meth03 Electrophysiology]], [[Ph03 Electric Fields and Potential]]

## Key takeaways
- GUI to explore, `pop_` functions to script; copy `EEG.history`/`eegh` into scripts.
- `EEG.data` channels × time × trials; `EEG.event.latency` in samples, `EEG.times` in ms, `pop_epoch` in s, `pop_rmbase` in ms.
- Filter (`pop_eegfiltnew`), re-reference (`pop_reref`), clean (`pop_clean_rawdata`), ICA (`pop_runica`) + ICLabel, epoch, baseline, average.
- Plug-ins extend import (BIDS, BrainVision, EDF), cleaning (Clean Rawdata, Zapline) and ERP analysis (ERPLAB).
