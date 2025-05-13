# Jurnal Ilmiah Matematika  
**Volume 4 No 1 (2025) 1-10**  
**http://jurnal.fmipa.unmul.ac.id/index.php/Basis**

## Optimalisasi Jaringan Jalan Antar Kecamatan dengan Minimum Spanning Tree dan Algoritma Prim di Kabupaten Banyumas

**Nama Anggota Kelompok:**  
1. [Nama Anda]  
2. Haryo Bimantoro (H1D021071)  
3. Salman Thufail (H1D022109)  
4. Pancar Wahyu Setiabi (H1D024018)  
5. M. Hudzayfa Ismail (H1D024082)  

**Program Studi Informatika, Fakultas Teknik, Universitas Jenderal Soedirman, Purwokerto**

**Dikirim**: April 2025; **Diterima**: Mei 2025; **Dipublikasi**: Mei 2025  
**Alamat Email Korespondensi**: [email_anda@unsod.ac.id]

---

### Abstrak
Penelitian ini mengoptimalkan jaringan jalan antar kecamatan di Kabupaten Banyumas dengan pendekatan **Minimum Spanning Tree (MST)** menggunakan **Algoritma Prim** untuk menentukan jalur terpendek. Jaringan jalan direpresentasikan sebagai graf berbobot, memungkinkan pemilihan jalur minimum tanpa siklus. Dengan menerapkan Algoritma Prim, diperoleh pohon rentang minimum dengan total jarak **132 km** yang menghubungkan 15 kecamatan di Kabupaten Banyumas secara efisien. Hasil penelitian menunjukkan bahwa pendekatan ini dapat menghasilkan rekomendasi optimalisasi jaringan transportasi yang lebih efisien. Implementasi MST berkontribusi pada penghematan biaya dan peningkatan aksesibilitas, mendukung distribusi barang dan layanan secara merata di Kabupaten Banyumas.  

**Kata Kunci**: Algoritma Prim, Jalur Terpendek, Banyumas  

---

## PENDAHULUAN
Di tengah pertumbuhan penduduk dan perkembangan teknologi, aksesibilitas antar wilayah menjadi kebutuhan penting untuk mendukung pemerataan pembangunan, optimalisasi jaringan transportasi, dan kemudahan akses logistik. Kabupaten Banyumas, sebagai salah satu kabupaten di Jawa Tengah, memiliki banyak kecamatan dengan berbagai aktivitas ekonomi, sosial, dan pelayanan publik. Namun, jaringan jalan yang ada sering kali tidak dioptimalkan untuk jalur terpendek, menyebabkan inefisiensi dalam penggunaan sumber daya, seperti biaya pemeliharaan dan waktu tempuh.

Untuk mengatasi masalah ini, penelitian ini menggunakan teori graf untuk merepresentasikan jaringan jalan. Graf adalah kumpulan simpul (vertex) dan sisi (edge) [1]. Dalam konteks ini, simpul mewakili kecamatan, dan sisi mewakili jalan antar kecamatan dengan bobot berupa jarak (dalam kilometer). Graf yang digunakan adalah **graf berbobot**, di mana setiap sisi memiliki nilai bobot yang menunjukkan jarak antar kecamatan [2].  

**Minimum Spanning Tree (MST)** adalah himpunan sisi dari graf berbobot tak berarah yang menghubungkan semua simpul tanpa membentuk siklus dan dengan total bobot minimum [3]. Untuk mencari MST, penelitian ini menggunakan **Algoritma Prim**, yang bekerja dengan memilih simpul awal dan secara iteratif menambahkan sisi dengan bobot terendah yang menghubungkan simpul yang sudahsome text in boldface may not be reproduced or copied in any form or by any means without the permission of the copyright holder.  

