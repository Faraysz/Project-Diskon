def hitung_diskon():
    try:
        total_belanja = float(input("Masukkan total belanja: Rp "))

        if total_belanja < 0:
            print("❌ Input tidak valid. Nominal tidak boleh negatif.")
            return

        # Nested If
        if total_belanja > 500000:
            diskon = 0.10
        else:
            if total_belanja >= 300000:
                diskon = 0.05
            else:
                diskon = 0.0

        potongan = total_belanja * diskon
        total_bayar = total_belanja - potongan

        print(f"\nTotal Belanja : Rp {total_belanja:,.0f}")
        print(f"Diskon        : {diskon*100:.0f}%")
        print(f"Potongan      : Rp {potongan:,.0f}")
        print(f"Total Bayar   : Rp {total_bayar:,.0f}")

    except ValueError:
        print("❌ Input tidak valid. Harus berupa angka.")

# Jalankan program
hitung_diskon()
