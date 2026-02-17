#%%

import pandas as pd

df = pd.read_csv("data/dataset.csv")

df.head()


# %%
for i in df.columns:
    print(i)

#%%
features = {
    "1.a_idade": "idade",
    "1.b_genero": "genero",
    "1.c_cor/raca/etnia": "etnia",
    "1.d_pcd": "pcd",
    "1.i.1_uf_onde_mora": "uf_onde_mora",
    "2.f_cargo_atual": "cargo_atual",
    "2.g_nivel": "nivel",
    "2.i_tempo_de_experiencia_em_dados": "tempo_de_experiencia_em_dados",
    "2.j_tempo_de_experiencia_em_ti": "tempo_de_experiencia_em_ti",
    "2.l.4_Flexibilidade de trabalho remoto": "trabalho remoto",
}

target = "2.h_faixa_salarial"

columns = list(features.keys()) + [target]

df = df[columns].copy()
df.rename(columns=features, inplace=True)

df


# %%
