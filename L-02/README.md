# Lab 02 — Processing Data of Different Modalities

Student-facing laboratory assignment for Practical 06–07. Independent work; no solutions.

## Files

- `Lab 02. Processing Data of Different Modalities.ipynb` — assignment notebook.
- `data/` — **four real-source datasets** in five files, shipped for offline use.
- `SOURCES_AND_DATA_DICTIONARY.md` — provenance, units, limitations and rights notes.
- `SHA256SUMS.txt` — file hashes for reproducibility.
- `rebuild_snapshots.py` — optional instructor-only instructions/code to reproduce snapshots from installed Python library datasets.

## Student workflow

1. Open the notebook from the extracted package root.
2. Select one option from Group A (Images/Text) and one from Group B (Time Series/Graphs).
3. Finish only the two selected sections, then the short comparison and conclusion.
4. Restart the Python kernel and run all cells before submission.

### Python requirements

Common: `numpy`, `pandas`, `matplotlib`, `ipykernel`.
- Text option: `scikit-learn`.
- Graph option: `networkx`.

The other libraries used for **snapshot preparation** (`gensim`, `statsmodels`, and `scikit-learn` for digit extraction) are **not** needed at student runtime.

**Important rights note:** The movie-review text is an actual academic corpus excerpt, not synthetic. See the rights note in `SOURCES_AND_DATA_DICTIONARY.md` **before uploading the dataset to a public GitHub repository**. This package is intended for classroom use.
