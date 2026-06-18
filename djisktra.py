import pandas as pd
import numpy as np
import networkx as nx
import heapq

ruta_archivo = 'EstacionesMetro.xlsx'

try:
    df = pd.read_excel(ruta_archivo)
except FileNotFoundError:
    print(f"Error: El archivo no se encontró en la ruta '{ruta_archivo}'.")
    print("Asegúrate de que el archivo esté en la misma carpeta que el script o actualiza la ruta.")
    exit()

df.columns = df.columns.str.strip()

df.dropna(subset=['Origen', 'Destino', 'Peso'], inplace=True)
df['Origen'] = df['Origen'].str.strip()
df['Destino'] = df['Destino'].str.strip()

Metro = nx.from_pandas_edgelist(df, source='Origen', target='Destino', edge_attr='Peso')


def dijkstra(graph, inicio, destino):
    distancias = {estacion: float('inf') for estacion in graph.nodes()}
    distancias[inicio] = 0
    estacion_anterior = {estacion: None for estacion in graph.nodes()}
    cola_prioridad = [(0, inicio)]

    if inicio not in graph.nodes() or destino not in graph.nodes():
        return None, float('inf')

    while cola_prioridad:
        distancia_actual, estacion_actual = heapq.heappop(cola_prioridad)

        if estacion_actual == destino:
            ruta = []
            while estacion_actual is not None:
                ruta.insert(0, estacion_actual)
                estacion_actual = estacion_anterior[estacion_actual]
            return ruta, distancia_actual

        if distancia_actual > distancias[estacion_actual]:
            continue

        for vecino in graph.neighbors(estacion_actual):
            peso_borde = graph[estacion_actual][vecino]['Peso']
            distancia = distancia_actual + peso_borde

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                estacion_anterior[vecino] = estacion_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return None, float('inf')



if __name__ == '__main__':
    inicio = 'Cuatro Caminos'
    destino = 'Indios Verdes'
    
    if 'Metro' in locals() or 'Metro' in globals():
        ruta_mas_corta, peso_total = dijkstra(Metro, inicio, destino)

        if ruta_mas_corta:
            print("--- Resultado de Dijkstra ---")
            print("Ruta más corta desde", inicio, "hasta", destino, ":\n")
            for i in ruta_mas_corta:
                print(f" -> {i}")
            print(f"\nTiempo total: {peso_total} minutos")
            print("---------------------------------")
        else:
            print(f"No se encontró ruta desde {inicio} hasta {destino}")
    else:
        pass