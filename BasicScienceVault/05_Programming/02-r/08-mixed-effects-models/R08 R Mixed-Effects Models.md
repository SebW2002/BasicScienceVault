---
aliases: [Mixed-Effects Models, lme4, lmerTest, Random Intercepts, Random Slopes, brms, Multilevel Models]
tags: [programming, r, statistics, mixed-models, bayes, type/overview, neuro]
---
# R08 R Mixed-Effects Models

> [[R00 R Overview|↑ R]] · [[MOC-programming|Programming MOC]] · [[R08 R Mixed-Effects Models - Worksheet|✏️ Worksheet]] · [[R08 R Mixed-Effects Models - Solutions|✅ Solutions]] · [[Mistakes - R|⚠️ Mistake log]]

## Why this matters
Neuroscience data are **nested**: trials within subjects, cells within animals, sessions within participants, electrodes within subjects. Treating all trials as independent inflates significance (pseudoreplication); averaging per subject throws away information and handles unbalanced or missing data poorly. **Mixed-effects (multilevel) models** model both levels at once: **fixed effects** for the questions you ask, **random effects** for the grouping structure. R's `lme4` is the standard tool.

## Fixed and random effects
- **Fixed effects:** population-level effects you want to estimate – condition, group, stimulus intensity.
- **Random effects:** variation between units of a grouping factor (subjects, animals, items, sessions) drawn from a population; the model estimates their **variance**, not each unit as a separate parameter of interest.

$$\text{RT}_{ij} = \underbrace{\beta_0 + \beta_1 x_{ij}}_{\text{fixed}} + \underbrace{u_{0j} + u_{1j}x_{ij}}_{\text{random, subject } j} + \varepsilon_{ij},\quad u_{0j}\sim N(0,\sigma^2_{u_0}),\ \varepsilon_{ij}\sim N(0,\sigma^2)$$

## lme4 syntax: random intercepts and slopes
```r
library(lme4); library(lmerTest)        # lmerTest adds p-values (Satterthwaite df)
m1 <- lmer(rt ~ condition + (1 | subject), data = d)               # random intercepts
m2 <- lmer(rt ~ condition + (1 + condition | subject), data = d)   # + random slopes (correlated)
m3 <- lmer(rt ~ condition + (1 | subject) + (1 | item), data = d)  # crossed: subjects and stimuli
m4 <- lmer(amp ~ condition + (1 | subject/session), data = d)       # nested: sessions within subjects
mg <- glmer(correct ~ condition + (1 | subject), family = binomial, data = d)   # GLMM
```
| Term | Meaning |
|---|---|
| `(1 \| subject)` | each subject has its own baseline (intercept) |
| `(1 + condition \| subject)` | each subject also has its own condition effect, and intercept and slope can correlate |
| `(1 + condition \|\| subject)` | random slopes without the correlation (simpler) |
| `(1 \| subject) + (1 \| item)` | **crossed** random effects (every subject sees every face) |
| `(1 \| subject/session)` | **nested**: `(1 \| subject) + (1 \| subject:session)` |
- **Random slopes matter:** if subjects differ in their condition effect and you model only random intercepts, the SE of the condition effect is too small (inflated false positives; Barr et al. 2013, "keep it maximal" – within what the data support).
- A factor needs enough levels to estimate a variance (≥ 5–6 subjects; with 3 sessions, use a fixed effect).
- Use **trial-level** data; mixed models handle unbalanced designs and missing trials (MAR) naturally.

## Interpretation
```r
summary(m2)
fixef(m2); confint(m2, method = "Wald")     # or "profile"/"boot" (slower, better)
ranef(m2)$subject                           # each subject's deviations (BLUPs)
VarCorr(m2)                                 # random-effect SDs and correlations
anova(m2)                                   # F-tests (lmerTest, Satterthwaite)
emmeans::emmeans(m2, pairwise ~ condition)  # estimated marginal means, contrasts
performance::icc(m1)                         # intraclass correlation
```
- Fixed effects are read like in `lm` ([[R07 R Statistical Modelling]]), but describe the **average subject**.
- **Random-effect SD:** e.g. subject intercept SD = 0.08 s → about 95 % of subjects' baselines lie within ±0.16 s of the mean.
- **ICC** = $\sigma^2_{u_0}/(\sigma^2_{u_0}+\sigma^2)$: proportion of variance due to subjects; high ICC = trials of a subject are very similar.
- **Shrinkage:** subject estimates are pulled towards the group mean, more strongly for subjects with few or noisy trials ("partial pooling").
- **p-values:** lme4 itself gives none (df are not well defined); lmerTest uses Satterthwaite (or Kenward–Roger) approximations.

