# Tanggal    : Selasa, 17 September 2019
# Deskripsi  : Program Kalkulator singkat


#Program Kalkulator

#Kamus
#integer : a,b
#string : o


#Algoritma

a = int(input("Masukkan bilangan bulat pertama: "))
b = int(input("Masukkan bilangan bulat kedua: "))
o = input("Masukkan operator: ")

print (a, "", end='')           #Print nilai bilangan pertama dan spasi saja, tanpa enter

#Cek operator
if (o == "+"):
    a += b
elif (o == "-"):
    a -= b
elif (o == "*"):
    a *= b
elif (o == "/"):
    a //= b
elif (o == "%"):
    a %= b
else:
    print("Operator tidak ada")

print(o, b, "=", a)             #Print operator, bilangan kedua sama dengan hasilnya
input()                         #Agar program tidak langsung exit ketika hasil operator selesai diprint
