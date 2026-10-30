---
tags: [methods, pcr, antibody, crispr, optogenetics, type/worksheet]
---
# Meth05 Molecular Biology Tools – Worksheet

> Theory: [[Meth05 Molecular Biology Tools]] · Solutions: [[Meth05 Molecular Biology Tools - Solutions]] · Log mistakes in [[Mistakes - Methods]]
> No calculator unless marked 🧮. $2^{10}\approx1000$.

## Level 1 – Recall
1. Name the three steps of a PCR cycle with their approximate temperatures.
2. What is separated in SDS-PAGE, and what is SDS for?
3. What is the difference between IHC and IF? Name four cell-type markers.
4. Which opsin activates and which silences neurons? With which light colours?
5. What is the packaging capacity of AAV, and why is it a practical limitation?

## Level 2 – Calculation
6. You start a PCR with 100 template copies. How many copies after 10 cycles? After 30 cycles (100 % efficiency)?
7. qPCR: target Ct = 24 in controls and 21 in treated; reference gene Ct = 18 in both. Compute ΔCt, ΔΔCt and the fold change.
8. A gene is downregulated with ΔΔCt = +2. What is the fold change?
9. A sample has a Ct 3.3 cycles lower than another. Roughly how many times more template does it contain? ($2^{3.3}\approx10$)
10. A 20-nt guide RNA: how often would a random 20-nt sequence match by chance in a genome of $3\times10^9$ bases (estimate with $4^{20}\approx10^{12}$)? Why do off-targets still happen?

## Level 3 – Experimental design
11. You want to express ChR2 **only** in parvalbumin interneurons of the mouse prefrontal cortex. Describe the components (mouse line, vector, promoter/construct, serotype, delivery).
12. Choose between optogenetics and DREADDs: a) silence neurons for exactly 200 ms during a decision, b) increase the activity of a population during 2 days of social behaviour, c) test a brain-wide effect without an implant.
13. Your antibody for protein X gives a band at the expected size in wild-type mice. What is the best control to prove specificity?
14. You want to know whether drug Y increases the phosphorylation of CREB in the hippocampus. Which method and which controls?

## Level 4 – Interpretation
15. CNO alone (without DREADD expression) changes behaviour in a few studies. Explain why, and how to control for it.
16. Optogenetic activation of neuron population P drives behaviour B. Can you conclude that P normally causes B? What other experiment would you add?
17. 🧮 PCR efficiency is 90 % ($E = 0.9$). How many copies are there after 30 cycles from 100 templates ($N = N_0(1 + E)^n$)? Compare with 100 % efficiency.
