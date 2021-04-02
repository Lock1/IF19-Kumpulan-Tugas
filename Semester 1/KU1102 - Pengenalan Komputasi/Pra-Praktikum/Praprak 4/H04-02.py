# Tanggal       : 28 Oktober 2019
# Deskripsi     : matreks

# Kamus
# Integer        : n,m,c
# String         : s
# Array of int   : a

# Algoritma
n = int(input("Masukkan N: "))
m = int(input("Masukkan M: "))
# Inisiasi array dengan format
a = [[int(input("Masukkan nilai A[{}][{}]: ".format(i+1,j+1))) for j in range(m)] for i in range(n)]
c, s = 0, ""        # c adalah penghitung positif, dan s adalah string kosong untuk print
for i in range(n):  # Loop ini menghitung bilangan positif dan membuat string s untuk diprint
    for j in range(m):
        if (a[i][j] > 0):
            c += 1
        s += str(a[i][j]) + " "     # Ditambahkan spasi setiap elemennya
    s += "\n"                       # Tambahkan newline pada string
print("Ada {} bilangan positif di matriks.".format(c))
print(s)
