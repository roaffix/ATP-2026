# Practical 10 — From Notebook to MVP/POC

The included example is a small **Streamlit Wine Data Explorer**. Students reuse concepts from Practicals 08–09 (standardization, PCA, K-means, silhouette), but focus on separating analysis code from UI, validating inputs, reproducibility, and providing a usable application.

## Files

```text
Practical 10. From Notebook to MVP and POC.ipynb  guided 70-minute session
app.py                                            Streamlit user interface
analysis.py                                       reusable data-processing functions
data/wine_features.csv                            included 178 × 13 real sample measurements
data/invalid_example.csv                          20-row teaching fixture with one inserted missing value
tests/test_analysis.py                            smoke / edge-case tests
requirements.txt                                  Python dependencies
README.md                                         this guide
```

## Quick start

From the unzipped folder:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS / Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python -m streamlit run app.py
```

Streamlit will print a local address (typically `http://localhost:8501`). Keep the terminal running while using the app. To exit, press `Ctrl+C`.

To open the tutorial notebook, run `jupyter notebook` from the same folder and open its `.ipynb` file. The notebook does **not** start a Streamlit server; its code cells can be run top-to-bottom separately.

## What students should do in class

1. Run the small notebook analysis and confirm its output.
2. Compare the notebook's one-off code with the testable `analyze()` function in `analysis.py`.
3. Use the app to vary K-means parameters and choose 13D or 2D clustering space.
4. Add one UI feature (cluster-size chart) and test what happens with invalid input.

## Data source and limitations

- Dataset: **UCI Wine**, 178 samples, 13 chemical measurements, 3 known cultivar categories. The included CSV has **only the 13 input features**; cultivar labels are deliberately omitted, so no labels are used to fit PCA/K-means.
- Original source: https://archive.ics.uci.edu/dataset/109/wine
- scikit-learn data loader: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html
- The CSV was exported from the packaged `sklearn.datasets.load_wine(as_frame=True).data` with the feature names preserved. It is supplied offline to avoid network access during class.
- This is a small research dataset for learning, not a representative sample of all wines. K-means clusters are *not* equivalent to the three known cultivars, nor do silhouette and PCA variance prove scientific validity.
- `data/invalid_example.csv` is a deliberately altered 20-row subset for testing validation; it is **not** an additional independent research dataset.
- Uploaded CSVs should have numerical features. The app makes no claim to handle arbitrary dirty data: it rejects missing, non-finite, or constant selected features; large inputs are capped for classroom use. Review uploaded CSVs for target leakage: do not include class labels as clustering features.

## Streamlit reference

- Starting an app: https://docs.streamlit.io/get-started/fundamentals/main-concepts
- Widgets and reruns: https://docs.streamlit.io/develop/concepts/architecture/widget-behavior
- App testing: https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest

## Instructor note

The app is a small, working **proof of concept**, not a production deployment: no authentication, service monitoring, cloud hosting, or guarantees for uploaded data. Lab 04 asks students to build an independent MVP/POC with their own scope.
