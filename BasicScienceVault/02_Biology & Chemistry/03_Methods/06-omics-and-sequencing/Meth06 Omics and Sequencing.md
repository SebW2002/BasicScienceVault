---
aliases: [Omics and Sequencing, RNA-seq, single-cell RNA-seq, scRNA-seq, Proteomics, Connectomics, Omics]
tags: [methods, sequencing, proteomics, connectomics, type/overview, neuro]
---
# Meth06 Omics and Sequencing

> [[MOC-methods|↑ Methods MOC]] · [[Meth06 Omics and Sequencing - Worksheet|✏️ Worksheet]] · [[Meth06 Omics and Sequencing - Solutions|✅ Solutions]] · [[Mistakes - Methods|⚠️ Mistake log]]

## Why this matters
"Omics" methods measure **everything at once**: all transcripts, all proteins, all synaptic connections. They have redefined what a cell type is (from shape to gene-expression profile), revealed disease mechanisms, and produced the first complete wiring diagrams of brains. They also turn neuroscience into **data science**, so the maths matters as much as the wet lab.

## RNA-seq (bulk)
**Workflow:**
1. Extract RNA.
2. Select or enrich (poly-A for mRNA, or rRNA depletion).
3. Fragment, **reverse-transcribe** to cDNA, add adapters (library preparation).
4. **Sequence** millions of short reads (e.g. Illumina, 50–150 bp).
5. **Align** reads to the genome or transcriptome, then **count** reads per gene.
6. **Normalise** (sequencing depth and gene length: CPM, TPM; or statistical normalisation in DESeq2/edgeR).
7. **Differential expression:** for each gene, estimate the **log₂ fold change** and a p-value, then **correct for multiple testing** (~20,000 genes, using FDR/Benjamini–Hochberg).
8. Interpret with gene set enrichment (GO terms, pathways).

**Strengths:** whole transcriptome without prior choice of genes; new isoforms and splicing ([[Bio04 Nucleic Acids and Gene Expression]]); quantitative.
**Limitation:** **bulk** tissue averages over all cell types. A change could mean altered expression **or** altered cell-type composition (e.g. fewer neurons, more microglia).

## Single-cell and single-nucleus RNA-seq (sc/snRNA-seq)
- Cells (or nuclei, from frozen post-mortem tissue) are separated, e.g. into **droplets** (10x Genomics) with a bead carrying a **cell barcode** and **unique molecular identifiers (UMIs)**. All reads from one cell share the barcode; UMIs remove PCR duplicates.
- **Output:** a matrix of **cells × genes** (e.g. 100,000 cells × 30,000 genes), which is very **sparse** (many zeros; "dropout").
- **Analysis pipeline:**
  1. quality control (remove doublets, dying cells with high mitochondrial reads)
  2. normalisation, log-transform
  3. selection of highly variable genes
  4. **PCA** (dimension reduction)
  5. a nearest-neighbour graph
  6. **clustering** (Leiden/Louvain)
  7. 2D visualisation (**UMAP**, t-SNE)
  8. annotation of clusters by marker genes (e.g. *Slc17a7* = excitatory, *Gad1* = inhibitory, *Pvalb*, *Sst*, *Vip*, *Gfap*, *Mbp*, *Cx3cr1*)
