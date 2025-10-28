import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# File paths
geojson_path = 'data.geojson'  # Replace with the correct path if needed
excel_path = 'index.xlsx'      # Replace with the actual Excel file name
output_path = 'thematic_map.png'  # Output file name

# 1. Load the GeoDataFrame
try:
    gdf = gpd.read_file(geojson_path)
except Exception as e:
    print(f"Error loading GeoJSON file: {e}")
    exit()

# 2. Rename columns if they exist
expected_columns = ["bairro_normalizado", "total_viagens"]
for col in expected_columns:
    if col not in gdf.columns:
        print(f"Missing column in GeoDataFrame: {col}")
        exit()

gdf = gdf.rename(columns={
    "bairro_normalizado": "neighborhood",
    "total_viagens": "trips"
})

# 3. Load the Excel spreadsheet
try:
    df_indices = pd.read_excel(excel_path)
except Exception as e:
    print(f"Error loading Excel file: {e}")
    exit()

# 4. Check column existence
if 'neighborhood' not in df_indices.columns or 'Index' not in df_indices.columns:
    print("Excel file must contain 'neighborhood' and 'Index' columns.")
    exit()

# 5. Merge data
gdf_merged = gdf.merge(df_indices, how='left', on='neighborhood')

# 6. Check for missing values
missing = gdf_merged['Index'].isnull().sum()
if missing > 0:
    print(f"Warning: {missing} neighborhoods have no associated index!")

# 7. Plot the thematic map
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
gdf_merged.plot(column='Index',
                cmap='viridis',
                linewidth=0.8,
                edgecolor='0.8',
                legend=True,
                ax=ax)

# 8. Customize the plot
#ax.set_title('Thematic Map by Neighborhood (Index)', fontsize=16)
ax.axis('off')

# 9. Save as PNG
try:
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Map successfully saved as '{output_path}'!")
except Exception as e:
    print(f"Error saving map: {e}")
finally:
    plt.close()
