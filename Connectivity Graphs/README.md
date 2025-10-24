# Connectivity Graphs of Fortaleza's Bike Sharing System

This repository contains Python code and visualizations that explore the connectivity of Fortaleza's bike sharing system in Northeast Brazil. The connectivity graphs were generated using real operational data from the system, spanning the years **2014 to 2024**.

## 📂 Contents

- `connectivity_graphs.py`: Python script to generate connectivity graphs from station data.
- `2014.png` to `2024.png`: Annual connectivity graphs showing station interactions and network structure.
- `README.md`: Project overview and usage instructions.

## 📊 Description

The connectivity graphs illustrate how bike stations are linked based on user trips. Each node represents a station, and each edge represents a connection based on trips between stations. These visualizations help identify:

- Central hubs in the network
- Temporal changes in connectivity
- Potential gaps or bottlenecks in the system

## 🛠️ Requirements

To run the Python script, make sure you have the following libraries installed:

```bash
pip install pandas geopandas matplotlib geometry contextily os

## 🌍 Data Source

The data used to generate these graphs comes from the official bike sharing system of **Fortaleza, Ceará, Brazil**, covering the period from **2014 to 2024**.

## 🤝 Contributing

Feel free to fork the repository, submit issues, or open pull requests to improve the code or visualizations.

## 📸 Connectivity Graphs by Year

Below are the annual connectivity graphs generated from Fortaleza's bike sharing system data:

### 2014
![Graph](2014.png)

### 2015
![Connectivity Graph 2015](2015.png)

### 2016
![Connectivity Graph 2016](2016.png)

### 2017
![Connectivity Graph 2017](2017.png)

### 2018
![Connectivity Graph 2018](2018.png)

### 2019
![Connectivity Graph 2019](2019.png)

### 2020
![Connectivity Graph 2020](2020.png)

### 2021
![Connectivity Graph 2021](2021.png)

### 2022
![Connectivity Graph 2022](2022.png)

### 2023
![Connectivity Graph 2023](2023.png)
