print("\n=== PRAKTIKUM 2 ===")
harga = 12500
jumlah = 4

# 2. Hitung total harga
total_harga = harga * jumlah

# 3. Hitung sisa pembagian total harga dengan 2.000 menggunakan operator %
sisa_bagi = total_harga % 2000

# 4. Hitung harga setelah diskon Rp5.000
harga_diskon = total_harga - 5000

# 5. Tampilkan hasil setiap perhitungan dengan label yang jelas
print("Harga satuan buku : Rp", harga)
print("Jumlah pembelian  :", jumlah, "buah")
print("Total harga       : Rp", total_harga)
print("Sisa bagi (% 2000): Rp", sisa_bagi)
print("Harga setelah diskon: Rp", harga_diskon)