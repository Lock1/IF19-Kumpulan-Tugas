# Tanggal       : 29 September 2019
# Deskripsi     : Program print 10^k

#Kamus
#Integer : x, n

#Algoritma
x = int(input("Masukkan N: "))  #Input N
n = 1                           #Nilai awal n, dengan n = 1, algoritma ini tidak dapat menerima bilangan negatif

while x >= n:                   #Loop hingga n*10^k >= x untuk suatu bilangan asli k
    n *= 10

print(n)

#Alternatif Algoritma
# x = input("Masukkan N: ")
# print(10**len(x))             #Namun input tidak boleh terdapat spasi karena akan menambah panjang string
input()                         #Agar program tidak langsung keluar jika dibuka langsung oleh python
