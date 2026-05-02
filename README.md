# uts-information-gain
# UTS Data Informasi Pengetahuan

## Implementasi Feature Selection Menggunakan Metode Information Gain

---

## Identitas Mahasiswa

**Nama** : Muhammad Bagus Al Hikma Azhar
**NIM**  : 202310370311405
**Kelas**: DIP Kelas D

---

## 1. Pendahuluan

Dalam bidang data mining, proses pemilihan fitur (feature selection) merupakan tahap penting untuk menentukan atribut yang paling berpengaruh terhadap hasil klasifikasi. Salah satu metode yang umum digunakan adalah **Information Gain**, yang didasarkan pada konsep **Entropy**.

Proyek ini bertujuan untuk mengimplementasikan perhitungan Entropy dan Information Gain secara manual menggunakan bahasa pemrograman Python tanpa bantuan library khusus.

---

## 2. Dasar Teori

### 2.1 Entropy

Entropy digunakan untuk mengukur tingkat ketidakpastian atau ketidakteraturan dalam suatu dataset.

Rumus Entropy:

[H(S) = - \sum p_i \log_2 p_i]

di mana (p_i) adalah probabilitas dari setiap kelas dalam dataset.

---

### 2.2 Information Gain

Information Gain digunakan untuk menentukan atribut terbaik yang akan digunakan sebagai pemisah (split) dalam proses pembentukan decision tree.

Rumus Information Gain:

[IG(S, A) = H(S) - \sum \frac{|S_i|}{|S|} H(S_i)]

di mana:

* (S) = dataset awal
* (A) = atribut
* (S_i) = subset data berdasarkan atribut (A)

---

## 3. Dataset

Dataset yang digunakan merupakan dataset sederhana dengan jumlah 14 data.

Atribut yang digunakan meliputi:

* Cuaca
* Suhu
* Kelembapan
* Angin
* Label (Main: Ya / Tidak)

---

## 4. Implementasi Program

Program dibuat menggunakan bahasa Python dengan perhitungan manual tanpa menggunakan library machine learning.

File utama:

```bash id="f9rq2s"
information_gain.py
```

Cara menjalankan program:

```bash id="ycn7eq"
python information_gain.py
```

## 5. Hasil Perhitungan

Output program menunjukkan nilai Entropy total dan Information Gain untuk setiap atribut sebagai berikut:

```bash id="h9p0sn"
Entropy Total: 0.940

Information Gain Cuaca = 0.246
Information Gain Suhu = 0.029
Information Gain Kelembapan = 0.151
Information Gain Angin = 0.048
```

## 6. Analisis

Berdasarkan hasil perhitungan, atribut **Cuaca** memiliki nilai Information Gain tertinggi dibandingkan atribut lainnya.

Hal ini menunjukkan bahwa atribut tersebut memiliki kemampuan terbaik dalam memisahkan data sehingga dipilih sebagai akar (root) dalam pembentukan decision tree.

---

## 7. Decision Tree (Representasi Sederhana)

```bash id="rqmb6s"
Cuaca?
├── Cerah   → Tidak
├── Mendung → Ya
└── Hujan   → (perlu pemisahan lanjutan)
```

## 8. Contoh Perhitungan Manual

### 8.1 Entropy Total

Jumlah data:

* Ya = 9
* Tidak = 5

[H(S) = - (9/14 \log_2 9/14) - (5/14 \log_2 5/14)]

[H(S) ≈ 0.940]

---

### 8.2 Entropy Atribut Cuaca

**Cerah (5 data)**

* Ya = 2, Tidak = 3

[H(Cerah) ≈ 0.971]

---

**Mendung (4 data)**

* Ya = 4, Tidak = 0

[H(Mendung) = 0]

---

**Hujan (5 data)**

* Ya = 3, Tidak = 2

[H(Hujan) ≈ 0.971]

---

### 8.3 Information Gain Cuaca

[IG(Cuaca) = 0.940 - [(5/14 × 0.971) + (4/14 × 0) + (5/14 × 0.971]

[IG(Cuaca) ≈ 0.246]

---

## 9. Kesimpulan

Berdasarkan hasil implementasi dan perhitungan yang telah dilakukan, dapat disimpulkan bahwa:

1. Metode Information Gain dapat digunakan untuk menentukan atribut terbaik dalam dataset.
2. Atribut **Cuaca** memiliki nilai Information Gain tertinggi.
3. Atribut tersebut dipilih sebagai root dalam pembentukan decision tree.

## 10. Struktur Proyek

```bash id="9sb9s6"
uts-information-gain/
│
├── information_gain.py
├── README.md
├── laporan.pdf
```
## 11. Penutup

Proyek ini menunjukkan bahwa perhitungan Entropy dan Information Gain dapat dilakukan secara manual menggunakan Python, serta memberikan pemahaman yang lebih mendalam terhadap proses pemilihan atribut dalam data mining.

**Penulis**
*Muhammad Bagus Al Hikma Azhar*
