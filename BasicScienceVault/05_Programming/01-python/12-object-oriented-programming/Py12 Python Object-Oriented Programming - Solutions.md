---
tags: [programming, python, oop, type/solution]
---
# Py12 Python Object-Oriented Programming – Solutions

> Worksheet: [[Py12 Python Object-Oriented Programming - Worksheet]] · Theory: [[Py12 Python Object-Oriented Programming]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. **Class:** blueprint describing data and behaviour. **Object:** one instance created from a class. **Attribute:** data stored in an object (`n.tau`). **Method:** function defined in a class that acts on an object. **`self`:** the instance a method is called on. **`__init__`:** method that runs on creation and initialises attributes.
2. `epochs` is an object (instance of `mne.Epochs`), `average` is a method; it returns a new `Evoked` object.
3. "is-a": subclass relation – an `AdaptiveNeuron` is a `Neuron`; "has-a": composition – an `Experiment` has a `Window`, a `Network` has a list of `Neuron`s.

## Level 2
4. `2 2 1` – `a` and `b` are the same object; `c` is separate.
5. `[Stim(0.1), Stim(0.5)]`
6. `self` is missing: `def __init__(self, tau): self.tau = tau`. (Also needs a newline/indentation for the body.)

## Level 3
7. ```python
   from dataclasses import dataclass
   @dataclass
   class Electrode:
       name: str
       x: float
       y: float
       bad: bool = False
   ```
8. ```python
       @property
       def isi(self):
           return np.diff(self.times)
       @property
       def cv(self):
           return self.isi.std(ddof=1) / self.isi.mean()
   ```
9. ```python
   class PoissonNeuron(Neuron):
       def __init__(self, rate, seed=0, **kwargs):
           super().__init__(**kwargs)
           self.rate = rate
           self.rng = np.random.default_rng(seed)
       def step(self, I, dt, t):
           if self.rng.random() < self.rate * dt:
               self.spikes.append(t)
   ```

## Level 4
10. a) function (input → output) b) class (many stateful units with a common `step`) – or vectorised arrays for speed c) plain script/function d) class(es): `Experiment` with `Trial` records.
11. They all provide a `step(I, dt, t)` method with the same signature; the loop only relies on that interface. This is **polymorphism** (duck typing in Python).
12. ```python
    import numpy as np
    dt, T, I = 1e-4, 1.0, 0.025
    n, a = Neuron(), AdaptiveNeuron()
    for k in range(int(T / dt)):
        n.step(I, dt, k * dt); a.step(I, dt, k * dt)
    print(len(n.spikes), len(a.spikes))
    print(np.diff(n.spikes)[:3], np.diff(a.spikes)[[0, 1, -1]])
    ```
    The plain LIF fires regularly: 31 spikes, constant ISI ≈ 32 ms (analytically $\tau\ln\frac{I}{I - (v_{th} - v_{rest})} = 20\text{ ms}\cdot\ln\frac{25}{5}\approx32.2$ ms, [[B10 Differential Equations]]). The adaptive neuron fires only 20 spikes, and its ISIs **lengthen** from ≈ 38 ms to ≈ 52 ms until they settle (**spike-frequency adaptation**): each spike increases `w`, which is subtracted from the input.