- **Neuro:** cell-type atlases of the whole mouse brain (Allen Brain Cell Atlas, BRAIN Initiative: thousands of types) and of human cortex; disease-associated states (e.g. "disease-associated microglia" in Alzheimer's); developmental trajectories (pseudotime).
- **Extensions:**
  - **Patch-seq**: electrophysiology + morphology + transcriptome of the same cell ([[Meth03 Electrophysiology]])
  - **spatial transcriptomics** (MERFISH, Visium, Slide-seq), which keeps the tissue location
  - **multiome** (RNA + chromatin accessibility via ATAC-seq)
  - lineage tracing with barcodes

## Proteomics
mRNA levels don't fully predict protein levels (translation, degradation, transport). Proteomics measures the proteins themselves, mostly by **mass spectrometry** ([[Meth02 Structural Biology]]):
- **Bottom-up/shotgun:** digest with trypsin → LC-MS/MS → identify peptides against a database → infer proteins → quantify (label-free, TMT/iTRAQ tags, SILAC).
- **Targeted proteomics** (SRM/PRM) for precise quantification of selected proteins (biomarkers).
- **Post-translational modifications:** phosphoproteomics, ubiquitinomics.
- **Spatial and interaction proteomics:** proximity labelling (BioID, APEX) maps the protein neighbourhood of, e.g., the synaptic cleft; affinity purification–MS maps complexes.
- **Neuro:** the **synaptic proteome** (> 1000 proteins in the PSD); changes after learning or in disease; **CSF and plasma proteomics** for biomarkers (Aβ, tau isoforms, NfL, synaptic proteins). Antibody-based multiplex methods (Olink, SomaScan) are also common.

## Connectomics
Connectomics is the reconstruction of **every neuron and every synapse** in a piece of nervous tissue, usually from **volume electron microscopy** ([[Meth01 Microscopy]]):
1. Fix and stain the tissue with heavy metals, embed it in resin.
2. Cut and image thousands of serial ultrathin sections (serial-section TEM, ATUM-SEM) or image the block face (SBF-SEM, FIB-SEM) at ~4–30 nm voxels.
3. **Align** the images into a 3D volume.
4. **Segment** neurons (today mostly with deep learning, followed by human proofreading).
5. **Detect synapses** and assign them to pre- and postsynaptic partners.
6. Build a **connectivity matrix** (graph) and analyse it.

**Landmarks** (approximate numbers):
| Connectome | Year | Size |
|---|---|---|
| *C. elegans* (White et al.) | 1986 | **302 neurons**, ~7,000 synapses |
| *Drosophila* larva | 2023 | ~3,000 neurons |
| *Drosophila* adult brain (FlyWire) | 2024 | ~140,000 neurons, ~50 million synapses |
| Human cortex fragment (H01) | 2024 | ~1 mm³: ~57,000 cells, ~150 million synapses, ~1.4 petabytes of data |
| Mouse visual cortex (MICrONS) | 2025 | ~1 mm³ with matched functional imaging of the same neurons: ~200,000 cells, ~500 million synapses |

**Limitations:** enormous data volumes and proofreading effort; a static snapshot of a single individual; EM shows a synapse but usually not its strength, transmitter or receptor types; electrical synapses and neuromodulation are hard to see. Light-microscopy-based alternatives (expansion microscopy, barcoded viral tracing such as MAPseq) trade completeness for throughput.

## In neuroscience #neuro
- **What is a cell type?** Multimodal definitions combine transcriptome (scRNA-seq), morphology, electrophysiology (Patch-seq) and connectivity (connectomics).
- **Genetics of brain disorders:** GWAS loci for schizophrenia, autism or Alzheimer's are mapped to the cell types where the genes are expressed (e.g. Alzheimer's risk genes enriched in microglia).
- **Connectome-constrained models:** the fly connectome allows simulation of circuits and predictions that can be tested experimentally.

## Math links #math-link
- Counts → log-transform, **log₂ fold change** → [[A3 Logarithms]], [[B3 Logarithmic Functions]]
- Multiple testing: with 20,000 tests at α = 0.05 you expect about 1000 false positives → [[A7 Sums Products and Factorials]], [[E1 Sets Logic and Quantifiers]]
- Count statistics: Poisson / negative binomial models of read counts → [[A7 Sums Products and Factorials]]
- Cells × genes matrix; **PCA** = eigenvectors of the covariance matrix → [[C1 Matrices]], [[C4 Eigenvalues and Eigenvectors]]
- Cell similarity = distances or cosine similarity in high-dimensional space → [[D1 Vectors in 2D and 3D]], [[D2 Dot and Cross Product]]
- Connectome = **adjacency matrix** $W_{ij}$; graph measures (degree = row/column sums, paths, motifs), eigenvector centrality → [[C1 Matrices]], [[C4 Eigenvalues and Eigenvectors]]
- Data volumes: powers of ten (TB, PB, EB) → [[A1 Exponent Rules]]

## Connections
- Gene expression and splicing → [[Bio04 Nucleic Acids and Gene Expression]]
- Mass spectrometry → [[Meth02 Structural Biology]]
- Volume EM → [[Meth01 Microscopy]]
- Cell types and circuits → [[Bio07 Neural Circuits and Systems]]
- PCR in library preparation → [[Meth05 Molecular Biology Tools]]

## Key takeaways
- RNA-seq: reads → counts → normalisation → log₂ fold change + FDR correction. Bulk data mix cell types.
- scRNA-seq: barcodes + UMIs → sparse cells × genes matrix → PCA → clustering → UMAP → cell types.
- Proteomics (LC-MS/MS) measures proteins and modifications directly.
- Connectomics: volume EM → segmentation → synapse detection → connectivity matrix. Complete for worm and fly; mm³ fragments for mouse and human.
