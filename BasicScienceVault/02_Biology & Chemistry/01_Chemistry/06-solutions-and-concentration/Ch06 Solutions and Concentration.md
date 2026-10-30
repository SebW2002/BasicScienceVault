---
aliases: [Solutions and Concentration, Molarity, Osmolarity, Diffusion, Osmosis, Lösungen]
tags: [chemistry, concentration, osmosis, diffusion, type/overview, neuro]
---
# Ch06 Solutions and Concentration

> [[MOC-chemistry|↑ Chemistry MOC]] · [[Ch06 Solutions and Concentration - Worksheet|✏️ Worksheet]] · [[Ch06 Solutions and Concentration - Solutions|✅ Solutions]] · [[Mistakes - Chemistry|⚠️ Mistake log]]

## Why this matters
Every lab day starts with concentrations: making artificial CSF, diluting a drug stock, choosing the osmolarity of a pipette solution. Physiologically, diffusion explains why synaptic transmission is fast but transport along axons needs motors, and osmosis explains brain oedema and why plasma sodium must be corrected slowly.

## Amount and concentration
| Quantity | Definition | Unit |
|---|---|---|
| Amount of substance $n$ | $n = \frac{m}{M}$ (mass / molar mass) | mol |
| **Molarity** $c$ | $c = \frac{n}{V}$ | mol/L = M |
| Mass concentration | $\frac{m}{V}$ | g/L, mg/mL |
| % (w/v) | g per 100 mL | – |
| **Osmolarity** | moles of **dissolved particles** per litre | Osm/L, mOsm/L |

Common scales: 1 M = 10³ mM = 10⁶ µM = 10⁹ nM.
Avogadro's number $N_A = 6.022\times10^{23}\,\text{mol}^{-1}$.

**Dilution** (the amount of substance stays the same):
$$c_1V_1 = c_2V_2$$
Example: 1 mM TTX stock to 1 µM in 10 mL means $V_1 = \frac{1\,\mu\text{M}\cdot10\,\text{mL}}{1000\,\mu\text{M}} = 10\,\mu\text{L}$ (a 1:1000 dilution).

## Osmolarity and osmosis
Osmolarity counts **particles**: osmolarity = $i\cdot c$, where $i$ is the number of particles per formula unit.
- glucose: $i = 1$, so 10 mM glucose = 10 mOsm/L
- NaCl → Na⁺ + Cl⁻: $i = 2$, so 150 mM = 300 mOsm/L (ideal)
- CaCl₂ → Ca²⁺ + 2 Cl⁻: $i = 3$
- Plasma and CSF are about **290 mOsm/L**.

**Osmosis** is the net flow of **water** across a semipermeable membrane towards the side with **higher osmolarity** (more particles, so "less free water").
Osmotic pressure (van 't Hoff): $\pi = i\,c\,RT$. A difference of only 1 mOsm/L corresponds to about **19 mmHg**, so small osmotic gradients move a lot of water.

**Tonicity** describes the effect on cell volume, and counts only particles that **cannot** cross the membrane:
- **Isotonic:** volume stays the same (0.9 % NaCl ≈ 300 mOsm/L).
- **Hypotonic:** water enters and the cell **swells**.
- **Hypertonic:** water leaves and the cell **shrinks**.
- Urea is osmotically active but crosses membranes, so it is not "effective". Mannitol does not cross the BBB, so it is effective.

## Diffusion
Diffusion is the random thermal motion of particles, which produces net movement from high to low concentration.

**Fick's first law:** the flux is proportional to the concentration gradient,
$$J = -D\frac{dc}{dx}$$
$D$ = diffusion coefficient. For small molecules in water it is about $10^{-9}\,\text{m}^2/\text{s} = 1\,\mu\text{m}^2/\text{ms}$; for proteins it is 10–100 times smaller.

**Mean diffusion distance:**
$$x_\text{rms} = \sqrt{2Dt}\ \ (\text{1D}),\qquad \sqrt{6Dt}\ \ (\text{3D}) \qquad\Rightarrow\qquad t\approx\frac{x^2}{2D}$$
Time grows with the **square** of the distance:
- 20 nm synaptic cleft: under 1 µs
- 10 µm (a cell body): about 50 ms
- 1 cm (an axon): many hours
- 1 m (sciatic nerve axon): years

Diffusion is fast over short distances and hopeless over long ones.

## In neuroscience #neuro
- **Artificial CSF (aCSF)** for slice electrophysiology, typical recipe in mM: NaCl 125, KCl 2.5, NaHCO₃ 26, NaH₂PO₄ 1.25, CaCl₂ 2, MgCl₂ 1, glucose 25. It is bubbled with 95 % O₂ / 5 % CO₂ (bicarbonate buffer, [[Ch04 Acids Bases and pH]]) and measures about 300–320 mOsm/kg. Pipette solutions are usually made **slightly hypo-osmotic** (e.g. 285–295 mOsm) to keep cells healthy.
- **Brain oedema:** after stroke or trauma, cells swell (cytotoxic oedema). Treatment with **mannitol** or **hypertonic saline** raises plasma osmolarity, so water is drawn out of the brain across the intact BBB. Astrocytes express **aquaporin-4** in their endfeet, the main water channel of the brain.
- **Hyponatraemia:** low plasma Na⁺ (hypotonic) makes brain cells swell, causing headache, confusion and seizures. If it is corrected **too quickly**, cells shrink abruptly, which risks **osmotic demyelination syndrome** (central pontine myelinolysis).
- **Synaptic transmission:** glutamate crosses the 20 nm cleft in under 1 µs and reaches about 1 mM briefly. Diffusion away and uptake by transporters end the signal. "Spillover" to neighbouring synapses and **volume transmission** (e.g. dopamine, neuropeptides) also rely on diffusion. The brain's extracellular space is about 20 % of tissue volume, and its tortuous geometry slows diffusion.
- **Axonal transport** with motor proteins (kinesin, dynein) is needed because diffusion along axons would take years ([[Bio01 Cell Biology]]).
- **Diffusion MRI / DTI:** measures how water diffuses in tissue. In white matter, diffusion is faster along axons than across them (anisotropy), which allows tractography of fibre tracts.

## Math links #math-link
- Unit prefixes and scientific notation → [[A1 Exponent Rules]]
- $x = \sqrt{2Dt}$: square-root scaling → [[A2 Root Rules]]
- Fick's law as a derivative ($dc/dx$); the diffusion equation $\partial c/\partial t = D\,\partial^2c/\partial x^2$ → [[B6 Differentiation Rules]]
- Rearranging $c_1V_1 = c_2V_2$ and recipes → [[A8 Solving Equations]], [[A5 Fractions]]
- DTI: diffusion tensor = symmetric 3×3 matrix; its eigenvectors give the fibre direction → [[C4 Eigenvalues and Eigenvectors]]

## Connections
- Concentration gradients and potentials → [[Ch05 Redox and Electrochemistry]]
- Water and hydration → [[Ch03 Intermolecular Forces and Solubility]]
- Membrane transport, aquaporins → [[Bio02 Membranes and Transport]]
- Diffusion MRI → [[Meth04 In Vivo Imaging]]

## Key takeaways
- $n = m/M$, $c = n/V$, $c_1V_1 = c_2V_2$.
- Osmolarity counts particles (NaCl gives 2). Water flows towards higher osmolarity.
- Diffusion time ∝ distance²: excellent over µm, useless over cm.
