# 🧭 A Data-Driven Exploration of Socio-Spatial Patterns in Bike-Sharing Systems

This repository contains three spatial analysis modules implemented in Python, each focusing on a different technique for understanding spatial patterns and relationships in geographic data.

---

## 📂 Repository Structure

### 1. **Connectivity Graphs**
This module explores spatial relationships using graph-based representations of geographic features.

**Contents:**
- Construction of spatial weights matrices (e.g., contiguity, distance-based)
- Visualization of neighborhood connectivity
- Graph-theoretic metrics for spatial topology

**Use cases:**
- Understanding spatial structure
- Preparing inputs for spatial econometrics

---

### 2. **Moran's Index**
This module implements **Global** and **Local Moran’s I** to measure spatial autocorrelation.

**Contents:**
- `moran.py`: Calculates Global and Local Moran's I
- `data.geojson`: Geospatial input data
- `moran_plot.png`: Global Moran’s I visualization
- `moran_local_plot.png`: Local Moran’s I significance plot
- `moran_local_cluster_map.png`: Cluster map showing spatial patterns

**Use cases:**
- Detecting spatial clusters and outliers
- Validating spatial dependence in variables

---

### 3. **Principal Component Analysis**
This module uses **PCA** to create a synthetic index of neighborhood suitability for shared bicycle use.

**Contents:**
- `PCA.py`: Performs PCA and generates a suitability index
- `neighborhoods.xlsx`: Input data with production and socio-economic variables
- `index.xlsx`: Output file with PCA scores
- `data.geojson`: Spatial data for mapping
- `map_index.py`: Script to generate thematic maps
- `thematic_map.png`: Visual representation of PCA-based index

**Use cases:**
- Dimensionality reduction
- Creating composite indicators
- Spatial visualization of multivariate patterns

---

## 🛠 Requirements

Install the required Python packages:

```bash
pip install pandas numpy geopandas matplotlib scikit-learn libpysal esda
