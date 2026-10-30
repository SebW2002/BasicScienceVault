---
aliases: [R Statistical Modelling, lm, glm, Linear Models in R, Residual Analysis, ANOVA in R, t-test in R]
tags: [programming, r, statistics, regression, glm, type/overview, neuro]
---
# R07 R Statistical Modelling

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · [[R07 R Statistical Modelling - Worksheet|✏️ Worksheet]] · [[R07 R Statistical Modelling - Solutions|✅ Solutions]] · [[Mistakes - R|⚠️ Mistake log]]

## Why this matters
t-tests, ANOVAs and correlations are all special cases of the **linear model**. R's formula interface makes this explicit: `rt ~ condition` is a t-test, `rt ~ condition * group` a two-way ANOVA, `count ~ stimulus` with a Poisson family a model of spike counts. Knowing what the coefficients mean and checking the assumptions is what turns output into results. Concepts → [[CS02 Probability and Statistics]].

## Formulas
| Formula | Model |
|---|---|
| `y ~ x` | $y = \beta_0 + \beta_1 x + \varepsilon$ |
| `y ~ x1 + x2` | two main effects |
| `y ~ x1 * x2` | main effects **and** interaction (`x1 + x2 + x1:x2`) |
| `y ~ x - 1` / `y ~ 0 + x` | no intercept |
| `y ~ log(x)`, `y ~ I(x^2)` | transformed predictors (`I()` protects arithmetic) |
| `y ~ poly(x, 2)` | polynomial |
| `y ~ .` | all other columns |
Categorical predictors (factors) are turned into **dummy variables**: with treatment coding (R's default), each coefficient is the difference of a level from the **reference level** ([[R01 R Basics and Syntax]]).

## Linear models: lm
```r
m <- lm(rt ~ condition + age, data = d)
summary(m)          # coefficients, SEs, t, p, R², F
coef(m); confint(m) # estimates and 95 % CIs
anova(m)            # sequential (type I) F-tests
predict(m, newdata = data.frame(condition = "face", age = 25), interval = "confidence")
```
**Reading `summary(lm(rt ~ condition))`** with levels house (reference) and face:
- `(Intercept)` = mean RT for **house**;
- `conditionface` = mean(face) − mean(house), with its t-test – identical to a two-sample t-test with equal variances.
- **Continuous predictor:** change in $y$ per unit of $x$. Centre continuous predictors (`age - mean(age)`) so the intercept and main effects in interactions are interpretable.
- **Interaction** `condition * age`: the effect of condition **depends on** age; main effects then refer to the reference level/zero point of the other variable.
- **Contrasts:** for ANOVA-style main effects use sum coding: `contrasts(d$condition) <- contr.sum(2)` (or `options(contrasts = c("contr.sum", "contr.poly"))`).

## Generalised linear models: glm
When $y$ isn't continuous and normal, a **GLM** models a transformed mean (link function) with a matching error distribution:
| Data | Family | Link | Coefficient meaning |
|---|---|---|---|
| binary (correct/incorrect, seen/unseen) | `binomial` | logit $\log\frac{p}{1-p}$ | change in **log-odds**; `exp(b)` = odds ratio |
| counts (spikes per bin, errors) | `poisson` | log | change in **log rate**; `exp(b)` = rate ratio |
| overdispersed counts | `quasipoisson`, `MASS::glm.nb` | log | same, with larger SEs |
| positive skewed (RT) | `Gamma` / `inverse.gaussian` | log / inverse | – |
```r
m_acc <- glm(correct ~ contrast, family = binomial, data = d)
m_spk <- glm(spikes ~ stimulus + offset(log(duration)), family = poisson, data = units)
exp(coef(m_spk))     # rate ratios
```
- `offset(log(duration))` models **rates** when bins/trials have different lengths.
- Check **overdispersion** for Poisson: residual deviance / df ≫ 1 (spike counts are often more variable than Poisson; [[CS02 Probability and Statistics]], Fano factor).
- Logistic regression on proportions: `cbind(successes, failures) ~ x`.

## Assumptions and residual analysis
Linear model assumptions: **linearity**, **independence** of errors, **homoscedasticity** (constant variance), **normality of residuals** (not of the raw data!), no overly influential points.
```r
par(mfrow = c(2, 2)); plot(m)     # 4 diagnostic plots
# or: performance::check_model(m)
```
| Plot | Look for | Problem → remedy |
|---|---|---|
| residuals vs. fitted | no pattern around 0 | curve → non-linearity (transform, add terms) |
| Q–Q plot | points on the line | heavy tails/skew → transform (log RT), GLM, robust methods |
| scale–location | flat band | funnel → heteroscedasticity (transform, weighted/robust SEs) |
| residuals vs. leverage | no points beyond Cook's distance lines | influential points → check data, robust regression |
- **Independence** can't be seen in these plots: repeated measures from the same subject violate it → mixed models ([[R08 R Mixed-Effects Models]]).
- With large $n$, formal normality tests (Shapiro–Wilk) reject trivial deviations; judge by plots.

## ANOVA, t-tests, non-parametric tests
```r
t.test(rt ~ group, data = d)                  # Welch two-sample (default var.equal = FALSE)
t.test(w$face, w$house, paired = TRUE)        # paired (wide data, same subject order!)
wilcox.test(rt ~ group, data = d)             # Mann–Whitney U
wilcox.test(w$face, w$house, paired = TRUE)   # Wilcoxon signed-rank
cor.test(x, y, method = "spearman")
kruskal.test(rt ~ condition, data = d)        # non-parametric one-way
chisq.test(table(d$group, d$response))
# ANOVA
aov(rt ~ condition * group, data = d) |> summary()   # balanced designs, type I SS
car::Anova(lm(rt ~ condition * group, data = d), type = 3)   # with sum contrasts
afex::aov_ez(id = "subject", dv = "rt", data = d, within = "condition", between = "group")  # repeated measures
emmeans::emmeans(m, pairwise ~ condition, adjust = "holm")  # post-hoc comparisons
```
- **Type I vs. II vs. III sums of squares** give different F-tests in unbalanced designs: type I depends on the order of terms; type III (with sum contrasts) matches SPSS. State which you used.
- Repeated-measures ANOVA needs one value per subject × cell and assumes sphericity (`afex` reports Greenhouse–Geisser corrections); mixed models are often the better choice.
- Correct for multiple comparisons: `p.adjust(p, method = "holm")` or `"BH"` (FDR).
- Report effect sizes (`effectsize::cohens_d`, partial η²) and CIs, not only p.

## Same idea in Python and MATLAB
Python: `statsmodels.formula.api.ols("rt ~ C(condition)", d)`, `smf.glm(..., family=sm.families.Poisson())`, `scipy.stats` tests ([[Py08 SciPy Scientific Computing]]). MATLAB: `fitlm`, `fitglm`, `anova`, `ttest` ([[MAT07 MATLAB Statistics Toolbox]]) – same Wilkinson formula notation.

## In neuroscience #neuro
- **Tuning curves:** Poisson GLM of spike counts on stimulus orientation with $\cos$ and $\sin$ regressors ([[CS09 Probabilistic and Bayesian Models]], [[B4 Trigonometric Functions]]).
- **Psychometric functions:** logistic regression of "seen" on log contrast; threshold = $-\beta_0/\beta_1$.
- **fMRI's GLM** is the same linear model, fitted per voxel ([[CS12 Neuroimaging Data Analysis]]).
- **Group comparisons** of patients vs. controls with covariates (age, sex) as ANCOVA = `lm(y ~ group + age)`.
- **Log-transform RTs** or use Gamma GLMs; RT distributions are right-skewed.

## Math links #math-link
- Least squares $\hat\beta = (X^TX)^{-1}X^Ty$, design matrices → [[C1 Matrices]], [[C3 Linear Systems and Gaussian Elimination]]
- Logit and log links, odds → [[A3 Logarithms]], [[B2 Exponential Functions]]
- Distributions, tests, effect sizes → [[CS02 Probability and Statistics]]
- Maximum likelihood fitting of GLMs → [[CS04 Optimization]]

## Connections
- Data preparation → [[R05 dplyr and tidyr]]; plotting fits → [[R06 ggplot2 Visualization]]
- Repeated measures → [[R08 R Mixed-Effects Models]]
- Concepts → [[CS02 Probability and Statistics]], [[CS07 Machine Learning Fundamentals]] (regression)
- MATLAB equivalent → [[MAT07 MATLAB Statistics Toolbox]]

## Key takeaways
- Formulas: `y ~ a * b`; factors become dummies relative to the reference level.
- `lm` for continuous outcomes; `glm(binomial)` for binary, `glm(poisson)` (+ offset) for counts – coefficients on the link scale (`exp()` → odds/rate ratios).
- Check residual plots; independence violations need mixed models.
- t-tests/ANOVAs are linear models; state SS type, correction method and effect sizes.
