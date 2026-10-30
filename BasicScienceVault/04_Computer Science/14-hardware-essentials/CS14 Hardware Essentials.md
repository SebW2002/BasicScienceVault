---
aliases: [Hardware Essentials, CPU GPU TPU, Memory Hierarchy, Storage and Bandwidth, Cloud vs Local Computing, Hardware]
tags: [computer-science, hardware, gpu, storage, type/overview, neuro]
---
# CS14 Hardware Essentials *(short overview)*

> [[MOC-computer-science|↑ CS MOC]] · [[CS14 Hardware Essentials - Worksheet|✏️ Worksheet]] · [[CS14 Hardware Essentials - Solutions|✅ Solutions]] · [[Mistakes - Computer Science|⚠️ Mistake log]]

## Why this matters
You don't need to build computers, but knowing a few hardware facts explains why an analysis takes 3 minutes or 3 days, why it crashes with "out of memory", why deep learning needs GPUs, and how to plan storage for a two-photon or Neuropixels project.

## CPU vs. GPU vs. TPU
| | **CPU** | **GPU** | **TPU** (and other AI accelerators) |
|---|---|---|---|
| Design | few (4–128) powerful, flexible cores; large caches; complex control (branch prediction) | thousands of simple cores executing the **same instruction on many data** in parallel (SIMD/SIMT); very high memory bandwidth | specialised matrix-multiply units (**systolic arrays**); low-precision arithmetic |
| Good at | sequential logic, branching code, general tasks, small or irregular problems | **dense linear algebra** (matrix multiplications, convolutions), image processing, deep learning, many independent simulations | large-scale neural network training and inference |
| Limits | limited parallel throughput | limited **VRAM** (e.g. 16–80 GB); data transfer CPU↔GPU costs time; branching code is slow | specialised, mainly via cloud |

**Why GPUs suit matrix operations:** the entries of $C = AB$, $c_{ij} = \sum_ka_{ik}b_{kj}$, are **independent** of each other, so thousands of them can be computed simultaneously. A matrix product of two $n\times n$ matrices costs about $2n^3$ floating-point operations (FLOPs). Modern GPUs reach tens to hundreds of TFLOP/s (10¹² FLOP/s; more at low precision such as float16/bfloat16).
- **Neuro uses:** deep learning (segmentation, pose estimation, decoding), spike sorting (Kilosort runs on GPUs), image registration, large simulations, motion correction of imaging data.

## Memory hierarchy (cache, RAM, disk)
| Level | Typical size | Access time (order of magnitude) |
|---|---|---|
| CPU registers | bytes | < 1 ns |
| **Cache** (L1/L2/L3) | KB – tens of MB | ~1–10 ns |
| **RAM** (main memory) | 8 GB – 1 TB+ | ~100 ns |
| GPU memory (VRAM) | 8–80 GB+ | very high bandwidth (TB/s) |
| SSD (NVMe) | TB | ~10–100 µs |
| HDD (spinning) | many TB | ~10 ms |
| Network storage / cloud | PB | ms – s, limited by bandwidth |

- Every level down is **larger but slower** (by orders of magnitude). Computation is often limited by **moving data**, not by arithmetic ("memory-bound").
- **Locality:** data accessed together should be stored together. Iterating along the memory layout of an array (row-major in NumPy/C, column-major in MATLAB/Fortran) is much faster than jumping across it. Contiguous reads from disk beat random reads.
- **Out of memory:** a 100 GB recording doesn't fit in 32 GB of RAM. Options:
  - **memory-mapping** (the OS loads only the parts you touch)
  - **chunked** processing (read a block, process it, write the result)
  - chunked formats (HDF5/Zarr, [[CS05 Data Formats and Representation]])
  - out-of-core libraries (Dask)
  - lower precision (float32 instead of float64)
- **Array size:** number of elements × bytes per element. A float64 matrix of 100,000 × 10,000 needs 8 GB.

