---
tags: [programming, r, mixed-models, type/worksheet]
---
# R08 R Mixed-Effects Models – Worksheet

> Theory: [[R08 R Mixed-Effects Models]] · Solutions: [[R08 R Mixed-Effects Models - Solutions]] · Log mistakes in [[Mistakes - R]]
> Work on paper; no calculator unless marked. Run code only for tasks marked 💻.

## Level 1 – Fixed or random?
1. Classify as fixed or random effect and justify: a) condition (face/house) b) subject (n = 30) c) stimulus image (60 faces) d) hemisphere (left/right) e) mouse (n = 8), cells recorded within mice f) session (2 sessions per subject).
2. Translate into lme4 syntax: a) subjects differ in baseline b) subjects differ in baseline and in their condition effect c) crossed subjects and items d) cells nested in animals.

## Level 2 – Interpretation
3. `lmer(rt ~ condition + (1 | subject))`: fixed `(Intercept) = 0.52`, `conditionface = -0.04`; random intercept SD = 0.06 s, residual SD = 0.12 s. a) Mean RT per condition for the average subject b) range containing ~95 % of subjects' baselines c) ICC.
4. Why can a model with only random intercepts give a too-small SE for the condition effect?
5. What is "shrinkage" and which subjects are shrunk most?
6. lme4 prints no p-values. Why? How do you get them?

## Level 3 – Model comparison and problems
7. You compare `rt ~ 1 + (1|subject)` and `rt ~ condition + (1|subject)` with `anova()`. Why must they be fitted with ML rather than REML? What does `anova()` do automatically?
8. Output: `boundary (singular) fit: see help('isSingular')`; random slope variance 0.000, correlation −1.00. What does this mean and what do you do?
9. AIC: model A 1520, model B 1514, model C 1513 (C has 6 more parameters than B). BIC: A 1560, B 1556, C 1590. Which model do you prefer and why?

## Level 4 – Neuro transfer and brms
10. 4 mice, 50–120 cells each, firing rate in two conditions. Write the model. Why is a t-test over all cells wrong?
11. Write a brms model for accuracy (0/1) with condition as fixed effect and by-subject random intercepts and slopes, with a normal(0, 1) prior on the fixed effect. Which convergence diagnostics do you check?
12. A brms posterior for `conditionface` has mean −0.035 and 95 % CrI [−0.058, −0.012]. Interpret in one sentence. How does this differ from a frequentist 95 % CI?
13. 💻 Simulate 20 subjects × 50 trials with a random intercept (SD 0.05), condition effect −0.03, residual SD 0.1 (`set.seed(3)`); fit `lmer` with random intercepts, compare the condition SE with that of `lm(rt ~ condition)` on the same trials and on subject means.
