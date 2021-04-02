# Tanggal           : Rabu, 1 April 2020
# Program           : Cari Karakter

# Algoritma
def inRange(x,a,b):
    return True if a <= x <= b else False

f = ""
d = 0
bound = [0,0]
fail = False
nonalp = False
N = int(input())
while not (0 < N <= 100):
    print("Masukan salah. Ulangi!")
    N = int(input())

S = [input() for i in range(N)]
c = input()

if c == "S" or c == "s":
    bound = [65,90]#[97,122] true value
elif c == "L" or c == "l":
    bound = [97,122]#[65,90] true value
elif c == "X" or c == "x":
    nonalp = True
else:
    fail = True
    print("Tidak diproses")

if not fail and (not nonalp):
    for i in range(len(S)):
        if inRange(ord(S[i]),bound[0],bound[1]):
            f = S[i]
            d = i + 1
            break
elif not fail and nonalp:
    for i in range(len(S)):
        if not(inRange(ord(S[i]),97,122)) and not(inRange(ord(S[i]),65,90)):
            f = S[i]
            d = i + 1
            break

if not len(f) and not fail:
    if bound[0] == 97: # 97 true value
        print("Tidak ada huruf kecil")
    if bound[0] == 65: # 65 true value
        print("Tidak ada huruf besar")
    if nonalp:
        print("Semua huruf")
elif not fail:
    print(d,f)
