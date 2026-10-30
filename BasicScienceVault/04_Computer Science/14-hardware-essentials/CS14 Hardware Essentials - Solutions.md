---
tags: [computer-science, hardware, type/solution]
---
# CS14 Hardware Essentials – Solutions

> Worksheet: [[CS14 Hardware Essentials - Worksheet]] · Theory: [[CS14 Hardware Essentials]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. Matrix entries can be computed **independently and with identical instructions**, which suits thousands of simple parallel GPU cores. Branching code makes different threads follow different paths; GPU threads in a group must execute the same instruction, so divergent branches are serialised and slow. CPUs have sophisticated control logic for branching.
2. L1 cache < RAM < SSD < HDD < network storage.
3. Memory is loaded in blocks (cache lines, pages). Accessing elements in storage order uses each loaded block fully (**locality**). Jumping across memory loads a new block for almost every element, so the CPU waits for memory (cache misses).

## Level 2
4. $2\cdot10^9$ FLOPs. CPU: $2\times10^9/10^{11} = 0.02$ s. GPU: $2\times10^9/2\times10^{13} = 10^{-4}$ s = 0.1 ms (plus data transfer to and from the GPU, which can dominate for small problems).
5. $10^9$ elements × 8 B = 8 GB; float32: 4 GB.
6. 1 Gbit/s = 125 MB/s: $10^{12}/1.25\times10^8 = 8000$ s ≈ 2.2 h. 10 Gbit/s: 800 s ≈ 13 min.
7. $4\cdot83\cdot200 = 66{,}400$ GB ≈ 66 TB per year; with 3 copies ≈ 200 TB.

## Level 3
8. Any three: **memory-mapping** (load only accessed parts), **chunked processing** (process blocks sequentially), chunked file formats (HDF5/Zarr) with lazy loading (Dask), **lower precision** (int16 raw data instead of float64), processing per channel or time window, a machine with more RAM (cluster).
9. 300 × 2 h = 600 GPU-hours, which is 25 days on one local GPU. An **HPC cluster** with many GPUs (jobs in parallel via SLURM, using a container for the sorter) is ideal if available. The cloud is an alternative for burst capacity, but costs, and the transfer and egress of ~TB-scale raw data, matter.
10. Any two: Is there a legal basis (consent, research exemption) covering cloud processing? Where are the servers located, and is transfer outside the EU covered? Is there a data processing agreement with the provider? Are the data pseudonymised or anonymised, encrypted, with access control and deletion policies? Has the data protection officer approved it?

## Level 4
11. A single GPU uses ~300–700 W, and training large models takes megawatt-hours, while the brain performs perception, learning and control continuously on ~20 W. Reasons include sparse, event-driven spiking, co-location of memory and computation (synapses), analogue processing and massive parallelism. **Neuromorphic hardware** (e.g. Intel Loihi, SpiNNaker, IBM TrueNorth) uses spiking, event-driven, in-memory computing inspired by the brain.
12. Seconds: $\frac{3\times10^{18}}{5\times10^{13}} = 6\times10^4$ s ≈ 16.7 GPU-hours. Energy: $16.7\cdot0.4\approx6.7$ kWh (in practice more, because of lower utilisation, cooling and many experiments).
