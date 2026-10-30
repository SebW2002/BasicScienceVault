---
tags: [programming, r, visualization, type/worksheet]
---
# R06 ggplot2 Visualization – Worksheet

> Theory: [[R06 ggplot2 Visualization]] · Solutions: [[R06 ggplot2 Visualization - Solutions]] · Log mistakes in [[Mistakes - R]]
> Work on paper: predict outputs, find bugs, write short snippets. Run code only for tasks marked 💻.

## Level 1 – Grammar
1. Name the component (data, aesthetic, geom, stat, scale, facet, coordinate, theme): a) `colour = condition` b) `geom_boxplot()` c) `facet_wrap(~ electrode)` d) `scale_y_log10()` e) `theme_classic()` f) `stat_summary()`.
2. What is the difference between `geom_point(aes(colour = group))` and `geom_point(colour = "red")`?
3. Why does `ggplot(df, aes(x, y)) |> geom_point()` fail?

## Level 2 – Predict / debug
4. `ggplot(df, aes(time, amp)) + geom_line()` with data from 3 conditions draws one zig-zag line. Why? Two ways to fix it.
5. `geom_point(aes(colour = "blue"))` draws red-ish points with a legend "blue". Explain and fix.
6. The x-axis shows conditions in the order "house, scrambled, face" but you want "scrambled, face, house". Fix it.
7. A bar chart of mean RT per condition from 24 subjects × 200 trials uses `stat_summary(fun.data = mean_se)` on the trial table. What's wrong with the error bars?

## Level 3 – Write code
8. Plot each subject's mean RT in two conditions with lines connecting a subject's points, plus the group mean ± 95 % CI.
9. Plot ERPs (`time`, `amp`, `condition`, `electrode`) as lines with a ±SE ribbon (`lo`, `hi` columns), one panel per electrode, colour-blind-safe colours.
10. Save the plot from task 9 as a vector PDF, 170 mm wide and 100 mm high.

## Level 4 – Neuro transfer
11. You plot a time–frequency map with `geom_tile(aes(time, freq, fill = power_change))`, where `power_change` is a signed % change from baseline. Which fill scale and limits?
12. Sketch the code for a psychometric function: proportion of "seen" responses vs. contrast (log scale), points per contrast level, and a logistic fit.
13. 💻 Use the built-in data set `ToothGrowth` (or your own) to make a violin + jitter plot with `theme_classic(base_size = 9)`, and export it with `ggsave` as PDF and PNG (600 dpi).
