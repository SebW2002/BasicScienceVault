---
aliases: [MATLAB Data Import, readtable, readmatrix, mat files, Struct Arrays, Cell Arrays, fullfile, dir]
tags: [programming, matlab, data-format, structs, type/overview, neuro]
---
# MAT04 MATLAB Data Import and Files

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT04 MATLAB Data Import and Files - Worksheet|✏️ Worksheet]] · [[MAT04 MATLAB Data Import and Files - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
MATLAB analyses read behavioural tables, `.mat` files from other labs and toolbox outputs, and they loop over folder structures with dozens of subjects. The key containers – **tables**, **structs** and **cell arrays** – are how EEGLAB (`EEG` struct), FieldTrip (`data.trial{…}`) and SPM store everything.

## readtable, readmatrix, load, save
```matlab
T = readtable("data/raw/sub-01_task-faces.csv");     % table with named, typed columns
T = readtable("events.tsv", "FileType", "text", "Delimiter", "\t");
opts = detectImportOptions("export.csv"); opts.VariableTypes{1} = 'char';  % control types
T = readtable("export.csv", opts);
M = readmatrix("lfp.csv");                            % numbers only → plain matrix
C = readcell("mixed.xlsx");                           % everything as cells
writetable(T, "data/derived/trials_clean.csv");
writematrix(M, "out.csv");
```
- **Tables** (`table`) are MATLAB's data frames: `T.rt`, `T(T.rt > 0.15, :)`, `T.rt_ms = T.rt * 1000`, `summary(T)`, `groupsummary(T, "condition", "mean", "rt")`, `join(T, P, "Keys", "subject")`, `stack/unstack` for long ↔ wide. `timetable` adds a time index (`retime` for resampling).
- **Categorical** columns: `T.condition = categorical(T.condition);` (like R factors).
- Missing values: `NaN` for numbers, `missing`/`<undefined>`; `rmmissing(T)`, `ismissing(T)`, `fillmissing`.
- `importdata`, `csvread`, `xlsread` are older functions – prefer `readtable`/`readmatrix`.

## .mat files
```matlab
save("results.mat", "erp", "times", "chanlocs");   % save selected variables (binary)
save("results.mat", "erp", "-append");              % add to an existing file
save("big.mat", "data", "-v7.3");                   % > 2 GB variables, HDF5-based
load("results.mat")                                  % pours ALL variables into the workspace
S = load("results.mat");                             % safer: into a struct, S.erp, S.times
S = load("results.mat", "erp");                      % only one variable
m = matfile("big.mat"); seg = m.data(1:10, 1:1000); % partial loading (v7.3)
whos("-file", "results.mat")                         % list contents without loading
```
- **`S = load(...)`** avoids variables silently overwriting your workspace (and makes clear where `erp` came from).
- Versions: `-v7` (default, compressed, ≤ 2 GB per variable), `-v7.3` (HDF5: large data, partial loading; readable by `h5py`, `rhdf5`, [[Py04 Python Files and Data Formats]], [[R09 R Neuroscience Packages]]). Python's `scipy.io.loadmat` reads v7 files; for v7.3 use `h5py`/`pymatreader`.
- `.mat` is MATLAB's "native" format – convenient within MATLAB, less so for sharing (prefer CSV/TSV, HDF5, NWB, BIDS; [[CS05 Data Formats and Representation]]).
- `jsondecode(fileread("sub-01_eeg.json"))` / `jsonencode(s, "PrettyPrint", true)` for JSON metadata.

## Struct arrays and cell arrays
**Struct:** named fields of any type – like a Python dict or R named list.
```matlab
info.subject = "sub-01";
info.fs = 1000;
info.bad = {'T7', 'Oz'};
info.fs                       % 1000
fieldnames(info), isfield(info, "fs")
f = "fs"; info.(f)            % dynamic field name
```
**Struct array:** many structs with the same fields – e.g. one element per trial or per channel:
```matlab
trials(1).condition = "face"; trials(1).rt = 0.42;
trials(2).condition = "house"; trials(2).rt = 0.55;
numel(trials)                 % 2
[trials.rt]                   % [0.42 0.55]  (comma-separated list → concatenate)
mean([trials.rt])
EEG.chanlocs(3).labels        % EEGLAB: label of channel 3
{EEG.chanlocs.labels}         % all labels as a cell array
struct2table(trials)          % → table
```
**Cell array:** a container of arbitrary items, indexed with `{}` for the contents and `()` for sub-cells:
```matlab
c = {'Fz', [1 2 3], struct("a", 1)};
c{2}                          % [1 2 3]  (content)
c(2)                          % {[1 2 3]} (a 1×1 cell)
data.trial{5}                 % FieldTrip: channels × time matrix of trial 5 (trials can differ in length)
cellfun(@(x) size(x, 2), data.trial)   % number of samples per trial
```
Cells are needed when elements have **different sizes or types** (trials of different length, channel names as char).

## Folder structures: dir, fullfile
```matlab
root = fileparts(mfilename("fullpath"));            % folder of the running script
raw  = fullfile(root, "..", "data", "raw");
files = dir(fullfile(raw, "sub-*", "eeg", "*_eeg.set"));  % wildcard search
for k = 1:numel(files)
    fpath = fullfile(files(k).folder, files(k).name);
    [~, base, ext] = fileparts(fpath);
    ...
end
files = dir(fullfile(raw, "**", "*.vhdr"));         % recursive (all subfolders)
if ~isfolder(out), mkdir(out); end
isfile(fpath), exist(fpath, "file")
```
- `fullfile` inserts the right separator (`/` or `\`) for the operating system.
- `dir` returns a **struct array** with fields `name`, `folder`, `date`, `bytes`, `isdir`; `dir` also lists `.` and `..` when you ask for a folder – filter with a pattern or `[files.isdir]`.
- Sort explicitly if order matters (`sort({files.name})`): `dir` order is alphabetical, so `sub-10` comes before `sub-2` unless IDs are zero-padded.

## Same idea in Python and R
| MATLAB | Python | R |
|---|---|---|
| `readtable` | `pd.read_csv` | `readr::read_csv` |
| `save/load .mat` | `np.save`, pickle, `scipy.io` | `saveRDS/readRDS` |
| struct | dict / dataclass | named list |
| cell array | list | list |
| struct array | list of dicts / DataFrame | data frame / list |
| `fullfile`, `dir` | `pathlib.Path`, `glob` | `file.path`, `list.files`, `here` |
→ [[Py04 Python Files and Data Formats]], [[R04 R Data Import and Tidy Data]]

## In neuroscience #neuro
- **EEGLAB's `EEG` struct:** `EEG.data` (channels × time × trials), `EEG.srate`, `EEG.chanlocs` (struct array), `EEG.event` (struct array with `type`, `latency` in samples) ([[MAT09 EEGLAB]]).
- **FieldTrip raw data:** `data.trial` and `data.time` are **cell arrays** (one cell per trial), `data.label` a cell of channel names, `data.fsample` ([[MAT10 MATLAB Neuroscience Toolboxes]]).
- **SPM** stores the whole first-level model in `SPM.mat` as a big struct.
- **BIDS loop:** `dir(fullfile(bids, "sub-*", "eeg", "*_task-oddball_eeg.vhdr"))` finds every subject's file.
- Psychtoolbox experiments typically save one `.mat` per participant with a results struct – convert to tables/CSV for analysis in R.

## Math links #math-link
- Matrices vs. collections of differently sized arrays → [[C1 Matrices]]
- Sample indices ↔ times (`latency / srate`) → [[Prog00 Shared Programming Concepts]]

## Connections
- Basics, char vs. string → [[MAT01 MATLAB Basics and Syntax]]
- Formats, metadata, BIDS → [[CS05 Data Formats and Representation]]
- Toolbox data structures → [[MAT09 EEGLAB]], [[MAT10 MATLAB Neuroscience Toolboxes]]
- Paths and projects → [[MAT12 MATLAB Reproducible Projects]]

## Key takeaways
- `readtable` for tables (MATLAB's data frame), `readmatrix` for plain numbers.
- `S = load(...)` into a struct; `-v7.3` for big data (HDF5, partial loading).
- Struct = named fields; struct array: `[s.field]` collects values; cell `{}` for mixed sizes/types (`c{k}` content, `c(k)` cell).
- `fullfile` + `dir` (with `**` for recursion) for folder loops; zero-pad IDs.
