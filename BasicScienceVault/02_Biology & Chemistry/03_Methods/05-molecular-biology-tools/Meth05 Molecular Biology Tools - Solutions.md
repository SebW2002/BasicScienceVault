---
tags: [methods, pcr, antibody, crispr, optogenetics, type/solution]
---
# Meth05 Molecular Biology Tools – Solutions

> Worksheet: [[Meth05 Molecular Biology Tools - Worksheet]] · Theory: [[Meth05 Molecular Biology Tools]] · Wrong? → [[Mistakes - Methods]]

## Level 1
1. Denaturation (~95 °C), annealing (~50–65 °C), extension (72 °C).
2. Proteins by **size** (molecular weight). SDS denatures them and coats them with uniform negative charge, so migration depends only on size, not native charge or shape.
3. IHC uses an enzymatic colour reaction (e.g. DAB, viewed in brightfield); IF uses fluorophores (multiple colours, confocal). Markers: NeuN (neurons), GFAP (astrocytes), Iba1 (microglia), Olig2/MBP (oligodendrocytes/myelin), PV/SST/VIP (interneurons), TH (dopamine neurons).
4. Activates: ChR2 (blue, ~470 nm). Silences: NpHR (yellow, ~590 nm), ArchT (green-yellow), GtACR (blue).
5. About 4.7 kb. Large genes (e.g. many ion channels, *DMD*, Cas9 with all its regulatory parts) don't fit, which requires split systems, smaller orthologues or other vectors.

## Level 2
6. $100\cdot2^{10}\approx10^5$; $100\cdot2^{30}\approx10^{11}$.
7. ΔCt control $= 24 - 18 = 6$; ΔCt treated $= 21 - 18 = 3$; ΔΔCt $= 3 - 6 = -3$; fold change $= 2^{3} = 8$ (eightfold up).
8. $2^{-2} = 0.25$ (fourfold down).
9. About 10 times more ($2^{3.3}\approx10$).
10. Expected matches $\approx\frac{3\times10^9}{10^{12}}\approx0.003$ (roughly ×2 for both strands), so a perfect random match is very unlikely. Off-targets happen because Cas9 **tolerates mismatches** (especially far from the PAM), and the genome is not random (repeats, gene families).

## Level 3
11. **PV-Cre** mouse + **Cre-dependent AAV** (DIO/FLEX-ChR2-eYFP, e.g. under a strong ubiquitous promoter such as EF1α) + a neurotropic serotype (AAV1, 5 or 9) + **stereotaxic injection** into the PFC (+ an optical fibre above the site). Only PV⁺ cells express Cre, which flips the transgene into the active orientation. Afterwards, verify by IF (PV + eYFP overlap).
12. a) Optogenetics (ms precision). b) DREADDs (hM3Dq; minutes to hours, repeated ligand dosing). c) DREADDs (systemic ligand, no implant), or optogenetics with transcranial red-shifted opsins.
13. A **knockout** (or knockdown) sample: the band must disappear. (Also: peptide blocking, a second antibody against a different epitope, and molecular weight checks.)
14. **Western blot** with a phospho-specific antibody (p-CREB Ser133) **and** total CREB on the same samples (report the ratio), plus a loading control. Vehicle-treated controls, the correct time point, rapid tissue harvest with phosphatase inhibitors, and blinded quantification. Optionally, IF for p-CREB to localise it to specific cell types.

## Level 4
15. CNO is **back-metabolised to clozapine**, which crosses the BBB and acts on many receptors (D2, 5-HT₂A, H1, …). Controls: DREADD-negative animals receiving the same ligand dose, the lowest effective dose, and newer ligands (DCZ, compound 21) with fewer off-target effects.
16. Not necessarily. Stimulation shows **sufficiency** under artificial conditions, possibly with unnatural synchronous patterns and rates. Add a **loss-of-function** experiment (silencing P during natural B should impair B: **necessity**) and a recording (calcium imaging or photometry) showing P is **naturally active** during B. Also: titrate stimulation to physiological levels and run opsin-free light controls (heat, light visible to the animal).
17. $100\cdot1.9^{30}$: $\ln1.9^{30} = 30\cdot0.642 = 19.26$, so $1.9^{30}\approx2.3\times10^8$, giving about $2.3\times10^{10}$ copies. With 100 %: $100\cdot2^{30}\approx1.07\times10^{11}$, about 4.6 times more. Small efficiency differences add up exponentially, which is why efficiency correction matters in qPCR.
