# Tanggal       : 29 September 2019
# Deskripsi     : Program print barisan

#Kamus
#Integer : x

#Algoritma
x = int(input("Masukkan N: "))  #Input N

for i in range(1,x+1):          #Loop dari 1 hingga n
    print(i, end=" ")           #Digunakan parameter end, agar tidak otomatis ter-new line

input()                         #Agar program tidak langsung keluar jika dibuka langsung oleh python
