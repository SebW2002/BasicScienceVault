---
aliases: [Quantum Basics for Biophysics, Photon Energy, Quantum Tunneling, Energy Levels, Absorption Spectra, Quantenphysik]
tags: [physics, quantum, photon, spectroscopy, type/overview, neuro]
---
# Ph12 Quantum Basics for Biophysics

> [[MOC-physics|↑ Physics MOC]] · [[Ph12 Quantum Basics for Biophysics - Worksheet|✏️ Worksheet]] · [[Ph12 Quantum Basics for Biophysics - Solutions|✅ Solutions]] · [[Mistakes - Physics|⚠️ Mistake log]]

## Why this matters
You don't need quantum mechanics to understand neurons, but three quantum ideas run through modern neuroscience:
1. **Light comes in photons** whose energy depends on wavelength. This decides which light excites which fluorophore or opsin, and why two infrared photons can replace one blue one.
2. **Molecules have discrete energy levels**, which explains absorption spectra and the colours of indicators.
3. **Tunnelling** lets electrons (and protons) cross barriers, which matters for electron transport in mitochondria. This part stays qualitative.

## Photon energy
$$E = hf = \frac{hc}{\lambda},\qquad h = 6.626\times10^{-34}\,\text{J·s}$$
**Handy form:** $E\,[\text{eV}]\approx\frac{1240}{\lambda\,[\text{nm}]}$ (1 eV = $1.602\times10^{-19}$ J; per mole, 1 eV ≈ 96.5 kJ/mol).

| Light | λ | Photon energy | In units of $kT$ (37 °C) |
|---|---|---|---|
| UV-B | 300 nm | 4.1 eV | ~150 |
| Blue (ChR2, GFP excitation) | 470 nm | 2.6 eV (≈ 255 kJ/mol) | ~100 |
| Yellow (NpHR) | 590 nm | 2.1 eV | ~80 |
| Red (Chrimson, ChRmine) | 630 nm | 2.0 eV | ~73 |
| Near-IR (two-photon) | 920 nm | 1.35 eV | ~50 |

- **Shorter wavelength means higher energy.** UV photons can break chemical bonds directly: DNA damage (thymine dimers), phototoxicity.
- A photon is absorbed **all or nothing**: a molecule can only absorb if the photon energy matches an energy gap. Many weak red photons can't do what one UV photon does, **unless two arrive at the same time**, which is the principle of **two-photon excitation**: $2\times1.35\,\text{eV}\approx2.7\,\text{eV}$, the energy of one blue photon. Because two photons must coincide, the probability ∝ $I^2$ ([[Meth01 Microscopy]]).
- **Single photons count:** rod photoreceptors can detect **one photon**. One rhodopsin isomerisation triggers a cascade (transducin → PDE → cGMP ↓ → channels close) amplified about 10⁵-fold.
- **Photon statistics:** photons arrive randomly (Poisson), so the noise in a measurement of $N$ photons is $\sqrt N$ (**shot noise**). The signal-to-noise ratio is $\sqrt N$, and dim signals are inherently noisy ([[A2 Root Rules]], [[A7 Sums Products and Factorials]]).
- **Detectors** use the photoelectric effect: one photon releases one electron, which is multiplied (photomultiplier tubes, GaAsP detectors in two-photon microscopes; sCMOS and EMCCD cameras).

## Energy levels and absorption spectra
Electrons in atoms and molecules occupy **discrete energy levels**. A photon is absorbed only if its energy matches a gap $\Delta E = E_2 - E_1$.
| Transition | Energy | Spectral region | Use |
|---|---|---|---|
| Electronic | ~1–10 eV | UV–visible | colour, fluorescence, photochemistry |
| Vibrational | ~0.05–0.5 eV | infrared | IR spectroscopy; heating by IR light |
| Rotational | ~10⁻⁴–10⁻³ eV | microwave | (microwave heating of water) |
| Nuclear spin in a magnetic field | ~10⁻⁷ eV | radio frequency | **NMR, MRI** ([[Meth02 Structural Biology]], [[Meth04 In Vivo Imaging]]) |

