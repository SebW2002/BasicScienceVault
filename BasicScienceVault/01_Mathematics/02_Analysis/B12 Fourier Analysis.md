---
aliases: [Fourier Analysis, Fourier Series, Fourier Transform, DFT, Fourieranalyse]
tags: [analysis, fourier, trigonometry, complex, type/overview, neuro]
---
# B12 Fourier Analysis

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B12 Fourier Analysis - Worksheet|✏️ Worksheet]] · [[B12 Fourier Analysis - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
Fourier analysis decomposes any signal into sine waves. It is everywhere in the vault:
- EEG/MEG/LFP spectra and brain rhythms
- filters and the convolution theorem
- **MRI image reconstruction** (the scanner measures the Fourier transform of the image)
- X-ray crystallography and cryo-EM (diffraction patterns are Fourier transforms)
- optics and the resolution limit

This note gives the mathematical foundation that [[Ph09 Waves and Oscillations]] and [[CS11 Time Series and Signal Processing]] apply. Prerequisites: [[B4 Trigonometric Functions]], [[B7 Antiderivatives and Integration]], [[E2 Complex Numbers]].

## Fourier series (periodic signals)
A function with period $T$ (fundamental frequency $f_0 = 1/T$, $\omega_0 = 2\pi/T$) can be written as
$$f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\big[a_n\cos(n\omega_0t) + b_n\sin(n\omega_0t)\big]$$
$$a_n = \frac2T\int_0^Tf(t)\cos(n\omega_0t)\,dt,\qquad b_n = \frac2T\int_0^Tf(t)\sin(n\omega_0t)\,dt$$
- **Why the coefficient formulas work: orthogonality.** Over one period, $\int_0^T\sin(n\omega_0t)\sin(m\omega_0t)\,dt = 0$ for $n\neq m$ (likewise for cos·cos, and sin·cos is always 0). Multiplying $f$ by one basis function and integrating "filters out" exactly its coefficient. Sines and cosines are like an orthogonal basis of vectors ([[D2 Dot and Cross Product]]), with the integral playing the role of the dot product.
- **Symmetry shortcuts:** an even $f$ has only cosines ($b_n = 0$); an odd $f$ has only sines ($a_n = 0$) ([[B1 Properties of Functions]]).
- **Example (square wave)** with values ±1, odd:
  $$f(t) = \frac4\pi\left(\sin\omega_0t + \frac13\sin3\omega_0t + \frac15\sin5\omega_0t + \dots\right)$$
  Only odd harmonics appear, with amplitudes $\propto1/n$. Sharp edges need many high-frequency components (and overshoot near the jumps, the **Gibbs phenomenon**).

## Complex form
Using Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ ([[E2 Complex Numbers]]):
$$f(t) = \sum_{n=-\infty}^{\infty}c_ne^{in\omega_0t},\qquad c_n = \frac1T\int_0^Tf(t)e^{-in\omega_0t}\,dt$$
Each $c_n = \lvert c_n\rvert e^{i\varphi_n}$ holds the **amplitude** and **phase** of frequency $nf_0$ in one complex number. For real signals, $c_{-n} = \overline{c_n}$.

## Fourier transform (non-periodic signals)
Let the period go to infinity, so the discrete frequencies become a continuum:
$$\hat f(\nu) = \int_{-\infty}^\infty f(t)\,e^{-2\pi i\nu t}\,dt,\qquad f(t) = \int_{-\infty}^\infty\hat f(\nu)\,e^{2\pi i\nu t}\,d\nu$$
**Key properties**
| Property | Time domain | Frequency domain |
|---|---|---|
| Linearity | $af + bg$ | $a\hat f + b\hat g$ |
| Time shift | $f(t - t_0)$ | $e^{-2\pi i\nu t_0}\hat f$ (only the **phase** changes, not the power) |
| Scaling | $f(at)$ | $\frac{1}{\lvert a\rvert}\hat f(\nu/a)$ (compressing in time **stretches** in frequency) |
| **Convolution theorem** | $f * g$ | $\hat f\cdot\hat g$ |
| Multiplication | $f\cdot g$ | $\hat f * \hat g$ |
| Differentiation | $f'$ | $2\pi i\nu\,\hat f$ |
| **Parseval** | $\int\lvert f\rvert^2dt$ | $= \int\lvert\hat f\rvert^2d\nu$ (energy is preserved) |

**Important pairs:**
- A **Gaussian** transforms into a Gaussian. A narrow Gaussian in time is wide in frequency, and vice versa.
- A **rectangle** (box) transforms into a **sinc** function, $\frac{\sin(\pi\nu T)}{\pi\nu T}$. Cutting a signal into a window therefore smears the spectrum (spectral leakage).
- A **delta impulse** transforms into a constant (all frequencies equally); a pure sine into two deltas at $\pm f$.

**Uncertainty principle:** $\Delta t\cdot\Delta\nu\gtrsim\frac{1}{4\pi}$. You can't have a signal that is sharply localised in both time and frequency. This is the **time–frequency trade-off** of spectrograms and wavelets ([[CS11 Time Series and Signal Processing]]).

## Discrete Fourier transform (DFT) and FFT
For $N$ samples $x_0,\dots,x_{N-1}$ taken at rate $f_s$:
$$X_k = \sum_{n=0}^{N-1}x_n\,e^{-2\pi ikn/N},\qquad k = 0,\dots,N-1$$
- Frequency of bin $k$: $f_k = k\frac{f_s}{N}$. **Resolution** $\Delta f = f_s/N = 1/T_\text{total}$. Bins above $N/2$ correspond to negative frequencies. The **Nyquist frequency** is $f_s/2$ (no information above it; aliasing, [[Ph09 Waves and Oscillations]]).
- **Power spectrum** $\lvert X_k\rvert^2$; **phase** $\arg X_k$.
- The **FFT** computes the DFT in $O(N\log N)$ operations instead of $O(N^2)$, one of the most important algorithms ever.
- The DFT treats the data as **periodic**: discontinuities between the end and the start create leakage, so taper with windows (Hann).

## 2D and 3D Fourier transforms
Images can be decomposed into 2D spatial frequencies (stripes of different orientation and spacing).
- Low spatial frequencies are coarse structure; high spatial frequencies are fine detail and edges.
- **MRI:** the scanner samples the image's 2D/3D Fourier transform directly (**k-space**). An inverse FFT gives the image. Sampling only the centre of k-space gives a blurry image; artefacts in k-space become stripes in the image.
- **Microscopy:** the objective acts as a low-pass filter in spatial frequency (the optical transfer function). Its cutoff, set by NA/λ, is the Abbe limit ([[Ph11 Optics and Fluorescence]]). SIM shifts high frequencies into the observable band.
- **Crystallography and cryo-EM:** diffraction patterns are Fourier transforms of the electron density. The **phase problem** arises because detectors measure only $\lvert F\rvert^2$ ([[Meth02 Structural Biology]]).

## In neuroscience #neuro
- **EEG/MEG power spectra:** alpha peak at ~10 Hz, 1/f background, band power ([[Meth03 Electrophysiology]]).
- **Filtering:** design in the frequency domain, apply via the convolution theorem.
- **Phase and amplitude:** the analytic signal (Hilbert transform, built via the FFT) gives instantaneous phase for phase-locking and phase–amplitude coupling.
- **Receptive fields:** V1 neurons act as spatial-frequency filters (Gabor functions = Gaussian × sine).
- **Spike-train spectra** reveal rhythmic firing; coherence between signals is a normalised cross-spectrum.

## Connections
- Sines, cosines, phase → [[B4 Trigonometric Functions]], [[D4 Unit Circle Trigonometry]]
- Integrals → [[B7 Antiderivatives and Integration]]
- Complex exponentials → [[E2 Complex Numbers]]
- Orthogonality and bases → [[D2 Dot and Cross Product]], [[C1 Matrices]] (the DFT is multiplication by a unitary matrix)
- Applications → [[Ph09 Waves and Oscillations]], [[CS11 Time Series and Signal Processing]], [[Meth04 In Vivo Imaging]]

## Where this is used in the vault
**Most important applications:** EEG/MEG spectra ([[Meth03 Electrophysiology]], [[Ph09 Waves and Oscillations]]), filtering ([[CS11 Time Series and Signal Processing]]), MRI k-space ([[Meth04 In Vivo Imaging]]), diffraction and resolution ([[Ph11 Optics and Fluorescence]], [[Meth02 Structural Biology]]).

**All notes that build on this topic:**
- *Physics:* [[Ph09 Waves and Oscillations]] · [[Ph11 Optics and Fluorescence]]
- *Methods:* [[Meth01 Microscopy]] · [[Meth02 Structural Biology]] · [[Meth03 Electrophysiology]] · [[Meth04 In Vivo Imaging]]
- *Computer Science:* [[CS11 Time Series and Signal Processing]] · [[CS12 Neuroimaging Data Analysis]]
- *Programming:* [[Py01 Python Basics and Syntax]] · [[Py08 SciPy Scientific Computing]] · [[Py10 Python Neuroscience Packages]] · [[R09 R Neuroscience Packages]] · [[MAT06 MATLAB Signal Processing Toolbox]] · [[MAT09 EEGLAB]] · [[MAT10 MATLAB Neuroscience Toolboxes]] · [[Doc06 LaTeX Math]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Any periodic signal = sum of sines and cosines; coefficients follow from orthogonality (integrate against each basis function).
- Complex form: $c_n$ = amplitude and phase in one number.
- The Fourier transform turns convolution into multiplication; a time shift only changes phase; Parseval preserves energy.
- Narrow in time means wide in frequency (uncertainty principle).
- DFT/FFT: resolution $f_s/N$, Nyquist at $f_s/2$, window against leakage.
- MRI k-space, microscope resolution and diffraction are all Fourier transforms.
