---
aliases: [Diffusion and Transport, Fick's Laws, Stokes-Einstein, Electrodiffusion, Nernst-Planck, Osmotic Pressure, Diffusion und Transport]
tags: [physics, diffusion, electrodiffusion, osmosis, type/overview, neuro]
---
# Ph07 Diffusion and Transport

> [[MOC-physics|↑ Physics MOC]] · [[Ph07 Diffusion and Transport - Worksheet|✏️ Worksheet]] · [[Ph07 Diffusion and Transport - Solutions|✅ Solutions]] · [[Mistakes - Physics|⚠️ Mistake log]]

## Why this matters
Diffusion moves transmitter across the synaptic cleft, distributes Ca²⁺ inside a spine, lets O₂ reach neurons and spreads drugs through tissue. Combined with electric fields, it becomes **electrodiffusion**, the physics behind ion currents, the Nernst equation and the GHK equation. This note looks at diffusion from the physics side; the chemistry side is in [[Ch06 Solutions and Concentration]].

## Diffusion as a random walk
Each molecule moves randomly through collisions with water molecules (Brownian motion, driven by thermal energy $kT$). No molecule "knows" the gradient. Net transport from high to low concentration arises purely statistically, because more molecules are on the high side to start with ([[Ph08 Thermodynamics and Statistics]]: entropy).
- Mean squared displacement grows **linearly** with time: $\langle x^2\rangle = 2Dt$ (1D), $4Dt$ (2D), $6Dt$ (3D).
- So the typical distance is $x_\text{rms} = \sqrt{2Dt}$ and the time to diffuse a distance $x$ is $t\approx\frac{x^2}{2D}$ (quadratic in distance).

## Fick's laws
**First law (flux):** the flux is proportional to the concentration gradient.
$$J = -D\frac{\partial c}{\partial x}\qquad[J] = \frac{\text{mol}}{\text{m}^2\text{s}}$$
The minus sign means flux flows "downhill".

**Second law (time evolution, diffusion equation):** combining the first law with mass conservation gives
$$\frac{\partial c}{\partial t} = D\frac{\partial^2c}{\partial x^2}$$
Concentration rises where the profile is curved upward (a local minimum) and falls at a local maximum, so peaks flatten.
- **Solution for a point release** (e.g. a vesicle releasing transmitter): a Gaussian that spreads with time,
  $$c(x,t) = \frac{N}{\sqrt{4\pi Dt}}\,e^{-x^2/(4Dt)}$$
  Its width is $\sigma = \sqrt{2Dt}$, and its peak falls as $1/\sqrt t$ (in 1D; in 3D as $t^{-3/2}$).

## The diffusion coefficient
**Stokes–Einstein relation** for a sphere of radius $r$ in a fluid of viscosity $\eta$:
$$D = \frac{kT}{6\pi\eta r}$$
- $D\propto T$: warmer means faster (more thermal energy).
- $D\propto1/\eta$: a more viscous medium means slower.
- $D\propto1/r$: larger molecules are slower, but only **linearly** in radius (and mass ∝ $r^3$, so $D\propto M^{-1/3}$).

| Substance / medium | $D$ (approx.) |
|---|---|
| O₂, small ions in water | 1–2 µm²/ms (= 1–2 × 10⁻⁹ m²/s) |
| Glucose, glutamate in water | ~0.7 µm²/ms |
| Small protein (~3 nm radius) in water | ~0.1 µm²/ms |
| In cytoplasm | 3–10× slower (crowding, viscosity) |
| Brain extracellular space | slowed by tortuosity $\lambda_t\approx1.6$: $D^* = D/\lambda_t^2\approx D/2.5$ |
| Membrane proteins (in the bilayer) | ~0.01–0.1 µm²/s (much slower; 2D) |
| Ca²⁺ in cytosol (buffered) | effective $D$ greatly reduced by binding to buffers |

## Electrodiffusion (Nernst–Planck equation)
For **charged** particles, both a concentration gradient and an electric field drive flux:
$$J = -D\left(\frac{\partial c}{\partial x} + \frac{zF}{RT}\,c\,\frac{\partial V}{\partial x}\right)$$
- First term: diffusion (Fick). Second term: drift in the field.
- **Einstein relation:** mobility and diffusion are linked by $D = \mu kT$. The same random collisions that cause diffusion also cause friction for drift.
- **Zero net flux** ($J = 0$) gives exactly the **Nernst equation** ([[Ph03 Electric Fields and Potential]], [[Ch05 Redox and Electrochemistry]]):
  $$\frac{dc}{c} = -\frac{zF}{RT}dV\quad\Rightarrow\quad\Delta V = \frac{RT}{zF}\ln\frac{c_\text{out}}{c_\text{in}}$$
- Assuming a **constant field** across the membrane and solving for the flux of each ion gives the **GHK current equation**. Setting the sum of all ionic currents to zero gives the **GHK voltage equation**.

## Osmosis and osmotic pressure
- **Osmosis** is the net diffusion of **water** across a membrane that is permeable to water but not to the solute. Water moves towards the side with the higher solute concentration (lower water "concentration"/chemical potential).
- **Osmotic pressure (van 't Hoff):** the pressure needed to stop this flow,
  $$\pi = i\,c\,RT$$
  ($c$ in mol/m³, $i$ = particles per formula unit). Physically, it is analogous to the ideal gas law $pV = nRT$: solute particles "push" like gas molecules.
- A 1 mOsm/L difference corresponds to about 19 mmHg, so small osmotic differences are powerful ([[Ch06 Solutions and Concentration]]).
- **Starling forces** at capillaries balance hydrostatic pressure (out) against oncotic pressure from plasma proteins (in).

## In neuroscience #neuro
- **Synaptic cleft:** glutamate diffuses 20 nm in under a microsecond; the concentration peaks at ~1 mM and falls within ~1 ms. Fast diffusion plus transporters keeps signals local, though some "spillover" to neighbouring synapses occurs.
- **Ca²⁺ nanodomains:** buffered Ca²⁺ diffuses only ~10–100 nm before binding, so Ca²⁺ channels must sit very close to the release machinery for fast coupling. The slow buffer EGTA vs. the fast buffer BAPTA is used experimentally to estimate this coupling distance.
- **Spine neck:** the thin neck limits diffusion between spine and dendrite, compartmentalising biochemical signals (e.g. CaMKII activation during LTP).
- **Drug delivery:** convection-enhanced delivery is used in the brain because diffusion of large molecules over cm takes far too long.
- **Diffusion MRI:** measures the effective $D$ (apparent diffusion coefficient, ADC) of water. It **drops within minutes** in acute ischaemic stroke (cells swell, extracellular space shrinks), which makes it the most sensitive early MRI marker of stroke. DTI uses anisotropy in white matter.

## Math links #math-link
- Partial derivatives, gradients, Jacobians, multiple integrals → [[B11 Multivariable Calculus]]
- Differential equations (steady state, time constant, stability, Euler steps) → [[B10 Differential Equations]]
- $x = \sqrt{2Dt}$: square-root law → [[A2 Root Rules]]
- Fick's first law as a derivative, the diffusion equation as a partial differential equation (second derivative = curvature) → [[B6 Differentiation Rules]], [[B8 Curve Sketching]]
- Gaussian solution, exponential of a square → [[B2 Exponential Functions]]
- Nernst from Nernst–Planck: separate variables and integrate ($\int dc/c = \ln c$) → [[B7 Antiderivatives and Integration]], [[A3 Logarithms]]
- Diffusion tensor: eigenvalues and eigenvectors → [[C4 Eigenvalues and Eigenvectors]]
- Random walk: sums of independent steps; variance adds → [[A7 Sums Products and Factorials]]

## Connections
- Chemistry view (molarity, osmolarity, BBB) → [[Ch06 Solutions and Concentration]]
- Thermal energy and entropy → [[Ph08 Thermodynamics and Statistics]]
- Electric potential → [[Ph03 Electric Fields and Potential]]
- Nernst and GHK → [[Ch05 Redox and Electrochemistry]]
- Transport proteins → [[Bio02 Membranes and Transport]]
- Diffusion MRI → [[Meth04 In Vivo Imaging]]

## Key takeaways
- Diffusion = random thermal motion. $\langle x^2\rangle = 2Dt$, so time ∝ distance².
- Fick 1: $J = -D\,\partial c/\partial x$. Fick 2: $\partial c/\partial t = D\,\partial^2c/\partial x^2$ (peaks flatten into Gaussians).
- Stokes–Einstein: $D = kT/(6\pi\eta r)$.
- Nernst–Planck = diffusion + drift. Zero flux gives Nernst; a constant field gives GHK.
- Osmotic pressure $\pi = icRT$, like an ideal gas of solute particles.
