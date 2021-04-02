# Tanggal           : Rabu, 1 April 2020
# Program           : Harga Makanan

# Algoritma
N = int(input())
#S = [int(input()) for i in range(N)]
S = [int(input())*100 if (i+1) % 2 else int(input())*200 for i in range(N)]
#for i in range(len(S)):
#    if (i + 1) % 2:
#        S[i] *= 100
#    else:
#        S[i] *= 200

print(sum(S), "rupiah")
