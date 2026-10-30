---
tags: [programming, matlab, eeglab, type/worksheet]
---
# MAT09 EEGLAB – Worksheet

> Theory: [[MAT09 EEGLAB]] · Solutions: [[MAT09 EEGLAB - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper; no calculator unless marked. Run code only for tasks marked 💻.

## Level 1 – Recall
1. What is the difference between `pop_epoch` and `epoch`? What happens if you call a `pop_` function with only `EEG`?
2. Give the units of `EEG.event(k).latency`, `EEG.times`, `EEG.xmin`, the limits in `pop_epoch` and the baseline in `pop_rmbase`.
3. Which plug-ins do you need to a) import BrainVision files b) classify ICA components c) detect bad channels and repair bursts d) import a whole BIDS dataset?
4. What do `EEG.icawinv` columns represent?

## Level 2 – Understanding
5. Why should you high-pass at 1 Hz before ICA? How do you still keep 0.1 Hz for the ERP analysis?
6. After average referencing and interpolating 2 of 64 channels, `runica` gives unstable results. Why? What option fixes it?
7. Explain how you turn a GUI session into a reproducible script.
8. Why does selecting epochs with `strcmp({EEG.epoch.eventtype}, "S  2")` sometimes fail?

## Level 3 – Calculate and write
9. Continuous data at 500 Hz; an event has latency 15001. At what time (s) does it occur? After `pop_epoch(EEG, {...}, [-0.2 0.8])`, how many points does each epoch have?
10. `EEG.data` after epoching is 64 × 500 × 180. Write the ERP of channel `Pz` averaged over all trials, and its time axis.
11. Write a script fragment: load `sub-01.set`, filter 0.1–30 Hz, average reference, epoch around `"S  1"` and `"S  2"` from −200 to 800 ms, baseline −200–0 ms, save.

## Level 4 – Neuro transfer
12. A 500 ms P300 window measured on data filtered with a 1 Hz high-pass looks smaller than in the literature. Why might that be?
13. ICLabel gives a component: "Eye 0.95", scalp map frontal, time course with large slow deflections. What is it and what do you do? Another one: "Brain 0.4, Muscle 0.35, Other 0.25" – what do you do?
14. 💻 Load EEGLAB's tutorial data set `eeglab_data.set` (in `eeglab/sample_data`), run `pop_eegfiltnew` 1–40 Hz, `pop_runica` and `pop_iclabel`, and list how many components ICLabel classifies as eye with probability ≥ 0.9.
