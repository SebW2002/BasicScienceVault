---
tags: [programming, r, statistics, type/worksheet]
---
# R07 R Statistical Modelling – Worksheet

> Theory: [[R07 R Statistical Modelling]] · Solutions: [[R07 R Statistical Modelling - Solutions]] · Log mistakes in [[Mistakes - R]]
> Work on paper; no calculator unless marked. Run code only for tasks marked 💻.

## Level 1 – Formulas
1. Write the formula: a) RT depends on condition and group, including their interaction b) accuracy depends on log contrast c) spike count depends on orientation, with trials of different durations.
2. Expand `y ~ a * b * c` into all its terms.
3. Which `family` for: a) correct/incorrect b) number of errors per block c) number of spikes in 500 ms bins d) a continuous, roughly normal amplitude?

## Level 2 – Read output
4. `lm(rt ~ condition)` with levels "house" (reference) and "face": `(Intercept) = 0.55`, `conditionface = -0.06`. What are the two condition means? Which test does the p-value of `conditionface` correspond to?
5. `lm(rt ~ age)`: slope 0.004 s/year, intercept 0.30. Predicted RT at 25 and 65 years? Why is the intercept hard to interpret, and how would centring help?
6. Logistic regression: `(Intercept) = -1.0`, `log_contrast = 2.0`. a) Log-odds and probability of "seen" at log_contrast = 0.5 b) the threshold (p = 0.5) c) the odds ratio per unit of log contrast (as $e^2\approx7.4$).
7. Poisson GLM: `(Intercept) = log(5)`, `stimulusB = log(2)`, offset log(duration in s). What are the firing rates for A and B?

## Level 3 – Assumptions
8. The residual-vs-fitted plot shows a U-shape; the Q–Q plot is fine. What's wrong and what do you try?
9. The scale–location plot shows a funnel opening to the right in an RT model. What's the likely cause and remedy?
10. You run `lm(rt ~ condition)` on 20 subjects × 100 trials. The residual plots look fine. Is the model OK? Explain.
11. A Poisson GLM has residual deviance 840 on 200 df. Problem? Remedy?

## Level 4 – Neuro transfer
12. Write the R code to compare ERP amplitudes between patients and controls, controlling for age, and get the adjusted group difference with a 95 % CI.
13. Paired design: 18 subjects, mean P300 amplitude for oddball and standard. Write the paired t-test and its non-parametric alternative. Why can't you use `t.test(amp ~ condition, data = long)` without `paired`?
14. 💻 Simulate 200 bins of spike counts with rate 10 Hz (stimulus A) or 20 Hz (stimulus B), bin length 0.1 s (`set.seed(2)`; `rpois`). Fit `glm(count ~ stimulus, family = poisson)` and check that `exp(coef)` recovers the expected count per bin for A (≈ 1) and the rate ratio (≈ 2).
