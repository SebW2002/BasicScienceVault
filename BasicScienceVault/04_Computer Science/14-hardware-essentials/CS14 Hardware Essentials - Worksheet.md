---
tags: [computer-science, hardware, type/worksheet]
---
# CS14 Hardware Essentials – Worksheet

> Theory: [[CS14 Hardware Essentials]] · Solutions: [[CS14 Hardware Essentials - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮.

## Level 1 – Concepts
1. Why are GPUs faster than CPUs for matrix multiplication but not necessarily for code with many if/else branches?
2. Order by access time: SSD, RAM, L1 cache, HDD, network storage.
3. Why does iterating over an array in the "wrong" order slow down code even though the number of operations is the same?

## Level 2 – Calculations
4. How many FLOPs does multiplying two 1000 × 1000 matrices take (≈ $2n^3$)? How long on a CPU at 100 GFLOP/s and on a GPU at 20 TFLOP/s?
5. How much memory does a float64 array of 100,000 × 10,000 need? And in float32?
6. How long does it take to transfer 1 TB over a 1 Gbit/s connection? Over 10 Gbit/s?
7. A lab records 4 hours of Neuropixels data per day (~83 GB/h) on 200 days per year. How much storage per year? With 3 copies (3-2-1 backup)?

## Level 3 – Planning
8. Your 120 GB recording doesn't fit into 32 GB of RAM. Name three strategies.
9. You need to run spike sorting for 300 sessions (each ~2 h on one GPU). Local workstation with one GPU, HPC cluster or cloud? Justify.
10. Name two GDPR-related questions you must answer before processing patient MRI data in a commercial cloud.

## Level 4 – Transfer
11. Why is the brain's energy efficiency (≈ 20 W) remarkable compared with GPUs? Name one hardware approach inspired by the brain.
12. 🧮 A deep network performs $3\times10^{18}$ FLOPs to train. A GPU sustains 50 TFLOP/s. How many GPU-hours are needed? At 0.4 kW per GPU, how much energy (kWh)?
