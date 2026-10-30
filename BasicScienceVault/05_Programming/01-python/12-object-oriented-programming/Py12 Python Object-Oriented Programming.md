---
aliases: [Python OOP, Classes and Objects, Inheritance, dataclass, Object-Oriented Programming]
tags: [programming, python, oop, type/overview, neuro]
---
# Py12 Python Object-Oriented Programming

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py12 Python Object-Oriented Programming - Worksheet|✏️ Worksheet]] · [[Py12 Python Object-Oriented Programming - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
You use objects constantly: `raw.filter(...)` in MNE, `df.groupby(...)` in pandas, `model.fit(...)` in scikit-learn, `nn.Module` in PyTorch. **Object-oriented programming (OOP)** bundles data (**attributes**) and the functions that act on them (**methods**) into one unit. Understanding it lets you read library code – and decide when your own code benefits from a class (and when a plain function is better).

## Classes, objects, attributes, methods
```python
class Neuron:
    """A leaky integrate-and-fire neuron."""
    def __init__(self, tau=0.02, v_rest=-0.070, v_th=-0.050, v_reset=-0.070):
        self.tau = tau            # attributes: the object's data
        self.v_rest = v_rest
        self.v_th = v_th
        self.v_reset = v_reset
        self.v = v_rest           # state
        self.spikes = []

    def step(self, I, dt, t):     # method: a function that gets the object as `self`
        self.v += dt / self.tau * (-(self.v - self.v_rest) + I)
        if self.v >= self.v_th:
            self.spikes.append(t)
            self.v = self.v_reset

n1 = Neuron()                 # an object (instance) of the class
n2 = Neuron(tau=0.01)         # another instance with its own data
n1.step(I=0.025, dt=1e-4, t=0.0)
n1.v, n2.v                    # each object keeps its own state
```
- **Class** = blueprint; **object/instance** = one concrete thing built from it.
- `__init__` runs when an object is created and sets up its attributes.
- `self` is the object the method is called on: `n1.step(...)` is `Neuron.step(n1, ...)`.
- Methods that change the object in place often return `None` (like `list.append`); others return a new object (pandas). MNE methods modify in place **and** return the object, which allows chaining: `raw.filter(1, 40).resample(250)`.

### Special methods and properties
```python
class SpikeTrain:
    def __init__(self, times, t_stop):
        self.times = np.asarray(times); self.t_stop = t_stop
    def __len__(self):                 # len(st)
        return len(self.times)
    def __repr__(self):                # how it prints
        return f"SpikeTrain(n={len(self)}, t_stop={self.t_stop} s)"
    @property
    def rate(self):                    # accessed like an attribute: st.rate
        return len(self) / self.t_stop
```

### dataclasses: classes for records
```python
from dataclasses import dataclass, field
@dataclass
class Trial:
    condition: str
    image: str
    rt: float | None = None
    correct: bool | None = None
t = Trial("face", "face01.png")
```
`@dataclass` writes `__init__`, `__repr__` and `__eq__` for you – ideal for parameter sets and trial records.

## Inheritance (conceptual)
A **subclass** inherits attributes and methods of a **base class** and can add or override them:
```python
class AdaptiveNeuron(Neuron):            # an AdaptiveNeuron *is a* Neuron
    def __init__(self, a=0.002, tau_w=0.1, **kwargs):
        super().__init__(**kwargs)       # set up the Neuron part
        self.w, self.a, self.tau_w = 0.0, a, tau_w
    def step(self, I, dt, t):            # override: adaptation current
        self.w -= dt / self.tau_w * self.w
        n_before = len(self.spikes)
        super().step(I - self.w, dt, t)
        if len(self.spikes) > n_before:
            self.w += self.a
```
- **"is-a"** relation: every `AdaptiveNeuron` can be used wherever a `Neuron` is expected (**polymorphism**): a simulation loop calling `n.step(...)` works for both.
- Libraries rely on this: every scikit-learn estimator inherits from `BaseEstimator`; every PyTorch model from `nn.Module` ([[Py09 Python Machine Learning Libraries]]).
- Keep hierarchies **shallow**. Often **composition** ("has-a": an `Experiment` *has* a `Window` and a list of `Trial`s) is simpler than inheritance.

## When OOP makes sense – and when not
| Use a class when … | Use functions when … |
|---|---|
| data and behaviour belong together and the object has **state** that changes (a neuron's voltage, an experiment's current trial) | you transform input → output (filter a signal, compute a statistic) |
| you create **many similar things** (1000 neurons, 300 trials) | the code is a linear pipeline |
| you need a common **interface** (all models have `fit`/`predict`, all stimuli `draw`) | a class would have only `__init__` and one method |
| a library expects it (`nn.Module`, sklearn estimator) | |
Analysis scripts are usually best as **functions** + data structures; simulations, experiments and reusable tools often benefit from classes.

## Same idea in R and MATLAB
R has several systems: S3 (`print.myclass`, used by `lm` objects), S4 and R6 (reference classes). MATLAB uses `classdef` files with properties and methods; `handle` classes behave like Python objects (reference), value classes are copied ([[MAT03 MATLAB Control Flow and Functions]]).

## In neuroscience #neuro
- **Model objects:** a `Neuron` or `Network` class with parameters, state and a `step` method makes simulations readable and extensible ([[CS10 Dynamical and Computational Neuro Models]]).
- **Experiment objects:** a `Trial` dataclass and an `Experiment` class that holds the window, the trial list and the data file give a clean PsychoPy script ([[Py11 PsychoPy Experiment Control]]).
- **Library objects:** MNE's `Raw`/`Epochs`/`Evoked`, Nilearn's maskers (sklearn-style `fit/transform`), SpikeInterface's `Recording`/`Sorting` – all are classes; their methods are documented on the class page.
- **Custom sklearn transformers** (e.g. a band-power feature extractor) only need `fit` and `transform` to plug into a Pipeline.

## Math links #math-link
- A neuron object's `step` implements the Euler update of an ODE → [[B10 Differential Equations]]
- "is-a" relations as subsets (every AdaptiveNeuron ∈ Neurons) → [[E1 Sets Logic and Quantifiers]]

## Connections
- Functions and scope → [[Py03 Python Control Flow and Functions]]
- Mutable state, aliasing → [[Py02 Python Data Structures]]
- Classes in libraries → [[Py09 Python Machine Learning Libraries]], [[Py10 Python Neuroscience Packages]]
- Testing classes → [[Py13 Python Reproducible Projects and Testing]]

## Key takeaways
- Class = blueprint; object = instance with its own attributes; methods get `self`.
- `__init__` sets up state; `@property` for computed attributes; `@dataclass` for records.
- Inheritance = "is-a", override methods, call `super()`; prefer shallow hierarchies and composition.
- Use classes for stateful things (models, experiments), functions for transformations.
