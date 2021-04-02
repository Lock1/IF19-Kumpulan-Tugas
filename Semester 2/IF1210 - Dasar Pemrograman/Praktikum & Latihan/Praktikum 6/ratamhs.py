# Tanggal       : 15 April 2020

# Program RataRataNilaiMahasiswa
import tulisdata

# KAMUS
# namafile: string


# ALGORITMA PROGRAM UTAMA
namafile = input()
tulisdata.TulisDataMhs(namafile)

# Inisialisasi
f = open(namafile)
data, tp, ct = [], [], 0

# Pembaca
for i in f:
    if ct < 3:
        tp.append(i.rstrip())
        ct += 1
    else:
        data.append(tp)
        if i == "99999999":
            break
        tp, ct = [i.rstrip()], 1

# Sort
for i in range(len(data)):
    nimcek = int(data[i][0])
    for j in range(i+1,len(data)):
        if nimcek > int(data[j][0]):
            data[i], data[j] = data[j], data[i]

st = int(data[0][0])
ct, n = 0, 0
for i in data:
    if st == int(i[0]):
        ct += int(i[2])
        n += 1
    else:
        print("{}={}".format(st,round(ct/n)))
        ct, n, st = int(i[2]), 1, int(i[0])
print("{}={}".format(st,round(ct/n)))
