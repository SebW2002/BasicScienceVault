---
aliases: [Math in Markdown, LaTeX in Markdown, MathJax, Inline Math, Display Math]
tags: [programming, markdown, latex, math-typesetting, type/overview, neuro]
---
# Doc02 Math in Markdown

> [[Doc00 Markdown HTML and LaTeX Overview|↑ Markdown, HTML & LaTeX]] · [[MOC-programming|Programming MOC]] · [[Doc02 Math in Markdown - Worksheet|✏️ Worksheet]] · [[Doc02 Math in Markdown - Solutions|✅ Solutions]] · [[Mistakes - Markdown HTML LaTeX|⚠️ Mistake log]]

## Why this matters
Every formula in this vault – the Nernst equation, the membrane equation, Fourier transforms – is written in **LaTeX math syntax** inside Markdown. The same syntax works in Obsidian, Jupyter, Quarto/R Markdown, GitHub, MATLAB Live Scripts and full LaTeX documents ([[Doc06 LaTeX Math]]). Learning it once pays off everywhere.

## Inline and display formulas
```markdown
The membrane time constant is $\tau = RC$.          ← inline: inside a sentence

$$
V(t) = V_\infty + (V_0 - V_\infty)\,e^{-t/\tau}
$$                                                   ← display: own line, centred
```
- **Inline** `$...$`: no space directly after the opening `$` or before the closing `$` (otherwise many renderers don't recognise it: `$ x $` may fail, and "costs $5 and $10" can accidentally become math).
- **Display** `$$...$$`: on its own lines; leave blank lines around the block.
- Rendering is done by **MathJax** or **KaTeX** (JavaScript libraries) in Obsidian, Jupyter, GitHub and HTML output; by real LaTeX for PDF output.
- A literal dollar sign: `\$`.

## Basic LaTeX syntax inside Markdown
| You want | Write | Result |
|---|---|---|
| sub- and superscripts | `x_i^2`, `x_{ij}`, `e^{-t/\tau}` | $x_i^2$, $x_{ij}$, $e^{-t/\tau}$ |
| fraction | `\frac{a}{b}`, `\dfrac{a}{b}` (display size) | $\frac{a}{b}$ |
| root | `\sqrt{2Dt}`, `\sqrt[3]{x}` | $\sqrt{2Dt}$ |
| Greek letters | `\alpha \beta \tau \lambda \Delta \Omega` | $\alpha\ \beta\ \tau\ \lambda\ \Delta\ \Omega$ |
| sums, integrals | `\sum_{i=1}^{n} x_i`, `\int_0^T I(t)\,dt` | $\sum_{i=1}^{n} x_i$, $\int_0^T I(t)\,dt$ |
| functions | `\ln`, `\log_{10}`, `\sin`, `\exp`, `\max` | upright, correctly spaced |
| relations | `\approx \neq \le \ge \propto \sim \to` | $\approx\ \neq\ \le\ \ge\ \propto\ \sim\ \to$ |
| text in math | `E_\text{rev}`, `\mathrm{mV}` | $E_\text{rev}$ |
| vectors / bold | `\mathbf{x}`, `\vec{v}` | $\mathbf{x}$, $\vec{v}$ |
| brackets that grow | `\left( \frac{a}{b} \right)` | $\left(\frac{a}{b}\right)$ |
| derivatives | `\frac{dV}{dt}`, `\frac{\partial f}{\partial x}`, `\dot{x}` | $\frac{dV}{dt}$, $\frac{\partial f}{\partial x}$ |
| spacing | `\,` thin, `\quad` wide | – |
- **Braces group:** `x^10` gives $x^10$ (only the 1 is raised) – write `x^{10}`.
- **Multi-letter names** in italics look like products: write `\text{SNR}` or `\mathrm{SNR}`, not `SNR`.

### Matrices and aligned equations
```latex
$$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad
\mathbf{y} = \begin{bmatrix} y_1 \\ \vdots \\ y_n \end{bmatrix}
$$

$$
\begin{aligned}
C_m \frac{dV}{dt} &= -g_L (V - E_L) + I \\
\tau &= \frac{C_m}{g_L}
\end{aligned}
$$

$$
f(x) = \begin{cases} 0 & x < 0 \\ x & x \ge 0 \end{cases}
$$
```
`&` marks alignment points / column separators, `\\` ends a row. `pmatrix` = round, `bmatrix` = square brackets, `vmatrix` = determinant bars.

## Differences between Obsidian, GitHub and Quarto
| Feature | Obsidian | GitHub | Quarto / R Markdown |
|---|---|---|---|
| engine | MathJax | MathJax | MathJax/KaTeX (HTML), LaTeX (PDF) |
| `$...$`, `$$...$$` | ✅ | ✅ (inline has quirks next to punctuation/backticks; alternative: `` $`...`$ ``) | ✅ |
| ```` ```math ```` block | ❌ (shows a code block) | ✅ | ❌ (use `$$`) |
| `aligned`, `cases`, `pmatrix` | ✅ | ✅ | ✅ |
| `align` environment (numbered) | renders, no cross-references | partly | ✅ in PDF; in HTML via MathJax |
| equation numbers / references | manual `\tag{1}` | manual `\tag{1}` | `$$ … $$ {#eq-name}` + `@eq-name` ✅ |
| macros (`\newcommand`) | ✅ within a note (MathJax) | limited | ✅ (in the document or a header file) |
| packages (`\usepackage`) | ❌ | ❌ | only in PDF output (LaTeX) |
| `\mathbb{R}`, `\boldsymbol` | ✅ | ✅ | ✅ |
- **Underscores and asterisks:** GitHub's Markdown parser sometimes treats `_` or `*` inside inline math as emphasis (e.g. `$a_1 + b_1$` on one line with other `_`). Workarounds: `` $`a_1`$ `` syntax, escaping (`\_`), or display math.
- **Obsidian:** math inside tables works, but a `|` inside math must be escaped (`\|` – also `\lvert … \rvert` for absolute values avoids the problem; that's why this vault writes $\lvert x\rvert$).
- **Quarto:** what renders in HTML may fail in PDF if you use MathJax-only commands; test both outputs ([[R10 R Markdown and Quarto]]).

## In neuroscience #neuro
- **Notes on models:** Nernst $E = \frac{RT}{zF}\ln\frac{[\text{ion}]_o}{[\text{ion}]_i}$, Hodgkin–Huxley, LIF, GLMs – written once in Markdown, reusable in reports and theses.
- **Methods sections in Quarto** with numbered equations (`{#eq-glm}`) referenced in the text.
- **Jupyter notebooks** explain the maths of an analysis (e.g. the Welch estimator) above the code that implements it.
- **README / GitHub:** model equations in a repository's documentation.

## Math links #math-link
- The formulas you'll write most: exponentials and logs → [[B2 Exponential Functions]], [[A3 Logarithms]]; matrices → [[C1 Matrices]]; derivatives and integrals → [[B6 Differentiation Rules]], [[B7 Antiderivatives and Integration]]; sets and logic notation → [[E1 Sets Logic and Quantifiers]]

## Connections
- Full LaTeX math (environments, numbering, packages) → [[Doc06 LaTeX Math]]
- Markdown basics → [[Doc01 Markdown Syntax]]
- Reports with formulas → [[R10 R Markdown and Quarto]], [[MAT11 MATLAB Live Scripts and Reports]]

## Key takeaways
- `$...$` inline (no inner spaces at the edges), `$$...$$` display (own lines).
- Group with braces: `x^{10}`, `e^{-t/\tau}`; `\frac`, `\sqrt`, `\sum`, `\int`, `\text{}`.
- `pmatrix`/`bmatrix` for matrices, `aligned` for multi-line equations, `cases` for piecewise functions.
- Numbering and cross-references: Quarto (`{#eq-}`/`@eq-`) or LaTeX; Obsidian/GitHub only `\tag{}`.
