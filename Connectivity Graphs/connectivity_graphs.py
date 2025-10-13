import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import LineString
import contextily as ctx
import os

# === 1. Carregar dados geográficos das estações uma vez ===
gdf_estacoes = gpd.read_file('estacoes_bicicletar.geojson')
gdf_estacoes_ret = gdf_estacoes.rename(columns={'Id': 'EstacaoRetirada'})
gdf_estacoes_dev = gdf_estacoes.rename(columns={'Id': 'EstacaoDevolucao'})

# === 2. Criar pasta de saída se não existir ===
os.makedirs('figuras', exist_ok=True)

# === 3. Loop pelos anos ===
for ano in range(2014, 2025):
    print(f"\n🔄 Processando ano {ano}...")

    # === 3.1 Tentar carregar o CSV com tratamento de codificação ===
    try:
        df = pd.read_csv(f'{ano}Viagens.csv', sep=';', quotechar='"')
    except UnicodeDecodeError:
        print(f"⚠️ Problema de codificação no arquivo {ano}Viagens.csv. Tentando com encoding='latin1'...")
        df = pd.read_csv(f'{ano}Viagens.csv', sep=';', quotechar='"', encoding='latin1')

    # === 3.2 Adicionar coordenadas das estações ===
    df = df.merge(gdf_estacoes_ret[['EstacaoRetirada', 'geometry']], on='EstacaoRetirada', how='left')
    df = df.rename(columns={'geometry': 'geometry_retirada'})
    df = df.merge(gdf_estacoes_dev[['EstacaoDevolucao', 'geometry']], on='EstacaoDevolucao', how='left')
    df = df.rename(columns={'geometry': 'geometry_devolucao'})

    # === 3.3 Filtrar viagens com coordenadas válidas ===
    df = df[df['geometry_retirada'].notnull() & df['geometry_devolucao'].notnull()]

    if df.empty:
        print(f"⚠️ Nenhuma viagem válida encontrada para {ano}. Pulando...")
        continue

    # === 3.4 Criar geometria de linhas entre retirada e devolução ===
    df['linha'] = df.apply(lambda row: LineString([row['geometry_retirada'], row['geometry_devolucao']]), axis=1)
    gdf_linhas = gpd.GeoDataFrame(df, geometry='linha', crs=gdf_estacoes.crs)

    # === 3.5 Agrupar por rota e contar número de viagens ===
    gdf_linhas['rota'] = gdf_linhas['linha'].apply(lambda x: (x.coords[0], x.coords[1]))
    gdf_agrupado = gdf_linhas.groupby('rota').size().reset_index(name='contagem')
    gdf_agrupado['geometry'] = gdf_agrupado['rota'].apply(lambda x: LineString([x[0], x[1]]))
    gdf_agrupado = gpd.GeoDataFrame(gdf_agrupado, geometry='geometry', crs=gdf_estacoes.crs)

    # === 3.6 Reprojetar para EPSG:3857 para mapa base ===
    gdf_agrupado = gdf_agrupado.to_crs(epsg=3857)

    # === 3.7 Filtrar estações utilizadas no ano ===
    estacoes_usadas = set(df['EstacaoRetirada']).union(set(df['EstacaoDevolucao']))
    gdf_estacoes_ano = gdf_estacoes[gdf_estacoes['Id'].isin(estacoes_usadas)].to_crs(epsg=3857)

    # === 3.8 Plotar o mapa ===
    fig, ax = plt.subplots(figsize=(12, 12))
    gdf_agrupado.plot(ax=ax,
                      linewidth=gdf_agrupado['contagem'] / gdf_agrupado['contagem'].max() * 5,
                      alpha=0.6,
                      color='red')
    gdf_estacoes_ano.plot(ax=ax, color='black', markersize=10, alpha=0.7)
    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)

    # === 3.9 Salvar figura ===
    output_path = f'figuras/hm_{ano}.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Figura salva: {output_path}")
