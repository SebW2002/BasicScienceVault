---
aliases: [Python Files, CSV JSON Pickle, h5py, Zarr, pynwb, Context Manager]
tags: [programming, python, data-format, hdf5, nwb, type/overview, neuro]
---
# Py04 Python Files and Data Formats

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py04 Python Files and Data Formats - Worksheet|✏️ Worksheet]] · [[Py04 Python Files and Data Formats - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
Every analysis begins by reading a file and ends by writing one. The format decides whether your data stay **readable, complete (with metadata) and safe**. This note is the practical side of [[CS05 Data Formats and Representation]]: how to read and write text, CSV, JSON, Pickle, HDF5, Zarr and NWB from Python.

## Paths with pathlib
```python
from pathlib import Path
root = Path(__file__).resolve().parent.parent   # project root (in a script)
raw = root / "data" / "raw"
for f in sorted(raw.glob("sub-*_eeg.edf")):     # all matching files
    print(f.name, f.stem, f.suffix)
(root / "data" / "derived").mkdir(parents=True, exist_ok=True)
```
`/` joins path parts on every operating system ([[Prog00 Shared Programming Concepts]]).

## Context managers: with open(...)
```python
with open("notes.txt", "w", encoding="utf-8") as f:   # "r" read, "w" overwrite, "a" append
    f.write("sub-01: bad channel T7\n")
# file is closed here, even if an error happened inside the block
with open("notes.txt", encoding="utf-8") as f:
    for line in f:                 # iterate line by line (memory-friendly)
        print(line.strip())
```
- A **context manager** runs setup code on entering `with` and guaranteed cleanup code on leaving it (closing files, releasing locks, closing HDF5 files, ending a PsychoPy window).
- Without `with`, an exception before `f.close()` leaves the file open (and on Windows, locked).
- Always state `encoding="utf-8"` for text: the default differs between systems (µ, ä, special symbols in channel names).

## CSV: csv module and pandas
```python
import csv
with open("trials.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):          # each row is a dict of strings!
        rt = float(row["rt"])

import pandas as pd
df = pd.read_csv("trials.csv")             # types inferred, NaN for empty cells
df = pd.read_csv("export.csv", sep=";", decimal=",")   # German Excel export
df.to_csv("derived/trials_clean.csv", index=False)
```
- The `csv` module gives **strings**; you convert. pandas infers types – check `df.dtypes`.
- **TSV** (`sep="\t"`) is the BIDS standard for tables (`events.tsv`, `participants.tsv`).

## JSON
```python
import json
meta = {"SamplingFrequency": 1000, "PowerLineFrequency": 50, "EEGReference": "Cz"}
with open("sub-01_eeg.json", "w") as f:
    json.dump(meta, f, indent=2)
with open("sub-01_eeg.json") as f:
    meta = json.load(f)
```
JSON = dicts, lists, strings, numbers, `true/false/null`. Human-readable, language-independent, ideal for **metadata**; not for big arrays. NumPy types must be converted (`int(x)`, `arr.tolist()`).

## Pickle – and why it is unsafe
```python
import pickle
with open("model.pkl", "wb") as f:      # binary mode
    pickle.dump(obj, f)
```
- Pickle stores (almost) any Python object, which is convenient for caching.
- **Unsafe:** unpickling can **execute arbitrary code** embedded in the file. Never `pickle.load` a file from a source you don't trust (downloads, e-mail attachments, shared drives you don't control).
- **Not portable:** tied to Python and often to library versions; not readable from R/MATLAB; may break after updates.
- Use pickle only for temporary caches of your own objects. For data use CSV/TSV, JSON, `.npy`, HDF5, Zarr or NWB; for scikit-learn models, `skops` or `joblib` (same trust caveat for joblib).

## HDF5 with h5py
**HDF5** = one file containing a hierarchy of **groups** (folders) and **datasets** (n-d arrays) with **attributes** (metadata).
```python
import h5py, numpy as np
with h5py.File("session.h5", "w") as f:
    d = f.create_dataset("lfp", data=lfp, compression="gzip", chunks=(64, 10000))
    d.attrs["fs"] = 1000
    d.attrs["unit"] = "uV"
with h5py.File("session.h5", "r") as f:
    seg = f["lfp"][:, 5000:6000]     # reads only this slice from disk
    fs = f["lfp"].attrs["fs"]
```
- **Lazy access:** slicing a dataset reads only that part, so files larger than RAM are fine.
- Readable from R (`rhdf5`, [[R09 R Neuroscience Packages]]) and MATLAB (`h5read`; v7.3 `.mat` files are HDF5 underneath, [[MAT04 MATLAB Data Import and Files]]).

## Zarr
Same idea as HDF5 (chunked, compressed n-d arrays + metadata), but stored as a **directory of chunk files** (or in cloud object storage). Many processes can read and write chunks in parallel, which suits cloud computing and very large imaging data (light-sheet, OME-Zarr).
```python
import zarr
z = zarr.open("volume.zarr", mode="w", shape=(2000, 2048, 2048), chunks=(64, 256, 256), dtype="uint16")
z[0:64] = block
```

## NWB with pynwb
**Neurodata Without Borders** is a standard (built on HDF5) for neurophysiology: raw and processed ephys, calcium imaging, behaviour, stimuli, **plus** standardised metadata (subject, electrodes, device, units). DANDI archives NWB files ([[Py10 Python Neuroscience Packages]]).
```python
from pynwb import NWBHDF5IO
with NWBHDF5IO("sub-01_ses-01.nwb", "r") as io:
    nwb = io.read()
    print(nwb.subject, nwb.session_start_time)
    units = nwb.units.to_dataframe()            # spike-sorted units
    lfp = nwb.acquisition["ElectricalSeries"]   # data loaded lazily
```

## Which format when?
| Data | Format |
|---|---|
| small tables (trials, participants) | CSV/TSV |
| metadata, parameters | JSON (BIDS sidecars), YAML |
| single NumPy array, fast | `.npy` / `.npz` |
| big arrays + metadata, one file | HDF5 |
| huge arrays, parallel / cloud | Zarr |
| neurophysiology for sharing | **NWB** |
| MRI | NIfTI ([[Py10 Python Neuroscience Packages]]) |
| temporary cache of Python objects | Pickle (own files only) |

## Same idea in R and MATLAB
R: `read.csv`/`readr::read_csv`, `jsonlite`, `saveRDS`, `rhdf5` ([[R04 R Data Import and Tidy Data]]). MATLAB: `readtable`, `jsondecode`, `save/load` `.mat`, `h5read` ([[MAT04 MATLAB Data Import and Files]]). Both have their "pickle": `.rds` and `.mat` store native objects – fine within one language, poor for exchange.

## In neuroscience #neuro
- **BIDS** datasets combine TSV (events), JSON (metadata) and NIfTI/EDF/BrainVision (data) – all readable with the tools above ([[CS05 Data Formats and Representation]]).
- **Large ephys** (Neuropixels: 384 channels × 30 kHz) is stored chunked (HDF5/NWB/Zarr/binary) and read slice by slice.
- **Sampling rate and units belong in the file** as attributes, not in your head.
- **Shared lab caches as pickles** break when someone updates pandas – and are a security risk.

## Math links #math-link
- Bytes per sample and file size (e.g. 384 × 30,000 × 2 bytes/s ≈ 23 MB/s) → [[A1 Exponent Rules]]
- n-d arrays as tensors (channels × time × trials) → [[C1 Matrices]], [[CS01 Mathematical Foundations]]

## Connections
- Concepts of formats, metadata, tidy data → [[CS05 Data Formats and Representation]]
- Tables in memory → [[Py06 pandas and Tabular Data]]; arrays → [[Py05 NumPy and Arrays]]
- Neuro readers (MNE, NiBabel, PyNWB, Neo) → [[Py10 Python Neuroscience Packages]]
- Recording methods producing these files → [[Meth03 Electrophysiology]], [[Meth04 In Vivo Imaging]]

## Key takeaways
- `with open(...)` always; state `encoding="utf-8"`; use `pathlib`.
- CSV/TSV for tables, JSON for metadata, HDF5/Zarr for big arrays, NWB for sharing neurophysiology.
- Never unpickle untrusted files; pickle is not an exchange format.
- HDF5/Zarr slices load lazily: only what you index is read.
