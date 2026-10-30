---
aliases: [Unit Circle, Unit Circle Trigonometry, Einheitskreis, Polar Coordinates]
tags: [geometry, trigonometry, unit-circle, type/overview, neuro]
---
# D4 Unit Circle Trigonometry

> [[D0 Geometry and Vectors MOC|↑ Geometry MOC]] · [[D4 Unit Circle Trigonometry - Worksheet|✏️ Worksheet]] · [[D4 Unit Circle Trigonometry - Solutions|✅ Solutions]] · [[Mistakes - Geometry and Vectors|⚠️ Mistake log]]

## Why this matters
The unit circle is where sine and cosine come from. It turns angles into points – which is exactly how **phases** of brain oscillations, **head directions** and **movement directions** are analysed with circular statistics. Learn the special values here once and you never need a calculator for them again.

## Definition
A point on the circle of radius 1 at angle $\theta$ (measured counter-clockwise from the positive $x$-axis) has coordinates
$$P(\theta) = (\cos\theta,\ \sin\theta)$$
- $\cos\theta$ = $x$-coordinate, $\sin\theta$ = $y$-coordinate, $\tan\theta = \frac{\sin\theta}{\cos\theta}$ = slope of the ray.
- Pythagoras on the circle: $\sin^2\theta + \cos^2\theta = 1$.
- **Radians:** $\theta$ = arc length on the unit circle. Full turn $= 2\pi$, $180° = \pi$.

In a right triangle (hypotenuse $c$): $\sin = \frac{\text{opposite}}{c}$, $\cos = \frac{\text{adjacent}}{c}$, $\tan = \frac{\text{opposite}}{\text{adjacent}}$ (SOH-CAH-TOA).

## Special values (learn by heart)
| $\theta$ | $0$ | $\frac\pi6$ (30°) | $\frac\pi4$ (45°) | $\frac\pi3$ (60°) | $\frac\pi2$ (90°) |
|---|---|---|---|---|---|
| $\sin\theta$ | $0$ | $\frac12$ | $\frac{\sqrt2}2$ | $\frac{\sqrt3}2$ | $1$ |
| $\cos\theta$ | $1$ | $\frac{\sqrt3}2$ | $\frac{\sqrt2}2$ | $\frac12$ | $0$ |
| $\tan\theta$ | $0$ | $\frac{\sqrt3}3$ | $1$ | $\sqrt3$ | – |

Memory trick: $\sin$ = $\frac{\sqrt0}2, \frac{\sqrt1}2, \frac{\sqrt2}2, \frac{\sqrt3}2, \frac{\sqrt4}2$; $\cos$ is the same list backwards.

## Other quadrants – signs and reference angles
| Quadrant | Angles | $\sin$ | $\cos$ | $\tan$ |
|---|---|---|---|---|
| I | $0$ – $90°$ | + | + | + |
| II | $90°$ – $180°$ | + | − | − |
| III | $180°$ – $270°$ | − | − | + |
| IV | $270°$ – $360°$ | − | + | − |

Use the **reference angle** (acute angle to the $x$-axis) and the sign of the quadrant. Example: $\cos 210° = -\cos30° = -\frac{\sqrt3}2$.
Symmetries: $\sin(-\theta) = -\sin\theta$, $\cos(-\theta) = \cos\theta$, $\sin(\pi - \theta) = \sin\theta$, $\cos(\pi - \theta) = -\cos\theta$.

## Polar coordinates
A 2D point/vector can be written as length $r$ and angle $\theta$:
$$x = r\cos\theta,\quad y = r\sin\theta \qquad\Longleftrightarrow\qquad r = \sqrt{x^2 + y^2},\quad \theta = \operatorname{atan2}(y, x)$$
⚠️ $\arctan\frac yx$ alone only gives angles in $(-90°, 90°)$ – check the quadrant!

**Law of cosines** (general triangle): $c^2 = a^2 + b^2 - 2ab\cos\gamma$ – Pythagoras plus a correction.

## In neuroscience #neuro
- **Phase as a point on the circle:** the phase $\varphi$ of an oscillation at the moment of a spike can be drawn as the unit vector $(\cos\varphi, \sin\varphi)$.
- **Circular mean and phase locking:** you can't average angles directly ($350°$ and $10°$ average to $0°$, not $180°$!). Instead, average the unit vectors:
  $$\bar{\mathbf z} = \frac1n\sum_k(\cos\varphi_k, \sin\varphi_k)$$
  The direction of $\bar{\mathbf z}$ is the mean phase; its length $R\in[0,1]$ is the **phase-locking value** / mean resultant length (1 = perfect locking, 0 = uniform). Basis of PLV, inter-trial phase coherence and spike–field coupling.
- **Head-direction and grid cells:** firing depends on the animal's heading angle; tuning curves are plotted in polar plots, and cosine tuning $\cos(\theta - \theta_\text{pref})$ ([[B4 Trigonometric Functions]]).
- **Rotations** of stimuli or coordinate systems use $R_\theta = \begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}$ ([[C1 Matrices]]).

## Connections
- Sine/cosine as functions of time → [[B4 Trigonometric Functions]]
- Angles via dot product → [[D2 Dot and Cross Product]]
- Polar form of complex numbers $re^{i\theta}$ → [[E2 Complex Numbers]]
- Vectors → [[D1 Vectors in 2D and 3D]]; rotation matrices → [[C1 Matrices]]

## Where this is used in the vault
**Most important applications:** Numerical aperture $n\sin\theta$ and Snell's law ([[Meth01 Microscopy]], [[Ph11 Optics and Fluorescence]]), Bragg's law ([[Meth02 Structural Biology]]), phases ([[Ph09 Waves and Oscillations]]).

**All notes that build on this topic:**
- *Physics:* [[Ph09 Waves and Oscillations]] · [[Ph11 Optics and Fluorescence]]
- *Methods:* [[Meth01 Microscopy]] · [[Meth02 Structural Biology]]
- *Programming:* [[Py11 PsychoPy Experiment Control]] · [[R06 ggplot2 Visualization]] · [[MAT08 Psychtoolbox]] · [[MAT09 EEGLAB]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- $(\cos\theta, \sin\theta)$ = point on the unit circle.
- Special values from the $\frac{\sqrt k}{2}$ pattern; signs from the quadrant.
- Average angles via unit vectors, not numbers.
