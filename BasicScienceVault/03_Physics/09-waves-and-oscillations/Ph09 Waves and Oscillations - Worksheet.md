---
tags: [physics, oscillation, fourier, type/worksheet]
---
# Ph09 Waves and Oscillations – Worksheet

> Theory: [[Ph09 Waves and Oscillations]] · Solutions: [[Ph09 Waves and Oscillations - Solutions]] · Log mistakes in [[Mistakes - Physics]]
> No calculator unless marked 🧮. $\pi\approx3.14$; $1/(2\pi)\approx0.16$.

## Level 1 – Describing oscillations
1. An alpha rhythm has a frequency of 10 Hz. What is its period? Its angular frequency?
2. A signal is $x(t) = 20\sin(2\pi\cdot6\,t)$ µV. Name amplitude, frequency, period and band.
3. Two 40 Hz oscillations are offset by 6.25 ms. What is the phase difference in degrees and radians?
4. Assign the bands: 2 Hz, 6 Hz, 10 Hz, 20 Hz, 60 Hz, 200 Hz.

## Level 2 – Fourier & sampling
5. A recording of 4 s is Fourier-transformed. What is the frequency resolution? What window length is needed to resolve 0.25 Hz?
6. What is the minimum sampling rate for an EEG signal containing frequencies up to 100 Hz? For spikes with components up to 6 kHz?
7. A 60 Hz signal is sampled at 100 Hz. At what (false) frequency does it appear? (Alias frequency = $\lvert f - f_s\rvert$ for $f_s/2 < f < f_s$.)
8. Why does a sharp square pulse require high frequencies in its Fourier representation?
9. A signal consists of 10 Hz with amplitude 4 µV and 40 Hz with amplitude 2 µV. Sketch the power spectrum (relative power values).

## Level 3 – Filters
10. Compute the cutoff frequency of an RC low-pass filter with $R = 10\,\text{k}\Omega$ and $C = 1\,\mu\text{F}$.
11. A membrane has τ = 20 ms. Compute its cutoff frequency. A neuron with τ = 5 ms?
12. Should spikes be extracted with a high-pass or a low-pass filter? The LFP?
13. A first-order low-pass filter has $f_c = 10$ Hz. Roughly how much is a 100 Hz component attenuated (factor and dB)?

## Level 4 – Neuro transfer
14. Why does the passive membrane favour slow inputs, and what does this mean for the precision of spike timing?
15. Explain how an HCN-channel (I_h) current can turn a neuron into a band-pass filter.
16. 🧮 A 1/f² background spectrum: by what factor does power fall from 2 Hz to 20 Hz? In dB?
