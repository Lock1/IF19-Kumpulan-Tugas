# Tanggal       : 28 Oktober 2019
# Deskripsi     : puscal

# Kamus
# Integer        : n
# Array of int   : a

# Algoritma
n = int(input("Masukkan N: "))
# Penginisasian array mengunakan operator logika
a = [[1 if ((((i) or (j)) and not(i and j)) or not(i and j)) else 0 for j in range(n)] for i in range(n)]
# 1 jika i atau j adalah 0 dan bukan keduanya adalah 0, atau keduanya adalah 0, selain itu 0
# 1 if (i xor j) or not(i and j) else 0
for i in range(n):
    for j in range(n):
        if (j < n-1) and (i < n-1):         # Pencegahan indeks berlebih
            a[i+1][j+1] = a[i][j+1] + a[i+1][j]
        print(a[i][j], end =" ")            # Print elemen array
    print()                                 # Print newline untuk baris baru
