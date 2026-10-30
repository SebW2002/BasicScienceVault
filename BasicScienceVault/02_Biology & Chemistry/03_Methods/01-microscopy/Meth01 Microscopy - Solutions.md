---
tags: [methods, microscopy, type/solution]
---
# Meth01 Microscopy – Solutions

> Worksheet: [[Meth01 Microscopy - Worksheet]] · Theory: [[Meth01 Microscopy]] · Wrong? → [[Mistakes - Methods]]

## Level 1
1. $d = \frac{\lambda}{2\text{NA}}$: $\lambda$ = wavelength, NA $= n\sin\theta$ = numerical aperture, where $n$ is the refractive index of the immersion medium and $\theta$ is the half-opening angle of the objective.
2. It blocks light from out-of-focus planes, so only light from the focal plane reaches the detector (optical sectioning).
3. (1) Infrared light is scattered less by tissue than visible light. (2) Excitation happens only at the focus (∝ $I^2$), so scattered emission photons can still be collected without a pinhole (all detected light comes from the focus).
4. SIM ~100–120 nm; STED ~30–80 nm; PALM/STORM ~10–30 nm (and MINFLUX ~1–5 nm; expansion ~70 nm effective).
5. TEM: electrons pass **through** ultrathin sections, giving a 2D projection with internal detail. SEM: a beam **scans** the surface and scattered or secondary electrons are detected, giving topography; with serial block-face SEM or FIB-SEM it gives 3D volumes.

## Level 2
6. $d = \frac{500}{2.5} = 200\,\text{nm}$. No: 50 nm is well below the limit. Super-resolution or EM is needed.
7. NA $= 1.5\cdot0.94\approx1.41$. In air $n = 1$ and $\sin\theta\le1$, so NA ≤ 1 (practically ≤ 0.95).
8. $2^2 = 4$ times more signal. Excitation is concentrated sharply at the focus (good sectioning), but photodamage also scales nonlinearly: at high power, damage at the focus rises quickly (with heating and higher-order effects).
9. $\sqrt{1 + I/I_\text{sat}} = 10\Rightarrow I/I_\text{sat} = 99$
10. $N = 100$: $100/10 = 10\,\text{nm}$. $N = 10\,000$: $100/100 = 1\,\text{nm}$. More photons give better precision, but only with the square root.

## Level 3
11. a) Chronic **two-photon** imaging through a cranial window (in vivo, deep, repeated). b) **Super-resolution** (STORM/STED) or immuno-EM, because vesicles (~40 nm) are below the diffraction limit. c) **Cryo-EM single-particle analysis** (or X-ray crystallography). d) **Serial-section EM** (connectomics). e) **Cryo-ET** of FIB-milled lamellae.
12. $250/4\approx62\,\text{nm}$. Possible artefacts: anisotropic or non-uniform expansion (distortion), loss of antigens or fluorescence during digestion, gaps or cracks. Validate with known structures.

## Level 4
13. Ice crystals would form, which (1) destroy membranes and proteins and (2) scatter electrons strongly. Very rapid freezing (plunging into liquid ethane, or high-pressure freezing) produces **amorphous (vitreous) ice**, which keeps the sample in a native, hydrated state.
14. **Averaging:** thousands to millions of identical particles are imaged in different orientations. They are classified and aligned computationally, and averaging increases the signal-to-noise ratio (∝ √number of particles). Combining all orientations reconstructs a 3D map (via the Fourier projection-slice theorem).
15. The sample can only be tilted up to about ±60–70° (beyond that the sample is too thick and the holder blocks the beam). Information from the missing angles is absent, forming a wedge in Fourier space. The result is **elongation and blurring along the beam axis** and poorer reconstruction of some features (e.g. flat membranes perpendicular to the beam).
16. $e^{-600/200} = e^{-3}\approx0.05$, so about 5 % of ballistic light reaches 600 µm. To keep the same excitation at the focus, power must rise about 20-fold, and since two-photon signal ∝ $I^2$, the loss of signal would otherwise be 400-fold. This sets practical depth limits (heating, out-of-focus background) and motivates three-photon microscopy at longer wavelengths for deeper imaging.
