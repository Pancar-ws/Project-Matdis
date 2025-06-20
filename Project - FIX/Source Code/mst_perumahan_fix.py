import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Data rumah
rumah = ["A", "B", "C", "D", "E", "F"]

# Matriks panjang kabel antar rumah (dalam meter)
# Sama dengan matriks di mst_kompleks_perumahan.py
jarak = [
    [0, 4, 5, 6, 7, 8],  # A
    [4, 0, 1, 4, 5, 6],  # B
    [5, 1, 0, 3, 4, 5],  # C
    [6, 4, 3, 0, 2, 4],  # D
    [7, 5, 4, 2, 0, 3],  # E
    [8, 6, 5, 4, 3, 0]   # F
]

# Fungsi untuk membuat dan menyimpan visualisasi graf pada setiap langkah
def visualize_step(step, visited, mst_edges, pos, filename, title):
    G_step = nx.Graph()
    # Tambahkan semua simpul
    for r in rumah:
        G_step.add_node(r)
    # Tambahkan sisi MST yang sudah dipilih
    for u, v, weight in mst_edges:
        G_step.add_edge(u, v, weight=weight)
    
    plt.figure(figsize=(8, 6))
    # Warna simpul: hijau untuk terkunjungi, abu-abu untuk belum terkunjungi
    node_colors = ['lightgreen' if r in visited else 'lightgray' for r in rumah]
    nx.draw(G_step, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=12, font_weight='bold')
    labels = nx.get_edge_attributes(G_step, 'weight')
    nx.draw_networkx_edge_labels(G_step, pos, edge_labels=labels)
    plt.title(title, fontsize=12)
    plt.savefig(filename)
    plt.close()

# Fungsi untuk membuat dan menyimpan visualisasi graf lengkap awal
def visualize_initial_graph(rumah, jarak, pos, filename):
    G_initial = nx.Graph()
    # Tambahkan semua simpul dan sisi
    for i in range(len(rumah)):
        for j in range(i + 1, len(rumah)):
            if jarak[i][j] > 0:
                G_initial.add_edge(rumah[i], rumah[j], weight=jarak[i][j])
    
    plt.figure(figsize=(8, 6))
    nx.draw(G_initial, pos, with_labels=True, node_color='lightgray', node_size=500, font_size=12, font_weight='bold')
    labels = nx.get_edge_attributes(G_initial, 'weight')
    nx.draw_networkx_edge_labels(G_initial, pos, edge_labels=labels)
    plt.title("Graf Lengkap Awal - Jaringan Kabel Antar Rumah", fontsize=12)
    plt.savefig(filename)
    plt.close()

# Fungsi untuk menghitung dan mengilustrasikan MST menggunakan Algoritma Prim
def prim_mst_steps_with_initial(rumah, jarak):
    n = len(rumah)
    G = nx.Graph()
    
    # Tambahkan simpul dan sisi ke graf
    for i in range(n):
        for j in range(i + 1, n):
            if jarak[i][j] > 0:
                G.add_edge(rumah[i], rumah[j], weight=jarak[i][j])
    
    # Atur posisi simpul sekali untuk konsistensi visual
    pos = nx.spring_layout(G)
    
    # Visualisasi graf lengkap awal
    print("Visualisasi Graf Lengkap Awal")
    visualize_initial_graph(rumah, jarak, pos, 'initial_graph.png')
    
    # Inisialisasi untuk Algoritma Prim, mulai dari Rumah B
    visited = {rumah[1]}  # Rumah B (indeks 1)
    mst_edges = []
    total_weight = 0
    
    # Langkah 0: Graf awal dengan hanya Rumah B terkunjungi
    print("Langkah 0: Memilih simpul awal Rumah B")
    visualize_step(0, visited, mst_edges, pos, 'mst_step_0.png', "Langkah 0 - Pembentukan MST")
    
    # Langkah 1: Pilih sisi B-C (1 meter)
    print("Langkah 1: Menghubungkan Rumah B ke Rumah C (1 meter)")
    mst_edges.append(("B", "C", 1))
    visited.add("C")
    total_weight += 1
    visualize_step(1, visited, mst_edges, pos, 'mst_step_1.png', "Langkah 1 - Pembentukan MST")
    
    # Langkah 2: Pilih sisi C-D (3 meter)
    print("Langkah 2: Menghubungkan Rumah C ke Rumah D (3 meter)")
    mst_edges.append(("C", "D", 3))
    visited.add("D")
    total_weight += 3
    visualize_step(2, visited, mst_edges, pos, 'mst_step_2.png', "Langkah 2 - Pembentukan MST")
    
    # Langkah 3: Pilih sisi D-E (2 meter)
    print("Langkah 3: Menghubungkan Rumah D ke Rumah E (2 meter)")
    mst_edges.append(("D", "E", 2))
    visited.add("E")
    total_weight += 2
    visualize_step(3, visited, mst_edges, pos, 'mst_step_3.png', "Langkah 3 - Pembentukan MST")
    
    # Langkah 4: Pilih sisi E-F (3 meter)
    print("Langkah 4: Menghubungkan Rumah E ke Rumah F (3 meter)")
    mst_edges.append(("E", "F", 3))
    visited.add("F")
    total_weight += 3
    visualize_step(4, visited, mst_edges, pos, 'mst_step_4.png', "Langkah 4 - Pembentukan MST")
    
    # Langkah 5: Pilih sisi B-A (4 meter)
    print("Langkah 5: Menghubungkan Rumah B ke Rumah A (4 meter)")
    mst_edges.append(("B", "A", 4))
    visited.add("A")
    total_weight += 4
    visualize_step(5, visited, mst_edges, pos, 'mst_step_5.png', "Langkah 5 - Pembentukan MST")
    
    # Visualisasi MST akhir
    G_mst = nx.Graph()
    for u, v, weight in mst_edges:
        G_mst.add_edge(u, v, weight=weight)
    
    plt.figure(figsize=(8, 6))
    nx.draw(G_mst, pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=12, font_weight='bold')
    labels = nx.get_edge_attributes(G_mst, 'weight')
    nx.draw_networkx_edge_labels(G_mst, pos, edge_labels=labels)
    plt.title("Minimum Spanning Tree - Jaringan Kabel Listrik Antar Rumah", fontsize=12)
    plt.savefig('mst_kompleks_perumahan_final.png')
    plt.close()
    
    return mst_edges, total_weight

# Hitung dan visualisasikan MST
print("Ilustrasi Pembentukan Minimum Spanning Tree:")
mst_edges, total_weight = prim_mst_steps_with_initial(rumah, jarak)

# Cetak hasil MST
print("\nMinimum Spanning Tree (MST) Edges:")
for u, v, weight in mst_edges:
    print(f"Rumah {u} - Rumah {v}: {weight} meter")
print(f"Total panjang kabel MST: {total_weight} meter")