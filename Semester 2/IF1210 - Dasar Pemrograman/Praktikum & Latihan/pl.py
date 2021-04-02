f = open('d.txt')
ctr = 1
for i in f:
    print("Line {}".format(ctr),i,end="")
    ctr += 1
    print("another line\n")
