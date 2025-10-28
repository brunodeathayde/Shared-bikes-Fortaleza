# 🌍 Spatial Autocorrelation Analysis with Moran's Index

This project performs spatial autocorrelation analysis using **Moran's I** in Python. It includes both **Global Moran's I** and **Local Moran's I (LISA)** to detect spatial patterns in geospatial data.

---

## 📁 Files

- `data.geojson`: Geospatial dataset containing polygon features (e.g., neighborhoods or regions).
- `moran.py`: Python script that calculates Global and Local Moran's I statistics and generates visualizations.
- `moran_plot.png`: Plot showing the distribution of Global Moran's I values.
- `moran_local_plot.png`: Plot showing Local Moran's I values and significance.
- `moran_local_cluster_map.png`: Cluster map highlighting statistically significant spatial clusters (High-High, Low-Low, High-Low, Low-High).

---

## 📊 Methodology

The analysis includes:

1. **Reading and preprocessing** geospatial data from `data.geojson`
2. **Calculating Global Moran's I** to assess overall spatial autocorrelation
3. **Calculating Local Moran's I (LISA)** to identify local clusters and outliers
4. **Generating visualizations** to interpret spatial patterns

---

## 🚀 How to Run

### Requirements

- Python 3.x
- geopandas
- libpysal
- esda
- matplotlib
