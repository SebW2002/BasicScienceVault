---
tags: [computer-science, signal-processing, type/solution]
---
# CS11 Time Series and Signal Processing – Solutions

> Worksheet: [[CS11 Time Series and Signal Processing - Worksheet]] · Theory: [[CS11 Time Series and Signal Processing]] · Wrong? → [[Mistakes - Computer Science]]

## Level 1
1. Nyquist frequency 500 Hz. The 700 Hz artefact appears at $1000 - 700 = 300$ Hz.
2. $(f * g)[n] = \sum_kf[k]g[n - k]$: $n = 0$: 1; $n = 1$: $2 + 1 = 3$; $n = 2$: $3 + 2 = 5$; $n = 3$: 3. Result $(1, 3, 5, 3)$.
3. $(3 + 6 + 9)/3 = 6$, $(6 + 9 + 12)/3 = 9$, giving $(6, 9)$. **FIR**: only a finite number of inputs, no feedback.
4. Convolution in the time domain equals multiplication in the frequency domain. For long signals or long kernels, FFT → multiply → inverse FFT ($O(N\log N)$) is much faster than direct convolution ($O(NM)$), and it makes filter design in terms of frequencies intuitive.

## Level 2
5. $y[0] = 0.5$, $y[1] = 0.25$, $y[2] = 0.125$, $y[3] = 0.0625$ (halving each step). Because of the feedback, the response to one impulse never becomes exactly zero; it decays geometrically, like an RC circuit ([[Ph05 Capacitance and RC Circuits]]).
6. $\Delta f = 1/T = 0.5$ Hz; $N = 2000$ samples.
7. Direct: $1024^2\approx1.05\times10^6$. FFT: $1024\cdot10\approx10^4$, about 100 times faster.
8. Forward-backward filtering cancels the phase shift (zero phase): waveforms and event timings are not shifted or distorted. It needs **future** samples (it is non-causal), so it is impossible in real time, where only causal filters can be used.

## Level 3
9. $\hat\sigma = 13.5/0.6745\approx20\,\mu\text{V}$; threshold $= 4.5\cdot20 = 90\,\mu\text{V}$ (for negative-going spikes, −90 µV).
10. $300/10{,}000 = 3\%$. That is too many for a single neuron (a typical criterion is < 0.5–1 %), so the cluster is probably contaminated by spikes from other neurons (multi-unit) and needs splitting or should be labelled multi-unit.
11. a) A gap (dip) around 0 ms (±1–3 ms), then a flat level. b) A tall peak at short lags (a few ms) right after the refractory dip. c) Periodic side peaks at multiples of 125 ms (±125, ±250 ms, …).
12. A narrow peak at +2 ms means B tends to fire 2 ms after A, consistent with a **monosynaptic excitatory connection A → B** (it should be confirmed by jitter/shuffle controls). A broad peak centred at 0 suggests **common input** or shared slow modulation (e.g. brain state), not a direct connection.

## Level 4
13. FA explicitly separates **shared** variance (latent factors common to many neurons) from **private** (independent) noise variance per neuron. PCA lumps everything together, so neurons with high individual noise can dominate PCs. FA gives a cleaner estimate of shared structure and dimensionality.
14. Valid: points within a cluster are similar to each other (local neighbourhoods), and there appear to be groups. **Not valid:** that the clusters are far apart in the original space (global distances are distorted); that the small cluster is "small" in variance (sizes and densities are distorted); that axes have meaning. Verify clusters in the original space and with stability analyses.
15. Contributions at $t = 32$: $e^{-22/5} = e^{-4.4}\approx0.0123$; $e^{-20/5} = e^{-4}\approx0.0183$; $e^{-2/5} = e^{-0.4}\approx0.670$; $e^{-1/5} = e^{-0.2}\approx0.819$. Sum ≈ **1.52**.
