---
aliases: [ggplot2, Grammar of Graphics, Aesthetics, Geoms, Facets, ggsave]
tags: [programming, r, visualization, ggplot2, type/overview, neuro]
---
# R06 ggplot2 Visualization

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · [[R06 ggplot2 Visualization - Worksheet|✏️ Worksheet]] · [[R06 ggplot2 Visualization - Solutions|✅ Solutions]] · [[Mistakes - R|⚠️ Mistake log]]

## Why this matters
ggplot2 is one of the main reasons people choose R. Instead of drawing lines and points by hand, you **describe** a plot: which data, which variables map to which visual properties, which geometric shapes. The same grammar scales from a quick look to a publication figure, and it works directly on tidy data ([[R04 R Data Import and Tidy Data]]).

## The grammar of graphics
A plot is built from layers:
| Component | Question | Example |
|---|---|---|
| **data** | which table? | `ggplot(df, …)` (tidy, long format) |
| **aesthetics** `aes()` | which variable → which visual property? | `aes(x = time, y = amp, colour = condition)` |
| **geoms** | which shape? | `geom_point()`, `geom_line()`, `geom_boxplot()` |
| **stats** | which transformation? | `stat_summary(fun.data = mean_cl_normal)`, `geom_smooth(method = "lm")` |
| **scales** | how are values mapped? | `scale_colour_viridis_d()`, `scale_y_log10()` |
| **facets** | small multiples by a variable | `facet_wrap(~ electrode)`, `facet_grid(group ~ condition)` |
| **coordinates** | which coordinate system? | `coord_flip()`, `coord_polar()` |
| **theme** | non-data look | `theme_classic()`, `theme(legend.position = "top")` |
```r
library(ggplot2)
ggplot(erp_long, aes(x = time, y = amp, colour = condition)) +
  geom_hline(yintercept = 0, colour = "grey70") +
  geom_line(linewidth = 0.6) +
  facet_wrap(~ electrode, ncol = 3) +
  labs(x = "Time (ms)", y = "Amplitude (µV)", colour = NULL) +
  theme_classic(base_size = 9)
```
- Layers are added with **`+`** (not `|>`!).
- **Mapping vs. setting:** inside `aes()` a property *depends on data* (`aes(colour = condition)`); outside it's a constant (`geom_point(colour = "black")`). `aes(colour = "black")` creates a legend entry called "black" – a classic mistake.
- Aesthetics: `x`, `y`, `colour`, `fill`, `shape`, `linetype`, `size`, `alpha`, `group` (which points form one line).
- Factor level order sets the order of categories on axes and in legends ([[R01 R Basics and Syntax]]).

## Common geoms for science
| Goal | Geom |
|---|---|
| every data point | `geom_point()`, `geom_jitter(width = 0.1)`, `ggbeeswarm::geom_quasirandom()` |
| distributions | `geom_histogram(binwidth = …)`, `geom_density()`, `geom_violin()`, `geom_boxplot()` |
| mean ± CI/SE | `stat_summary(fun.data = mean_cl_boot)` / `mean_se`, `geom_pointrange()`, `geom_errorbar()` |
| time courses | `geom_line()`, `geom_ribbon(aes(ymin = lo, ymax = hi), alpha = 0.3)` |
| paired data | `geom_line(aes(group = subject), alpha = 0.3)` + points |
| relationships | `geom_point()` + `geom_smooth(method = "lm")` |
| matrices, time–frequency | `geom_tile(aes(fill = power))` / `geom_raster()` |
**Show the data**, not just bars ([[CS06 Data Science Workflow]]):
```r
ggplot(subj_means, aes(condition, rt)) +
  geom_line(aes(group = subject), colour = "grey80") +      # paired lines
  geom_point(colour = "grey50") +
  stat_summary(fun.data = mean_cl_normal, colour = "black", size = 0.6) +   # mean ± 95 % CI
  labs(x = NULL, y = "Mean RT (s)")
```
Compute subject means first; `stat_summary` on raw trials would treat trials as independent (pseudoreplication).

