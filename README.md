# PraktikumTeoriGraf

## Soal 1: Knight's Tour 🐴

### Deskripsi soal
implementasi program visualisasi bidak kuda yang harus jalan ke seluiruh kotak papan catur 8x8 tepat satu kali

### Cara pakai
```
python praktikum1.py
```
1. Window muncul dengan papan catur 8x8
2. pilih **"Open Tour"** atau **"Closed Tour"**
   - Open Tour: kuda bebas berhenti di mana saja tempatnya
   - Closed Tour: kuda harus bisa balik ke start dengan tambahan 1 langkah lagi
3. Solusi akan muncul
4. Klik **"Animate"** untuk melihat animasinya
5. Klik **"Reset"** untuk ulang program dari awal

### Input
Tidak ada input manual, program langsung berjalan dari posisi (0,0)

### Output
- **Terminal:** `Solution found for OPEN tour!`
- **Window:** 
  - Papan catur dengan garis yang menunjukkan jalur kuda
  - Angka 0-63 di setiap kotak yang memeberi tahu urutan kunjungan
  - Panah merah menunjukkan posisi kuda sekarang
  - Sidebar kanan akan muncul info progress dan tombol kontrol
 
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
Terminal akan menunjukkan 4 langkah:

1. **Tree Structure** - menunjukkan semua angka di input
2. **Ekspansi Setiap Node** - Semua path yang bisa dibuat dari setiap angka
```
   Dari 4:
     * 4 ✓
     * 4 → 7 → 8 → 11 ✓
     ...
```
3. **Hitung Total Path** - Berapa banyak path dari tiap angka
4. **Cari Path Terpanjang** - menunjukkan semua LIS
```
   LIS (Longest Increasing Subsequence):
      [4, 7, 8, 11]
      [1, 7, 8, 11]
   
   Panjang LIS = 4
   Total Path = 48 path
```
