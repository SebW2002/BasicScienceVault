---
tags: [programming, matlab, type/solution]
---
# MAT04 MATLAB Data Import and Files – Solutions

> Worksheet: [[MAT04 MATLAB Data Import and Files - Worksheet]] · Theory: [[MAT04 MATLAB Data Import and Files]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. a) `readtable` b) `readmatrix` c) `save(..., "-v7.3")` d) `m = matfile("f.mat"); m.var(1:10, :)` e) `whos("-file", "f.mat")` f) `fullfile`.
2. Variables go into a struct (`S.erp`) instead of being created in (and overwriting) the workspace; it's explicit where they come from, and it works inside functions without "hidden" variables.
3. `char`; `cell`; `double` (value 3).

## Level 2
4. `[0.4 0.6 0.5]`; `0.5`; `3`; a 1 × 1 struct with field `rt = 0.6`.
5. $t = (2501 - 1)/500 = 5.0$ s after the first sample.
6. `labels = string({EEG.chanlocs.labels});`
7. Trials can have **different lengths** (e.g. variable trial durations) and a matrix needs equal sizes; a cell array holds one channels × time matrix per trial.

## Level 3
8. a) `Tv = T(T.rt >= 0.15 & T.rt <= 2, :);` b) `T.rt_ms = T.rt * 1000;` c) `groupsummary(T, "condition", "mean", "rt")` (or `varfun(@mean, T, "InputVariables", "rt", "GroupingVariables", "condition")`).
9. `dir` sorts names **alphabetically** as text: "1" < "10" < "2". Fix: zero-pad IDs (`sub-01`, `sub-02`, `sub-10`), or extract the number and sort numerically: `n = str2double(extractBetween({files.name}, "sub-", ".csv")); [~, i] = sort(n); files = files(i);`.
10. ```matlab
    files = dir(fullfile("bids", "**", "*_events.tsv"));
    events_all = table();      % not "all": that would shadow the built-in all()
    for k = 1:numel(files)
        f = fullfile(files(k).folder, files(k).name);
        t = readtable(f, "FileType", "text", "Delimiter", "\t");
        t.file = repmat(string(files(k).name), height(t), 1);
        events_all = [events_all; t]; %#ok<AGROW>
    end
    ```
    (Columns must match across files for vertical concatenation.)

## Level 4
11. Loop over the participants' `.mat` files with `dir`; `S = load(f, "res")`; `t = struct2table(S.res)`; add a `subject` column (from the file name); stack the tables; `writetable(trials_all, "trials_all.csv")`. In R: `read_csv("trials_all.csv")` ([[R04 R Data Import and Tidy Data]]).
12. `h5py` (or `pymatreader` / `mat73`, which wrap it). Arrays may appear **transposed** (MATLAB is column-major, HDF5/NumPy row-major), so a 64 × 5000 MATLAB matrix often arrives as 5000 × 64 – check shapes. Strings and cells are stored as references and need extra decoding.
13. ```matlab
    s = struct("trial", {1, 2, 3}, "cond", {"face", "house", "face"}, "rt", {0.42, 0.55, 0.48});
    T = struct2table(s);
    T.rt_ms = T.rt * 1000;
    writetable(T, "trials.csv");
    T2 = readtable("trials.csv", "TextType", "string");
    isequal(T.rt_ms, T2.rt_ms)   % true (watch text columns: char vs. string types)
    ```