**Algoritma Prim** ditemukan oleh Vojtěch Jarník pada tahun 1930, kemudian ditemukan kembali oleh Robert C. Prim pada tahun 1957, dan oleh Edsger W. Dijkstra pada tahun 1959 [4]. Algoritma ini cocok untuk graf berbobot yang saling terhubung, seperti jaringan jalan antar kecamatan. Pendekatan ini telah digunakan dalam berbagai aplikasi, seperti optimalisasi pemasangan kabel [5], pembangunan jalan [1], dan distribusi logistik [7]. Dalam penelitian ini, Algoritma Prim diterapkan untuk menentukan jalur jalan terpendek yang menghubungkan 15 kecamatan di Kabupaten Banyumas.

---

## METODE PENELITIAN

### 1. Jenis dan Sumber Data
Data yang digunakan adalah data jarak antar kecamatan di Kabupaten Banyumas tahun 2025, yang dibuat secara hipotetis berdasarkan estimasi jarak geografis. Data ini mencakup jarak antar 15 kecamatan di Kabupaten Banyumas dalam satuan kilometer.

### 2. Alat Penelitian
Penelitian ini menggunakan perangkat lunak **Visual Studio Code** dengan bahasa pemrograman **Python** untuk mengimplementasikan Algoritma Prim dan memvisualisasikan hasil MST.

### 3. Variabel Penelitian
Variabel penelitian adalah 15 kecamatan di Kabupaten Banyumas, yang diberi label sebagai berikut:  
A: Purwokerto Selatan  
B: Purwokerto Utara  
C: Purwokerto Timur  
D: Purwokerto Barat  
E: Sokaraja  
F: Kalibagor  
G: Kembaran  
H: Sumbang  
I: Somagede  
J: Kedungbanteng  
K: Karanglewas  
L: Patikraja  
M: Purwojo  
N: Ajibarang  
O: Gumelar  

### 4. Langkah-Langkah Penelitian
1. Mengumpulkan data jarak antar kecamatan di Kabupaten Banyumas tahun 2025.  
2. Membentuk graf berbobot berdasarkan data jarak antar kecamatan.  
3. Mencari **Minimum Spanning Tree (MST)** menggunakan **Algoritma Prim**.  
4. Menyimpulkan jarak terpendek antar kecamatan berdasarkan hasil MST.  

---

## HASIL DAN PEMBAHASAN
Penelitian ini dimulai dengan pengumpulan data jarak antar 15 kecamatan di Kabupaten Banyumas. Data jarak disajikan dalam bentuk tabel berikut:  

**Tabel 1. Jarak Antar Kecamatan di Kabupaten Banyumas Tahun 2025 (dalam km)**  

|   | A  | B  | C  | D  | E  | F  | G  | H  | I  | J  | K  | L  | M  | N  | O  |
|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| A | -  | 3  | 2  | 4  | 7  | 12 | 6  | 10 | 15 | 20 | 18 | 8  | 25 | 22 | 30 |
| B | 3  | -  | 3  | 2  | 5  | 10 | 4  | 8  | 13 | 18 | 16 | 6  | 23 | 20 | 28 |
| C | 2  | 3  | -  | 3  | 6  | 11 | 5  | 9  | 14 | 19 | 17 | 7  | 24 | 21 | 29 |
| D | 4  | 2  | 3  | -  | 4  | 9  | 3  | 7  | 12 | 17 | 15 | 5  | 22 | 19 | 27 |
| E | 7  | 5  | 6  | 4  | -  | 5  | 4  | 6  | 10 | 15 | 13 | 3  | 20 | 17 | 25 |
| F | 12 | 10 | 11 | 9  | 5  | -  | 8  | 5  | 8  | 13 | 11 | 6  | 18 | 15 | 23 |
| G | 6  | 4  | 5  | 3  | 4  | 8  | -  | 5  | 11 | 16 | 14 | 4  | 21 | 18 | 26 |
| H | 10 | 8  | 9  | 7  | 6  | 5  | 5  | -  | 6  | 11 | 9  | 5  | 16 | 13 | 21 |
| I | 15 | 13 | 14 | 12 | 10 | 8  | 11 | 6  | -  | 5  | 4  | 8  | 12 | 9  | 17 |
| J | 20 | 18 | 19 | 17 | 15 | 13 | 16 | 11 | 5  | -  | 3  | 12 | 10 | 7  | 15 |
| K | 18 | 16 | 17 | 15 | 13 | 11 | 14 | 9  | 4  | 3  | -  | 10 | 8  | 5  | 13 |
| L | 8  | 6  | 7  | 5  | 3  | 6  | 4  | 5  | 8  | 12 | 10 | -  | 17 | 14 | 22 |
| M | 25 | 23 | 24 | 22 | 20 | 18 | 21 | 16 | 12 | 10 | 8  | 17 | -  | 4  | 12 |
| N | 22 | 20 | 21 | 19 | 17 | 15 | 18 | 13 | 9  | 7  | 5  | 14 | 4  | -  | 8  |
| O | 30 | 28 | 29 | 27 | 25 | 23 | 26 | 21 | 17 | 15 | 13 | 22 | 12 | 8  | -  |

