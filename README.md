# PraktikumTeoriGraf

## Soal 1: Knight's Tour 🐴
### Deskripsi soal
Implementasi program visualisasi pergerakan bidak kuda yang harus mengunjungi seluruh kotak papan catur 8x8 tepat satu kali 

### Cara pakai
```
python praktikum1.py
```
1. Window muncul dengan papan catur 8x8 kosong
2. **Klik kotak mana saja** di papan untuk memilih titik awal kuda
3. Pilih jenis tour:
   - **"Open Tour"**: Kuda mengunjungi 64 kotak, boleh berhenti di mana saja
   - **"Closed Tour"**: Kuda mengunjungi 64 kotak dan harus bisa kembali ke posisi awal
4. Tunggu algoritma menemukan solusi (ditandai dengan status "Solved: 64 kotak")
5. Klik **"Visualisasi"** untuk melihat animasi pergerakan kuda step-by-step
6. Klik **"Reset"** untuk memulai dari awal dengan titik start berbda

### Input
- **User**: Klik mouse pada papan catur untuk memilih posisi awal kuda
- **Button**: Pilihan Open/Closed Tour dan kontrol visualisasi

### Output
**Window GUI:** 
  - Papan catur 8x8 
  - Kotak terpilih ditandai dengan warna biru muda
  - Jalur pergerakan kuda ditampilkan dengan panah berurutan
  - Angka 1-64 di setiap kotak menunjukkan urutan kunjungan
  - Sidebar kanan menampilkan:
    - Status pemilihan titik awal
    - Jenis tour yang dipilih (Open/Closed)
    - Konfirmasi "Solved: 64 kotak"
---

## Soal 2: LONGEST INCREASING SUBSEQUENCE (LIS) 📈

### Deskripsi soal
Mencari semua subsequence yang naik dari barisan angka, lalu mencari mana yang paling panjang (LIS)

### Cara pakai
```
python praktikum2.py
```
Program akan menampilkan hasil di terminal.

### Input
Default: `[4, 1, 13, 7, 0, 2, 8, 11, 3]`

untuk mengganti input, cari baris ini di kode:
```python
sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]
```

### Output
Terminal akan menunjukkan hasil analisis Longest Increasing Subsequence (LIS):

1. **Input Sequence** - Menampilkan array input yang akan dianalisis
```
   Input Sequence:
   [4, 1, 13, 7, 0, 2, 8, 11, 3]
```
2. **Longest Increasing Subsequence (LIS)** - Menampilkan semua LIS dengan panjang maksimal yang berhasil ditemukan:
```
   Longest Increasing Subsequence (LIS):
   [1, 7, 8, 11]
   [1, 2, 8, 11]
   [0, 2, 8, 11]
```
3. **Panjang LIS** - Menampilkan panjang dari subsequence terpanjang:
```
   Panjang LIS = 4
```
