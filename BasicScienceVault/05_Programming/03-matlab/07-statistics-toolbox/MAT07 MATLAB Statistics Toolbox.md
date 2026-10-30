---
aliases: [MATLAB Statistics, fitlm, fitglm, fitlme, ttest, anova in MATLAB, signrank, Permutation Test]
tags: [programming, matlab, statistics, regression, mixed-models, permutation, type/overview, neuro]
---
# MAT07 MATLAB Statistics Toolbox

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT07 MATLAB Statistics Toolbox - Worksheet|✏️ Worksheet]] · [[MAT07 MATLAB Statistics Toolbox - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
Many labs do their statistics where their data already are – in MATLAB. The **Statistics and Machine Learning Toolbox** offers linear, generalised and mixed models with the same formula notation as R ([[R07 R Statistical Modelling]]), the classical tests, and the building blocks for **permutation tests**, which are the standard for EEG/MEG cluster statistics (FieldTrip). Concepts → [[CS02 Probability and Statistics]].

## Models: fitlm, fitglm, fitlme
All three take a **table** and a **Wilkinson formula** (`y ~ x1 + x2`, `*` for interactions, `(1|subject)` for random effects):
```matlab
T.condition = categorical(T.condition);          % factors must be categorical
mdl = fitlm(T, "rt ~ condition + age")            % linear model
mdl.Coefficients                                  % Estimate, SE, tStat, pValue
coefCI(mdl); mdl.Rsquared.Ordinary
anova(mdl)                                        % F-tests per term
plotResiduals(mdl, "fitted"); plotResiduals(mdl, "probability")   % diagnostics
predict(mdl, newT)

g = fitglm(T, "correct ~ contrast", "Distribution", "binomial");  % logistic
p = fitglm(U, "spikes ~ stimulus", "Distribution", "poisson", "Offset", log(U.duration));

lme = fitlme(T, "rt ~ condition + (1 + condition | subject)");     % mixed model
lme.Coefficients; randomEffects(lme); anova(lme)
compare(lme_small, lme)                           % likelihood-ratio test (fit with "FitMethod","ML")
glme = fitglme(T, "correct ~ condition + (1|subject)", "Distribution", "binomial");
```
- The first category of a `categorical` is the **reference level** (`reordercats` changes the order) – coefficients are differences from it, as in R.
- `fitlme` defaults to ML fitting; `"FitMethod", "REML"` for REML. Use ML when comparing fixed effects with `compare` ([[R08 R Mixed-Effects Models]]).
- `fitlme` p-values use residual df by default; `"DFMethod", "satterthwaite"` in `anova`/`coefTest` is more accurate.

## Classical tests: ttest, anova, signrank
```matlab
[h, p, ci, stats] = ttest(diff_scores)            % one-sample / paired (ttest(x, y))
[h, p, ci, stats] = ttest(oddball, standard)      % paired: same subject order!
[h, p, ci, stats] = ttest2(patients, controls, "Vartype", "unequal")   % Welch
p = signrank(oddball, standard)                    % Wilcoxon signed-rank (paired, non-parametric)
p = ranksum(patients, controls)                    % Mann–Whitney U (independent)
[p, tbl, stats] = anova1(rt, group)                % one-way ANOVA
[p, tbl] = anovan(rt, {cond, group}, "model", "interaction", "varnames", ["cond" "group"])
c = multcompare(stats, "CType", "bonferroni")      % post-hoc comparisons
[r, p] = corr(x, y, "Type", "Spearman")
```
- `h` is 1 if the null is rejected at α = 0.05 – report **p, the statistic, df (`stats.df`) and the CI**, not only `h`.
- `ttest2` defaults to **equal variances** (Student) – unlike R's `t.test` (Welch). Set `"Vartype", "unequal"`.
- Repeated-measures ANOVA: `fitrm` + `ranova` (with sphericity corrections), or better a mixed model.
- Multiple comparisons: `mafdr` (Bioinformatics Toolbox) or implement Benjamini–Hochberg; `bonferroni`/`holm` by hand.

## Permutation tests
When assumptions are doubtful, or the statistic is complex (cluster mass, decoding accuracy), build the null distribution by **shuffling** what the null hypothesis says is exchangeable:
```matlab
rng(42)                                          % reproducible
d = oddball - standard;                          % paired differences, one per subject
obs = mean(d);
nPerm = 10000; null = zeros(nPerm, 1);
for k = 1:nPerm
    signs = sign(rand(size(d)) - 0.5);           % paired design: randomly flip signs
    null(k) = mean(signs .* d);
end
p = (sum(abs(null) >= abs(obs)) + 1) / (nPerm + 1)   % two-sided, includes the observed value
```
- **Independent groups:** shuffle group labels (`randperm`) and recompute the statistic.
- **Paired data:** flip the sign of each subject's difference (exchangeable under H0).
- Use the `+1` correction so p is never exactly 0; with 10,000 permutations the smallest possible p is ≈ 1e-4.
- **Cluster-based permutation tests** (Maris & Oostenveld 2007) control the family-wise error over channels × time × frequency by comparing the observed cluster mass with the permutation distribution of the **maximum** cluster mass – implemented in FieldTrip (`ft_timelockstatistics` with `cfg.method = 'montecarlo'`, `cfg.correctm = 'cluster'`) ([[MAT10 MATLAB Neuroscience Toolboxes]], [[CS12 Neuroimaging Data Analysis]]).
- Also: `bootci(2000, @mean, x)` for bootstrap confidence intervals.

## Same idea in Python and R
| MATLAB | R | Python |
|---|---|---|
| `fitlm(T, "y ~ x")` | `lm(y ~ x, data)` | `smf.ols("y ~ x", df)` |
| `fitglm(..., "Distribution", "poisson")` | `glm(family = poisson)` | `smf.glm(..., family=Poisson())` |
| `fitlme(T, "y ~ x + (1\|s)")` | `lmer(y ~ x + (1\|s))` | `smf.mixedlm` |
| `ttest2` (Student by default) | `t.test` (Welch by default) | `stats.ttest_ind` (Student by default) |
| `signrank`, `ranksum` | `wilcox.test` | `stats.wilcoxon`, `mannwhitneyu` |
| permutation loop | `replicate` / `coin` | `stats.permutation_test` |
→ [[R07 R Statistical Modelling]], [[R08 R Mixed-Effects Models]], [[Py08 SciPy Scientific Computing]]

## In neuroscience #neuro
- **ERP amplitude differences** between conditions within subjects: paired `ttest` or `signrank` on subject means; mixed models for trial-level data.
- **EEG/MEG sensor-level statistics** over channels × time: cluster-based permutation tests (FieldTrip) instead of thousands of uncorrected t-tests.
- **Spike counts:** Poisson `fitglm` with stimulus regressors; check dispersion.
- **Decoding accuracy significance:** permutation of labels (rerun the cross-validation for each permutation).

## Math links #math-link
- Least squares and design matrices → [[C3 Linear Systems and Gaussian Elimination]]
- Distributions, t/F statistics, multiple comparisons → [[CS02 Probability and Statistics]]
- Log/logit links → [[A3 Logarithms]], [[B2 Exponential Functions]]
- Counting permutations ($2^n$ sign flips, $\binom{n}{k}$ label assignments) → [[A6 Binomial Formulas and Theorem]], [[A7 Sums Products and Factorials]]

## Connections
- Tables and categoricals → [[MAT04 MATLAB Data Import and Files]]
- Models in R (more features) → [[R07 R Statistical Modelling]], [[R08 R Mixed-Effects Models]]
- Cluster statistics → [[MAT10 MATLAB Neuroscience Toolboxes]] (FieldTrip), [[CS12 Neuroimaging Data Analysis]]
- Concepts → [[CS02 Probability and Statistics]]

## Key takeaways
- `fitlm`/`fitglm`/`fitlme` on tables with formulas; categoricals set reference levels.
- `ttest` (paired/one-sample), `ttest2` (Student by default – set `"Vartype", "unequal"`), `signrank`/`ranksum`, `anova1`/`anovan` + `multcompare`.
- Permutation tests: shuffle labels or flip signs, seed `rng`, p = (count + 1)/(nPerm + 1); clusters for channels × time.
