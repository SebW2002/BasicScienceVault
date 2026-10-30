---
tags: [programming, python, type/solution]
---
# Py04 Python Files and Data Formats – Solutions

> Worksheet: [[Py04 Python Files and Data Formats - Worksheet]] · Theory: [[Py04 Python Files and Data Formats]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. `"r"` read text (default), `"w"` write (**truncates** the file, destroying content), `"a"` append, `"rb"` read binary (pickle, raw data).
2. That cleanup runs when the block is left, even after an exception. Examples: `h5py.File(...)`, `NWBHDF5IO(...)`, a lock, `np.errstate(...)`, a temporary directory, a database connection.
3. A **string**. Convert with `float(row["rt"])` (empty strings need handling: missing value).
4. Groups (folders), datasets (n-d arrays), attributes (metadata on groups or datasets).

## Level 2
5. Unpickling can execute arbitrary code contained in the file (e.g. delete files, install malware). Other drawbacks: Python-only, version-fragile, not human-readable.
6. `pd.read_csv(path, sep=";", decimal=",")`
7. HDF5 reads lazily: indexing a slice reads only the chunks that contain it from disk.
8. HDF5 is one file; Zarr is a directory (or object store) of separate chunk files. Matters for parallel writes from many processes and cloud storage (Zarr wins); a single file is easier to copy and share (HDF5).

## Level 3
9. ```python
   import json
   with open("meta.json", "w", encoding="utf-8") as f:
       json.dump(meta, f, indent=2)
   with open("meta.json", encoding="utf-8") as f:
       meta2 = json.load(f)
   ```
10. The file is opened in read mode (default `"r"`) but written to → `io.UnsupportedOperation`; and it is never closed. Fix: `with open("log.txt", "a", encoding="utf-8") as f: f.write("done\n")`.
11. ```python
    from pathlib import Path
    import pandas as pd
    for f in sorted(Path("data/raw").glob("sub-*_events.tsv")):
        df = pd.read_csv(f, sep="\t")
        print(f.name, len(df))
    ```

## Level 4
12. a) CSV/TSV. b) JSON (or YAML) sidecar, saved next to the derived data. c) NWB (required by DANDI). d) Zarr (OME-Zarr): chunked, parallel, cloud-friendly.
13. $384\times30{,}000\times2\text{ B} = 23{,}040{,}000$ B/s ≈ **23 MB/s**; × 3600 s ≈ 83 GB per hour.
14. ```python
    import h5py, numpy as np
    rng = np.random.default_rng(0)
    with h5py.File("test.h5", "w") as f:
        d = f.create_dataset("lfp", data=rng.standard_normal((4, 10000)))
        d.attrs["fs"] = 1000
    with h5py.File("test.h5", "r") as f:
        seg = f["lfp"][2, 2000:3000]      # channel index 2 = third channel
        print(seg.shape, f["lfp"].attrs["fs"])   # (1000,) 1000
    ```
    If "channel 2" means the second channel (1-based counting), use index `1`. Say which convention you use.
