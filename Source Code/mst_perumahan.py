import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Data rumah
rumah = ["A", "B", "C", "D", "E", "F"]

# Matriks panjang kabel antar rumah (dalam meter)
# Dibuat hipotetis berdasarkan hasil MST: B-C (1m), C-D (3m), D-E (2m), E-F (3m), B-A (4m)
jarak = [
    [0, 4, 5, 6, 7, 8],  # A
    [4, 0, 1, 4, 5, 6],  # B
    [5, 1, 0, 3, 4, 5],  # C
    [6, 4, 3, 0, 2, 4],  # D
    [7, 5, 4, 2, 0, 3],  # E
    [8, 6, 5, 4, 3, 0]   # F
]

# Fungsi untuk menghitung MST menggunakan Algoritma Prim
def prim_mst(rumah, jarak):
    n = len(rumah)
    G = nx.Graph()
    
    # Tambahkan simpul dan sisi ke graf
    for i in range(n):
        for j in range(i + 1, n):
            if jarak[i][j] > 0:  # Hanya tambahkan sisi dengan jarak > 0
                G.add_edge(rumah[i], rumah[j], weight=jarak[i][j])
    
    # Inisialisasi untuk Algoritma Prim, mulai dari Rumah B
    visited = {rumah[1]}  # Rumah B (indeks 1)
    mst_edges = []
    total_weight = 0
    
    while len(visited) < n:
        min_weight = float('inf')
        min_edge = None
        
        # Cari sisi dengan bobot minimum yang menghubungkan simpul terkunjungi ke simpul belum terkunjungi
        for u in visited:
            for v in rumah:
                if v not in visited and G.has_edge(u, v):
                    weight = G[u][v]['weight']
                    if weight < min_weight:
                        min_weight = weight
                        min_edge = (u, v, weight)
        
        if min_edge:
            u, v, weight = min_edge
            mst_edges.append((u, v, weight))
            visited.add(v)
            total_weight += weight
    
    return mst_edges, total_weight

# Hitung MST
mst_edges, total_weight = prim_mst(rumah, jarak)

# Cetak hasil MST
print("Minimum Spanning Tree (MST) Edges:")
for u, v, weight in mst_edges:
    print(f"Rumah {u} - Rumah {v}: {weight} meter")
print(f"Total panjang kabel MST: {total_weight} meter")

# Visualisasi MST
G_mst = nx.Graph()
for u, v, weight in mst_edges:
    G_mst.add_edge(u, v, weight=weight)

# Atur posisi simpul menggunakan layout spring
pos = nx.spring_layout(G_mst)

# Gambar graf MST
plt.figure(figsize=(8, 6))
nx.draw(G_mst, pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G_mst, 'weight')
nx.draw_networkx_edge_labels(G_mst, pos, edge_labels=labels)
plt.title("Minimum Spanning Tree - Jaringan Kabel Listrik Antar Rumah", fontsize=12)
plt.savefig('mst_kompleks_perumahan.png')
plt.show()