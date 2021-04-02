# Tanggal       : Senin, 30 Maret 2020
# Dosen / Kelas : Dicky Prima Satya / 05

# Program BelahKetupat
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar belah ketupat sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan:

# KAMUS
# Variabel
#    N : int


def GambarBelahKetupat(N):
    for i in range(N):
        if (N // 2 >= i):
            print(" "*((N // 2) - i) + "*"*(2*i + 1))
        else:
            print(" "*(i - (N // 2)) + "*"*(N + 2*((N // 2) - i)))
# I.S. N > 0 dan N ganjil
# F.S. Gambar belah ketupat dengan panjang diagonal mendatar sebesar N
#      sesuai spesifikasi soal
# Lengkapilah kamus lokal dan algoritma prosedur di bawah ini


def IsValid(N):
    return True if (N > 0) and (N % 2) else False
# menghasilkan true jika N positif dan ganjil, false jika tidak
# Lengkapilah kamus lokal dan algoritma fungsi di bawah ini

# ALGORITMA PROGRAM UTAMA
N = int(input())
if (IsValid(N)):  # lengkapi dengan pemanggilan fungsi IsValid
    GambarBelahKetupat(N)    # lengkapi dengan pemanggilan prosedur GambarBelahKetupat
else: # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")
