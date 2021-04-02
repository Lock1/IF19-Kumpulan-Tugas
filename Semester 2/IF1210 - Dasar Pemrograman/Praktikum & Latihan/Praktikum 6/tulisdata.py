# Module untuk menulis data file keperluan praktikum

# type dataMhs = (NIM:int, KdKul:string, Nilai:int)

def TulisDataMhs(namafile):
    # Menulis data mahasiswa ke file namafile
    # Kamus
    # f : file teks
    # Algoritma
    f = open(namafile,'w')
    row1 = input().rstrip() # NIM
    # simpan sampai teks = 99999999
    while (row1 != "99999999"):
        # asumsikan selalu baca 3 data
        f.write(row1 + "\n") # write NIM
        row2 = input() # KdKul
        f.write(row2 + "\n") # write KdKul
        row3 = input() # nilai
        f.write(row3 + "\n") # write nilai
        # simpan ke file
        row1 = input().rstrip() # next-NIM
    # tulis NIM terakhir
    f.write(row1) # mark
    f.close()
