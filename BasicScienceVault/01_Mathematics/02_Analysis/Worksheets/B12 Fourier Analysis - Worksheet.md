---
tags: [analysis, fourier, type/worksheet]
---
# B12 Fourier Analysis – Worksheet

> Theory: [[B12 Fourier Analysis]] · Solutions: [[B12 Fourier Analysis - Solutions]] · Log mistakes in [[Mistakes - Analysis]]
> No calculator unless marked 🧮.

## Level 1 – Basics
1. A signal is $x(t) = 3\sin(2\pi\cdot5t) + \cos(2\pi\cdot20t)$. Which frequencies appear, with which amplitudes? Sketch the amplitude spectrum.
2. Show that $\int_0^{2\pi}\sin t\cos t\,dt = 0$ and $\int_0^{2\pi}\sin^2t\,dt = \pi$. (Hint: $\sin t\cos t = \tfrac12\sin2t$, $\sin^2t = \tfrac12(1 - \cos2t)$.)
3. A function is even. Which Fourier coefficients vanish? And for an odd function?
4. Write $\cos(\omega t)$ in complex exponential form.

## Level 2 – Series
5. The square wave series is $\frac4\pi(\sin t + \frac13\sin3t + \frac15\sin5t + \dots)$. What is the amplitude of the 3rd and 5th harmonic relative to the fundamental? Why are there no even harmonics?
6. What happens to the shape of the reconstructed square wave if you only use the first term? The first three terms?
7. Compute the Fourier coefficients of $f(t) = 2 + \sin t + 4\cos3t$ by inspection: $a_0/2$, $a_n$, $b_n$.

## Level 3 – Transform properties
8. A signal is delayed by 10 ms. What happens to its power spectrum? To its phase spectrum?
9. Signal A is a Gaussian pulse of width 1 ms; signal B is a Gaussian of width 10 ms. Which has the broader spectrum?
10. Why does cutting a long sine wave into a short window produce power at neighbouring frequencies? How do window functions help?
11. Use the convolution theorem: what is the Fourier transform of a signal convolved with a Gaussian smoothing kernel? What kind of filter is Gaussian smoothing?

## Level 4 – DFT and applications
12. A 4 s EEG segment is sampled at 250 Hz. How many samples? What are the frequency resolution, the frequency of bin $k = 40$, and the Nyquist frequency?
13. Compute the DFT of $x = (1, 0, -1, 0)$ by hand ($N = 4$, $e^{-2\pi ik n/4}$ gives the values $1, -i, -1, i$). Which frequency does the signal contain?
14. In MRI, only the central part of k-space was acquired. What does the image look like? Why?
15. 🧮 Compute the ratio of operations of a direct DFT ($N^2$) and an FFT ($N\log_2N$) for $N = 2^{20}$.