## Storage and bandwidth limits for large datasets
| Data source | Approximate rate |
|---|---|
| Neuropixels probe (384 ch, 30 kHz, int16) | ~83 GB/h |
| Two-photon imaging (512², 30 Hz, uint16) | ~57 GB/h |
| Widefield/light-sheet microscopy | up to TB per session/day |
| fMRI study (one subject, all runs) | ~1–5 GB |
| Volume EM connectomics (1 mm³) | ~1–2 PB |

- **Transfer time** = size / bandwidth. 1 TB over a 1 Gbit/s network (≈ 125 MB/s) takes ~8000 s ≈ 2.2 h; over 10 Gbit/s, ~13 min. Shipping disks can still be faster for 100+ TB.
- **Bits vs. bytes:** network speeds are usually in **bits** per second (1 byte = 8 bits).
- **Compression:** lossless (e.g. Blosc/Zstd in Zarr, FLAC-like for ephys) often gives 2–5× for neural data. Lossy compression only with validated, controlled error.
- **Backups:** the 3-2-1 rule (3 copies, 2 media, 1 off-site). Raw data are irreplaceable.
- **Costs:** storage is cheap per TB but adds up over years and copies; plan in the data management plan.

## Cloud vs. local computing for neuroscience workloads
| | **Local workstation** | **University HPC cluster** | **Cloud** (commercial or research clouds) |
|---|---|---|---|
| Pros | full control, interactive, no queue, data stay local | many cores and GPUs, large storage, free or cheap for members | elastic (scale up or down), latest GPUs, no hardware maintenance; data and compute near public datasets (DANDI, OpenNeuro on cloud storage) |
| Cons | limited resources, you maintain it | **job scheduler** (e.g. SLURM) and queues; shared environment (containers help) | **costs** (compute, storage, and especially data **egress**); data protection (where are servers located? GDPR); requires setup skills |
| Good for | development, small analyses, visualisation | large batch processing (spike sorting of many sessions, fMRIPrep for hundreds of subjects, parameter sweeps) | bursts of demand, collaboration across institutions, deep learning on large GPUs |

**Typical workflow:** develop and test on a small subset locally → run in a container on the cluster or cloud → keep results and provenance ([[CS13 Reproducibility and Research Software]]).

**Energy:** a modern GPU draws ~300–700 W; training large models consumes megawatt-hours. The brain runs on ~20 W ([[Ph01 Mechanics and Energy]]), a constant reminder of how efficient biological computation is.

## Math links #math-link
- Powers of 2 and 10 (KB/KiB, GB, TB, PB), bits vs. bytes → [[A1 Exponent Rules]]
- $O(n^3)$ scaling of matrix multiplication → [[C1 Matrices]]
- Transfer times = size / rate (unit conversions) → [[A5 Fractions]]

## Connections
- In code → [[Py09 Python Machine Learning Libraries]] (GPUs in PyTorch), [[Py04 Python Files and Data Formats]] (chunked HDF5/Zarr), [[Py03 Python Control Flow and Functions]] (generators for large data)
- Data volumes and chunked formats → [[CS05 Data Formats and Representation]]
- Deep learning → [[CS08 Deep Neural Networks]]
- Containers and workflows → [[CS13 Reproducibility and Research Software]]
- Recording methods that generate the data → [[Meth03 Electrophysiology]], [[Meth04 In Vivo Imaging]], [[Meth06 Omics and Sequencing]]

## Key takeaways
- CPU: few flexible cores. GPU: thousands of simple cores for independent arithmetic, ideal for matrix operations. TPU: dedicated matrix units.
- Memory hierarchy: cache ≪ RAM ≪ SSD ≪ HDD ≪ network in latency. Data movement often dominates; use locality, chunking and memory-mapping.
- Size = elements × bytes. Transfer time = size / bandwidth (watch bits vs. bytes).
- Local for development, HPC for batch jobs, cloud for elastic or large GPU needs. Consider costs, egress and GDPR.
