#Simple matrix calculator

######################### Function #########################
#Pop function , eliminating column in index x and row in index 0, returning integer array M with size (n-1)*(n-1), *note to self, extended pop with y arg
# NOTE! x and y does not represent column and row (my bad xd)
def pop(A,x,y):
    M = [[0 for i in range(len(A)-1)] for j in range(len(A)-1)]
    i, j, k, l = 0, 0, 0, 0
    while i < len(A):
        j, k = 0, 0
        if i == y:
            i += 1
            continue
        while j < len(A):
            if j == x:
                j += 1
                continue
            M[l][k] = A[i][j]
            j += 1
            k += 1
        i += 1
        l += 1
    return M

#Determinant function, calculating using cofactor method and recursion
def det(A):
    if len(A) == 2:
        return (A[0][0]*A[1][1]-A[1][0]*A[0][1])
    else:
        sum = 0
        for i in range(len(A)):
             sum += A[0][i]*det(pop(A,i,0))*((-1)**i)
        return sum

#Transpose function, just for square matrix
def trp(A):
    T = [[0 for i in range(len(A))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            T[i][j]= A[j][i]
    return T

#Inverse function, filter any matrices that having determinant 0, else inverse function will raise divisionbyzero
#First loop directly calculate minor and its sign, second loop calculating inverse
def inv(A):
    if len(A) == 1:
        return (1/A[0][0])
    InvDeterminant = 1 / det(A)
    Cofactor = [[0 for i in range(len(A))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            Cofactor[i][j] = det(pop(A,j,i))*((-1)**(i+j))
    Adjoint = trp(Cofactor)
    for i in range(len(A)):
        for j in range(len(A)):
            Adjoint[i][j] *= InvDeterminant
    return Adjoint

def prt(A):
    for i in range(len(A)):
        for j in range(len(A)):
            print(A[i][j], end =" ")
        print()



######################### Main #########################
#Variable initialization, c is menu list, inMemory checking matrix is still in memory or not
c = 0
inMemory = False

#Main menu loop
while True:
    print("Determinan dan invers matriks")
    print("1. Determinan")
    print("2. Invers")
    if c == 1 :
        print("3. Bersihkan matriks")
        print("4. Tampilkan matriks")
        print("5. Keluar")
    else:
        print("3. Keluar")
    #Input handler
    n = input(">>> ")
    try:
        n = int(n)
    except ValueError:
        print("Masukan tidak diketahui")
        print()
        continue
    else:
        n = int(n)

#############  Input check  #############
    #Exit check
    if (c == 0) and (n == 3):
        print(";)")
        exit()
    elif (c == 1) and (n == 5):
        print(":D")
        exit()

    #Case for determinant menu
    if n == 1:
        if not(inMemory):
            # Matrix Initialization Block #
            n = int(input("Masukkan ukuran matriks persegi : "))
            A = [[0 for i in range(n)] for j in range(n)]
            for i in range(len(A)):
                for j in range(len(A)):
                    print("Masukkan elemen baris", i+1, "dan kolom", j+1, ": ", end="")
                    A[i][j] = int(input())
            inMemory = True
            ############# end #############
        print("Matriks memiliki determinan : ",det(A))
        c = 1
    #Case for inverse menu
    elif n == 2:
        if not(inMemory):
            # Matrix Initialization Block #
            n = int(input("Masukkan ukuran matriks persegi : "))
            A = [[0 for i in range(n)] for j in range(n)]
            for i in range(len(A)):
                for j in range(len(A)):
                    print("Masukkan elemen baris", i+1, "dan kolom", j+1, ": ", end="")
                    A[i][j] = int(input())
            inMemory = True
            ############# end #############
        if len(A) == 1:
            print("Invers matriksnya adalah skalar")
            print(inv(A))
        elif det(A) == 0:
            print("Matriks tidak mempunyai invers")
        else:
            print("Invers matriksnya adalah")
            prt(inv(A))
        c = 1
    #Case for deleting matrix
    elif (n == 3) and (c == 1):
        del A
        inMemory = False
        c = 0
    #Case for printing matrix
    elif (n == 4) and (c == 1):
        prt(A)
    else:
        print("Masukkan tidak diketahui")
    print()