- **Absorption spectra** are broad bands rather than sharp lines in molecules, because each electronic level contains many vibrational sublevels and the environment adds variation.
- **Conjugated systems:** chains of alternating single and double bonds delocalise electrons. A longer conjugated system gives a smaller energy gap and a longer absorbed wavelength (in the "particle in a box" picture, $E_n\propto n^2/L^2$, so a longer box has smaller gaps). Examples: retinal in rhodopsin and in channelrhodopsins; the GFP chromophore; chlorophyll.
- **The protein environment tunes the gap:** the same retinal chromophore absorbs at ~420 nm (blue cones), ~530 nm (green cones), ~560 nm (red cones) or ~500 nm (rods), depending on the surrounding opsin. Protein engineers use this to create blue-, green- and red-shifted opsins and indicators.
- **Beer–Lambert law** (absorption in solution): $A = \varepsilon cl$ and $I = I_010^{-A}$, used to measure concentrations (e.g. DNA at 260 nm, protein at 280 nm).

## Quantum tunnelling (qualitative)
- Classically, a particle needs enough energy to climb over a barrier. Quantum mechanically, its wavefunction extends into the barrier, so there is a small probability of **passing through** it even with too little energy.
- The probability falls **exponentially** with barrier width and with the square root of the particle mass times barrier height: roughly $P\sim e^{-2d\sqrt{2m\Delta E}/\hbar}$.
- **Consequence: only very light particles tunnel noticeably over molecular distances.**
  - **Electrons** tunnel across ~1–2 nm (≈ 10–20 Å) between redox centres in proteins. This is how electrons move along the **mitochondrial electron transport chain** ([[Ch05 Redox and Electrochemistry]]): cofactors are spaced ≤ ~14 Å apart, and the protein acts as a tuned barrier.
  - **Protons** (and hydrogen atoms) tunnel over much shorter distances (< 1 Å). This contributes to the speed of some **enzyme** reactions that transfer hydrogen (kinetic isotope effects).
  - **Ions** like Na⁺ or K⁺ are far too heavy to tunnel through channel barriers. Ion permeation is classical: thermally activated hopping between binding sites, shedding of water ([[Ch01 Atomic Structure]]). Quantum effects matter at most in subtle ways (e.g. in the electronic structure of the selectivity filter), and claims of "quantum ion channels" or a "quantum brain" are speculative.
- **Technology:** the **SQUIDs** used in MEG rely on electron-pair tunnelling through Josephson junctions ([[Ph06 Magnetism and Induction]]); scanning tunnelling microscopes image surfaces atom by atom.

## In neuroscience #neuro
- **Choosing optogenetic tools:**
  - photon energy must match the opsin's absorption
  - blue light (ChR2) scatters strongly and is absorbed by haemoglobin, so it reaches only shallow tissue
  - red-shifted opsins allow deeper and even transcranial activation
- **Fluorescent indicators** must have excitation and emission spectra that fit your lasers and filters, and that don't overlap with opsins (crosstalk in all-optical experiments).
- **Vision** begins with a photochemical reaction: 11-*cis*-retinal → all-*trans*-retinal after absorbing one photon (quantum yield ≈ 0.65), one of the fastest reactions in biology (~200 fs).
- **UV damage:** sunlight causes thymine dimers in skin DNA. Defective repair (xeroderma pigmentosum) can also involve progressive neurodegeneration in some forms.

## Math links #math-link
- $E = hc/\lambda$: inverse proportionality, unit conversion (eV, J, kJ/mol) → [[A1 Exponent Rules]], [[A5 Fractions]]
- Tunnelling probability decays exponentially with distance → [[B2 Exponential Functions]]
- Beer–Lambert absorbance as a decadic logarithm → [[A3 Logarithms]]
- Shot noise $\sqrt N$ (Poisson statistics) → [[A2 Root Rules]], [[A7 Sums Products and Factorials]]
- Particle in a box: $E_n\propto n^2/L^2$ (power laws) → [[A1 Exponent Rules]]

## Connections
- Fluorescence, Stokes shift → [[Ph11 Optics and Fluorescence]]
- Thermal energy for comparison → [[Ph08 Thermodynamics and Statistics]]
- Two-photon and super-resolution microscopy → [[Meth01 Microscopy]]
- Opsins, optogenetics → [[Meth05 Molecular Biology Tools]]
- Electron transport chain → [[Ch05 Redox and Electrochemistry]]
- cis/trans isomerisation of retinal → [[Ch07 Organic Chemistry Essentials]]

## Key takeaways
- $E = hf = hc/\lambda\approx1240/\lambda[\text{nm}]$ eV. Blue ≈ 2.6 eV ≈ 100 $kT$. Two 920 nm photons ≈ one blue photon.
- Molecules absorb only photons matching an energy gap. Conjugation and protein environment set the colour.
- Photon counting is Poisson: SNR = $\sqrt N$.
- Tunnelling is exponential in distance and mass: electrons tunnel ~1–2 nm (ETC), protons barely, ions essentially not.
