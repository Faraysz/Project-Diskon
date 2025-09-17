# Program Penentuan Diskon Belanja

Program ini dibuat untuk menghitung diskon belanja dengan aturan:

- Jika total belanja **> Rp1.000.000** → Diskon **20% + potongan Rp100.000**
- Jika total belanja **> Rp500.000** → Diskon **10%**
- Jika total belanja **>= Rp300.000** → Diskon **5%**
- Jika total belanja **< Rp300.000** → **Tidak ada diskon**

---

## 🛠️ Persyaratan
- Python **3.8+**
- Text editor / IDE (misalnya: VS Code, PyCharm, IDLE)

---

## 📥 Cara Menjalankan
1. Clone atau download project ini
   ```bash
   git clone https://github.com/username/projek-diskon-belanja.git
   ```
   *(atau cukup simpan file `.py` di komputer Bos)*

2. Buka terminal / command prompt di folder file.

3. Jalankan program:
   ```bash
   python diskon.py
   ```

---

## 🖥️ Input & Output
- Input berupa **angka total belanja**
- Program otomatis menentukan diskon, potongan, dan total bayar

Contoh:
```
Masukkan total belanja: Rp 1200000

===== Rincian Belanja =====
Total Belanja       : Rp 1,200,000
Diskon Persentase   : 20%
Potongan Tambahan   : Rp 100,000
Total Potongan      : Rp 340,000
Total Bayar         : Rp 860,000
```

---

## ✅ Hal yang Harus Diperhatikan
1. **Input hanya angka** (tanpa koma/titik desimal ribuan, gunakan `1200000` bukan `1.200.000`).
2. **Tidak boleh negatif** → jika input negatif, program akan menolak.
3. Gunakan **Python versi terbaru** untuk menghindari error.
4. Coba uji dengan **nilai batas (boundary values)**:
   - Rp299.999 → Tidak dapat diskon
   - Rp300.000 → Diskon 5%
   - Rp500.000 → Diskon 5%
   - Rp500.001 → Diskon 10%
   - Rp1.000.001 → Diskon 20% + potongan Rp100.000

---
