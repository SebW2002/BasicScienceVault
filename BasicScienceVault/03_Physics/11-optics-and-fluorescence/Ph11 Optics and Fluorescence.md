---
aliases: [Optics and Fluorescence, Refraction, Lens Equation, Diffraction Limit, Fluorescence, Photobleaching, Optik]
tags: [physics, optics, fluorescence, diffraction, type/overview, neuro]
---
# Ph11 Optics and Fluorescence

> [[MOC-physics|↑ Physics MOC]] · [[Ph11 Optics and Fluorescence - Worksheet|✏️ Worksheet]] · [[Ph11 Optics and Fluorescence - Solutions|✅ Solutions]] · [[Mistakes - Physics|⚠️ Mistake log]]

## Why this matters
Much of modern neuroscience is optical: microscopes, calcium indicators, optogenetics through optical fibres, and the eye itself. Understanding refraction, lenses, the diffraction limit and fluorescence explains why microscopes have a resolution limit, why super-resolution needed a Nobel prize, and why imaging is always a trade-off with photobleaching and phototoxicity. The methods side is in [[Meth01 Microscopy]].

## Light basics
- Light is an electromagnetic wave: $c = \lambda f$, with $c\approx3\times10^8$ m/s in vacuum.
- Visible: ~400 nm (violet) to ~700 nm (red). Near-infrared (700–1300 nm) penetrates tissue better.
- Light also comes in packets (photons) with energy $E = hf = hc/\lambda$ ([[Ph12 Quantum Basics for Biophysics]]).

## Refraction and the refractive index
- **Refractive index** $n = \frac{c}{v}$ (how much slower light travels in a medium): air ≈ 1.00, water 1.33, brain tissue ≈ 1.36–1.40, glass ≈ 1.5, immersion oil 1.52, lipids ≈ 1.45–1.5.
- **Snell's law** at an interface:
  $$n_1\sin\theta_1 = n_2\sin\theta_2$$
  Going into a denser medium (higher $n$), light bends **towards** the normal.
- **Total internal reflection:** going from high to low $n$ beyond the **critical angle** $\sin\theta_c = \frac{n_2}{n_1}$, all light is reflected. This guides light in **optical fibres** (optogenetics, fibre photometry) and is the basis of **TIRF** microscopy (only a ~100 nm layer near the coverslip is illuminated).
- **Refractive index mismatch** between sample, immersion medium and objective causes **aberrations** that blur deep images; tissue clearing methods equalise $n$ to make tissue transparent. Differences in $n$ between cell components cause **scattering**, which is why tissue looks white and opaque.
- **Scattering** depends strongly on wavelength (for small particles roughly $\propto1/\lambda^4$; in tissue somewhat weaker). Longer wavelengths scatter less, which is why two-photon microscopy (920 nm and beyond) and red-shifted opsins reach deeper.

## Lens equation and magnification
**Thin lens equation:**
$$\frac1f = \frac{1}{d_o} + \frac{1}{d_i}$$
($f$ = focal length, $d_o$ = object distance, $d_i$ = image distance)
**Magnification:**
$$M = -\frac{d_i}{d_o}$$
(negative = inverted image)
- Object outside $2f$: real, inverted, smaller image (camera, eye).
- Object between $f$ and $2f$: real, inverted, magnified image (microscope objective, projector).
- Object inside $f$: virtual, upright, magnified image (magnifying glass, eyepiece).
- **Microscope:** total magnification = objective × eyepiece (e.g. 40× × 10× = 400×). **Resolution**, however, is set by the objective's **numerical aperture**, not by magnification. Magnifying beyond resolution is "empty magnification".
- Refractive power $D = 1/f$ in dioptres (1/m). The eye has about 60 dpt (cornea ~43 dpt, lens ~17–20 dpt).

## Diffraction limit
Light passing through an aperture (the objective) is **diffracted**. A point source is imaged as a blurred spot (the Airy pattern, point spread function).
- **Abbe limit:**
  $$d = \frac{\lambda}{2\,\text{NA}},\qquad \text{NA} = n\sin\theta$$
- **Rayleigh criterion** (two points just resolved): $d = 0.61\frac{\lambda}{\text{NA}}$.
- With $\lambda = 500$ nm and NA = 1.4: $d\approx180$–220 nm laterally; axially 2–3 times worse.
- **To improve resolution:** a shorter wavelength (UV, or electrons with pm wavelengths in EM), a higher NA (oil immersion, large angle), or tricks that **bypass** diffraction: **super-resolution** (STED, PALM/STORM, SIM; [[Meth01 Microscopy]]).

