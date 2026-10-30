---
tags: [programming, r, visualization, type/solution]
---
# R06 ggplot2 Visualization – Solutions

> Worksheet: [[R06 ggplot2 Visualization - Worksheet]] · Theory: [[R06 ggplot2 Visualization]] · Wrong? → [[Mistakes - R]]

## Level 1
1. a) aesthetic b) geom c) facet d) scale e) theme f) stat.
2. The first **maps** the variable `group` to colour (colours vary with data, a legend appears); the second **sets** all points to red (no legend).
3. ggplot layers are combined with `+`, not with the pipe. Write `ggplot(df, aes(x, y)) + geom_point()`.

## Level 2
4. ggplot connects all points in x order as one group. Fix: `aes(colour = condition)` (grouping follows from the colour) or `aes(group = condition)`.
5. Inside `aes()`, `"blue"` is treated as a data value (a constant category called "blue"), mapped to the first default colour, with a legend. Fix: `geom_point(colour = "blue")` outside `aes()`.
6. Set the factor levels: `df$condition <- factor(df$condition, levels = c("scrambled", "face", "house"))` (or `scale_x_discrete(limits = …)`).
7. The SE treats 4800 trials as independent observations, so bars are far too small; the relevant variability is between the 24 subjects. Compute subject means first, then summarise across subjects (and show the subject points).

## Level 3
8. ```r
   ggplot(subj_means, aes(condition, rt)) +
     geom_line(aes(group = subject), colour = "grey80") +
     geom_point(colour = "grey50") +
     stat_summary(fun.data = mean_cl_normal, colour = "black") +
     labs(x = NULL, y = "Mean RT (s)") + theme_classic()
   ```
   (`mean_cl_normal` needs the Hmisc package installed.)
9. ```r
   p <- ggplot(erp, aes(time, amp, colour = condition, fill = condition)) +
     geom_ribbon(aes(ymin = lo, ymax = hi), alpha = 0.2, colour = NA) +
     geom_line() +
     facet_wrap(~ electrode) +
     scale_colour_viridis_d(end = 0.8) + scale_fill_viridis_d(end = 0.8) +
     labs(x = "Time (ms)", y = "Amplitude (µV)") + theme_classic(base_size = 8)
   ```
10. `ggsave("figures/erp.pdf", p, width = 170, height = 100, units = "mm")`

## Level 4
11. A **diverging** scale centred on 0 with symmetric limits: `scale_fill_distiller(palette = "RdBu", limits = c(-m, m))` with `m = max(abs(power_change))` (or `scale_fill_gradient2(midpoint = 0)`), so "no change" is the neutral colour.
12. ```r
    ggplot(psy, aes(contrast, p_seen)) +
      geom_point() +
      geom_smooth(aes(weight = n), method = "glm", method.args = list(family = binomial), se = FALSE) +
      scale_x_log10() + labs(x = "Contrast (log)", y = "P(seen)")
    ```
    (With proportions, `weight = n` gives the number of trials per point; a proper fit uses `glm(cbind(seen, n - seen) ~ log(contrast), family = binomial)`, [[R07 R Statistical Modelling]].)
13. ```r
    library(ggplot2)
    p <- ggplot(ToothGrowth, aes(supp, len)) +
      geom_violin(fill = "grey90") +
      geom_jitter(width = 0.08, alpha = 0.6) +
      labs(x = "Supplement", y = "Tooth length") +
      theme_classic(base_size = 9)
    ggsave("violin.pdf", p, width = 80, height = 60, units = "mm")
    ggsave("violin.png", p, width = 80, height = 60, units = "mm", dpi = 600)
    ```
