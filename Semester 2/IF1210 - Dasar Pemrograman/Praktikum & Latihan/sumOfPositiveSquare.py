# Tanggal           : Rabu, 1 April 2020
# Program           : Positive Square

# Algoritma
S = []
while True:
    temp = int(input())
    if temp != -999:
        S.append(temp**2) if temp > 0 else 0
    else:
        if not len(S):
            S.append(0)
        break

print(sum(S))