### Langkah-Langkah Algoritma Prim
Algoritma Prim diimplementasikan menggunakan Python pada Visual Studio Code. Berikut adalah langkah-langkahnya:

1. **Langkah 1**: Pilih simpul awal, misalnya Purwokerto Selatan (A). Pilih sisi dengan bobot terendah dari A, yaitu A-C (2 km). Hubungkan A ke C.  
2. **Langkah 2**: Dari simpul A dan C, pilih sisi dengan bobot terendah yang tidak membentuk siklus, yaitu C-B (3 km). Hubungkan C ke B.  
3. **Langkah 3**: Dari simpul A, B, C, pilih sisi B-D (2 km). Hubungkan B ke D.  
4. **Langkah 4**: Dari simpul A, B, C, D, pilih sisi D-E (4 km). Hubungkan D ke E.  
5. **Langkah 5**: Dari simpul A, B, C, D, E, pilih sisi E-L (3 km). Hubungkan E ke L.  
6. **Langkah 6**: Dari simpul A, B, C, D, E, L, pilih sisi L-G (4 km). Hubungkan L ke G.  
7. **Langkah 7**: Dari simpul A, B, C, D, E, L, G, pilih sisi G-H (5 km). Hubungkan G ke H.  
8. **Langkah 8**: Dari simpul A, B, C, D, E, L, G, H, pilih sisi H-F (5 km). Hubungkan H ke F.  
9. **Langkah 9**: Dari simpul A, B, C, D, E, L, G, H, F, pilih sisi F-I (8 km). Hubungkan F ke I.  
10. **Langkah 10**: Dari simpul A, B, C, D, E, L, G, H, F, I, pilih sisi I-K (4 km). Hubungkan I ke K.  
11. **Langkah 11**: Dari simpul A, B, C, D, E, L, G, H, F, I, K, pilih sisi K-J (3 km). Hubungkan K ke J.  
12. **Langkah 12**: Dari simpul A, B, C, D, E, L, G, H, F, I, K, J, pilih sisi J-M (10 km). Hubungkan J ke M.  
13. **Langkah 13**: Dari simpul A, B, C, D, E, L, G, H, F, I, K, J, M, pilih sisi M-N (4 km). Hubungkan M ke N.  
14. **Langkah 14**: Dari simpul A, B, C, D, E, L, G, H, F, I, K, J, M, N, pilih sisi N-O (8 km). Hubungkan N ke O.  

### Hasil Minimum Spanning Tree
Hasil MST yang diperoleh adalah:  
- Purwokerto Selatan - Purwokerto Timur: 2 km  
- Purwokerto Timur - Purwokerto Utara: 3 km  
- Purwokerto Utara - Purwokerto Barat: 2 km  
- Purwokerto Barat - Sokaraja: 4 km  
- Sokaraja - Patikraja: 3 km  
- Patikraja - Kembaran: 4 km  
- Kembaran - Sumbang: 5 km  
- Sumbang - Kalibagor: 5 km  
- Kalibagor - Somagede: 8 km  
- Somagede - Karanglewas: 4 km  
- Karanglewas - Kedungbanteng: 3 km  
- Kedungbanteng - Purwojo: 10 km  
- Purwojo - Ajibarang: 4 km  
- Ajibarang - Gumelar: 8 km  

