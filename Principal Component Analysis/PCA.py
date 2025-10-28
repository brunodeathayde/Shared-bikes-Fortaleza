import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

df = pd.read_excel("neighborhoods.xlsx", skiprows=1, header=None)
df = df.select_dtypes(include=[np.number])

scaler = MinMaxScaler()
x = scaler.fit_transform(df.values)

y = x[:, 0:1]              
insumos = x[:, 1:]
insumos_inv = 1 - insumos
x_pca = np.hstack([y, insumos_inv])

pca = PCA(n_components=1)
scores = pca.fit_transform(x_pca).ravel()

scores_norm = (scores - scores.min()) / (scores.max() - scores.min())

scores_norm[x[:, 0] == 0] = 0


df_result = pd.DataFrame(x_pca, columns=[f"Var{i+1}" for i in range(x_pca.shape[1])])
df_result["Índice_PCA"] = scores_norm
df_result.to_excel("index_pca.xlsx", index=False)
print("PCA - componente 1 explica {:.1f}% da variância.".format(100 * pca.explained_variance_ratio_[0]))
