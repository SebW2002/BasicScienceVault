---
tags: [programming, matlab, signal-processing, type/worksheet]
---
# MAT06 MATLAB Signal Processing Toolbox – Worksheet

> Theory: [[MAT06 MATLAB Signal Processing Toolbox]] · Solutions: [[MAT06 MATLAB Signal Processing Toolbox - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper; no calculator unless marked. Run code only for tasks marked 💻.

## Level 1 – Recall
1. Which function: a) zero-phase filtering b) a Butterworth design c) PSD by averaging windows d) time–frequency map e) peaks of a spike waveform f) amplitude envelope.
2. What must you divide `abs(fft(x))` by to get amplitudes? Why double the one-sided spectrum?
3. In `butter(4, Wn)`, what are the units of `Wn`?

## Level 2 – Calculate
4. fs = 1000 Hz, 4 s recording. What is N, the frequency resolution of `fft(x)`, and the Nyquist frequency? Which bin index (1-based) corresponds to 10 Hz?
5. You want a 1 Hz high-pass and a 40 Hz low-pass at fs = 500 Hz. What are the normalised cut-offs?
6. `pwelch(x, hann(500), 250, [], 250)`: window length in s, overlap in %, frequency resolution?
7. A pure 10 Hz sine of amplitude 2 µV, 1 s at fs = 100 Hz: what values do the bins at 10 Hz of `abs(fft(x))` and of the single-sided amplitude spectrum have?

## Level 3 – Debug
8. `y = filtfilt(b, a, EEG)` with `EEG` 64 × 10000 (channels × time) gives strange results. Why? Fix.
9. A 4th-order Butterworth high-pass at 0.05 Hz with fs = 2000 Hz in `[b, a]` form produces NaNs/explosions. Why, and what do you use instead?
10. An ERP filtered with `filter(b, a, x)` (low-pass 20 Hz) peaks 15 ms later than in the literature. Explain.
11. `findpeaks(v, "MinPeakDistance", 2)` on data at 30 kHz still finds several peaks per spike. Why?

## Level 4 – Neuro transfer
12. Write the MATLAB lines to compute alpha (8–12 Hz) band power per channel of resting EEG `X` (channels × time, fs = 500 Hz) with 2-s Welch windows.
13. You see a sharp peak at 50 Hz and smaller ones at 100 and 150 Hz. What are they and what do you do?
14. 💻 Generate 2 s of `x = 2*sin(2*pi*10*t) + 0.5*randn(size(t))` at fs = 500 Hz, compute the single-sided amplitude spectrum with `fft`, and check that the 10 Hz peak is ≈ 2. Then zero-pad to 4096 and compare.
