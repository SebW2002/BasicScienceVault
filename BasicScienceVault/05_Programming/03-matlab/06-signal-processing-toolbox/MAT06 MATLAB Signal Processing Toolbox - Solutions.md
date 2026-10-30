---
tags: [programming, matlab, signal-processing, type/solution]
---
# MAT06 MATLAB Signal Processing Toolbox – Solutions

> Worksheet: [[MAT06 MATLAB Signal Processing Toolbox - Worksheet]] · Theory: [[MAT06 MATLAB Signal Processing Toolbox]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. a) `filtfilt` b) `butter` (or `designfilt`) c) `pwelch` d) `spectrogram` (or `cwt`) e) `findpeaks` f) `abs(hilbert(x))` (after band-pass filtering).
2. By $N$ (the FFT is unscaled). The energy of a real signal is split between positive and negative frequencies; the single-sided spectrum adds the mirrored half back (except DC and Nyquist, which have no mirror).
3. Fractions of the Nyquist frequency $f_s/2$ (0 < Wn < 1).

## Level 2
4. N = 4000; Δf = 1000/4000 = 0.25 Hz (= 1/4 s); Nyquist = 500 Hz. 10 Hz is bin 10/0.25 = 40 in 0-based counting → **index 41** in MATLAB (index 1 is 0 Hz).
5. 1/250 = **0.004** and 40/250 = **0.16**.
6. 500 samples / 250 Hz = **2 s** windows; 250/500 = **50 %** overlap; Δf = 1/2 s = **0.5 Hz**.
7. N = 100; `abs(fft(x))` at 10 Hz = A·N/2 = 2 · 100/2 = **100**; single-sided amplitude = 100/N · 2 = **2 µV**.

## Level 3
8. `filtfilt` filters along the **columns** (first dimension), i.e. across the 64 channels at each time point – nonsense. Transpose: `y = filtfilt(b, a, EEG')';`.
9. With $W_n = 0.05/1000 = 5\cdot10^{-5}$ the poles lie extremely close to the unit circle; the polynomial coefficients `b, a` lose precision, so the filter becomes unstable. Use second-order sections (`[z,p,k] = butter(...); [sos, g] = zp2sos(z, p, k); filtfilt(sos, g, x)`), `designfilt`, an FIR filter, or downsample first.
10. `filter` is causal: an IIR low-pass delays (and phase-shifts) the signal, so peaks appear later. Use `filtfilt` (zero phase) for offline ERP analysis.
11. Without `fs`, `MinPeakDistance` is in **samples**: 2 samples = 67 µs at 30 kHz – far shorter than a spike. Use `findpeaks(v, fs, "MinPeakDistance", 0.001)` (1 ms) or 30 samples, and/or `MinPeakProminence`.

## Level 4
12. ```matlab
    fs = 500;
    [P, f] = pwelch(X', hann(2*fs), fs, [], fs);   % columns = channels → P is nf × 64
    alpha = bandpower(P, f, [8 12], "psd");        % 1 × 64 band power per channel
    ```
13. **Line noise** at 50 Hz (European mains) and its harmonics. Fix the recording setup (grounding, shielding, impedances); in analysis use notch/band-stop filters at 50, 100, 150 Hz, spectral interpolation, or methods like CleanLine/ZapLine; or simply low-pass below 50 Hz if your band of interest allows it.
14. ```matlab
    fs = 500; t = 0:1/fs:2-1/fs; x = 2*sin(2*pi*10*t) + 0.5*randn(size(t));
    N = numel(x); X = fft(x); f = (0:N-1)*fs/N;
    a1 = abs(X(1:N/2+1))/N; a1(2:end-1) = 2*a1(2:end-1);
    [~, i] = max(a1); [f(i) a1(i)]          % ≈ [10 2]
    X2 = fft(x, 4096); f2 = (0:4095)*fs/4096;
    a2 = abs(X2(1:2049))/N; a2(2:end-1) = 2*a2(2:end-1);   % divide by the original N
    plot(f(1:N/2+1), a1, "o", f2(1:2049), a2, "-")         % zero-padding interpolates: smoother, same peak
    ```
