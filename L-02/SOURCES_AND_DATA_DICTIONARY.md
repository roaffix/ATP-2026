# Sources and data dictionary

All four datasets are **derived from genuine observations or published research corpora**.
No synthetic records were added. Files are shipped with the notebook for offline use.
The choice to make small, fixed snapshots does **not** make the observations synthetic.

## Group A — Images: handwritten digits

- **Files:** `data/handwritten_digits.npz`, arrays `images` (1,797 × 8 × 8, uint8) and `labels` (1,797).
- **Unit:** one handwritten digit image, reduced to 8×8 block counts (0–16), not an original photo.
- **Primary source:** UCI Optical Recognition of Handwritten Digits, E. Alpaydin and C. Kaynak (1998), https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits, DOI https://doi.org/10.24432/C50P49.
- **Distribution used:** `sklearn.datasets.load_digits()`; a copy of the UCI test subset, not the complete 5,620-record UCI release. https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html
- **License:** UCI declares CC BY 4.0; preserve source attribution.
- **Limitations:** historical handwriting from a limited set of writers, already transformed from 32×32 to 8×8. Labels are for evaluating comparisons only.

## Group A — Text: movie-review sentiment snippets

- **File:** `data/movie_review_snippets.csv`, columns `snippet_id`, `text`, `sentiment` (`pos` / `neg`).
- **Unit:** one real short movie-review sentence/snippet; 200 excerpts, 100 with each label.
- **Original research:** Bo Pang and Lillian Lee, *Seeing Stars*, ACL 2005; public release at https://www.cs.cornell.edu/people/pabo/movie-review-data/.
- **Packaged copy:** `gensim/test/test_data/pang_lee_polarity.cor` (Gensim library test fixture), decoded with Windows-1252 and written as UTF-8 CSV; label prefix removed and IDs added. The Gensim fixture is a **small subset**, not the full 10,662-sentence release.
- **Rights:** original snippets are third-party review text. The academic corpus is publicly distributed for research. Its primary Cornell page does not make an explicit CC BY declaration for this exact Gensim fixture. Please verify the relevant distribution terms before placing this text collection in a **public** repository; attribution alone does not resolve underlying authors' rights. A separate distribution labels a related Pang–Lee movie-review dataset CC BY 4.0, but that must not be automatically assumed to govern this fixture.
- **Limitations:** balanced curated subset; source labels represent sentiment judgments, not a universal ground truth. Sentences can be ambiguous or depend on context; no date, reviewer identity, or movie metadata is supplied.

## Group B — Time series: Mauna Loa atmospheric CO₂

- **File:** `data/mauna_loa_co2_weekly.csv`, `date` (YYYY-MM-DD) and `co2_ppm` (weekly concentration; blank when unavailable).
- **Unit:** a week-indexed observation at Mauna Loa, Hawaii.
- **Source data:** the Mauna Loa CO₂ record compiled from Scripps/Keeling observations; **snapshot source:** `statsmodels.datasets.co2`, https://www.statsmodels.org/stable/datasets/generated/co2.html.
- **Coverage:** 1958-03-29 to 2001-12-29, 2,284 weekly index positions, 2,225 recorded measurements and 59 missing values (do not silently fill zeros).
- **Source citation:** Keeling, C.D. and T.P. Whorf (2004), Atmospheric CO₂ concentrations derived from flask air samples, Carbon Dioxide Information Analysis Center, Oak Ridge National Laboratory.
- **Rights:** statsmodels documentation describes the dataset as **public domain**.
- **Limitations:** historical snapshot, not a live/current CO₂ dataset. Changes of atmospheric concentration over time do not establish a causal attribution from this single series.

## Group B — Graph: Zachary's Karate Club

- **Files:** `data/karate_edges.csv` (`node_a`, `node_b`, `interaction_contexts`) and `data/karate_members.csv` (`node_id`, `club_after_split`).
- **Unit:** a person (node), or an observed social relation (undirected edge), in a karate club.
- **Original study:** W. W. Zachary (1977), *An Information Flow Model for Conflict and Fission in Small Groups*, Journal of Anthropological Research 33, 452–473.
- **Distribution used:** `networkx.karate_club_graph()`, https://networkx.org/documentation/stable/reference/generated/networkx.generators.social.karate_club_graph.html. Re-exported deterministically to CSV with an explicit complete node list.
- **Coverage:** 34 members and 78 undirected edges.
- **Important:** `interaction_contexts` measures strength/contexts of interaction, **not** a travel-time cost. `club_after_split` is an outcome observed after the club divided, **not** a node coordinate or a pre-existing group assignment.
- **Limitations:** a small historical observed social network; collected relations are subject to the original study's definitions and measurement.

## How to use the files

- Every file is a fixed snapshot. Load only the two sources you select in the notebook.
- No outside downloads are needed for student execution.
- The package also provides `rebuild_snapshots.py` to document how snapshots were prepared from library copies; **students do not need to run it**.
- For integrity checks, see `SHA256SUMS.txt` (SHA-256 hashes of the exact files in this package).
