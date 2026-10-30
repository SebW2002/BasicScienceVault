---
aliases: [Sets, Logic, Quantifiers, Mengen, Logik, Quantoren]
tags: [foundations, set, logic, type/overview, neuro]
---
# E1 Sets, Logic and Quantifiers

> [[E0 Foundations MOC|↑ Foundations MOC]] · [[E1 Sets Logic and Quantifiers - Worksheet|✏️ Worksheet]] · [[E1 Sets Logic and Quantifiers - Solutions|✅ Solutions]] · [[Mistakes - Foundations|⚠️ Mistake log]]

## Why this matters
This is the **language** of mathematics. You need it to read definitions in textbooks and methods sections ("for all $\varepsilon > 0$ there exists…"), to reason about experiments correctly (necessary vs. sufficient, converse vs. contrapositive), and for probability (events are sets). Use it as a reference alongside all other topics.

## Sets
| Symbol | Meaning | Example |
|---|---|---|
| $x\in A$ | $x$ is an element of $A$ | $2\in\{1,2,3\}$ |
| $A\subseteq B$ | every element of $A$ is in $B$ | $\mathbb N\subseteq\mathbb Z$ |
| $A\cup B$ | union: in $A$ **or** $B$ | $\{1,2\}\cup\{2,3\} = \{1,2,3\}$ |
| $A\cap B$ | intersection: in $A$ **and** $B$ | $\{1,2\}\cap\{2,3\} = \{2\}$ |
| $A\setminus B$ | difference: in $A$ but not in $B$ | $\{1,2\}\setminus\{2,3\} = \{1\}$ |
| $A^c$ or $\bar A$ | complement (w.r.t. a universal set) | – |
| $\emptyset$ | empty set | $\emptyset\neq\{0\}$! |
| $A\times B$ | Cartesian product: all pairs $(a, b)$ | $\mathbb R\times\mathbb R = \mathbb R^2$ |
| $\lvert A\rvert$ | cardinality (number of elements) | $\lvert\{a,b,c\}\rvert = 3$ |
| $\mathcal P(A)$ | power set (all subsets), $\lvert\mathcal P(A)\rvert = 2^{\lvert A\rvert}$ | – |

**Set-builder notation:** $\{x\in\mathbb R\mid x^2 < 4\} = (-2, 2)$.

**Number sets:** $\mathbb N = \{1, 2, 3, \dots\}$ (some authors include 0) $\subset\mathbb Z$ (integers) $\subset\mathbb Q$ (fractions) $\subset\mathbb R$ (reals, includes $\sqrt2, \pi$) $\subset\mathbb C$ ([[E2 Complex Numbers]]).

**Intervals:** $[a, b]$ closed (endpoints included), $(a, b)$ open, $[a, b)$ half-open; $[a, \infty)$.

**De Morgan's laws:** $(A\cup B)^c = A^c\cap B^c$, $\;(A\cap B)^c = A^c\cup B^c$.
**Inclusion–exclusion:** $\lvert A\cup B\rvert = \lvert A\rvert + \lvert B\rvert - \lvert A\cap B\rvert$.

## Propositional logic
| Symbol | Name | True when … |
|---|---|---|
| $\neg p$ | not | $p$ is false |
| $p\wedge q$ | and | both true |
| $p\vee q$ | or (inclusive) | at least one true |
| $p\Rightarrow q$ | implies | **false only if** $p$ true and $q$ false |
| $p\Leftrightarrow q$ | equivalent | both have the same truth value |

Truth table of the implication:
| $p$ | $q$ | $p\Rightarrow q$ |
|---|---|---|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

**Important equivalences**
- **Contrapositive:** $(p\Rightarrow q)\iff(\neg q\Rightarrow\neg p)$ ✅ always equivalent.
- **Converse** $q\Rightarrow p$ is **not** equivalent to $p\Rightarrow q$.
- De Morgan: $\neg(p\wedge q)\iff\neg p\vee\neg q$, $\;\neg(p\vee q)\iff\neg p\wedge\neg q$.
- In $p\Rightarrow q$: $p$ is **sufficient** for $q$, $q$ is **necessary** for $p$.

