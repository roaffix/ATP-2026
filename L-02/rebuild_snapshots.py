from pathlib import Path
import hashlib, json, re, zipfile, sys
import numpy as np
import pandas as pd
import nbformat as nbf
import sklearn, statsmodels.api as sm, networkx as nx, gensim
from textwrap import dedent

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'; DATA.mkdir(parents=True,exist_ok=True)

# A1 - real digit scans, curated by UCI; exact sklearn copy of historical test set
from sklearn.datasets import load_digits
digits=load_digits()
np.savez_compressed(DATA/'handwritten_digits.npz',images=digits.images.astype(np.uint8),labels=digits.target.astype(np.uint8))

# A2 - text excerpt shipped as a Gensim test corpus, originally Pang & Lee sentiment snippets
source=Path(gensim.__file__).parent/'test'/'test_data'/'pang_lee_polarity.cor'
rows=[]
for i,line in enumerate(source.read_text(encoding='cp1252').splitlines()):
    label,text=line.split(' ',1)
    rows.append({'snippet_id':i,'text':text.strip(),'sentiment':label.removeprefix('__label__')})
review_df=pd.DataFrame(rows)
review_df.to_csv(DATA/'movie_review_snippets.csv',index=False,encoding='utf-8')

# B1 - actual atmospheric CO2 weekly measurements from packaged statsmodels snapshot
co2=sm.datasets.co2.load_pandas().data.reset_index().rename(columns={'index':'date','co2':'co2_ppm'})
co2['date']=pd.to_datetime(co2['date']).dt.strftime('%Y-%m-%d')
co2.to_csv(DATA/'mauna_loa_co2_weekly.csv', index=False, na_rep='', float_format='%.3f')

# B2 - observed Zachary Karate Club network from NetworkX (1977)
G=nx.karate_club_graph()
edges=pd.DataFrame([{'node_a':min(a,b),'node_b':max(a,b),'interaction_contexts':int(attrs['weight'])}
  for a,b,attrs in G.edges(data=True)]).sort_values(['node_a','node_b']).reset_index(drop=True)
edges.to_csv(DATA/'karate_edges.csv',index=False)
nodes=pd.DataFrame([{'node_id':int(n),'club_after_split':attrs['club']}
 for n,attrs in G.nodes(data=True)]).sort_values('node_id')
nodes.to_csv(DATA/'karate_members.csv',index=False)

assert digits.images.shape==(1797,8,8)
assert set(review_df.sentiment)=={'pos','neg'} and len(review_df)==200
assert len(co2)==2284 and co2.co2_ppm.isna().sum()==59
assert G.number_of_nodes()==34 and G.number_of_edges()==78 and nx.has_bridges(G)


print('Rebuilt all 5 source snapshot files in', DATA)
