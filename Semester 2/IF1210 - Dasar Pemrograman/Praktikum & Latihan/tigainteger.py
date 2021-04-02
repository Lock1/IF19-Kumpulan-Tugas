# Tanggal       : Senin, 30 Maret 2020
# Dosen / Kelas : Dicky Prima Satya / 05

# Program TigaInteger
# Input: 3 integer: A, B, C
# Output: Sifat integer dari A, B, C (positif/negatif/nol dan ganjil/genap)
#         Nilai maksimum, minimum, dan nilai tengah

# KAMUS
# variabel
#    A, B, C : int
#    nilaitengah : int

# PROCEDURE DAN FUNCTION
def CekInteger (x):
    if x == 0:
        print("NOL")
    elif x < 0:
        print("NEGATIF")
    else:
        print("POSITIF-GANJIL") if x % 2 else print("POSITIF-GENAP")
# I.S.: x terdefinisi, bertype int
# F.S.: Jika x positif dan genap, maka tertulis di layar: POSITIF-GENAP
#       Jika x positif dan ganjil, maka tertulis di layar: POSITIF-GANJIL
#       Jika x negatif, maka tertulis di layar: NEGATIF
#       Jika x nol, maka tertulis di layar: NOL
# Tuliskan realisasi prosedur CekInteger di bawah ini

def Max (a, b, c):
    return max(a,max(b,c))
# menghasilkan nilai terbesar di antara a, b, c (integer)
# Tuliskan realisasi fungsi Max di bawah ini

def Min (a, b, c):
    return min(a,min(b,c))
# menghasilkan nilai terkecil di antara a, b, c (integer)
# Tuliskan realisasi fungsi Min di bawah ini

# PROGRAM UTAMA
# Input
A = int(input())
B = int(input())
C = int(input())

# Menuliskan sifat integer
CekInteger(A)
CekInteger(B)
CekInteger(C)

# Penulisan maksimum, minimum, dan nilai tengah
print(Max(A,B,C))
print(Min(A,B,C))
nilaitengah = A + B + C - Max(A,B,C) - Min(A,B,C)
print(nilaitengah)
