---
aliases: [Mechanics and Energy, Force Work Energy Power, Mechanik und Energie]
tags: [physics, mechanics, energy, type/overview, neuro]
---
# Ph01 Mechanics and Energy

> [[MOC-physics|↑ Physics MOC]] · [[Ph01 Mechanics and Energy - Worksheet|✏️ Worksheet]] · [[Ph01 Mechanics and Energy - Solutions|✅ Solutions]] · [[Mistakes - Physics|⚠️ Mistake log]]

## Why this matters
Energy is the common currency of physics, chemistry and biology. The brain uses about 20 W. Motor proteins do mechanical work with ATP. Ion pumps convert chemical energy into electrical energy. Thermal motion constantly shakes every molecule. To reason about any of this you need force, work, energy, power, and the law that energy is conserved.

## Force
**Newton's second law:**
$$F = m\cdot a\qquad[\text{N} = \text{kg·m/s}^2]$$
- Weight: $F_G = m\cdot g$ with $g\approx9.81\,\text{m/s}^2$.
- Forces are **vectors**: they have magnitude and direction, and they add as vectors ([[D1 Vectors in 2D and 3D]]).
- **Newton's third law:** every force has an equal and opposite counterforce.
- **Hooke's law** (spring): $F = -k\,x$. Elastic structures in cells, such as the tip links of hair cells or the "gating springs" of mechanosensitive channels, are modelled as springs.

## Work, energy and power
| Quantity | Formula | Unit |
|---|---|---|
| **Work** | $W = F\cdot s\cdot\cos\alpha = \vec F\cdot\vec s$ (force along the path × distance) | J = N·m |
| **Kinetic energy** | $E_\text{kin} = \tfrac12mv^2$ | J |
| **Potential energy (gravity)** | $E_\text{pot} = mgh$ | J |
| **Potential energy (spring)** | $E = \tfrac12kx^2$ | J |
| **Electrical potential energy** | $E = qV$ → [[Ph03 Electric Fields and Potential]] | J |
| **Power** | $P = \frac{W}{t} = \frac{\Delta E}{t}$; also $P = F\cdot v$ and $P = V\cdot I$ (electrical) | W = J/s |

- **Potential energy** is stored in a position or configuration: a raised object, a stretched spring, separated charges, an ion gradient, a chemical bond.
- **Kinetic energy** is energy of motion.
- Work done *against* a force is stored as potential energy. When the force acts *along* the motion, potential energy turns into kinetic energy (or heat).

**Useful energy units:** 1 kWh = 3.6 MJ; 1 kcal ≈ 4.19 kJ; 1 eV = $1.602\times10^{-19}$ J ([[Ph12 Quantum Basics for Biophysics]]); per mole: multiply by $N_A = 6.022\times10^{23}$.

## Conservation of energy
**Energy can't be created or destroyed, only converted.** In a closed system:
$$E_\text{kin} + E_\text{pot} + \dots = \text{const.}$$
- A falling ball turns $mgh$ into $\tfrac12mv^2$. With friction, part of it becomes **heat** (disordered thermal motion).
- In thermodynamics this is the **first law**: $\Delta U = Q + W$, i.e. the change in internal energy equals heat added plus work done on the system ([[Ph08 Thermodynamics and Statistics]]).
- **Biological energy chains:**
  - Glucose (chemical) → ATP (chemical) → ion gradients (electrochemical potential energy) → currents and action potentials (electrical) → heat.
  - ATP → motor proteins (mechanical work) → heat.
  - Every step loses some energy as heat, so efficiencies are below 100 %.

## Forces at the molecular scale
At the scale of molecules, gravity and inertia are irrelevant. Three forces dominate:
| Force | Scale | Notes |
|---|---|---|
| **Electrostatic** (Coulomb) | strong; long-range ($\propto1/r^2$); screened in water | ions, salt bridges, voltage sensors → [[Ph02 Electricity and Charge]], [[Ch02 Chemical Bonds]] |
| **Van der Waals** | weak; very short-range ($\propto1/r^7$ force, $1/r^6$ energy) | close packing of lipid tails, protein cores |
| **Thermal motion** (random collisions) | energy $\sim kT\approx4.3\times10^{-21}\,\text{J}$ at 37 °C | Brownian motion, diffusion, spontaneous channel opening → [[Ph08 Thermodynamics and Statistics]] |

**Molecular units:** forces in **piconewtons** (1 pN = 10⁻¹² N), distances in **nanometres**. A handy energy unit is **pN·nm** = 10⁻²¹ J, so $kT\approx4.3$ pN·nm.
- A kinesin motor takes **8 nm steps** against loads up to about **6–7 pN**, so one step does at most ~50 pN·nm of work. One ATP provides about 80–100 pN·nm (≈ 50 kJ/mol in the cell), giving an efficiency of roughly 50 %.
- **Low Reynolds number:** for objects the size of cells and molecules, viscosity dominates and inertia is negligible. A bacterium that stops swimming coasts for less than a nanometre. Motion stops the instant force stops.

## In neuroscience #neuro
- **The brain's power budget:** about **20 W**, roughly 20 % of the body's resting energy use, although the brain is only about 2 % of body mass. Most of it goes to restoring ion gradients after signalling (Na⁺/K⁺-ATPase, [[Bio02 Membranes and Transport]]).
- **Mechanotransduction:**
  - In hair cells of the inner ear, deflection of the hair bundle stretches tip links (springs) and opens channels. Displacements of about 1 nm are detectable.
  - Touch and proprioception use Piezo2 channels.
- **Axonal transport:** kinesin and dynein convert ATP into mechanical work along microtubules ([[Bio01 Cell Biology]]).
- **Traumatic brain injury:** rapid acceleration and deceleration ($F = ma$) produces shear forces that stretch and tear axons (diffuse axonal injury).
- **Optical tweezers and AFM** measure pN forces on single molecules, e.g. motor proteins or the unfolding of proteins.

## Math links #math-link
- Work as a dot product $\vec F\cdot\vec s$ → [[D2 Dot and Cross Product]]
- Power laws ($1/r^2$, $1/r^6$) and units → [[A1 Exponent Rules]]
- Work as an integral of force over distance, $W = \int F\,dx$ (spring: $\int kx\,dx = \tfrac12kx^2$) → [[B7 Antiderivatives and Integration]]
- Force as the negative slope of potential energy, $F = -\frac{dE_\text{pot}}{dx}$ → [[B6 Differentiation Rules]]

## Connections
- Electrical energy and potential → [[Ph03 Electric Fields and Potential]]
- Thermal energy, first law → [[Ph08 Thermodynamics and Statistics]]
- Bonds and molecular forces → [[Ch02 Chemical Bonds]]
- ATP and metabolism → [[Ch05 Redox and Electrochemistry]], [[Ch08 Biomolecules]]

## Key takeaways
- $F = ma$; $W = F\cdot s$; $E_\text{kin} = \tfrac12mv^2$; $E_\text{pot} = mgh$; $P = W/t$.
- Energy is conserved and only converted. Every biological conversion loses some as heat.
- At the molecular scale, electrostatics, van der Waals forces and thermal motion ($kT\approx4.3$ pN·nm) dominate. Inertia is irrelevant.
