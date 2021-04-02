# Tanggal       : 15 April 2020

# Program SortMhs
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
ct,l = 1,1
print(data,"awal")
for i in range(len(data)):
    nimcek = int(data[i][0])
    for j in range(i+1,len(data)):
        if nimcek > int(data[j][0]):
            data[i], data[j] = data[j], data[i]
    print(data,"Sort ke",ct)
    ct += 1

# Print
for i in data:
    print("{},{},{}".format(i[0],i[1],i[2]))
