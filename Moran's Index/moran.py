# Packages (stantard)
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.formula.api as sm
import os

# Plotting
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.float_format = '{:.2f}'.format    # pandas: para todos os números aparecerem com duas casas decimais

# Spatial Analysis
import geopandas as gp
import pysal as ps
import splot
import mapclassify as mc
from libpysal.weights import Queen
from libpysal import weights
from esda import Moran, Moran_Local, G_Local
from splot.esda import plot_moran, moran_scatterplot, lisa_cluster, plot_local_autocorrelation

# Read GeoJSON
gdf = gp.read_file("data.geojson")

# Variables labels
gdf = gdf.rename(columns={
    "bairro_normalizado": "neighborhood",
    "total_viagens": "trips"
})

# Lista apenas os nomes das colunas que não são 'geometry'
non_spatial_vars = gdf.columns.drop("geometry")
print(non_spatial_vars)

# Cria matriz de vizinhança
w = Queen.from_dataframe(gdf)

# Calcula índice de Moran
moran = Moran(gdf["trips"], w)
print("The Moran's index is:", moran.I)

alpha = 0.05  # commonly used threshold

# === 5. Print results and interpretation ===
print(f"Moran's I: {moran.I:.4f}")
print(f"p-value: {moran.p_sim:.4f}")

if moran.p_sim < alpha:
    print("→ The spatial autocorrelation is statistically significant.")
else:
    print("→ The spatial autocorrelation is NOT statistically significant.")

# Salva no diretório atual com nome 'moran_plot.png'
fig, ax = plot_moran(moran, zstandard=False)
plt.show()  # Exibe no ambiente gráfico
fig.savefig("moran_plot.png", dpi=300)

# Local Moran
# Calcula o Moran Local
moran_local = Moran_Local(gdf["trips"], w)

# Gera o gráfico e captura a figura
fig, ax = moran_scatterplot(moran_local, p=0.05)

# Salva a figura na pasta desejada
fig.savefig("moran_local_plot.png", dpi=300, bbox_inches="tight")

# Opcional: exibe o gráfico
plt.show()

# LISA Cluster
fig, ax = lisa_cluster(moran_local,gdf,p=0.05)

# Salva a figura na pasta desejada
fig.savefig("lisa_cluster.png", dpi=300, bbox_inches="tight")

# Opcional: exibe o gráfico
plt.show()

# Local autocorrelation
fig, ax = plot_local_autocorrelation(moran_local,gdf,gdf["trips"])

# Salva a figura na pasta desejada
fig.savefig("local_autocorrelation.png", dpi=300, bbox_inches="tight")

# Opcional: exibe o gráfico
plt.show()



# Gera apenas o terceiro subgráfico (mapa de clusters)
fig, ax = lisa_cluster(moran_local, gdf, p=0.05)

# Salva o gráfico em alta resolução
fig.savefig("moran_local_cluster_map.png", dpi=300, bbox_inches="tight")

# Opcional: exibe o gráfico
plt.show()

