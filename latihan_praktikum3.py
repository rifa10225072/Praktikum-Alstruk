print("\n=== PRAKTIKUM 3 ===")
nilai = 82
kehadiran = 90

# 2. Gunakan operator >= untuk memeriksa masing-masing syarat (minimal nilai 75, kehadiran 80%)
syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

print("Syarat nilai terpenuhi (> 75)       :", syarat_nilai)
print("Syarat kehadiran terpenuhi (> 80%) :", syarat_kehadiran)

# 3. Gunakan operator and untuk menentukan apakah mahasiswa memenuhi kedua syarat
lulus_and = syarat_nilai and syarat_kehadiran
print("Status kelulusan (menggunakan and) :", lulus_and)

# 4 & 5. Simulasi ubah nilai menjadi 70 dan coba gunakan or
nilai_baru = 70
syarat_nilai_baru = nilai_baru >= 75
lulus_or = syarat_nilai_baru or syarat_kehadiran
print("\nJika nilai diubah menjadi 70:")
print("Status kelulusan (menggunakan and):", syarat_nilai_baru and syarat_kehadiran)
print("Status kelulusan (menggunakan or) :", lulus_or)