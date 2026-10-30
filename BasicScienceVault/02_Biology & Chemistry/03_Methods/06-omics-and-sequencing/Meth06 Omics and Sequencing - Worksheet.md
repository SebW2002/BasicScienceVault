---
tags: [methods, sequencing, proteomics, connectomics, type/worksheet]
---
# Meth06 Omics and Sequencing – Worksheet

> Theory: [[Meth06 Omics and Sequencing]] · Solutions: [[Meth06 Omics and Sequencing - Solutions]] · Log mistakes in [[Mistakes - Methods]]
> No calculator unless marked 🧮.

## Level 1 – Recall
1. List the main steps of a bulk RNA-seq experiment from tissue to differentially expressed genes.
2. What are cell barcodes and UMIs used for in droplet-based scRNA-seq?
3. Why is snRNA-seq (nuclei) often used for human post-mortem brain tissue?
4. What does the protease trypsin do in bottom-up proteomics?
5. How many neurons does the *C. elegans* connectome contain, and which imaging method underlies connectomics?

## Level 2 – Calculation
6. A gene has 400 normalised counts in controls and 100 in a disease group. Compute the fold change and the log₂ fold change. And for 100 → 800?
7. You test 20,000 genes at α = 0.05 without correction, and no gene is truly changed. How many "significant" genes do you expect? What is the Bonferroni threshold?
8. A connectome of $N$ neurons is stored as an $N\times N$ matrix. How many entries for $N = 302$? For $N = 140{,}000$? Why is it stored as a sparse matrix?
9. In the connectivity matrix $W$ (rows = postsynaptic, columns = presynaptic), what do the row sums and the column sums mean?

## Level 3 – Interpretation
10. Bulk RNA-seq of Alzheimer's cortex shows lower neuronal genes and higher microglial genes. Give two different explanations and say how scRNA-seq could tell them apart.
11. Two scRNA-seq clusters differ in a few hundred genes. What extra evidence would make you call them distinct cell types rather than states?
12. Why do mRNA and protein levels for the same gene often correlate only moderately?
13. A connectome shows a synapse from neuron A to neuron B. Name three things this does **not** tell you.

## Level 4 – Design & scale
14. You want to find which hippocampal cell type changes gene expression after learning, while keeping information about where those cells are in the tissue. Which method(s) would you use?
15. Patch-seq combines which three data types from a single cell? Why is this valuable?
16. 🧮 The H01 dataset is ~1.4 PB for ~1 mm³. The human brain has a volume of about 1.2 million mm³. Estimate the data volume for a whole human brain at the same resolution (in zettabytes, 1 ZB = 10²¹ bytes).
