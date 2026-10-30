# BasicScienceVault – R packages for all R topics (R01–R11)
# Run once in R or RStudio:  source("setup/install_r_packages.R")

cran <- c(
  # data handling and plotting (R02–R06)
  "tidyverse", "readxl", "writexl", "haven", "arrow", "here", "janitor",
  "patchwork", "ggbeeswarm", "svglite", "viridis",
  # statistics (R07–R08)
  "lme4", "lmerTest", "emmeans", "afex", "car", "performance", "effectsize",
  "Hmisc", "modelsummary", "BayesFactor", "brms", "psych", "psychometric",
  # neuroscience and file formats (R09)
  "signal", "oro.nifti", "neurobase", "fmri", "reticulate", "R.matlab", "hdf5r",
  # reports and reproducibility (R10–R11)
  "rmarkdown", "knitr", "quarto", "gt", "renv", "testthat", "usethis", "sessioninfo",
  # editor support (VS Code R extension)
  "languageserver"
)
missing <- setdiff(cran, rownames(installed.packages()))
if (length(missing) > 0) install.packages(missing)

# Bioconductor: rhdf5 (HDF5, MATLAB v7.3 files)
if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager")
if (!requireNamespace("rhdf5", quietly = TRUE)) BiocManager::install("rhdf5", update = FALSE)

# eegUtils is installed from r-universe (not CRAN)
if (!requireNamespace("eegUtils", quietly = TRUE)) {
  install.packages("eegUtils", repos = c("https://craddm.r-universe.dev", "https://cloud.r-project.org"))
}

# Check
pkgs <- c(cran, "rhdf5", "eegUtils")
ok <- vapply(pkgs, requireNamespace, logical(1), quietly = TRUE)
cat("\nInstalled:", sum(ok), "of", length(ok), "packages\n")
if (any(!ok)) cat("Missing:", paste(pkgs[!ok], collapse = ", "), "\n")
