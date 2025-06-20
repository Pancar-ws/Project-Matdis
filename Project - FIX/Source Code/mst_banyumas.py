import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Data kecamatan dan jarak antar kecamatan (dari Tabel 1 laporan)
kecamatan = [
    "Purwokerto Selatan", "Purwokerto Utara", "Purwokerto Timur", "Purwokerto Barat",
    "Sokaraja", "Kalibagor", "Kembaran", "Sumbang", "Somagede", "Kedungbanteng",
    "Karanglewas", "Patikraja", "Purwojo", "Ajibarang", "Gumelar"
]

# Matriks jarak antar kecamatan (dalam km)
jarak = [
    [0, 3, 2, 4, 7, 12, 6, 10, 15, 20, 18, 8, 25, 22, 30],
    [3, 0, 3, 2, 5, 10, 4, 8, 13, 18, 16, 6, 23, 20, 28],
    [2, 3, 0, 3, 6, 11, 5, 9, 14, 19, 17, 7, 24, 21, 29],
    [4, 2, 3, 0, 4, 9, 3, 7, 12, 17, 15, 5, 22, 19, 27],
    [7, 5, 6, 4, 0, 5, 4, 6, 10, 15, 13, 3, 20, 17, 25],
    [12, 10, 11, 9, 5, 0, 8, 5, 8, 13, 11, 6, 18, 15, 23],
    [6, 4, 5, 3, 4, 8, 0, 5, 11, 16, 14, 4, 21, 18, 26],
    [10, 8, 9, 7, 6, 5, 5, 0, 6, 11, 9, 5, 16, 13, 21],
    [15, 13, 14, 12, 10, 8, 11, 6, 0, 5, 4, 8, 12, 9, 17],
    [20, 18, 19, 17, 15, 13, 16, 11, 5, 0, 3, 12, 10, 7, 15],
    [18, 16, 17, 15, 13, 11, 14, 9, 4, 3, 0, 10, 8, 5, 13],
    [8, 6, 7, 5, 3, 6, 4, 5, 8, 12, 10, 0, 17, 14, 22],
    [25, 23, 24, 22, 20, 18, 21, 16, 12, 10, 8, 17, 0, 4, 12],
    [22, 20, 21, 19, 17, 15, 18, 13, 9, 7, 5, 14, 4, 0, 8],
    [30, 28, 29, 27, 25, 23, 26, 21, 17, 15, 13, 22, 12, 8, 0]
]

# Fungsi untuk menghitung MST menggunakan Algoritma Prim
def prim_mst(kecamatan, jarak):
    n = len(kecamatan)
    G = nx.Graph()
    
    # Tambahkan simpul dan sisi ke graf
    for i in range(n):
        for j in range(i + 1, n):
            if jarak[i][j] > 0:  # Hanya tambahkan sisi dengan jarak > 0
                G.add_edge(kecamatan[i], kecamatan[j], weight=jarak[i][j])
    
    # Inisialisasi untuk Algoritma Prim
    visited = {kecamatan[0]}  # Mulai dari simpul pertama (Purwokerto Selatan)
    mst_edges = []
    total_weight = 0
    
    while len(visited) < n:
        min_weight = float('inf')
        min_edge = None
        
        # Cari sisi dengan bobot minimum yang menghubungkan simpul terkunjungi ke simpul belum terkunjungi
        for u in visited:
            for v in kecamatan:
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
mst_edges, total_weight = prim_mst(kecamatan, jarak)

# Cetak hasil MST
print("Minimum Spanning Tree (MST) Edges:")
for u, v, weight in mst_edges:
    print(f"{u} - {v}: {weight} km")
print(f"Total jarak MST: {total_weight} km")

# Visualisasi MST
G_mst = nx.Graph()
for u, v, weight in mst_edges:
    G_mst.add_edge(u, v, weight=weight)

# Atur posisi simpul menggunakan layout spring
pos = nx.spring_layout(G_mst)

# Gambar graf MST
plt.figure(figsize=(12, 8))
nx.draw(G_mst, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G_mst, 'weight')
nx.draw_networkx_edge_labels(G_mst, pos, edge_labels=labels)
plt.title("Minimum Spanning Tree - Jaringan Jalan Antar Kecamatan di Kabupaten Banyumas", fontsize=12)
plt.savefig('mst_banyumas.png')
plt.show()