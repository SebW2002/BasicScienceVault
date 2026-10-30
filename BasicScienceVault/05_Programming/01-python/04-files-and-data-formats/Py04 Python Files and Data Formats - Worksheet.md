---
tags: [programming, python, type/worksheet]
---
# Py04 Python Files and Data Formats – Worksheet

> Theory: [[Py04 Python Files and Data Formats]] · Solutions: [[Py04 Python Files and Data Formats - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Recall
1. What do the modes `"r"`, `"w"`, `"a"`, `"rb"` mean in `open()`? Which one destroys existing content?
2. What does a context manager guarantee? Give two examples besides files.
3. `csv.DictReader` returns `row["rt"] == "0.43"`. What type is it, and what must you do before averaging?
4. Name the three building blocks of an HDF5 file.

## Level 2 – Understanding
5. Why is `pickle.load` on a file downloaded from a forum dangerous? Name a second, non-security drawback of pickle.
6. A colleague's CSV export from German Excel shows `0,43;1,12`. What arguments does `pd.read_csv` need?
7. Why can you slice a 200 GB HDF5 dataset on a laptop with 16 GB RAM?
8. HDF5 vs. Zarr: what is the main structural difference, and when does it matter?

## Level 3 – Write code
9. Write code that saves `meta = {"fs": 1000, "bad": ["T7", "Oz"]}` as pretty-printed JSON and reads it back.
10. Find two bugs:
    ```python
    f = open("log.txt")
    f.write("done")
    ```
11. Write a loop with `pathlib` over all files `data/raw/sub-*_events.tsv`, read each with pandas and print the number of rows.

## Level 4 – Neuro transfer
12. Choose a format and justify: a) 300 trials × 5 columns of behavioural data, b) the filter settings used in preprocessing, c) a 2-hour Neuropixels recording to deposit on DANDI, d) a light-sheet volume of 2 TB analysed on a cluster.
13. Estimate the data rate (MB/s) of 384 channels at 30 kHz stored as int16. How much is one hour?
14. 💻 Create an HDF5 file with a random dataset `lfp` (shape 4 × 10000) and an attribute `fs = 1000`, close it, reopen it and read only samples 2000–2999 of channel 2. (Needs `pip install h5py`.)
