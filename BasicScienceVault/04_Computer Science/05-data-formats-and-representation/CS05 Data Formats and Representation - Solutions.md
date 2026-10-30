---
tags: [computer-science, data-format, type/solution]
---
# CS05 Data Formats and Representation – Solutions

> Worksheet: [[CS05 Data Formats and Representation - Worksheet]] · Theory: [[CS05 Data Formats and Representation]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. Each variable is a column; each observation is a row; each value is a cell.
2. | neuron | condition | rate |
   |---|---|---|
   | 1 | light | 12 |
   | 1 | dark | 8 |
   | 2 | light | 5 |
   | 2 | dark | 6 |
3. a) **NWB** (via SpikeInterface for raw data and sorting) b) **BIDS** with NIfTI files and JSON sidecars c) **OME-TIFF** (or OME-Zarr) d) PNG/SVG/PDF (vector graphics for line plots).
4. JPEG compression is **lossy**: it changes pixel values (block artefacts, smoothing) in ways that depend on the image content. Intensities are no longer quantitatively reliable, and fine structures can be invented or lost. Most JPEG is also limited to 8 bits.

## Level 2
5. $2^{12} = 4096$; $2^{16} = 65{,}536$.
6. float32: $4\times10^8$ bytes = 400 MB; float64: 800 MB.
7. $1000\cdot0.195 = 195\,\mu\text{V}$. Maximum: $32{,}767\cdot0.195\approx6.39\,\text{mV}$ (larger signals clip).
8. 0.1, 0.2 and 0.3 have no exact binary representation, so rounding errors accumulate ($0.1 + 0.2 = 0.30000000000000004$). Compare with a tolerance, e.g. `abs(a - b) < 1e-9` or `isclose(a, b)`.

## Level 3
9. $64\cdot1000\cdot4 = 256{,}000$ B/s; $\times3600\approx921.6\,\text{MB}\approx0.92\,\text{GB}$.
10. $512\cdot512\cdot2\cdot30 = 15{,}728{,}640$ B/s ≈ 15.7 MB/s; ×3600 ≈ 56.6 GB/h.
11. $2048^2\cdot2\cdot100\approx8.39\times10^8$ B/s ≈ 0.84 GB/s. $10^{13}/8.39\times10^8\approx11{,}900\,\text{s}\approx3.3\,\text{h}$.

## Level 4
12. Subject 07, session 02, task "nback", run 1, BOLD fMRI, compressed NIfTI. The TR (and other acquisition parameters) is in the JSON sidecar `sub-07_ses-02_task-nback_run-1_bold.json` (`RepetitionTime`).
13. The header can contain **personal data** (name, birth date, patient ID, dates, institution, sometimes burned-in text in the image). Check that you are allowed to share (consent, ethics, data processing agreement), **anonymise the headers** (or convert to NIfTI), and for structural MRI also consider **defacing**, because faces can be reconstructed ([[CS13 Reproducibility and Research Software]]).
14. Any five: **units** (µV? mV? arbitrary?), **sampling rate**, start time and time reference, **channel or electrode** identity and location, reference electrode, filter settings already applied, subject/session ID, condition and trial markers (events), recording device and gain, data type and precision, preprocessing history.
15. Chunks: $100{,}000/100 = 1000$. Each chunk: $100\cdot512\cdot512\cdot2 = 52{,}428{,}800$ B ≈ 52 MB. For the time series of one pixel you need **all 1000 chunks** (52 GB read for 200 KB of useful data), which is very inefficient. Chunk shapes should match the expected access pattern, e.g. (10,000, 32, 32) for pixel time series, or store two copies with different chunking.
