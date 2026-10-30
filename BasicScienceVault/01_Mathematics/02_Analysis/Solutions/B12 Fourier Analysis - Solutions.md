---
tags: [analysis, fourier, type/solution]
---
# B12 Fourier Analysis – Solutions

> Worksheet: [[B12 Fourier Analysis - Worksheet]] · Theory: [[B12 Fourier Analysis]] · Wrong? → [[Mistakes - Analysis]]

## Level 1
1. 5 Hz with amplitude 3 and 20 Hz with amplitude 1. The spectrum shows two lines (power 9 and 1).
2. $\int_0^{2\pi}\tfrac12\sin2t\,dt = \tfrac12\left[-\tfrac12\cos2t\right]_0^{2\pi} = 0$. $\int_0^{2\pi}\tfrac12(1 - \cos2t)\,dt = \tfrac12\cdot2\pi - 0 = \pi$.
3. Even: all $b_n = 0$ (only cosines and constant). Odd: all $a_n = 0$ (including $a_0$; only sines).
4. $\cos\omega t = \frac{e^{i\omega t} + e^{-i\omega t}}{2}$.

## Level 2
5. 1/3 and 1/5 of the fundamental. The square wave has half-wave symmetry ($f(t + T/2) = -f(t)$), which cancels all even harmonics.
6. One term: a plain sine with the same period (peak $4/\pi\approx1.27$). Three terms: a flatter top and steeper edges, with ripples. It approaches the square wave, but the overshoot at the edges stays at about 9 % (Gibbs).
7. $a_0/2 = 2$; $b_1 = 1$; $a_3 = 4$; all others 0.

## Level 3
8. The power spectrum is **unchanged** ($\lvert e^{-2\pi i\nu t_0}\rvert = 1$). The phase spectrum gets an extra linear term $-2\pi\nu t_0$ (larger phase shift for higher frequencies).
9. **A** (narrow in time means broad in frequency).
10. A window multiplies the sine by a rectangle, so in frequency the spectrum is convolved with a sinc function, whose side lobes spread power into neighbouring bins (leakage). Smooth windows (Hann) taper the edges, which gives much smaller side lobes at the cost of a slightly broader main peak.
11. $\mathcal F\{x * g\} = \hat x\cdot\hat g$, and the transform of a Gaussian is a Gaussian centred at 0. High frequencies are multiplied by small values, so Gaussian smoothing is a **low-pass filter** (without ringing).

## Level 4
12. $N = 1000$; $\Delta f = 0.25$ Hz; $f_{40} = 40\cdot0.25 = 10$ Hz (alpha); Nyquist frequency 125 Hz.
13. $X_k = \sum_nx_ne^{-2\pi ikn/4} = 1\cdot1 + (-1)\cdot e^{-\pi ik}$, so $X_k = 1 - (-1)^k$. $X_0 = 0$, $X_1 = 2$, $X_2 = 0$, $X_3 = 2$. Power is at bin 1 (and its mirror, bin 3 = −1): one cycle per 4 samples, i.e. the frequency $f_s/4$. (The signal is $\cos(\pi n/2)$.)
14. The image is **blurred** (low resolution, with possible ringing at edges). The centre of k-space holds the low spatial frequencies (contrast, coarse structure); the edges hold the high ones (fine detail, sharp edges).
15. $N^2 = 2^{40}$; $N\log_2N = 2^{20}\cdot20$. The ratio is $\frac{2^{20}}{20}\approx52{,}429$: the FFT is about 50,000 times faster.
