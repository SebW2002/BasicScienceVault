---
tags: [computer-science, signal-processing, type/worksheet]
---
# CS11 Time Series and Signal Processing – Worksheet

> Theory: [[CS11 Time Series and Signal Processing]] · Solutions: [[CS11 Time Series and Signal Processing - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮. $\log_21024 = 10$.

## Level 1 – Sampling and convolution
1. An LFP is sampled at 1000 Hz. What is the Nyquist frequency? A 700 Hz artefact is present without anti-aliasing. At which frequency does it appear?
2. Compute the discrete convolution of $f = (1, 2, 3)$ and $g = (1, 1)$.
3. A 3-point moving average has $b = (\tfrac13, \tfrac13, \tfrac13)$. Apply it to $x = (3, 6, 9, 12)$ (only where all three points exist). Is this FIR or IIR?
4. What does the convolution theorem state, and why is it useful for filtering long signals?

## Level 2 – Filters and spectra
5. The IIR filter $y[n] = 0.5x[n] + 0.5y[n - 1]$ receives an impulse $x = (1, 0, 0, 0, \dots)$. Compute $y[0..3]$. Why is it called "infinite impulse response"?
6. A recording lasts 2 s at $f_s = 1000$ Hz. What is the frequency resolution of its FFT? How many samples is that?
7. Compare the cost of a direct DFT ($N^2$) and an FFT ($N\log_2N$) for $N = 1024$.
8. Why use `filtfilt` (forward-backward filtering) for offline analysis, and why can't you use it for closed-loop stimulation?

## Level 3 – Spikes
9. A high-pass filtered trace has $\text{median}(\lvert x\rvert) = 13.5\,\mu\text{V}$. Estimate σ and a detection threshold of 4.5σ.
10. A unit has 10,000 spikes, and 300 ISIs are shorter than 1.5 ms. What fraction is that? Is this a well-isolated single unit?
11. Describe what you would see in the autocorrelogram of a) a regular-spiking neuron with a refractory period, b) a bursting neuron, c) a neuron locked to an 8 Hz theta rhythm.
12. A cross-correlogram between neurons A and B shows a narrow peak at +2 ms (B fires 2 ms after A). Interpret. What would a broad peak centred at 0 suggest?

## Level 4 – Population analyses
13. What does factor analysis provide that PCA does not?
14. A UMAP plot shows two clusters far apart and one small cluster. Which conclusions are valid, and which are not?
15. 🧮 Spike train with spikes at 10, 12, 30 and 31 ms is convolved with a causal exponential kernel $k(t) = e^{-t/5}$ (t in ms, for $t\ge0$). Compute the smoothed value at $t = 32$ ms.
