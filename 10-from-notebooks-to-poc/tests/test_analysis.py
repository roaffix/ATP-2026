"""Run from the project directory: python -m pytest -q"""
import numpy as np
import pandas as pd
import pytest
from sklearn.datasets import load_wine

from analysis import analyze, select_features


@pytest.fixture
def data():
    return load_wine(as_frame=True).data


def test_analysis_shapes_and_determinism(data):
    a = analyze(data, data.columns.tolist(), n_clusters=3, representation="scaled")
    b = analyze(data, data.columns.tolist(), n_clusters=3, representation="scaled")
    assert a["projection"].shape == (178, 3)
    assert a["counts"].sum() == 178
    assert np.array_equal(a["labels"].to_numpy(), b["labels"].to_numpy())
    assert 0 < a["variance_2d"] <= 1


def test_alternative_representation(data):
    r = analyze(data, data.columns.tolist(), n_clusters=3, representation="pca2")
    assert set(r["labels"].unique()) <= {0, 1, 2}
    assert r["silhouette"] is not None


def test_missing_value_is_reported(data):
    broken = data.copy()
    broken.iloc[0, 0] = np.nan
    with pytest.raises(ValueError, match="missing values"):
        select_features(broken, broken.columns.tolist())


def test_constant_column_is_reported(data):
    broken = data.copy()
    broken["constant"] = 1
    with pytest.raises(ValueError, match="constant"):
        select_features(broken, broken.columns.tolist())


def test_non_numeric_and_invalid_cluster_count(data):
    broken = data.copy()
    broken["comment"] = "test"
    with pytest.raises(ValueError, match="numerical"):
        select_features(broken, ["alcohol", "comment"])
    with pytest.raises(ValueError, match="Number of clusters"):
        analyze(data, ["alcohol", "malic_acid"], n_clusters=178)


def test_two_features_and_ten_rows(data):
    small = data.loc[:, ["alcohol", "malic_acid"]].head(10)
    result = analyze(small, small.columns.tolist(), n_clusters=2)
    assert len(result["labels"]) == 10
