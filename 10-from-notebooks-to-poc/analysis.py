"""Small, testable numerical core for the Practical 10 data explorer."""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def select_features(frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Return a validated numerical feature table; never silently discard rows."""
    if len(frame) < 10:
        raise ValueError("At least 10 rows are required for this demonstration.")
    if len(frame) > 5000:
        raise ValueError("Use at most 5,000 rows in this classroom app.")
    if len(columns) < 2 or len(set(columns)) != len(columns):
        raise ValueError("Choose at least two different numerical columns.")
    if not set(columns).issubset(frame.columns):
        raise ValueError("Some selected feature columns are not in the CSV.")

    x = frame.loc[:, columns].copy()
    if not all(pd.api.types.is_numeric_dtype(dtype) for dtype in x.dtypes):
        raise ValueError("Selected features must be numerical; remove text columns.")
    if x.isna().any().any():
        raise ValueError("Selected features contain missing values; clean the CSV first.")
    if not np.isfinite(x.to_numpy(dtype=float)).all():
        raise ValueError("Selected features contain infinity or invalid numbers.")
    constant = x.columns[x.nunique(dropna=False) <= 1].tolist()
    if constant:
        raise ValueError(f"Remove constant features: {', '.join(constant)}")
    return x


def analyze(
    frame: pd.DataFrame,
    columns: list[str],
    n_clusters: int = 3,
    representation: str = "scaled",
    random_state: int = 42,
) -> dict:
    """Fit PCA for visualization and K-means in the chosen feature space.

    Labels (if available) must not be included among `columns`.
    Silhouette is measured in the same space in which K-means was fitted.
    """
    x = select_features(frame, columns)
    if not 2 <= n_clusters < len(x):
        raise ValueError("Number of clusters must be between 2 and rows - 1.")
    if representation not in {"scaled", "pca2"}:
        raise ValueError("Representation must be 'scaled' or 'pca2'.")

    scaled = StandardScaler().fit_transform(x)
    pca = PCA(n_components=2)
    scores = pca.fit_transform(scaled)
    clustering_space = scaled if representation == "scaled" else scores

    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=random_state)
    labels = kmeans.fit_predict(clustering_space)
    found_clusters = len(np.unique(labels))
    silhouette = (
        float(silhouette_score(clustering_space, labels))
        if 2 <= found_clusters < len(x)
        else None
    )
    plotted = pd.DataFrame({
        "PC1": scores[:, 0],
        "PC2": scores[:, 1],
        "cluster": labels,
    }, index=frame.index)
    return {
        "projection": plotted,
        "labels": pd.Series(labels, index=frame.index, name="cluster"),
        "counts": pd.Series(labels).value_counts().sort_index().rename("samples"),
        "variance_2d": float(pca.explained_variance_ratio_.sum()),
        "silhouette": silhouette,
        "inertia": float(kmeans.inertia_),
        "representation": representation,
    }
