# Tanggal       : 13 Oktober 2019
# Deskripsi     : Program cek anagram

#Kamus
#Array of Integer   : a,b,k
#Integer            : na, nb

#Algoritma
#"Asumsikan elemen pada array A dan B maksimal 10"
#Inisiasi kamus k, a dan b setelah itu input elemen a dan b
k,a,b = [0 for i in range(11)],[],[]
na = int(input("Masukkan banyak elemen A: "))
for i in range(na):
    print("Masukkan elemen A ","ke-",i+1,": ",end="",sep="")
    a.append(int(input()))

nb = int(input("Masukkan banyak elemen B: "))
for i in range(nb):
    print("Masukkan elemen B ","ke-",i+1,": ",end="",sep="")
    b.append(int(input()))


#Pengecekan kondisi jika panjang beda
if len(a) != len(b):
    print("A bukan anagram dari B")
else:
    #Setiap elemen akan menambahkan 1 dan mengurangi 1 pada indeks miliknya, jika k hanya memiliki elemen 0 maka setiap angka pada a dan b memiliki banyak yang sama
    for i in a:
        k[i] += 1
    for i in b:
        k[i] -= 1
    if k.count(0) == len(k):
        print("A adalah anagram dari B")
    else:
        print("A bukan anagram dari B")
    #Metode count(x) menghitung berapa jumlah elemen x pada suatu list

#Algoritma alternatif dengan metode sort()
#else:
    #a.sort()
    #b.sort()
    #if a == b:
        #print("A adalah anagram dari B")
    #else:
        #print("A bukan anagram dari B")
