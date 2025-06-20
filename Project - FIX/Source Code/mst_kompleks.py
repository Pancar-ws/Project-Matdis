import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# rumah = [
#     "A", "B", "C", "D", "E",\
# ]

# jarak = [
#     [0, 5, 7, 10, 12]
# ]

def prim(graph, start):
    vertices = list(graph.keys())
    mst = []
    visited = {start}
    edges = []

    while len(visited) < len(vertices):
        for u in visited:
            for v, weight in graph[u].items():
                if v not in visited:
                    edges.append((weight, u, v))
        
        edges.sort()
        if not edges:
            break
        weight, u, v = edges.pop(0)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
    
    return mst

# Definisi graf berdasarkan matriks ketetanggaan
graph = {
    'A': {'B': 5, 'C': 7, 'D': 10, 'E': 12},
    'C': {'A': 7, 'B': 4, 'D': 6, 'E': 8},
    'B': {'A': 5, 'C': 4, 'D': 8, 'E': 10},
    'D': {'A': 10, 'B': 8, 'C': 6, 'E': 5},
    'E': {'A': 12, 'B': 10, 'C': 8, 'D': 5},
}

# graph = {
#     'A': {'B': 5, 'C': 7, 'D': 10, 'E': 12, 'F': 15, 'G': 8, 'H': 14, 'I': 20, 'J': 25, 'K': 22, 'L': 9, 'M': 30, 'N': 28, 'O': 35},
#     'B': {'A': 5, 'C': 4, 'D': 8, 'E': 10, 'F': 13, 'G': 6, 'H': 12, 'I': 18, 'J': 23, 'K': 20, 'L': 7, 'M': 28, 'N': 26, 'O': 33},
#     'C': {'A': 7, 'B': 4, 'D': 6, 'E': 8, 'F': 11, 'G': 5, 'H': 10, 'I': 16, 'J': 21, 'K': 18, 'L': 6, 'M': 26, 'N': 24, 'O': 31},
#     'D': {'A': 10, 'B': 8, 'C': 6, 'E': 5, 'F': 8, 'G': 4, 'H': 7, 'I': 13, 'J': 18, 'K': 15, 'L': 5, 'M': 23, 'N': 21, 'O': 28},
#     'E': {'A': 12, 'B': 10, 'C': 8, 'D': 5, 'F': 6, 'G': 5, 'H': 6, 'I': 11, 'J': 16, 'K': 13, 'L': 4, 'M': 21, 'N': 19, 'O': 26},
#     'F': {'A': 15, 'B': 13, 'C': 11, 'D': 8, 'E': 6, 'G': 7, 'H': 5, 'I': 9, 'J': 14, 'K': 11, 'L': 6, 'M': 18, 'N': 16, 'O': 23},
#     'G': {'A': 8, 'B': 6, 'C': 5, 'D': 4, 'E': 5, 'F': 7, 'H': 6, 'I': 12, 'J': 17, 'K': 14, 'L': 4, 'M': 22, 'N': 20, 'O': 27},
#     'H': {'A': 14, 'B': 12, 'C': 10, 'D': 7, 'E': 6, 'F': 5, 'G': 6, 'I': 7, 'J': 12, 'K': 9, 'L': 5, 'M': 17, 'N': 15, 'O': 22},
#     'I': {'A': 20, 'B': 18, 'C': 16, 'D': 13, 'E': 11, 'F': 9, 'G': 12, 'H': 7, 'J': 6, 'K': 5, 'L': 9, 'M': 13, 'N': 11, 'O': 18},
#     'J': {'A': 25, 'B': 23, 'C': 21, 'D': 18, 'E': 16, 'F': 14, 'G': 17, 'H': 12, 'I': 6, 'K': 4, 'L': 13, 'M': 11, 'N': 9, 'O': 16},
#     'K': {'A': 22, 'B': 20, 'C': 18, 'D': 15, 'E': 13, 'F': 11, 'G': 14, 'H': 9, 'I': 5, 'J': 4, 'L': 10, 'M': 9, 'N': 7, 'O': 14},
#     'L': {'A': 9, 'B': 7, 'C': 6, 'D': 5, 'E': 4, 'F': 6, 'G': 4, 'H': 5, 'I': 9, 'J': 13, 'K': 10, 'M': 18, 'N': 16, 'O': 23},
#     'M': {'A': 30, 'B': 28, 'C': 26, 'D': 23, 'E': 21, 'F': 18, 'G': 22, 'H': 17, 'I': 13, 'J': 11, 'K': 9, 'L': 18, 'N': 5, 'O': 13},
#     'N': {'A': 28, 'B': 26, 'C': 24, 'D': 21, 'E': 19, 'F': 16, 'G': 20, 'H': 15, 'I': 11, 'J': 9, 'K': 7, 'L': 16, 'M': 5, 'O': 10},
#     'O': {'A': 35, 'B': 33, 'C': 31, 'D': 28, 'E': 26, 'F': 23, 'G': 27, 'H': 22, 'I': 18, 'J': 16, 'K': 14, 'L': 23, 'M': 13, 'N': 10}
# }

# Jalankan Algoritma Prim
mst = prim(graph, 'A')
total_weight = sum(edge[2] for edge in mst)

print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"Rumah {u} - Rumah {v}: {weight} meter")
print(f"Total panjang kabel: {total_weight} meter")