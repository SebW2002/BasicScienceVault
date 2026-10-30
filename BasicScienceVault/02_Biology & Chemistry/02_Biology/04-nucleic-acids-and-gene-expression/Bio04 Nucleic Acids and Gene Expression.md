---
aliases: [Gene Expression, Nucleic Acids, Transcription, Translation, Epigenetics, Alternative Splicing, Genexpression]
tags: [biology, gene-expression, epigenetics, splicing, type/overview, neuro]
---
# Bio04 Nucleic Acids and Gene Expression

> [[MOC-biology|↑ Biology MOC]] · [[Bio04 Nucleic Acids and Gene Expression - Worksheet|✏️ Worksheet]] · [[Bio04 Nucleic Acids and Gene Expression - Solutions|✅ Solutions]] · [[Mistakes - Biology|⚠️ Mistake log]]

## Why this matters
All neurons in your brain carry the same genome, yet there are thousands of distinct cell types. The difference lies in **which genes are expressed, how they are spliced and how this is regulated**. Long-term memory needs new gene expression. Most modern methods (CRISPR, AAVs, RNA-seq) work by reading or writing genetic information.

## Central dogma
$$\text{DNA}\xrightarrow{\text{replication}}\text{DNA}\qquad\text{DNA}\xrightarrow{\text{transcription}}\text{RNA}\xrightarrow{\text{translation}}\text{protein}$$
(plus reverse transcription in retroviruses, used in lentiviral vectors and RT-qPCR)

## DNA replication
- **Semiconservative** (Meselson–Stahl): each new double helix contains one old and one new strand.
- **Helicase** unwinds the helix; **primase** lays down an RNA primer; **DNA polymerase** synthesises **only 5' → 3'** and proofreads (very low error rate after repair).
- The **leading strand** is made continuously; the **lagging strand** is made discontinuously in **Okazaki fragments**, which **ligase** joins.
- **Neurons are postmitotic:** they don't replicate their DNA, but they **repair** it constantly. DNA damage accumulates with age, and defective repair causes neurodegeneration (e.g. ataxia telangiectasia). Even normal activity induces DNA double-strand breaks at immediate early genes.

## Transcription (DNA → RNA)
- **RNA polymerase II** (for mRNA) binds the **promoter** with the help of transcription factors.
  - The template strand is read 3' → 5' and RNA is synthesised 5' → 3'.
  - U replaces T.
- **Enhancers/silencers** can be far away and bind specific transcription factors, which gives cell-type-specific expression.
- **Pre-mRNA processing** in the nucleus:
  - a **5' cap** is added
  - a **3' poly(A) tail** is added
  - **splicing** removes introns and joins exons, carried out by the spliceosome (snRNPs)

