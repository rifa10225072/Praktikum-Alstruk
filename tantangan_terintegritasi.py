# --- Mahasiswa 1 ---
# 1. Simpan nama mahasiswa dalam variabel string
nama1 = "Rifa Nuraini"

# 2. Simpan nilai tugas dan nilai ujian dalam variabel numerik
nilai_tugas1 = 85
nilai_ujian1 = 90

# 3. Hitung rata-rata kedua nilai
rata_rata1 = (nilai_tugas1 + nilai_ujian1) / 2

# 4. Mahasiswa dinyatakan lulus jika rata-rata minimal 75
lulus1 = rata_rata1 >= 75

# 5. Tampilkan nama, kedua nilai, rata-rata, dan status lulus (True/False)
print("=== Rekap Nilai Mahasiswa 1 ===")
print("Nama        :", nilai_tugas1)
print("Nilai Tugas :", nilai_tugas1)
print("Nilai Ujian :", nilai_ujian1)
print("Rata-rata   :", rata_rata1)
print("Status Lulus:", lulus1)
print("-" * 30)

# --- Mahasiswa 2 (Uji dengan kombinasi nilai lain) ---
# 6. Uji program dengan minimal dua kombinasi nilai yang berbeda
nama2 = "Rahma Adawiyah"
nilai_tugas2 = 65
nilai_ujian2 = 70

rata_rata2 = (nilai_tugas2 + nilai_ujian2) / 2
lulus2 = rata_rata2 >= 75

print("=== Rekap Nilai Mahasiswa 2 ===")
print("Nama        :", nama2)
print("Nilai Tugas :", nilai_tugas2)
print("Nilai Ujian :", nilai_ujian2)
print("Rata-rata   :", rata_rata2)
print("Status Lulus:", lulus2)
print("-" * 30)