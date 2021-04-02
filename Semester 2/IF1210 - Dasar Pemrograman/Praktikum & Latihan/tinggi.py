# Tanggal           : Rabu, 1 April 2020
# Program           : Tinggi

# Algoritma
S = []
kurangtinggi = 0
ketinggian = 0
while True:
    temp = int(input())
    if temp != -999:
        S.append(temp) if 100 <= temp <= 300 else 0
    else:
        if not len(S):
            print("Data kosong")
        else:
            for i in S:
                if i <= 150:
                    kurangtinggi += 1
                elif i >= 170:
                    ketinggian += 1
            print(len(S))
            print(kurangtinggi)
            print(ketinggian)
            print(round(sum(S)/len(S)))
        break