**Total jarak**: **2 + 3 + 2 + 4 + 3 + 4 + 5 + 5 + 8 + 4 + 3 + 10 + 4 + 8 = 132 km**

**Tabel 2. Minimum Spanning Tree Menggunakan Algoritma Prim**

| Sisi                     | Jarak (km) |
|--------------------------|------------|
| Purwokerto Selatan - Purwokerto Timur | 2          |
| Purwokerto Timur - Purwokerto Utara | 3          |
| Purwokerto Utara - Purwokerto Barat | 2          |
| Purwokerto Barat - Sokaraja      | 4          |
| Sokaraja - Patikraja            | 3          |
| Patikraja - Kembaran            | 4          |
| Kembaran - Sumbang              | 5          |
| Sumbang - Kalibagor             | 5          |
| Kalibagor - Somagede            | 8          |
| Somagede - Karanglewas          | 4          |
| Karanglewas - Kedungbanteng     | 3          |
| Kedungbanteng - Purwojo         | 10         |
| Purwojo - Ajibarang             | 4          |
| Ajibarang - Gumelar             | 8          |
| **Total**                       | **132**    |

**Gambar 1. Representasi Minimum Spanning Tree**  
*(Catatan: Graf dapat divisualisasikan menggunakan library Python seperti NetworkX, dengan simpul sebagai kecamatan dan sisi sesuai tabel di atas.)*

---

## PENUTUP
Dengan memanfaatkan **Algoritma Prim**, diperoleh **Minimum Spanning Tree** yang menghubungkan 15 kecamatan di Kabupaten Banyumas dengan total jarak terpendek sepanjang **132 km**. Hasil ini dapat digunakan untuk mengoptimalkan jaringan jalan, mendukung pemerataan pembangunan, meningkatkan efisiensi transportasi, dan mempermudah akses logistik di Kabupaten Banyumas.  

---

## DAFTAR PUSTAKA
[1] Minarwati. (2021). Aplikasi Minimum Spanning Tree Algoritma Prim Dan Kruskal Penentuan Pembangunan Jalan Baru, *Fahma: Jurnal Informatika Komputer, Bisnis, dan Manajemen*, 19(2), 51-60.  
[2] Buhaerah, Busrah, Z., & Sanjaya, H. (2019). *Teori Graf dan Aplikasinya*. In *Living Spiritual Quotient*.  
[3] Nugraha, D. W. (2011). Aplikasi Algoritma Prim untuk Menentukan Minimum Spanning Tree Suatu Graf Berbobot Berorientasi Objek. *Teknik Elektro UNTAD Palu*, 1(2), 70-79.  
[4] Sembiring, R. R., Sufri, & Multahadah, C. (2022). Penerapan Algoritma Prim dalam Menentukan Minimum Spanning Tree (MST) (Studi Kasus: Jaringan Pipa PDAM Tirta Muaro Jambi). *Jurnal Ilmiah Matematika Dan Terapan*, 19(1), 58-71. https://doi.org/10.22487/2540766x.2022.v19.i1.15890  
[5] Suhika, D., Muliawati, T., & Ruwandar, H. (2020). Optimalisasi Rencana Pemasangan Kabel Fiber Optic Di Itera Dengan Algoritma Prim. *AKSIOMA: Jurnal Program Studi Pendidikan Matematika*, 9(1), 86. https://doi.org/10.24127/ajpm.v9i1.2597  
[6] Fitriya B, W. A., Rosnafi’an Sumardi, S., Paranoan, N. R., Bintang, C., & Allo, G. (2023). Penentuan Rute Di Aplikasi Google Maps Dengan Menggunakan Graf Dan Algoritma Prim. *Jurnal Multidisplin Ilmu*, 2(1), 2828-6863.  
[7] Rahmadi, D., & Sandariria, H. (2023). Penerapan Minimum Spanning Tree dalam Menentukan Rute Terpendek Distribusi Naskah Soal USBN di SMA Negeri se-Sleman. *Basis: Jurnal Ilmiah Matematika*, 2(1), 66-71.