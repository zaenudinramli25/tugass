nilai = [25, 90, 40, 95, 35, 70, 50, 20, 80, 65]

nilai_terbesar = nilai[0]

for n in nilai:
    
    if n > nilai_terbesar:
        nilai_terbesar = n

print("Nilai terbesar dari hasil ujian mahasiswa adalah:", nilai_terbesar)
