---
aliases: [MATLAB Signal Processing, fft in MATLAB, butter filtfilt, pwelch, spectrogram, findpeaks]
tags: [programming, matlab, signal-processing, fourier, filter, type/overview, neuro]
---
# MAT06 MATLAB Signal Processing Toolbox

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT06 MATLAB Signal Processing Toolbox - Worksheet|✏️ Worksheet]] · [[MAT06 MATLAB Signal Processing Toolbox - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
Filtering, spectra and peak detection are the first steps of every EEG, LFP and spike analysis. `fft` is built into MATLAB; `butter`, `filtfilt`, `pwelch`, `spectrogram` and `findpeaks` come from the **Signal Processing Toolbox** (a licensed add-on – check `ver`). EEGLAB and FieldTrip call these functions internally (or ship their own replacements). The maths is in [[B12 Fourier Analysis]] and [[CS11 Time Series and Signal Processing]].

## fft: the discrete Fourier transform
```matlab
fs = 500; T = 2; t = (0:1/fs:T-1/fs);          % N = 1000 samples
x = 2*sin(2*pi*10*t) + 0.5*randn(size(t));
N = numel(x);
X = fft(x);                                     % complex, length N
f = (0:N-1) * fs / N;                           % frequency of each bin: Δf = fs/N = 1/T
amp = abs(X) / N;                               % two-sided amplitude
amp1 = amp(1:N/2+1); amp1(2:end-1) = 2 * amp1(2:end-1);   % single-sided amplitude
f1 = f(1:N/2+1);
plot(f1, amp1)                                  % peak ≈ 2 at 10 Hz
phase = angle(X);                               % phase in radians
```
- `fft` does **no scaling**: divide by $N$ for amplitudes; double the one-sided spectrum except DC and Nyquist.
- **Resolution** $\Delta f = f_s/N = 1/T$ depends on the **duration**, not the sampling rate; zero-padding (`fft(x, 4096)`) interpolates the spectrum but adds no information.
- Frequencies above $f_s/2$ (Nyquist) are the mirrored negative frequencies; `fftshift` centres 0 Hz.
- `ifft` inverts; use the **convolution theorem** for fast filtering/convolution (`conv` for direct convolution).
- Window before the FFT (`x .* hann(N)'`) to reduce **spectral leakage**.

## filter, filtfilt, butter
```matlab
[b, a] = butter(4, [1 40] / (fs/2), "bandpass");   % 4th-order Butterworth band-pass
% (a band-pass of order n has 2n poles)
y_causal = filter(b, a, x);                        % causal: phase shift / delay
y = filtfilt(b, a, x);                             % zero-phase: forward + backward
[b, a] = butter(4, 1 / (fs/2), "high");            % high-pass
[z, p, k] = butter(8, 40 / (fs/2)); [sos, g] = zp2sos(z, p, k);  y = filtfilt(sos, g, x);   % numerically stable SOS form
d = designfilt("bandstopiir", "FilterOrder", 4, "HalfPowerFrequency1", 49, ...
               "HalfPowerFrequency2", 51, "SampleRate", fs);
y = filtfilt(d, x);                                % notch for 50 Hz line noise
freqz(b, a, 2048, fs)                              % inspect the frequency response
fvtool(b, a)                                       % filter visualisation tool
```
- `butter(n, Wn)` expects cut-offs **normalised to Nyquist** ($W_n = f_c/(f_s/2)$, between 0 and 1) – unlike SciPy with `fs=` ([[Py08 SciPy Scientific Computing]]). `designfilt` takes Hz with `"SampleRate"`.
- `filter` is causal (delays the signal and shifts phases); `filtfilt` is zero-phase but non-causal and squares the magnitude response (doubles attenuation in dB).
- High-order IIR filters in `[b, a]` form become numerically unstable, especially for low cut-offs relative to $f_s$ (e.g. 0.1 Hz high-pass at 1 kHz). Use second-order sections (`zp2sos`, `designfilt`) or FIR filters (`fir1`, `designfilt("bandpassfir", ...)`) – EEGLAB's `pop_eegfiltnew` uses windowed-sinc FIR.
- Filters operate along the **first non-singleton dimension** – for channels × time data, transpose (`filtfilt(b, a, X')'`): `filtfilt` works down the columns.
- Built-in convenience functions: `lowpass`, `highpass`, `bandpass`, `bandstop` (R2018a+).

## spectrogram and pwelch
```matlab
[Pxx, f] = pwelch(x, hann(2*fs), fs, [], fs);    % 2-s Hann windows, 50 % overlap → Δf = 0.5 Hz
plot(f, 10*log10(Pxx)); xlabel("Frequency (Hz)"); ylabel("PSD (dB/Hz)")
alpha = bandpower(Pxx, f, [8 12], "psd");       % band power from a PSD
[s, f, t] = spectrogram(x, hann(256), 192, 512, fs);   % window 256, overlap 192, nfft 512
imagesc(t, f, 10*log10(abs(s).^2)); axis xy; colorbar
spectrogram(x, 256, 192, 512, fs, "yaxis")      % without outputs: plots directly
```
- **Welch's method** averages periodograms of overlapping windowed segments: less variance than one FFT of the whole signal, at the cost of resolution ($\Delta f = 1/T_\text{window}$).
- **Time–frequency trade-off:** long windows → fine frequency, coarse time resolution; short windows → the reverse ([[B12 Fourier Analysis]], uncertainty). Neuroscience often uses **wavelets** (`cwt`) or multitapers (Chronux, FieldTrip `mtmconvol`) instead.
- Inputs are (signal, window, noverlap, nfft, fs) – positional; empty `[]` means default.

## findpeaks
```matlab
[pks, locs] = findpeaks(v, fs, "MinPeakHeight", 0, "MinPeakDistance", 0.002);  % locs in s when fs is given
[pks, locs, w, p] = findpeaks(v, "MinPeakProminence", 20);   % widths and prominences
findpeaks(-x, "MinPeakHeight", thr)                          % troughs (negative spikes)
```
- With `fs` as second argument, locations and distances are in **seconds**; without it, in samples.
- `MinPeakProminence` (how much a peak stands out from its surroundings) is usually more robust than height alone.

## Same idea in Python and R
| MATLAB | SciPy / NumPy | R |
|---|---|---|
| `fft`, `ifft` | `np.fft.fft`, `np.fft.rfft` | `fft()` |
| `butter(n, fc/(fs/2))` | `signal.butter(n, fc, fs=fs)` | `signal::butter(n, fc/(fs/2))` |
| `filtfilt` | `signal.filtfilt`, `sosfiltfilt` | `signal::filtfilt` |
| `pwelch` | `signal.welch` | `stats::spec.pgram`, `bspec` |
| `spectrogram` | `signal.spectrogram` | `signal::specgram` |
| `findpeaks` | `signal.find_peaks` | `pracma::findpeaks` |
→ [[Py08 SciPy Scientific Computing]], [[R09 R Neuroscience Packages]]

## In neuroscience #neuro
- **EEG/LFP:** high-pass 0.1–1 Hz (drifts), low-pass 30–100 Hz, notch 50/60 Hz; band power in delta–gamma with `pwelch` + `bandpower`.
- **Spikes:** band-pass 300–6000 Hz, threshold at −4.5 × median(|x|)/0.6745, `findpeaks(-x, ...)`.
- **ERP latencies** are distorted by causal filters (`filter`); use `filtfilt` offline and report the filter type/order/cut-offs.
- **Time–frequency analysis** of induced oscillations (e.g. alpha desynchronisation) with `spectrogram`/wavelets, baseline-normalised in dB.
- **Hilbert transform** (`hilbert`) for amplitude envelopes and instantaneous phase of band-passed signals (phase–amplitude coupling; [[E2 Complex Numbers]]).

## Math links #math-link
- DFT, $\Delta f = 1/T$, Nyquist, leakage, convolution theorem → [[B12 Fourier Analysis]]
- Complex amplitude and phase (`abs`, `angle`) → [[E2 Complex Numbers]]
- Sines and frequencies → [[B4 Trigonometric Functions]]
- Decibels → [[A3 Logarithms]]

## Connections
- Concepts → [[CS11 Time Series and Signal Processing]], [[Ph09 Waves and Oscillations]]
- Plotting spectra → [[MAT05 MATLAB Plotting]]
- EEGLAB filtering → [[MAT09 EEGLAB]]
- Python equivalent → [[Py08 SciPy Scientific Computing]]

## Key takeaways
- `fft` is unscaled: divide by $N$; $f = (0{:}N{-}1)\,f_s/N$; resolution $1/T$.
- `butter` needs normalised cut-offs $f_c/(f_s/2)$; `filtfilt` = zero-phase offline; use SOS/FIR for low cut-offs; mind the filtering dimension.
- `pwelch` for PSDs (window length sets resolution), `spectrogram` for time–frequency.
- `findpeaks` with `fs` gives seconds; prominence is robust.
