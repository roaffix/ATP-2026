"""A deliberately small data explorer. Start with: streamlit run app.py"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from analysis import analyze


st.set_page_config(page_title="Wine Data Explorer", layout="wide")
st.title("Wine Data Explorer")
st.caption("Practical 10 · PCA visualization and K-means · No labels used to fit clusters")


@st.cache_data
def load_demo_data() -> pd.DataFrame:
    path = Path(__file__).resolve().parent / "data" / "wine_features.csv"
    return pd.read_csv(path)


uploaded = st.sidebar.file_uploader("Optional: upload your own CSV", type=["csv"])
if uploaded is None:
    frame = load_demo_data()
    st.sidebar.caption("Using the included UCI Wine measurements.")
else:
    if uploaded.size > 3_000_000:
        st.error("Please upload a CSV smaller than 3 MB.")
        st.stop()
    try:
        frame = pd.read_csv(uploaded)
    except (pd.errors.ParserError, UnicodeDecodeError, ValueError) as exc:
        st.error(f"Could not read the CSV: {exc}")
        st.stop()

numeric_cols = frame.select_dtypes(include="number").columns.tolist()
excluded_by_default = {"target", "label", "class", "class_label", "id"}
default_cols = [c for c in numeric_cols if c.lower() not in excluded_by_default]

if len(numeric_cols) < 2:
    st.error("This CSV needs at least two numerical columns.")
    st.stop()

columns = st.sidebar.multiselect("Numerical features", numeric_cols, default=default_cols)
st.sidebar.caption("Do not select identifiers or known target/class labels as features.")
representation_title = st.sidebar.radio(
    "K-means clustering space",
    ("All standardized features", "First two PCA components"),
)
representation = "scaled" if representation_title.startswith("All") else "pca2"
n_clusters = st.sidebar.slider("Number of clusters (k)", 2, 8, 3)

if len(columns) < 2:
    st.warning("Select at least two numerical features.")
    st.stop()

try:
    result = analyze(frame, columns, n_clusters=n_clusters, representation=representation)
except (ValueError, TypeError) as exc:
    st.error(f"Cannot analyze this CSV: {exc}")
    st.stop()

left, middle, right = st.columns(3)
left.metric("Rows", len(frame))
middle.metric("Features used", len(columns))
right.metric("Variance shown in PCA plot", f"{result['variance_2d']:.1%}")

st.subheader("Clusters in the PCA view")
fig, ax = plt.subplots(figsize=(8, 4.6))
plot_data = result["projection"]
ax.scatter(plot_data["PC1"], plot_data["PC2"], c=plot_data["cluster"],
           cmap="tab10", s=32, alpha=0.85)
ax.set(xlabel="PC1", ylabel="PC2")
ax.grid(alpha=0.2)
st.pyplot(fig)
plt.close(fig)

score = result["silhouette"]
st.write(f"Silhouette in the clustering space: **{score:.3f}**" if score is not None
         else "Silhouette: unavailable (fewer than two nonempty clusters).")
st.caption("The scatter plot always shows PCA coordinates. When clustering uses all features, "
           "the plot is only a 2D view of that higher-dimensional partition. "
           "Silhouette values across different spaces are not directly comparable.")

st.subheader("Cluster sizes")
st.dataframe(result["counts"].rename_axis("cluster").to_frame(), use_container_width=True)

st.subheader("Data preview")
st.dataframe(frame.head(8), use_container_width=True)

export = frame.reset_index(drop=True).copy()
export["cluster"] = result["labels"].to_numpy()
st.download_button(
    "Download CSV with cluster IDs",
    data=export.to_csv(index=False).encode("utf-8"),
    file_name="clustered_data.csv",
    mime="text/csv",
)
