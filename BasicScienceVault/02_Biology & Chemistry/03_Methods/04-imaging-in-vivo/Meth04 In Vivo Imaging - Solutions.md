---
tags: [methods, imaging, type/solution]
---
# Meth04 In Vivo Imaging – Solutions

> Worksheet: [[Meth04 In Vivo Imaging - Worksheet]] · Theory: [[Meth04 In Vivo Imaging]] · Wrong? → [[Mistakes - Methods]]

## Level 1
1. Neurovascular coupling increases **blood flow** much more than O₂ consumption. More oxygenated blood flows in than is used, so the local concentration of paramagnetic **deoxyhaemoglobin falls**, T2* lengthens, and the signal rises.
2. About 4–6 s after stimulus onset.
3. Two **511 keV gamma photons** in opposite directions. Only pairs detected simultaneously (within ns) on opposite detectors come from one annihilation, which defines a line of response through the source. This gives localisation and rejects random events.
4. GCaMP is a GFP fused to calmodulin and the M13 peptide. When Ca²⁺ binds calmodulin, the complex changes conformation and the fluorescence of the circularly permuted GFP increases.
5. Advantages: direct measure of membrane potential, ms resolution, subthreshold events and hyperpolarisation visible. Challenge: small signals and few photons (photon budget), photobleaching, limited field of view.

## Level 2
6. Any three: whether the activity is **excitatory or inhibitory**; whether it reflects **spiking output** or synaptic input; whether the region is **necessary** for the task (correlation ≠ causation); the **timing** (ms-scale sequence); which **cell types** are involved; whether the effect is neural or partly vascular (e.g. changed vascular reactivity).
7. Raclopride and endogenous dopamine **compete** for the same D2/D3 receptors. More released dopamine occupies more receptors, so fewer are available for the tracer and binding potential falls.
8. ¹¹C decays with $t_{1/2}\approx20$ min, so within 2 hours only ~1/64 is left. ¹⁸F lasts ~110 min, long enough for transport over a few hours.
9. Inhibition and subthreshold depolarisation open few or no Ca²⁺ channels, so intracellular Ca²⁺ barely changes. Hyperpolarisation doesn't produce a Ca²⁺ drop that indicators can easily detect. Calcium imaging therefore mainly reports spikes (and dendritic Ca²⁺ events).

## Level 3
10. $\frac{260 - 200}{200} = 0.3 = 30\,\%$
11. 220 min = 2 half-lives, so $\frac14 = 25\,\%$. 330 min = 3 half-lives, so $\frac18 = 12.5\,\%$.
12. 60 min = 3 half-lives, so $\frac18$ of the initial activity.
13. $0.05\cdot100\,000 = 5000$ false-positive voxels. Bonferroni: $\alpha_\text{voxel} = 0.05/100\,000 = 5\times10^{-7}$ (very conservative, because neighbouring voxels are correlated; alternatives include FDR and cluster-based or random-field methods).

## Level 4
14. a) **Amyloid PET** (or CSF/blood biomarkers). b) **fMRI** (face localiser). c) **Chronic two-photon calcium imaging** through a cranial window. d) **Voltage imaging** (or dual patch clamp of dendrite and soma). e) **[¹¹C]raclopride PET** (displacement during the task).
15. The haemodynamic responses overlap strongly (HRF ~ 15–20 s long), so the two regressors are highly **correlated** (collinear) and the GLM can't uniquely assign variance ($X^TX$ nearly singular, [[C2 Determinants]]). Fixes: **jitter** the interval randomly (e.g. 2–8 s), include trials with a cue but no reward (catch trials), and use longer and variable intervals.
16. Contributions at 1.5 s: AP at 0: $20e^{-1.5}\approx20\cdot0.223 = 4.5\,\%$. AP at 0.5: $20e^{-1}\approx7.4\,\%$. AP at 1: $20e^{-0.5}\approx12.1\,\%$. Sum ≈ **24.0 %**.
