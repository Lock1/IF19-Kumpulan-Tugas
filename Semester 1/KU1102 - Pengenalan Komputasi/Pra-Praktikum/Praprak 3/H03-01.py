# Tanggal       : 13 Oktober 2019
# Deskripsi     : Program print array terbailk

#Kamus
#Array of strings   : x
#Integer            : n

#Algoritma
n = int(input("Masukkan N: "))
#Input setiap elemen x
x = [input() for i in range(n)]

#Print hasil balik, dimulai dari indeks n-1 hingga 0 turun 1 setiap langkah
print("Hasil dibalik:")
for i in range(n-1,-1,-1):
    print(x[i])

#Karena pada komprehensi list x digunakan input() saja, maka x adalah array dengan tipe string
