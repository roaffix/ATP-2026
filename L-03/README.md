# Lab 03 — Dimensionality Reduction and Clustering

Individual graded laboratory after Practical 08 (PCA/LDA) and Practical 09 (clustering).

## Files

- `Lab 03. Dimensionality Reduction and Clustering.ipynb`: student-facing notebook, no solutions.
- `data/measurements.csv`: 569 observations × 30 numeric features, with a course-assigned `sample_id`.
- `data/reference_labels.csv`: separate reference diagnosis categories; consult only in notebook Section 5.
- `SOURCES_AND_DATA_DICTIONARY.md`: data provenance, license, limitations, column meaning.
- `generate_data.py`: recreate both CSV snapshots using the built-in scikit-learn data loader.
- `requirements.txt`: Python dependencies.

## Run

From the extracted directory (working directory must contain `data/`):

```bash
python -m pip install -r requirements.txt
jupyter lab
```

Open the `.ipynb` file and complete the blank solution cells. The starter cells are runnable without
network access; full analysis is intentionally left to students.

The data are real, not synthetic. They were repackaged from the scikit-learn copy of UCI WDBC.
They are for education in numerical data analysis, **not for diagnosis or clinical use**.
