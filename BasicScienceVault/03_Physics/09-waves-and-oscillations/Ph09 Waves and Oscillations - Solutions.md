---
tags: [physics, oscillation, fourier, type/solution]
---
# Ph09 Waves and Oscillations – Solutions

> Worksheet: [[Ph09 Waves and Oscillations - Worksheet]] · Theory: [[Ph09 Waves and Oscillations]] · Wrong? → [[Mistakes - Physics]]

## Level 1
1. $T = 0.1\,\text{s} = 100\,\text{ms}$; $\omega = 2\pi\cdot10\approx62.8\,\text{rad/s}$
2. $A = 20\,\mu\text{V}$, $f = 6\,\text{Hz}$, $T\approx167\,\text{ms}$, theta band.
3. $\Delta\varphi = 2\pi\cdot40\cdot0.00625 = 2\pi\cdot0.25 = \frac\pi2$ = 90°
4. 2 Hz delta; 6 Hz theta; 10 Hz alpha; 20 Hz beta; 60 Hz gamma; 200 Hz ripple.

## Level 2
5. $\Delta f = 1/4 = 0.25\,\text{Hz}$; for 0.25 Hz, 4 s (as computed).
6. > 200 Hz (in practice ≥ 500 Hz); > 12 kHz (in practice 20–30 kHz).
7. $\lvert60 - 100\rvert = 40\,\text{Hz}$. The 60 Hz signal appears as a 40 Hz "gamma oscillation", a dangerous artefact. This is why anti-aliasing filters are applied before sampling.
8. Sharp edges are fast changes. Representing them requires the summation of many high-frequency components (harmonics). Without them, edges become rounded and show ringing (the Gibbs phenomenon).
9. Power ∝ amplitude²: 10 Hz → 16, 40 Hz → 4. A spectrum with two peaks, the 10 Hz peak four times higher (not twice).

## Level 3
10. $f_c = \frac{1}{2\pi\cdot10^4\cdot10^{-6}} = \frac{1}{2\pi\cdot10^{-2}}\approx16\,\text{Hz}$
11. τ = 20 ms: $\frac{1}{2\pi\cdot0.02}\approx8\,\text{Hz}$. τ = 5 ms: ≈ 32 Hz.
12. Spikes: **high-pass** (> 300 Hz). LFP: **low-pass** (< 300 Hz).
13. 100 Hz is one decade above $f_c$, so the amplitude is attenuated about 10-fold, i.e. −20 dB.

## Level 4
14. The membrane capacitance must be charged. Fast fluctuations are "smoothed out" before the voltage can follow, while slow inputs reach their full effect. Inputs are integrated over about τ, so spike times are less precisely locked to fast input features. Neurons that need precise timing (auditory brainstem) have very short τ.
15. I_h is activated by **hyperpolarisation** and is slow (time constants of tens to hundreds of ms). It depolarises the cell back when the voltage drops, opposing slow voltage changes, which acts like a **high-pass** filter. Together with the passive membrane (**low-pass**), the result is a **band-pass**: the neuron responds most strongly to inputs at an intermediate frequency (resonance, often 4–10 Hz).
16. $P\propto f^{-2}$, so $(20/2)^{-2} = 10^{-2}$: power falls 100-fold. $10\log_{10}(0.01) = -20$ dB.
