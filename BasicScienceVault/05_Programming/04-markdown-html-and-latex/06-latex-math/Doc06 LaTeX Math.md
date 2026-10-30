---
aliases: [LaTeX Math, equation environment, align environment, amsmath, eqref, mathtools]
tags: [programming, latex, math-typesetting, type/overview, neuro]
---
# Doc06 LaTeX Math

> [[Doc00 Markdown HTML and LaTeX Overview|↑ Markdown, HTML & LaTeX]] · [[MOC-programming|Programming MOC]] · [[Doc06 LaTeX Math - Worksheet|✏️ Worksheet]] · [[Doc06 LaTeX Math - Solutions|✅ Solutions]] · [[Mistakes - Markdown HTML LaTeX|⚠️ Mistake log]]

## Why this matters
LaTeX's math mode is *the* notation language of science: the same commands you use in Obsidian ([[Doc02 Math in Markdown]]) produce publication-quality equations in a LaTeX document – plus **numbering**, **cross-references** and multi-line **alignment**. This note covers what a full LaTeX document adds.

## Inline and displayed formulas
```latex
The membrane time constant is $\tau = R_m C_m$.              % inline (also \( ... \))
\[ V(t) = V_\infty + (V_0 - V_\infty)\, e^{-t/\tau} \]        % displayed, unnumbered
\begin{equation}                                             % displayed, numbered (1)
  I_\text{ion} = g_\text{Na} m^3 h (V - E_\text{Na}) + g_\text{K} n^4 (V - E_\text{K}) + g_L (V - E_L)
  \label{eq:hh}
\end{equation}
\begin{equation*} ... \end{equation*}                       % displayed, unnumbered (amsmath)
```
- Prefer `\[ … \]` over `$$ … $$` in LaTeX documents (`$$` is plain-TeX syntax and spacing can be wrong); in Markdown `$$` is the norm.
- Punctuation after a displayed equation belongs inside it: `… \, ,` or `.` at the end.

### Multi-line equations: align and friends (amsmath)
```latex
\begin{align}
  C_m \frac{dV}{dt} &= -g_L (V - E_L) + I(t) \label{eq:lif} \\
  \tau_m            &= \frac{C_m}{g_L} \nonumber                % no number for this line
\end{align}

\begin{align*}                                               % no numbers at all
  \mathcal{L}(\lambda) &= \prod_{i=1}^{n} \frac{\lambda^{k_i} e^{-\lambda}}{k_i!} \\
  \log \mathcal{L}     &= \sum_{i=1}^{n} \bigl( k_i \log\lambda - \lambda - \log k_i! \bigr)
\end{align*}

\begin{equation}                                             % one number for several lines
  \begin{split}
    y &= X\beta + \varepsilon \\
      &\approx X\hat\beta
  \end{split}
\end{equation}
```
- `&` marks the alignment point (usually before `=`), `\\` ends a line. Don't use the old `eqnarray`.
- `gather` (centred lines, no alignment), `multline` (one long equation broken over lines), `cases` for piecewise definitions.

## Fractions, roots, sums, integrals, matrices
| Construct | LaTeX | Notes |
|---|---|---|
| fraction | `\frac{a}{b}`, `\dfrac`, `\tfrac` | display/text size variants |
| binomial | `\binom{n}{k}` | amsmath |
| root | `\sqrt{x}`, `\sqrt[n]{x}` | – |
| sum, product | `\sum_{i=1}^{n}`, `\prod_{i}` | limits below/above in display |
| integral | `\int_{0}^{\infty} f(t)\,\mathrm{d}t`, `\iint`, `\oint` | `\,` thin space before d$t$ |
| limit | `\lim_{t\to\infty}` | – |
| derivatives | `\frac{\partial f}{\partial x}`, `\nabla`, `\dot{x}`, `\ddot{x}` | – |
| delimiters | `\left( … \right)`, `\bigl( … \bigr)`, `\lvert x\rvert`, `\lVert x\rVert` | sizes |
| matrices | `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` | `bmatrix` [ ], `vmatrix` \| \|, `Bmatrix` { } |
| dots | `\cdots` (centred), `\ldots`, `\vdots`, `\ddots` | – |
```latex
\[
  \mathbf{y} = W\mathbf{x} + \mathbf{b}, \quad
  W = \begin{bmatrix} w_{11} & \cdots & w_{1n} \\ \vdots & \ddots & \vdots \\ w_{m1} & \cdots & w_{mn} \end{bmatrix}
\]
```

