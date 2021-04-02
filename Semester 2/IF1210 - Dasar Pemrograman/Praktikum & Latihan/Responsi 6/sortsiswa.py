# Program SortSiswa
# Spesifikasi : ....
import tulisdata

# KAMUS
# namafile: string


# ALGORITMA PROGRAM UTAMA
namafile = input()
tulisdata.TulisDataSiswa(namafile)

# Inisialisasi
f = open(namafile)
data, tp, ct = [], [], 0

# Pembaca
for i in f:
    if (i == "99999999") and (not len(data)):
        break
    if ct < 3:
        tp.append(i.rstrip())
        ct += 1
    else:
        data.append(tp)
        if i == "99999999":
            break
        tp, ct = [i.rstrip()], 1

if not len(data):
    print("File kosong")
else:
    # Sort
    l = 1
    for i in range(1,len(data)):
        nimcek = int(data[i][0])
        j = i - 1
        index = i
        while j >= 0:
            if nimcek < int(data[j][0]):
                data[index], data[j] = data[j], data[index]
                index -= 1
                j -= 1
            elif (j == 1) and (nimcek < int(data[j-1][0])):
                data[i], data[j] = data[j], data[i]
            else:
                break

    # Print
    for i in data:
        print("{},{},{}".format(i[0],i[1],i[2]))
