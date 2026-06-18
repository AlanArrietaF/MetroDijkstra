# MetroDijkstra 

Aplicación en Python que implementa el algoritmo de Dijkstra para encontrar la ruta más corta (o de menor tiempo) entre las estaciones del Sistema de Transporte Colectivo Metro (CDMX).

El programa lee los datos de las conexiones entre estaciones y sus respectivos "pesos" (que pueden representar tiempo o distancia) desde un archivo de Excel, construye un grafo y calcula el camino óptimo desde una estación de origen hasta una de destino.

## Características
- Lectura automática de datos desde un archivo `.xlsx`.
- Construcción de grafos utilizando la librería `networkx`.
- Implementación eficiente del algoritmo de Dijkstra apoyado en colas de prioridad (`heapq`).
- Impresión en consola de la ruta detallada estación por estación y el tiempo/peso total del recorrido.

## Requisitos previos

Para poder ejecutar este script, necesitas tener instalado Python en tu sistema, junto con las siguientes librerías:

- `pandas` (para la manipulación de datos).
- `numpy` (dependencia común de pandas).
- `networkx` (para la creación y manejo del grafo).
- `openpyxl` (necesaria para que pandas pueda leer archivos `.xlsx`).

Puedes instalar todas las dependencias ejecutando el siguiente comando en tu terminal:

```bash
pip install pandas numpy networkx openpyxl
```
## Estructura del proyecto

- dijkstra.py: Es el script principal que contiene la lógica del algoritmo de Dijkstra y la ejecución del programa.
- EstacionesMetro.xlsx: Archivo de Excel que actúa como base de datos. Contiene las columnas Origen, Destino y Peso.

