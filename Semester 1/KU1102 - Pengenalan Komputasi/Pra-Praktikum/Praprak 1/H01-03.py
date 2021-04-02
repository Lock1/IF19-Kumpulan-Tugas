# Tanggal    : Selasa, 17 September 2019
# Deskripsi  : Program cek bilangan


#Program cek bilangan

#Kamus
#integer : a

#Algoritma

a = float(input("Masukkan angka yang akan dicek: "))

#Pengecekan bilangan a
if (a < 0):
    print("Bilangan negatif")
elif (a == 0):
    print("Bilangan nol")
else:
    if (a % 2 == 0):
        print("Bilangan positif genap")
    else:
        print("Bilangan positif ganjil")

input()                 #Agar program tidak langsung exit