## Translation (mRNA → protein)
- **Genetic code:** triplet **codons**, $4^3 = 64$ codons for 20 amino acids plus stop. The code is **redundant** (degenerate). **AUG** is the start codon (Met); **UAA, UAG, UGA** are stop codons.
- **Ribosome** (rRNA + proteins): **tRNAs** carry amino acids and recognise codons with their **anticodon**. The ribosome reads mRNA 5' → 3' and builds the protein from N- to C-terminus.
- Translation occurs in the cytosol (free ribosomes) or on the **rough ER** for membrane and secreted proteins ([[Bio01 Cell Biology]]).
- **Mutation types:**
  - silent (same amino acid)
  - missense (different amino acid)
  - nonsense (premature stop)
  - frameshift (insertion or deletion of a number of bases that is not a multiple of 3)
  - **repeat expansion** (CAG in Huntington's, CGG in fragile X)

## Gene regulation and epigenetics
"Epi-genetics" means heritable or stable changes in gene activity **without changes in DNA sequence**.

| Mechanism | Effect |
|---|---|
| **DNA methylation** (5-methylcytosine, mainly at CpG; in neurons also abundant at non-CpG sites) | usually **silences** promoters; read by methyl-binding proteins such as **MeCP2** |
| **Histone acetylation** (HATs add, HDACs remove) | opens chromatin and **activates** transcription |
| Histone methylation | activating (H3K4me3) or repressive (H3K27me3, H3K9me3) depending on the site |
| Chromatin remodelling, 3D genome folding | brings enhancers to promoters |
| Non-coding RNAs (miRNAs, lncRNAs) | miRNAs bind mRNAs and reduce their translation or stability |

**Activity-dependent transcription:**
1. Synaptic activity lets Ca²⁺ in.
2. Kinases (CaMKIV, PKA, MAPK) phosphorylate **CREB**.
3. **Immediate early genes** (*c-Fos*, *Arc*, *Egr1*, *Npas4*) are expressed within minutes.
4. These in turn regulate late-response genes.

This is required for long-term memory (late LTP, [[Bio06 Synapses and Neurotransmitters]]). c-Fos staining is used to map recently active neurons.

## Alternative splicing
One gene can produce **several mRNA and protein isoforms** by combining exons differently: exon skipping, mutually exclusive exons, alternative 5'/3' sites, intron retention.
- About 95 % of human multi-exon genes are alternatively spliced, and the **brain has the highest splicing complexity** of any tissue (neuron-specific splicing factors such as NOVA, RBFOX, PTBP, SRRM4).
- **Neuro examples:**
  - **Neurexins**: three genes with alternative promoters and splicing produce **thousands** of isoforms. These presynaptic adhesion molecules help specify synapse identity.
  - **Dscam** in *Drosophila*: up to 38,016 isoforms, which give each neuron a unique identity for self-avoidance of dendrites.
  - **AMPA receptor flip/flop** exons change desensitisation kinetics.
  - **Tau** exon 10 gives 3R and 4R isoforms; an imbalance between them causes frontotemporal dementia.
- **Therapy:** in **spinal muscular atrophy (SMA)**, *SMN1* is lost. The backup gene *SMN2* mostly skips exon 7, producing unstable protein. **Nusinersen**, an antisense oligonucleotide, binds the pre-mRNA and promotes exon 7 inclusion, producing functional SMN protein. It was a breakthrough in treating a fatal neurological disease.

## In neuroscience #neuro
- **Cell type identity** = a gene expression profile, measured by single-cell RNA-seq ([[Meth06 Omics and Sequencing]]).
- **Rett syndrome:** mutations in *MECP2* (X-linked) disrupt reading of DNA methylation, causing a severe neurodevelopmental disorder, mostly in girls.
- **Early-life environment:** in rats, maternal licking and grooming alters methylation of the glucocorticoid receptor gene in the offspring's hippocampus, which changes their stress responses (a famous example, still debated in detail).
- **HDAC inhibitors** enhance memory formation in animal models.
- **Genetic tools:** promoters (hSyn, CaMKIIα, GFAP) drive cell-type-specific expression in AAVs; Cre-lox; CRISPR ([[Meth05 Molecular Biology Tools]]).

## Math links #math-link
- Differential equations (steady state, time constant, stability, Euler steps) → [[B10 Differential Equations]]
- Codon combinatorics $4^3 = 64$; number of isoforms from combining independent exon choices = product of the options → [[A7 Sums Products and Factorials]], [[A1 Exponent Rules]]
- Information: $\log_2 4 = 2$ bits per base → [[A3 Logarithms]]
- Gene expression dynamics (production and degradation): $\frac{dm}{dt} = k - \gamma m$ gives an exponential approach to steady state $k/\gamma$ → [[B2 Exponential Functions]], [[B6 Differentiation Rules]]
- Expression data are analysed as log fold changes → [[B3 Logarithmic Functions]]

## Connections
- Nucleotides, base pairing → [[Ch08 Biomolecules]], [[Ch02 Chemical Bonds]]
- Proteins and folding → [[Bio03 Proteins and Enzymes]]
- Plasticity requires transcription → [[Bio06 Synapses and Neurotransmitters]]
- Tools: PCR, CRISPR, AAVs → [[Meth05 Molecular Biology Tools]]; RNA-seq → [[Meth06 Omics and Sequencing]]

## Key takeaways
- Replication is semiconservative; polymerases work 5' → 3'. Neurons don't divide but constantly repair their DNA.
- Transcription → processing (cap, poly-A, splicing) → translation (codons, tRNA, ribosome).
- Epigenetics: methylation silences, acetylation opens chromatin. Activity → CREB → immediate early genes → long-term memory.
- Alternative splicing multiplies protein diversity, and the brain uses it most.