## Model comparison
```r
m0 <- lmer(rt ~ 1 + (1 | subject), data = d, REML = FALSE)
m1 <- lmer(rt ~ condition + (1 | subject), data = d, REML = FALSE)
anova(m0, m1)          # likelihood-ratio test, AIC, BIC
```
- **REML** (default) gives better variance estimates; for comparing models with different **fixed** effects, fit with **ML** (`REML = FALSE`; `anova()` refits automatically).
- Comparing random-effect structures (same fixed effects) can use REML; the LRT is conservative for variances (boundary at 0).
- **AIC/BIC:** lower is better; BIC penalises complexity more.
- **Convergence warnings / singular fits** (`isSingular(m)`: a variance estimated as 0 or correlation ±1) mean the random structure is too complex for the data: simplify (remove correlations, then slopes with ~0 variance), rescale predictors, or try another optimiser (`control = lmerControl(optimizer = "bobyqa")`).

## A short introduction to Bayesian models with brms
**brms** fits (generalised) multilevel models with the **same formula syntax**, using Stan (MCMC sampling) in the background ([[CS09 Probabilistic and Bayesian Models]]).
```r
library(brms)
b <- brm(rt ~ condition + (1 + condition | subject), data = d,
         family = lognormal(),                       # RT distribution
         prior = c(prior(normal(0, 0.5), class = "b"),
                   prior(exponential(2), class = "sd")),
         chains = 4, iter = 2000, seed = 1, cores = 4)
summary(b)            # posterior means, 95 % credible intervals, Rhat, ESS
plot(b); pp_check(b)  # trace plots, posterior predictive check
hypothesis(b, "conditionface < 0")    # posterior probability of a directional hypothesis
```
- **Priors** encode prior knowledge or regularise (weakly informative priors stabilise complex random structures that fail in lme4).
- The result is a **posterior distribution** for every parameter: "95 % credible interval" = the parameter lies in it with 95 % posterior probability (given model and prior).
- **Check convergence:** $\hat R\le1.01$, enough effective samples (ESS), no divergent transitions.
- Flexible families (lognormal, shifted lognormal, Wiener diffusion for RT + accuracy, zero-inflated counts).
- Bayes factors: `BayesFactor` package, or `brms` + bridge sampling ([[R09 R Neuroscience Packages]]).

## Same idea in Python and MATLAB
Python: `statsmodels.formula.api.mixedlm` (more limited), `pymer4` (wraps lme4), `bambi` (brms-like, PyMC). MATLAB: `fitlme`, `fitglme` with the same `(1 | subject)` syntax ([[MAT07 MATLAB Statistics Toolbox]]).

## In neuroscience #neuro
- **Trial-level RT/accuracy** with subjects and stimuli as crossed random effects (faces, words).
- **Single-unit studies:** cells nested in animals – `(1 | animal/cell)`; treating 300 cells from 4 mice as independent overstates evidence (Aarts et al. 2014).
- **ERP amplitudes** with random effects for subject (and electrode), single-trial EEG analyses.
- **Longitudinal studies:** sessions within patients, random slopes for time (individual trajectories).
- **Spike counts:** Poisson GLMMs with random effects for neuron (`glmer(..., family = poisson)`).

## Math links #math-link
- Linear model in matrix form $y = X\beta + Zu + \varepsilon$ → [[C1 Matrices]]
- Variances, normal distributions, likelihood, ML vs. REML → [[CS02 Probability and Statistics]]
- Priors and posteriors → [[CS09 Probabilistic and Bayesian Models]]
- Log-likelihood ratio tests → [[A3 Logarithms]]

## Connections
- Linear models and GLMs → [[R07 R Statistical Modelling]]
- Long-format data → [[R05 dplyr and tidyr]]
- Pseudoreplication, unit of inference → [[CS02 Probability and Statistics]], [[CS06 Data Science Workflow]]
- Bayesian concepts → [[CS09 Probabilistic and Bayesian Models]]
- MATLAB `fitlme` → [[MAT07 MATLAB Statistics Toolbox]]

## Key takeaways
- Fixed = effects of interest; random = variation between grouping units (subjects, items, animals).
- `(1 | subject)` intercepts, `(1 + x | subject)` slopes; crossed `+ (1 | item)`, nested `(1 | a/b)`.
- Use lmerTest for p-values; compare fixed effects with ML-fitted models (`anova`), check singular fits.
- brms: same formulas, priors, posteriors; check $\hat R$, ESS and posterior predictive plots.
