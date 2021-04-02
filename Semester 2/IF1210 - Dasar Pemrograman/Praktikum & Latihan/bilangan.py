def ci(x,a,b):
    return (a <= x <= b)

N = int(input())
while not ci(N,1,100):
    print("Masukkan salah. Ulangi!")
    N = int(input())

S = [int(input()) for i in range(N)]
c = int(input())

if c == 0:
    for i in range(N):
        if S[i] == 0:
            print(i+1,0)
            break
    else:
        print("Tidak ada 0")
elif c == 1:
    for i in range(N):
        if S[i] > 0:
            print(i+1,S[i])
            break
    else:
        print("Tidak ada positif")
elif c == -1:
    for i in range(N):
        if S[i] < 0:
            print(i+1,S[i])
            break
    else:
        print("Tidak ada negatif")
else:
    print("Tidak diproses")
