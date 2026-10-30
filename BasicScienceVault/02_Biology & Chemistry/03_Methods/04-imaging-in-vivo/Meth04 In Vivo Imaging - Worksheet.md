---
tags: [methods, imaging, type/worksheet]
---
# Meth04 In Vivo Imaging – Worksheet

> Theory: [[Meth04 In Vivo Imaging]] · Solutions: [[Meth04 In Vivo Imaging - Solutions]] · Log mistakes in [[Mistakes - Methods]]
> No calculator unless marked 🧮.

## Level 1 – Recall
1. Why does the BOLD signal *increase* during neural activity, although neurons consume more oxygen?
2. At what time does the haemodynamic response typically peak after a brief stimulus?
3. What is emitted when a positron annihilates, and why does the PET detector look for coincidences?
4. Describe in one sentence how GCaMP works.
5. Name two advantages of voltage imaging over calcium imaging and one major challenge.

## Level 2 – Understanding
6. A study reports "region X is activated by task Y" based on BOLD. List three things this does **not** directly tell you.
7. Why does [¹¹C]raclopride binding decrease when dopamine is released?
8. Why must ¹¹C tracers be produced on-site while ¹⁸F tracers can be shipped?
9. Why does calcium imaging struggle to detect inhibition or subthreshold activity?

## Level 3 – Calculation
10. Baseline fluorescence $F_0 = 200$ counts, peak $F = 260$ counts. Compute $\Delta F/F$ in %.
11. [¹⁸F] has a half-life of 110 min. What fraction of the activity remains after 220 min? After 330 min?
12. [¹¹C] has a half-life of 20 min. A tracer is produced at 9:00. How much activity is left at 10:00?
13. An fMRI study tests 100,000 voxels at $\alpha = 0.05$ without correction. How many false positives do you expect if there is no true effect anywhere? What does Bonferroni correction do to the threshold?

## Level 4 – Method choice & design
14. Choose the method: a) whether a patient's memory complaints are associated with amyloid plaques, b) which brain regions respond to faces in healthy volunteers, c) how 300 identified neurons in mouse V1 change their responses over 2 weeks of learning, d) the timing of dendritic spikes vs. somatic spikes in a single neuron, e) dopamine release in the human striatum during a reward task.
15. Two fMRI regressors (e.g. "cue" and "reward") are always presented 1 s apart. Why is it difficult to separate their effects? How could you change the design?
16. 🧮 A GCaMP6s transient after one AP decays with $\tau = 1\,\text{s}$. A neuron fires 3 APs at $t = 0$, 0.5 and 1 s, each adding $\Delta F/F = 20\,\%$ (linear summation). What is $\Delta F/F$ at $t = 1.5\,\text{s}$?
