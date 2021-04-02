from time import *

s = int(input())

start1 = time()

def f(n):
    return 1 if n <= 2 else f(n-1) + f(n-2)

end1 = time()
print("Fib s:",f(s))
print("Elapsed:", end1-start1)

start2 = time()

a, b = 1, 1
for i in range(s//2):
    a,b = a+b,b+a

end2 = time()

print("Fib s:",a, "and", b)
print("Elapsed:", end2-start2)

start3 = time()

end3 = time()