## Themes and publication figures
```r
theme_set(theme_classic(base_size = 8, base_family = "Helvetica"))   # once, for all plots
p + theme(legend.position = "bottom",
          strip.background = element_blank(),
          axis.text = element_text(colour = "black"))
p + scale_colour_viridis_d(end = 0.8) + scale_fill_brewer(palette = "Set2")   # colour-blind safe
p + scale_fill_distiller(palette = "RdBu", limits = c(-m, m))                  # diverging, centred
```
- Built-in themes: `theme_classic()`, `theme_minimal()`, `theme_bw()`; journals usually like `classic`.
- Colour: viridis for ordered data, Brewer "Set2"/"Dark2" or Okabe–Ito for categories, diverging maps centred on 0 for signed values (same rules as [[Py07 Python Plotting and Visualization]]).
- Combine panels with **patchwork**: `(p1 | p2) / p3 + plot_annotation(tag_levels = "A")`.

## Export to PDF and SVG
```r
ggsave("figures/fig2_erp.pdf", p, width = 85, height = 60, units = "mm")   # one column ≈ 85 mm
ggsave("figures/fig2_erp.svg", p, width = 85, height = 60, units = "mm")   # needs the svglite package
ggsave("figures/fig2_erp.png", p, width = 85, height = 60, units = "mm", dpi = 600)
```
- Set the **final size** in `ggsave`; then font sizes in the theme are true point sizes in the paper.
- PDF/SVG are vector formats: sharp at any zoom, editable in Inkscape/Illustrator; use `cairo_pdf` (`device = cairo_pdf`) if special characters (µ, −) don't render.
- Include figures in documents → [[R10 R Markdown and Quarto]], [[Doc08 LaTeX Figures Tables and References]].

## Same idea in Python and MATLAB
seaborn's `relplot/catplot` and plotnine copy ggplot's ideas ([[Py07 Python Plotting and Visualization]]); MATLAB builds plots imperatively with `plot`, `hold on`, `tiledlayout` ([[MAT05 MATLAB Plotting]]).

## In neuroscience #neuro
- **ERPs per electrode**: `geom_line` + `geom_ribbon` (± SE across subjects), `facet_wrap(~ electrode)`.
- **Behaviour**: paired subject lines for within-subject designs; violin + points for groups.
- **Psychometric functions**: proportion "yes" vs. stimulus intensity with `geom_point` + `geom_smooth(method = "glm", method.args = list(family = binomial))` ([[R07 R Statistical Modelling]]).
- **Model predictions** from mixed models (`ggeffects`, `emmeans`) plotted over raw subject means ([[R08 R Mixed-Effects Models]]).
- **Topographies** need specialised packages (`eegUtils`, [[R09 R Neuroscience Packages]]).

## Math links #math-link
- Log scales (`scale_x_log10`) for frequencies, concentrations → [[B3 Logarithmic Functions]]
- Linear fits `geom_smooth(method = "lm")` → [[C3 Linear Systems and Gaussian Elimination]] (least squares)
- Logistic curve of psychometric functions → [[B2 Exponential Functions]]
- Polar coordinates for directional tuning (`coord_polar`) → [[D4 Unit Circle Trigonometry]]

## Connections
- Tidy data and dplyr → [[R04 R Data Import and Tidy Data]], [[R05 dplyr and tidyr]]
- Visualisation principles → [[CS06 Data Science Workflow]]
- Python plotting → [[Py07 Python Plotting and Visualization]]
- Figures in reports → [[R10 R Markdown and Quarto]]

## Key takeaways
- `ggplot(data, aes(...)) + geom_*() + facet_*() + scale_*() + theme_*()`; layers with `+`.
- Map data in `aes()`, set constants outside.
- Show raw (subject-level) data; summarise per subject before CIs.
- `ggsave` with final width/height in mm; PDF/SVG for vector output.
