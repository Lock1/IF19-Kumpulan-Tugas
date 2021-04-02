# Tanggal           : Rabu, 1 April 2020
# Program           : Segitiga

# Algoritma
S = [int(x) for x in input().split()]
print(round(0.5*S[0]*S[1])) if S[0] > 0 and S[1] > 0 else print("Alas dan tinggi harus > 0")
