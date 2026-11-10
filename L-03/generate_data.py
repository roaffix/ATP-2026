"""Recreate the two *real-data* CSVs from the bundled sklearn WDBC dataset.

The only generated values are course `sample_id` keys; measurements and labels come
from load_breast_cancer. Does not download data from the internet.
"""
from pathlib import Path
import pandas as pd
from sklearn.datasets import load_breast_cancer

out_dir = Path(__file__).resolve().parent / "data"
out_dir.mkdir(parents=True, exist_ok=True)
data = load_breast_cancer(as_frame=True)
keys = [f"S{i:04d}" for i in range(1, len(data.data) + 1)]
measurements = data.data.reset_index(drop=True).copy()
measurements.insert(0, "sample_id", keys)
reference = pd.DataFrame({
    "sample_id": keys,
    "diagnosis": [str(data.target_names[int(i)]) for i in data.target.to_numpy()],
})
measurements.to_csv(out_dir / "measurements.csv", index=False)
reference.to_csv(out_dir / "reference_labels.csv", index=False)
print("Wrote", len(measurements), "observations to", out_dir)