## Greek letters, operators, vectors
- **Greek:** `\alpha \beta \gamma \delta \epsilon \varepsilon \theta \lambda \mu \pi \rho \sigma \tau \phi \varphi \omega`; capitals `\Gamma \Delta \Theta \Lambda \Sigma \Phi \Omega` (no `\Alpha`: use A).
- **Operators:** `\sin \cos \exp \log \ln \max \min \arg \det` are typeset upright with correct spacing. Define your own: `\DeclareMathOperator{\Var}{Var}` (preamble) → `\Var(X)`. Common: `\argmax` via `\DeclareMathOperator*{\argmax}{arg\,max}` (the `*` puts limits underneath).
- **Relations and symbols:** `\le \ge \neq \approx \sim \propto \equiv \in \subset \cup \cap \forall \exists \to \mapsto \Rightarrow \infty \pm \times \cdot`.
- **Vectors and fonts:** `\vec{v}` (arrow), `\mathbf{x}` (bold upright – common for vectors/matrices), `\boldsymbol{\mu}` (bold Greek, amsmath/`bm`), `\mathbb{R}`, `\mathbb{E}` (amssymb), `\mathcal{L}`, `\mathrm{d}`, `\hat{\beta}`, `\bar{x}`, `\tilde{x}`.
- **Text inside math:** `\text{if } V \ge V_\text{th}` (amsmath).
- **Units** with `siunitx`: `\qty{20}{\milli\second}`, `\unit{\micro\volt}` (upright, correctly spaced) – never `20 ms` in math mode (would be italic "m·s").

## Numbering and references: \label, \eqref
```latex
\begin{equation}
  E_\text{K} = \frac{RT}{zF} \ln \frac{[\mathrm{K}^+]_o}{[\mathrm{K}^+]_i}
  \label{eq:nernst}
\end{equation}
Inserting the concentrations into \eqref{eq:nernst} gives $E_\text{K} \approx \qty{-90}{\milli\volt}$.
```
- `\label{key}` **after** (or inside) the numbered thing; `\eqref{key}` prints "(1)" with parentheses, `\ref{key}` prints "1".
- Use prefixes in keys (`eq:`, `fig:`, `tab:`, `sec:`) to keep them organised; with `cleveref`, `\cref{eq:nernst}` prints "eq. (1)" automatically ([[Doc08 LaTeX Figures Tables and References]]).
- Numbering by section: `\numberwithin{equation}{section}` → (2.3).
- Two compile passes are needed for references to appear ([[Doc05 LaTeX Basics]]).

## The packages amsmath, amssymb, mathtools
| Package | Provides |
|---|---|
| **amsmath** | `align`, `gather`, `multline`, `split`, `cases`, `equation*`, `\text`, `\eqref`, `\dfrac`, `\binom`, matrix environments, `\DeclareMathOperator`, `\boldsymbol` |
| **amssymb** | extra symbols and fonts: `\mathbb`, `\varnothing`, `\lesssim`, `\therefore`, … |
| **mathtools** | loads and extends amsmath: `\coloneqq` (:=), `\DeclarePairedDelimiter` (auto-sized `\abs{}`, `\norm{}`), `dcases`, `\mathclap`, `\shortintertext`, fixes |
```latex
\usepackage{amsmath, amssymb, mathtools}
\DeclarePairedDelimiter{\abs}{\lvert}{\rvert}
\DeclarePairedDelimiter{\norm}{\lVert}{\rVert}
% \abs{x}, \abs*{\frac{a}{b}} (auto-sized), \norm{\mathbf{w}}_2
```
Also useful: `bm` (bold math), `siunitx` (units), `physics` (derivative and bra-ket shortcuts; use with care).

## Same idea in Markdown
Everything inside `$…$` and math environments is the same in Obsidian/Quarto ([[Doc02 Math in Markdown]]); only packages, `\label/\eqref` and preamble macros need a real LaTeX document (or Quarto's own cross-reference syntax).

## In neuroscience #neuro
- **Model equations** in theses and papers: Hodgkin–Huxley (referenced with `\eqref{eq:hh}`), cable equation, GLM, drift–diffusion models.
- **Methods sections** with consistent notation: define macros once (`\newcommand{\Vm}{V_\mathrm{m}}`) so changing notation is one edit.
- **Statistical models** written in `align*` (likelihood, priors, posteriors – [[CS09 Probabilistic and Bayesian Models]]).
- **Units** typeset with `siunitx` (`\qty{-70}{\milli\volt}`, `\qty{30}{\kilo\hertz}`).

## Math links #math-link
- What you'll typeset: [[B10 Differential Equations]] (membrane equation), [[C1 Matrices]], [[B12 Fourier Analysis]], [[A3 Logarithms]] (Nernst), [[CS02 Probability and Statistics]] (likelihoods)

## Connections
- Math in Markdown → [[Doc02 Math in Markdown]]
- Document basics → [[Doc05 LaTeX Basics]]; references and cross-refs → [[Doc08 LaTeX Figures Tables and References]]
- Equations in reports → [[R10 R Markdown and Quarto]], [[MAT11 MATLAB Live Scripts and Reports]]

## Key takeaways
- `$…$` inline; `\[ … \]` unnumbered; `equation` numbered; `align` for aligned multi-line systems (`&`, `\\`, `\nonumber`).
- `\frac`, `\sqrt`, `\sum`, `\int … \,\mathrm{d}t`, `pmatrix`/`bmatrix`, `\left( \right)`.
- Upright operators (`\sin`, `\DeclareMathOperator`), `\mathbf`/`\vec` for vectors, `\text{}` for words, `siunitx` for units.
- `\label{eq:x}` + `\eqref{eq:x}`; load `amsmath`, `amssymb`, `mathtools`.
