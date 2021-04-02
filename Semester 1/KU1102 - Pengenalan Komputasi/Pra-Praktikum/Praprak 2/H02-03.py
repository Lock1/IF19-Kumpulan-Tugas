# Tanggal       : 29 September 2019
# Deskripsi     : Program cek prima

#Kamus
#Integer : x, i

#Algoritma
x = int(input("Masukkan X: "))          #Input
i = 3
if (x > 1) and (x <= 3):                #Mengecek kondisi untuk x = 2 dan 3, dan mengecek x bukan bilangan genap
    print(x,"adalah bilangan prima")
elif (x % 2 == 0):
    print(x,"bukan bilangan prima")
else:
    while (i < x):                      #Loop mengecek dari 3 hingga x-2
        if (x % i == 0):
            print(x,"bukan bilangan prima")
            break
        elif (i == x - 2):
            print(x,"adalah bilangan prima")
            break                       #Break agar mengeluarkan dari loop while
        i += 2                          #Karena tidak perlu mengecek bilangan genap
input()                                 #Agar program tidak langsung keluar jika dibuka langsung oleh python
