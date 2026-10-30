---
tags: [programming, python, oop, type/worksheet]
---
# Py12 Python Object-Oriented Programming – Worksheet

> Theory: [[Py12 Python Object-Oriented Programming]] · Solutions: [[Py12 Python Object-Oriented Programming - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper. Run code only for tasks marked 💻.

## Level 1 – Vocabulary
1. Explain class, object, attribute, method, `self`, `__init__` in one sentence each.
2. In `epochs.average()`, what is `epochs`, what is `average`, and what (probably) is returned?
3. What is the difference between an "is-a" and a "has-a" relation? Give one neuroscience example of each.

## Level 2 – Predict the output
4. ```python
   class Counter:
       def __init__(self): self.n = 0
       def add(self): self.n += 1
   a = Counter(); b = a; c = Counter()
   a.add(); b.add(); c.add()
   print(a.n, b.n, c.n)
   ```
5. ```python
   class Stim:
       def __init__(self, contrast=1.0): self.contrast = contrast
       def __repr__(self): return f"Stim({self.contrast})"
   print([Stim(c) for c in (0.1, 0.5)])
   ```
6. Find the bug: `class Neuron: def __init__(tau): self.tau = tau`

## Level 3 – Write code
7. Write a `@dataclass` `Electrode` with `name: str`, `x: float`, `y: float`, `bad: bool = False`.
8. Add a `@property` `isi` to the `SpikeTrain` class from the note that returns the inter-spike intervals (`np.diff`), and a `cv` property (SD/mean of ISIs).
9. Write a subclass `PoissonNeuron(Neuron)` whose `step` ignores the voltage and spikes with probability `rate * dt` (use a `rng` attribute).

## Level 4 – Design decisions
10. For each, class or function? a) compute alpha power of a signal b) a network of 100 LIF neurons simulated step by step c) a 10-line script that plots one ERP d) an experiment with blocks, trials, a window and a data file.
11. Why can a simulation loop `for n in neurons: n.step(I, dt, t)` mix `Neuron`, `AdaptiveNeuron` and `PoissonNeuron` objects? What is this property called?
12. 💻 Implement `Neuron` and `AdaptiveNeuron` from the note, drive both with a constant input `I = 0.025` (V) for 1 s (dt = 0.1 ms), and compare spike counts and ISIs. What does adaptation do?
