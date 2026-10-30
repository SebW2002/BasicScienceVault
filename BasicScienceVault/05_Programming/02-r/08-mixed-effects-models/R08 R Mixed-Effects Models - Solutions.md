---
tags: [programming, r, mixed-models, type/solution]
---
# R08 R Mixed-Effects Models – Solutions

> Worksheet: [[R08 R Mixed-Effects Models - Worksheet]] · Theory: [[R08 R Mixed-Effects Models]] · Wrong? → [[Mistakes - R]]

## Level 1
1. a) **fixed** (effect of interest, 2 fixed levels) b) **random** (sample from a population of people) c) **random** (sample of possible stimuli; crossed with subjects) d) **fixed** (only 2 levels, of interest) e) mouse **random**, cells nested in mice (random `mouse/cell` if there are repeated measures per cell) f) usually **fixed** (2 levels are too few for a variance) or a random effect nested in subject if you have many sessions.
2. a) `(1 | subject)` b) `(1 + condition | subject)` c) `(1 | subject) + (1 | item)` d) `(1 | animal/cell)` = `(1 | animal) + (1 | animal:cell)`.

## Level 2
3. a) house (reference) 0.52 s, face 0.48 s. b) 0.52 ± 2 · 0.06 → about 0.40 to 0.64 s. c) ICC = $0.06^2/(0.06^2 + 0.12^2) = 0.0036/0.018 = 0.2$.
4. If subjects really differ in their condition effect, this variability is part of the uncertainty about the **average** effect. Ignoring it treats every trial as evidence about one shared effect, so the SE is too small and false positives increase.
5. Subject-specific estimates (BLUPs) are pulled towards the group mean. Subjects with **few trials or noisy data** are shrunk most, because their own data provide less information (partial pooling).
6. The degrees of freedom for the t/F tests are not exactly defined in mixed models. Use `lmerTest` (Satterthwaite or Kenward–Roger df), likelihood-ratio tests, parametric bootstrap, or confidence intervals.

## Level 3
7. REML likelihoods depend on the fixed-effect structure, so REML fits with different fixed effects aren't comparable. `anova()` on `lmerMod` objects **refits with ML** automatically before the likelihood-ratio test.
8. The data don't support estimating that random slope: its variance is estimated as zero and the correlation at the boundary. Simplify: drop the correlation (`||`), then the slope; or use a Bayesian model with regularising priors. Don't interpret the degenerate parameters.
9. AIC slightly prefers C (1 point better than B – a negligible difference), BIC strongly prefers B (C pays a big penalty for 6 extra parameters). Choose **B**: simplest model that fits well; C's gain is not worth 6 parameters. (Ideally, hypotheses decide the model; selection criteria help with nuisance structure.)

## Level 4
10. `lmer(rate ~ condition + (1 + condition | mouse/cell), data = d)` (or at least `(1 | mouse) + (1 + condition | mouse:cell)` – simplify if singular). A t-test over all cells treats ~300 cells as independent, but cells from the same mouse share genetics, preparation and recording quality; the effective sample size for conclusions about mice is closer to 4 → pseudoreplication, inflated false positives.
11. ```r
    b <- brm(correct ~ condition + (1 + condition | subject), data = d,
             family = bernoulli(), prior = prior(normal(0, 1), class = "b"),
             chains = 4, iter = 2000, seed = 1)
    ```
    Check $\hat R\le1.01$ for all parameters, bulk/tail ESS (hundreds or more), no divergent transitions, trace plots well mixed, and a posterior predictive check.
12. "Given the model, the priors and the data, there's a 95 % probability that faces speed RTs by between 12 and 58 ms (posterior mean 35 ms)." A frequentist CI is a statement about the procedure (95 % of such intervals would contain the true value in repeated experiments), not a probability about the parameter.
13. ```r
    library(lme4)
    set.seed(3)
    d <- expand.grid(trial = 1:50, subject = factor(1:20))
    d$condition <- factor(rep(c("house", "face"), length.out = nrow(d)))
    u <- rnorm(20, 0, 0.05)
    d$rt <- 0.5 + u[d$subject] - 0.03 * (d$condition == "face") + rnorm(nrow(d), 0, 0.1)
    summary(lmer(rt ~ condition + (1 | subject), data = d))$coefficients
    summary(lm(rt ~ condition, data = d))$coefficients
    m <- aggregate(rt ~ subject + condition, data = d, mean)
    summary(lm(rt ~ condition + subject, data = m))$coefficients["conditionhouse", ]
    ```
    Here condition varies **within** subjects, so the random intercepts remove between-subject variance from the condition comparison: the `lmer` SE (≈ 0.0063) is smaller than the naive `lm` SE (≈ 0.0071), which lumps subject differences into the residual. The subject-means analysis (paired) gives about the same SE as `lmer`. (With a between-subject factor, the naive `lm` SE would instead be **too small**. And if the condition effect varied across subjects, you'd also need random slopes.)
