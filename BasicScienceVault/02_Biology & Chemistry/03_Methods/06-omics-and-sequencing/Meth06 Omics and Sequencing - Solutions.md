---
tags: [methods, sequencing, proteomics, connectomics, type/solution]
---
# Meth06 Omics and Sequencing – Solutions

> Worksheet: [[Meth06 Omics and Sequencing - Worksheet]] · Theory: [[Meth06 Omics and Sequencing]] · Wrong? → [[Mistakes - Methods]]

## Level 1
1. RNA extraction → library preparation (enrich mRNA, fragment, reverse-transcribe, add adapters) → sequencing → alignment → counting reads per gene → normalisation → statistical testing (log₂FC, p-values) → multiple-testing correction (FDR) → interpretation (enrichment).
2. **Cell barcode:** labels all transcripts from one cell (one droplet), so reads can be assigned to cells. **UMI:** labels each original mRNA molecule, so PCR duplicates can be collapsed and molecules counted accurately.
3. Frozen post-mortem tissue can't be dissociated into intact living cells (neurons in particular break apart), but nuclei survive freezing and can be isolated. It also reduces dissociation-induced stress genes.
4. It cuts proteins after **lysine (K) and arginine (R)** (not before proline), giving peptides of predictable size and charge for MS/MS.
5. 302 neurons; **(serial-section) electron microscopy**.

## Level 2
6. $100/400 = 0.25$, so $\log_2 0.25 = -2$. $800/100 = 8$, so $\log_2 8 = +3$. (The log scale makes up- and down-regulation symmetric.)
7. $0.05\cdot20\,000 = 1000$ false positives. Bonferroni: $0.05/20\,000 = 2.5\times10^{-6}$. In practice the Benjamini–Hochberg FDR (e.g. 5 %) is used.
8. $302^2 = 91{,}204$ entries. $140{,}000^2 = 1.96\times10^{10}$ entries. Most entries are 0 (each neuron connects to only a tiny fraction of all others), so a sparse format stores only the non-zero entries (pairs + weights), saving orders of magnitude of memory.
9. Row sum: **total input** to a neuron (in-degree or total synaptic weight received). Column sum: **total output** of a neuron (out-degree or total weight sent).

## Level 3
10. (1) **Cell composition**: neurons are lost and microglia proliferate or are recruited, so expression per cell may be unchanged. (2) **Regulation**: neurons express their genes less, and microglia express inflammatory genes more. scRNA-seq or snRNA-seq measures each cell separately: you can count cell-type proportions **and** compare expression *within* each type.
11. Converging evidence across modalities: stable differences in **morphology**, **electrophysiology**, **connectivity** or **location**; marker genes for developmental lineage; reproducibility across individuals and datasets; and the differences shouldn't reflect transient activity (e.g. immediate early genes) or stress. Patch-seq and spatial methods help.
12. mRNA → protein involves translation regulation (miRNAs, local translation), different **half-lives** of mRNA and protein (proteins can last days), protein degradation, transport (to synapses), and measurement differences (sensitivity, dynamic range).
13. Any three: the **strength** of the synapse (EM size gives only a rough proxy); the **transmitter** and **receptors** (excitatory vs. inhibitory, ionotropic vs. metabotropic); **dynamics** (short-term plasticity); whether it is **active** during behaviour; electrical synapses and neuromodulation (volume transmission); variability between individuals.

## Level 4
14. **Spatial transcriptomics** (e.g. MERFISH for a targeted gene panel at single-cell resolution, or Slide-seq/Visium) in hippocampal sections after learning vs. controls. Possibly combine with **snRNA-seq** for full-transcriptome cell-type identification and integrate the datasets (mapping clusters onto spatial positions). Activity-dependent labelling (e.g. *Fos*-based TRAP mice) can tag the neurons that were active during learning.
15. **Electrophysiology** (patch clamp), **morphology** (fill with biocytin and reconstruct) and **transcriptome** (aspirate the cytoplasm for RNA-seq). It links molecular cell-type definitions to function and shape in the same cell, the basis of multimodal cell-type taxonomies.
16. $1.4\times10^{15}\,\text{B}\cdot1.2\times10^6\approx1.7\times10^{21}\,\text{B}$, about **1.7 ZB**, a million times the size of H01. Whole-human-brain EM connectomics is far beyond current capabilities, so compression, lower resolution or sampling strategies are needed.
