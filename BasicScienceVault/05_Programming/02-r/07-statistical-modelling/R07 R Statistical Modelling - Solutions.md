---
tags: [programming, r, statistics, type/solution]
---
# R07 R Statistical Modelling – Solutions

> Worksheet: [[R07 R Statistical Modelling - Worksheet]] · Theory: [[R07 R Statistical Modelling]] · Wrong? → [[Mistakes - R]]

## Level 1
1. a) `rt ~ condition * group` b) `correct ~ log(contrast)` with `family = binomial` c) `count ~ orientation + offset(log(duration))` with `family = poisson` (orientation as factor, or $\cos/\sin$ terms).
2. `a + b + c + a:b + a:c + b:c + a:b:c`
3. a) binomial b) poisson (or negative binomial if overdispersed) c) poisson (check overdispersion) d) gaussian (`lm`).

## Level 2
4. house = 0.55 s, face = 0.55 − 0.06 = 0.49 s. It's the two-sample t-test with **equal variances** (Student's), testing face − house = 0.
5. 25 years: 0.30 + 0.1 = 0.40 s; 65 years: 0.30 + 0.26 = 0.56 s. The intercept is the predicted RT at age **0** – outside the data. With centred age (e.g. `age - 40`), the intercept is the RT of a 40-year-old.
6. a) log-odds = −1 + 2 · 0.5 = 0 → p = 0.5. b) threshold where log-odds = 0: log_contrast = 1/2 = 0.5 (that's a). c) odds ratio $e^{2}\approx7.4$: each unit of log contrast multiplies the odds of "seen" by 7.4.
7. With the offset, coefficients are on the log-**rate** scale: A = 5 Hz, B = 5 · 2 = **10 Hz**.

## Level 3
8. **Non-linearity**: the relationship is curved. Try a transformation (log), a polynomial/spline term (`poly(x, 2)`, `splines::ns(x, 3)`), or a missing predictor.
9. Variance grows with the mean (RTs are right-skewed, slow conditions vary more) → heteroscedasticity. Log-transform RT, use a Gamma GLM, or robust (sandwich) SEs.
10. **No.** The 2000 trials aren't independent – trials of the same subject are correlated. The SEs are far too small (pseudoreplication). Use subject means (one per subject × condition) or a mixed model with random effects for subject ([[R08 R Mixed-Effects Models]]).
11. Deviance/df = 4.2 ≫ 1 → **overdispersion**: SEs too small, p-values too optimistic. Use `quasipoisson`, a negative binomial model (`MASS::glm.nb`), or a mixed model with an observation-level random effect.

## Level 4
12. ```r
    m <- lm(amp ~ group + age, data = d)
    summary(m); confint(m)["grouppatient", ]
    # or adjusted means: emmeans::emmeans(m, pairwise ~ group)
    ```
13. ```r
    t.test(w$oddball, w$standard, paired = TRUE)
    wilcox.test(w$oddball, w$standard, paired = TRUE)
    ```
    The formula version without pairing treats the two conditions as independent groups and ignores that each subject contributes to both – it loses the within-subject variance reduction (and is the wrong test). (Recent R versions don't accept `paired = TRUE` with the formula interface anyway: use wide data.)
14. ```r
    set.seed(2)
    d <- data.frame(stimulus = factor(rep(c("A", "B"), each = 100)))
    d$count <- rpois(200, lambda = ifelse(d$stimulus == "A", 10, 20) * 0.1)
    m <- glm(count ~ stimulus, family = poisson, data = d)
    exp(coef(m))   # (Intercept) ≈ 1 count/bin (10 Hz × 0.1 s); stimulusB ≈ 2 (rate ratio)
    ```
