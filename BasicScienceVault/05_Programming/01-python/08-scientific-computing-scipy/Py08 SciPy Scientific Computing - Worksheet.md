---
tags: [programming, python, scipy, type/worksheet]
---
# Py08 SciPy Scientific Computing – Worksheet

> Theory: [[Py08 SciPy Scientific Computing]] · Solutions: [[Py08 SciPy Scientific Computing - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Which function?
1. Name the SciPy function for: a) zero-phase band-pass filtering b) power spectrum averaged over windows c) detecting action potentials above 0 mV d) a paired t-test e) fitting an exponential decay f) simulating Hodgkin–Huxley g) resampling eye-tracking data onto the EEG clock.
2. `stats.norm.cdf(0)`, `stats.norm.ppf(0.5)`, `stats.norm.sf(1.96)` (approx.)?
3. What is the difference between `quad` and `trapezoid`?

## Level 2 – Understanding
4. `signal.butter(4, 40, btype="low")` without `fs=`. What does the 40 mean, and what happens?
5. Why does `filtfilt` not shift an ERP peak, while `lfilter` does? When is `filtfilt` not allowed?
6. You use `welch(x, fs=500, nperseg=250)`. What is the frequency resolution? How do you get 0.25 Hz resolution, and what is the price?
7. `find_peaks(v)` on a noisy trace returns 4000 peaks in 1 s. Which arguments do you add?
8. `curve_fit` returns `tau = 3e5` for a membrane decay with τ ≈ 20 ms. Likely cause?

## Level 3 – Calculate and write
9. For λ = 2 spikes per bin, compute $P(K = 0)$ and $P(K \ge 1)$ by hand ($e^{-2}\approx0.135$). Write the `stats.poisson` calls.
10. Write code for a 4th-order Butterworth high-pass at 1 Hz, applied zero-phase to EEG sampled at 500 Hz.
11. An exponential ISI distribution with mean 50 ms: what fraction of ISIs are shorter than 2 ms (a refractory-period violation in a real neuron)? Hint: $1 - e^{-x}\approx x$ for small $x$. Which SciPy call gives the exact value?

## Level 4 – Neuro transfer
12. Describe a pipeline (functions + parameters) to compute alpha power (8–12 Hz) per channel from resting-state EEG at 500 Hz.
13. Write the `solve_ivp` call for $\tau\dot V = -(V - E_L) + RI$ with τ = 10 ms, $E_L$ = −65 mV, $RI$ = 10 mV, $V(0) = -65$ mV, for 100 ms. What is $V$ at the end (analytically)?
14. 💻 Simulate 10 s of a 10 Hz sine plus white noise at fs = 250 Hz, compute the Welch PSD with 2-s windows and find the peak frequency.
