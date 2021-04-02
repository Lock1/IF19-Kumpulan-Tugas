x = int(input("::"))

a = 1
while a < x:
    b = 2
    while b < x:
        if (a ** b) == x:
            print("Bilangan indah")
            break
        b += 1
    if (a ** b) == x:
        break
    a += 1
else:
    print("Bukan bil indah")

input()
