# Tanggal           : Rabu, 1 April 2020
# Program           : Umur

# Algoritma
S = [int(input()) for i in range(20)]
for i in range(20):
    print("[P{}]{}".format(i+1,S[i]))
print("Tertinggi =",max(S))
print("Terendah =",min(S))
