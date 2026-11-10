# Source and data dictionary

## Source

**Breast Cancer Wisconsin (Diagnostic)** — UCI Machine Learning Repository.

> Wolberg, W., Mangasarian, O., Street, N., & Street, W. (1993). *Breast Cancer Wisconsin (Diagnostic)* [Dataset].
> UCI Machine Learning Repository. https://doi.org/10.24432/C5DW2B

Official dataset: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic  
UCI dataset identifier: 17  
Distribution used to create this package: `sklearn.datasets.load_breast_cancer(as_frame=True)`  
scikit-learn version used for packaging: `1.8.0`  
UCI dataset license: **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Give attribution when redistributing.

This is a historical research collection of features derived from digitized fine-needle aspirate images
of breast masses. It is not a contemporary or representative patient sample. Observations must not
be interpreted as independent patients without source evidence. There is no basis here for clinical
conclusions or deployment.

## Contents and preparation

- **569 rows**, **30 numeric features**, no missing values in the scikit-learn distribution.
- The feature matrix and diagnosis categories were exported unchanged in value; only a synthetic,
  stable **course row key** (`sample_id`) was added for alignment. The original source ID was **not**
  included in the scikit-learn loader and has **not** been reconstructed.
- `data/measurements.csv`: `sample_id` plus 30 numeric predictors. It intentionally contains no diagnosis.
- `data/reference_labels.csv`: `sample_id`, `diagnosis`. `diagnosis` is `malignant` for 212 records
  and `benign` for 357 records. Never use `diagnosis` to fit the unsupervised representation or clustering.
- The original feature groups reflect ten measured characteristics (radius, texture, perimeter, area,
  smoothness, compactness, concavity, concave points, symmetry and fractal dimension), summarized in
  three ways: mean, standard error, and worst. See UCI for exact feature definitions and measurement context.

## Columns in `measurements.csv`

`sample_id`: a newly generated key `S0001`...`S0569`, aligned by original scikit-learn row order.
It is **not** an original UCI case identifier and must not be included in numerical features.

The 30 numeric feature columns, retaining their scikit-learn column names:

- `mean radius`
- `mean texture`
- `mean perimeter`
- `mean area`
- `mean smoothness`
- `mean compactness`
- `mean concavity`
- `mean concave points`
- `mean symmetry`
- `mean fractal dimension`
- `radius error`
- `texture error`
- `perimeter error`
- `area error`
- `smoothness error`
- `compactness error`
- `concavity error`
- `concave points error`
- `symmetry error`
- `fractal dimension error`
- `worst radius`
- `worst texture`
- `worst perimeter`
- `worst area`
- `worst smoothness`
- `worst compactness`
- `worst concavity`
- `worst concave points`
- `worst symmetry`
- `worst fractal dimension`

## Data integrity checksums (SHA-256)

Checksums refer to the two shipped CSV files. `generate_data.py` recreates the same files from the
installed scikit-learn dataset (file hashes can differ across platforms/serialization versions).

- `measurements.csv`: `2780d88cd175ced1f053cc485f12144ec610e6e7f3e2d4dded76fa2051476080`
- `reference_labels.csv`: `eca47e6b7820981acd0237abdfd16b070058f194435668607f2d31566f9aef5e`

## Limits of the exercise

- No image pixels or clinical history are provided in this package: the features are already computed.
- Diagnosis labels are for **retrospective comparison**, not a definition of the number of naturally
  occurring clusters.
- A cluster-label agreement metric is not diagnostic accuracy, clinical validity, or evidence of utility.
- No missingness-imputation exercise is needed on this particular dataset.