## Fluorescence basics
**Jablonski diagram (simplified):**
1. **Absorption** of a photon lifts the molecule from the ground state S₀ to an excited state S₁ (~10⁻¹⁵ s).
2. **Vibrational relaxation** within S₁ loses a little energy as heat (~10⁻¹² s).
3. **Emission** of a photon on return to S₀: **fluorescence**, after a **lifetime** of ~1–10 ns.
4. Alternatives: non-radiative decay (heat), or **intersystem crossing** to the long-lived triplet state T₁, which can react with O₂ (photobleaching, ROS).

| Concept | Meaning |
|---|---|
| **Excitation and emission spectra** | wavelengths absorbed vs. emitted; filters separate them |
| **Stokes shift** | emission is at a **longer** wavelength (lower energy) than excitation, because energy is lost in relaxation. GFP: excitation ~488 nm, emission ~510 nm |
| **Quantum yield** $\Phi$ | $\frac{\text{photons emitted}}{\text{photons absorbed}}$ (0–1); EGFP ≈ 0.6 |
| **Extinction coefficient** $\varepsilon$ | how strongly a molecule absorbs |
| **Brightness** | $\propto\varepsilon\cdot\Phi$ |
| **Fluorescence lifetime** | ~ns; it can report the environment (FLIM) |
| **FRET** | non-radiative energy transfer between two fluorophores; efficiency $\propto\frac{1}{1 + (r/R_0)^6}$ with $R_0\approx5$ nm, a "molecular ruler" used in biosensors (e.g. cAMP or PKA sensors) |

**Indicators** change their fluorescence with a biological variable: Ca²⁺ (GCaMP), voltage (GEVIs), pH (pHluorin), neurotransmitters (iGluSnFR for glutamate, dLight/GRAB sensors for dopamine). See [[Meth04 In Vivo Imaging]].

## Photobleaching and phototoxicity
- **Photobleaching:** irreversible destruction of the fluorophore, mostly via the triplet state and reactions with oxygen. Each molecule emits only a limited number of photons (~10⁵–10⁶ for good dyes) before it bleaches. This limits imaging time and is the core of the **photon budget** problem in voltage imaging and super-resolution.
- **Phototoxicity:** light (especially UV and blue, and very high intensities) creates **reactive oxygen species** and heat, which damage cells, alter physiology or kill them. In vivo, heating by laser light can itself change neuronal activity and confound optogenetic experiments.
- **Mitigation:** use as little light as possible, more sensitive detectors, red-shifted fluorophores, two-photon excitation (confines excitation to the focus), light-sheet microscopy, and oxygen scavengers or antifade media for fixed samples.

## In neuroscience #neuro
- **The eye:** cornea and lens refract light onto the retina; accommodation changes the lens's focal length. Myopia means the eye is too long for its refractive power (the image falls in front of the retina).
- **Optical fibres** for optogenetics rely on total internal reflection. Their NA determines the light cone emitted into the tissue.
- **Two-photon imaging** in living brains: long wavelength (less scattering) plus $I^2$ excitation (sectioning).
- **Ca²⁺ and voltage indicators** are fluorescent proteins designed to change brightness with the variable of interest.

## Math links #math-link
- Fourier series and transforms (spectra, convolution theorem, k-space) → [[B12 Fourier Analysis]]
- Snell's law and NA: sines of angles → [[D4 Unit Circle Trigonometry]], [[B4 Trigonometric Functions]]
- Lens equation: fractions and solving for $d_i$ → [[A5 Fractions]], [[A8 Solving Equations]]
- $\lambda^{-4}$ scattering, $r^{-6}$ FRET: power laws → [[A1 Exponent Rules]]
- Exponential attenuation in tissue $I = I_0e^{-z/\ell}$; fluorescence decay $e^{-t/\tau}$ → [[B2 Exponential Functions]]
- Image formation as convolution with the PSF; Fourier optics → [[B7 Antiderivatives and Integration]], [[E2 Complex Numbers]]

## Connections
- Microscope types → [[Meth01 Microscopy]]
- Indicators → [[Meth04 In Vivo Imaging]]; opsins → [[Meth05 Molecular Biology Tools]]
- Photon energy, energy levels → [[Ph12 Quantum Basics for Biophysics]]
- Waves → [[Ph09 Waves and Oscillations]]

## Key takeaways
- $n = c/v$; Snell: $n_1\sin\theta_1 = n_2\sin\theta_2$; total internal reflection guides light in fibres.
- $1/f = 1/d_o + 1/d_i$; $M = -d_i/d_o$. Resolution depends on NA, not on magnification.
- Abbe: $d = \lambda/(2\text{NA})\approx200$ nm. Super-resolution methods bypass it.
- Fluorescence: absorb → relax → emit at a longer wavelength (Stokes shift). Quantum yield = emitted/absorbed. Bleaching and phototoxicity limit how much light you can use.
