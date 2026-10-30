---
aliases: [Data Formats and Representation, Tidy Data, HDF5, NWB, BIDS, NIfTI, TIFF, DICOM, Float Precision, Datenformate]
tags: [computer-science, data-format, metadata, nwb, bids, type/overview, neuro]
---
# CS05 Data Formats and Representation

> [[MOC-computer-science|↑ CS MOC]] · [[CS05 Data Formats and Representation - Worksheet|✏️ Worksheet]] · [[CS05 Data Formats and Representation - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
Neuroscience produces huge, heterogeneous data: hours of 30 kHz recordings on hundreds of channels, terabytes of imaging, MRI volumes, behaviour videos, tables of metadata. The **format** decides whether the data can be read in ten years, shared with colleagues, combined across labs and analysed without loading everything into memory. Wrong choices (lossy compression, missing units, Excel-mangled tables) silently ruin analyses.

## Tabular data (CSV, TSV) and the tidy data principle
- **CSV/TSV:** plain text, one row per line, columns separated by commas or tabs. Universal and human-readable, but no types, no units, no hierarchy, and large on disk.
  - **Pitfalls:**
    - **decimal comma** in German locales (1,5 vs 1.5) collides with the comma separator, so prefer TSV or `.` as decimal
    - text encoding (always UTF-8)
    - quoting of fields containing separators
    - Excel auto-converting gene names to dates (e.g. SEPT2 → 2-Sep), which corrupted many published gene lists
- **Tidy data (Wickham 2014):**
  1. each **variable** is a column
  2. each **observation** is a row
  3. each **value** is a cell
  4. (each type of observational unit is a table)
- **Wide vs. long:** "wide" has one column per condition (`rate_condA`, `rate_condB`); "long/tidy" has columns `neuron`, `condition`, `rate`. Statistical and plotting tools (mixed models, grouped plots) usually want the **long** format.

| neuron | animal | condition | trial | rate_Hz |
|---|---|---|---|---|
| 1 | M01 | light | 1 | 12.3 |
| 1 | M01 | dark | 1 | 7.9 |
| … | | | | |

- **Other text formats:** JSON and YAML for nested metadata and configuration (JSON sidecars in BIDS).

## Hierarchical and array formats (HDF5, NetCDF, Zarr)
| Format | Structure | Strengths | Typical use |
|---|---|---|---|
| **HDF5** | a "file system in a file": **groups** (folders) containing **datasets** (n-D arrays) and **attributes** (metadata) | binary, typed, **chunked** and compressed, partial reading (slice without loading all), very large files | basis of NWB, many microscopy and ephys formats |
| **NetCDF** (v4 is built on HDF5) | arrays with **named dimensions** and coordinates | self-describing; xarray integration | climate/geo origin; labelled neuro arrays |
| **Zarr** | array split into many **chunk files** (in a folder or object store) | **cloud-native**, parallel reads and writes | large imaging on cloud storage, OME-Zarr for microscopy |

**Chunking:** arrays are stored in blocks. Read patterns should match chunk shapes (e.g. chunk by time for time-series reads, by tiles for images). See [[CS14 Hardware Essentials]].

## Neuroscience-specific formats and standards
| Standard | What | Details |
|---|---|---|
| **NWB** (Neurodata Without Borders) | a file **format** (on HDF5) for neurophysiology: extracellular and intracellular ephys, optical physiology, behaviour, stimuli | standardised groups for data and metadata (subject, session, electrodes, units); shared via the **DANDI** archive |
| **BIDS** (Brain Imaging Data Structure) | a **folder and naming convention** plus JSON sidecars for MRI, EEG, MEG, iEEG, PET, microscopy | e.g. `sub-01/ses-01/func/sub-01_ses-01_task-rest_bold.nii.gz` + `..._bold.json`; validators; used by OpenNeuro and pipelines like fMRIPrep |
| **NIfTI** (.nii, .nii.gz) | 3D/4D MRI volumes with a header | the header includes voxel size and an **affine matrix** mapping voxel indices to world coordinates ([[C1 Matrices]]) |
| **SpikeInterface** | a **software framework** (not a format) that reads many raw ephys formats (SpikeGLX, Open Ephys, Intan, …) behind one API and runs many spike sorters | makes spike sorting comparable and reproducible ([[CS11 Time Series and Signal Processing]]) |
| EDF/BDF, BrainVision, FIF | EEG/MEG raw formats | FIF for MNE/Elekta MEG; EDF common in clinical EEG |

## Image formats (TIFF for microscopy, DICOM for clinical imaging)
| Format | Properties | Use |
|---|---|---|
| **TIFF** | lossless; 8/16/32-bit; multi-page (stacks, time series); BigTIFF for > 4 GB | microscopy raw data, two-photon movies |
| **OME-TIFF / OME-Zarr** | TIFF/Zarr + standardised XML metadata (pixel size, channels, objective) | interoperable microscopy |
| **DICOM** | clinical standard: image + extensive header (scanner, sequence, **patient name, birth date, IDs**) | clinical MRI, CT, PET → usually converted to NIfTI for research; **headers must be anonymised** ([[CS13 Reproducibility and Research Software]]) |
| PNG | lossless, 8/16-bit | figures, masks |
| **JPEG** | **lossy** compression (blocks, artefacts) | photos only, **never** for quantitative data |

**Bit depth:** an $n$-bit integer image has $2^n$ grey levels (8-bit: 256; 12-bit: 4096; 16-bit: 65,536). Saturated pixels (at the maximum value) lose information, so check histograms.

## Binary vs. text, precision and sampling rates
- **Text** ("1.234567") is human-readable but big (one byte per character) and slow to parse. **Binary** stores the raw bytes of numbers: compact, exact, fast, but needs a known layout (data type, byte order/**endianness**, shape).

| Data type | Bytes | Range / precision | Use |
|---|---|---|---|
| `uint8` | 1 | 0–255 | images, masks |
| `int16` | 2 | −32,768 … 32,767 | raw ADC samples of ephys (multiply by a gain to get µV) |
| `uint16` | 2 | 0 … 65,535 | camera/microscope images |
| `float32` | 4 | ~7 significant decimal digits; relative precision ≈ $10^{-7}$ | most analysis and deep learning |
| `float64` | 8 | ~16 significant digits; ≈ $10^{-16}$ | numerically sensitive computations (default in NumPy) |

- **Rounding:** floats can't represent most decimals exactly ($0.1 + 0.2\neq0.3$ exactly), so compare with tolerances. Summing very many small numbers in float32 loses precision.
- **Integer overflow:** adding two large `int16` values can wrap around. Convert before arithmetic.
- **Data volume** = channels × sampling rate × bytes × duration. Example: 384 channels × 30 kHz × 2 bytes ≈ 23 MB/s ≈ 83 GB/h. A two-photon movie of 512 × 512 pixels × 30 Hz × 2 bytes ≈ 15.7 MB/s ≈ 57 GB/h.
- **Sampling rate** must exceed twice the highest frequency (Nyquist, [[Ph09 Waves and Oscillations]]). Store it **with** the data; a missing sampling rate makes time axes guesswork.

## Metadata standards and reproducibility
**Metadata** = data about data: units, sampling rate, channel locations, coordinate systems, stimulus timing, subject information (age, sex, genotype), preprocessing history (provenance), software versions.
- Without metadata, numbers are meaningless ("is this mV or µV? is time in samples or seconds?").
- Standards (NWB, BIDS, OME) define **which** metadata must be present and **how** to name them, so data become machine-readable and comparable.
- They are part of the **FAIR** principles (Findable, Accessible, Interoperable, Reusable, [[CS13 Reproducibility and Research Software]]).
- **Keep raw data read-only**; derived data go in separate folders with a record of how they were produced (BIDS `derivatives/`).

## In neuroscience #neuro
- **Public archives:** DANDI (NWB), OpenNeuro (BIDS), Allen Brain Observatory, IBL data, which are only usable because of standards.
- Converting lab-specific formats to NWB/BIDS is often the first step of a project and pays off at publication.

## Math links #math-link
- Data volume calculations, powers of 2 and 10 (bits, bytes, KiB vs kB) → [[A1 Exponent Rules]]
- Bit depth: $2^n$ levels; dynamic range in dB → [[A3 Logarithms]]
- NIfTI affine: a 4×4 matrix (rotation, scaling, translation) → [[C1 Matrices]], [[D1 Vectors in 2D and 3D]]
- Floating-point numbers: mantissa × $2^\text{exponent}$ → [[A1 Exponent Rules]]

## Connections
- In code → [[Py04 Python Files and Data Formats]] (CSV, JSON, HDF5, Zarr, NWB), [[R04 R Data Import and Tidy Data]], [[MAT04 MATLAB Data Import and Files]]
- Recording methods that produce these data → [[Meth03 Electrophysiology]], [[Meth04 In Vivo Imaging]], [[Meth01 Microscopy]]
- Storage and memory → [[CS14 Hardware Essentials]]
- Sharing, FAIR, anonymisation → [[CS13 Reproducibility and Research Software]]
- Workflow → [[CS06 Data Science Workflow]]

## Key takeaways
- Tidy tables: variables in columns, observations in rows; prefer long format; beware Excel and decimal commas.
- HDF5/NetCDF/Zarr hold large, chunked, typed arrays with metadata; Zarr for the cloud.
- NWB = format for physiology (on HDF5); BIDS = folder/naming standard for imaging and EEG/MEG; NIfTI for MRI volumes; SpikeInterface = framework for ephys formats and sorters.
- TIFF (lossless) for microscopy; DICOM is clinical (anonymise headers!); never JPEG for data.
- Know your dtype (int16, float32, float64), units and sampling rate. Metadata make data reusable.
