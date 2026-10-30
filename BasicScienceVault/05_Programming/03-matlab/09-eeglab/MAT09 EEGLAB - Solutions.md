---
tags: [programming, matlab, eeglab, type/solution]
---
# MAT09 EEGLAB – Solutions

> Worksheet: [[MAT09 EEGLAB - Worksheet]] · Theory: [[MAT09 EEGLAB]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. `pop_epoch` is the user-level wrapper: it takes the `EEG` structure, checks inputs, can open a dialog, updates the structure and history. `epoch` is the low-level function working on data arrays. With only `EEG`, a `pop_` function opens its GUI dialog to ask for the parameters.
2. `latency`: samples (1-based, continuous data); `EEG.times`: ms; `EEG.xmin`: s; `pop_epoch` limits: s; `pop_rmbase` baseline: ms.
3. a) bva-io b) ICLabel c) Clean Rawdata (ASR) d) bids-matlab-tools.
4. Each column is the **scalp map** (mixing weights over channels) of one independent component.

## Level 2
5. Slow drifts are large, non-stationary and dominate the decomposition, so ICA separates sources poorly; 1 Hz high-pass improves component quality. Keep a copy filtered at 0.1 Hz, compute ICA on the 1 Hz copy, then copy `icaweights`/`icasphere` to the 0.1 Hz data and remove components there.
6. Average referencing removes one dimension, interpolation two more: the data rank is 61, not 64. ICA on rank-deficient data produces duplicate/unstable ("ghost") components. Use `pop_runica(EEG, "icatype", "runica", "extended", 1, "pca", 61)` (or EEGLAB's automatic rank detection).
7. After exploring in the GUI, type `eegh` (or look at `EEG.history`), copy the `pop_` calls into a script, replace hard-coded file names with variables/`fullfile`, wrap in a subject loop, and run the script from raw data.
8. When several events fall into one epoch, `eventtype` is a **cell array** of all event types in that epoch, so the comparison doesn't return one logical per epoch (or errors). Select by the time-locking event (latency 0), e.g. with a helper that checks `EEG.epoch(k).eventtype{find(cell2mat(EEG.epoch(k).eventlatency) == 0)}`, or use `pop_selectevent`.

## Level 3
9. $t = (15001 - 1)/500 = 30.0$ s. Epoch −0.2 … 0.8 s at 500 Hz: 1.0 s × 500 = **500 points** (EEGLAB excludes the end point; −200 to 798 ms).
10. ```matlab
    ch = find(strcmp({EEG.chanlocs.labels}, "Pz"));
    erp = mean(EEG.data(ch, :, :), 3);     % 1 × 500
    t = EEG.times;                          % ms
    plot(t, erp)
    ```
11. ```matlab
    EEG = pop_loadset("filename", "sub-01.set", "filepath", datadir);
    EEG = pop_eegfiltnew(EEG, "locutoff", 0.1, "hicutoff", 30);
    EEG = pop_reref(EEG, []);
    EEG = pop_epoch(EEG, {"S  1", "S  2"}, [-0.2 0.8]);
    EEG = pop_rmbase(EEG, [-200 0]);
    EEG = pop_saveset(EEG, "filename", "sub-01_epochs.set", "filepath", outdir);
    ```

## Level 4
12. The P300 is a slow, long-lasting component; a 1 Hz high-pass attenuates its low-frequency content and can distort it (reduced amplitude, artificial opposite-polarity deflections). Use 0.1 Hz (or lower) for ERP measurement; apply 1 Hz only to the ICA copy.
13. First: a blink/eye-movement component – remove it (high probability, typical frontal map and slow time course). Second: ambiguous – inspect scalp map, spectrum and time course; when in doubt **keep** it (removing brain activity is worse than leaving some noise), or decide by a pre-registered rule.
14. ```matlab
    eeglab nogui
    EEG = pop_loadset("filename", "eeglab_data.set", "filepath", fullfile(fileparts(which("eeglab")), "sample_data"));
    EEG = pop_eegfiltnew(EEG, "locutoff", 1, "hicutoff", 40);
    EEG = pop_runica(EEG, "icatype", "runica", "extended", 1);
    EEG = pop_iclabel(EEG, "default");
    p = EEG.etc.ic_classification.ICLabel.classifications;   % components × 7 classes
    nEye = sum(p(:, 3) >= 0.9)                               % column 3 = "Eye"
    ```
    Class order: Brain, Muscle, Eye, Heart, Line Noise, Channel Noise, Other.
