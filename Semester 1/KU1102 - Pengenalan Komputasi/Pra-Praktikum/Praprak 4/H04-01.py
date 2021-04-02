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
while a <= b:                           # Loop mengeprint hingga a = b
    print("f({})".format(a),"=",f(a))   # Print f(a) = a
    a += 1