## Quantifiers
- $\forall x\in A: P(x)$ – "for all $x$ in $A$, $P(x)$ holds"
- $\exists x\in A: P(x)$ – "there exists (at least one) $x$ with $P(x)$"; $\exists!$ = exactly one

**Negation swaps the quantifier:**
$$\neg\big(\forall x: P(x)\big)\iff\exists x: \neg P(x), \qquad \neg\big(\exists x: P(x)\big)\iff\forall x: \neg P(x)$$
**Order matters:** $\forall x\,\exists y: y > x$ (true in $\mathbb R$: for every number there's a bigger one) vs. $\exists y\,\forall x: y > x$ (false: no number is bigger than all numbers).

Example – continuity at $a$ ([[B5 Limits and Continuity]]):
$$\forall\varepsilon > 0\ \exists\delta > 0\ \forall x: \lvert x - a\rvert < \delta\Rightarrow\lvert f(x) - f(a)\rvert < \varepsilon$$

## In neuroscience #neuro
- **Neuron populations as sets:** $F$ = face-selective neurons, $H$ = house-selective. $F\cap H$ = mixed-selectivity neurons; inclusion–exclusion counts how many respond to at least one category.
- **Probability:** events are sets; $P(A\cup B) = P(A) + P(B) - P(A\cap B)$.
- **Necessary vs. sufficient in causal neuroscience:** a lesion/inactivation study tests **necessity** ("without region X, no behaviour Y" ⟹ X is necessary for Y); optogenetic activation tests **sufficiency** ("activating X evokes Y"). Mixing them up is a common reasoning error.
- **Contrapositive vs. converse:** "If the hippocampus is lesioned, then no new episodic memories form" implies "if new episodic memories form, the hippocampus is intact" – but **not** "if no memories form, the hippocampus is lesioned".
- **Statistics:** "not significant" ≠ "no effect" – absence of evidence is not evidence of absence (logical negation vs. failing to reject).

## Connections
- Number sets & intervals → used everywhere, e.g. domains in [[B1 Properties of Functions]]
- $\varepsilon$-$\delta$ definitions → [[B5 Limits and Continuity]]
- Solution sets of equations → [[A8 Solving Equations]], [[C3 Linear Systems and Gaussian Elimination]]
- $\mathbb C$ → [[E2 Complex Numbers]]

## Where this is used in the vault
**Most important applications:** Necessity vs. sufficiency in causal experiments ([[Meth05 Molecular Biology Tools]], [[Bio07 Neural Circuits and Systems]]), logic of hypothesis tests and multiple testing ([[CS02 Probability and Statistics]], [[CS06 Data Science Workflow]]).

**All notes that build on this topic:**
- *Biology:* [[Bio07 Neural Circuits and Systems]]
- *Methods:* [[Meth05 Molecular Biology Tools]] · [[Meth06 Omics and Sequencing]]
- *Computer Science:* [[CS02 Probability and Statistics]] · [[CS06 Data Science Workflow]] · [[CS13 Reproducibility and Research Software]]
- *Programming:* [[Prog00 Shared Programming Concepts]] · [[Py02 Python Data Structures]] · [[Py06 pandas and Tabular Data]] · [[Py12 Python Object-Oriented Programming]] · [[R01 R Basics and Syntax]] · [[R02 R Data Structures and Vectorization]] · [[R03 R Control Flow and Functions]] · [[R04 R Data Import and Tidy Data]] · [[R05 dplyr and tidyr]] · [[MAT02 MATLAB Matrices and Vectorization]] · [[Doc02 Math in Markdown]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- $\cup$ = or, $\cap$ = and; De Morgan flips them under negation.
- $p\Rightarrow q$ ⟺ $\neg q\Rightarrow\neg p$; the converse is a different statement.
- Negating swaps $\forall\leftrightarrow\exists$ and negates the inner statement.
