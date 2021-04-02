# Tanggal       : 28 Oktober 2019
# Deskripsi     : fongsi

# Kamus
# Integer        : a,b
# Fungsi
def f(x):
    return (x**2-2*x+5)
# Algoritma
a = int(input("Masukkan A: "))
b = int(input("Masukkan B: "))

if (a < b):
    while a <= b:
        print("f({})".format(a),"=",f(a))
        a += 1
else:
    print("Masukan tidak valid")
