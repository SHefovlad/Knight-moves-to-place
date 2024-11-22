N = 20

def PoleOld(N):
    matrix = []
    for i in range(0, N):
        matrix.append([])
        for j in range(0, N):
            matrix[i].append(0)

    matrix[N-1][0] = 'N'

    for i in range(0, N):
        for j in range(0, N):
            if matrix[i][j] == 'N':
                if i+2 < N and i+2 >= 0 and j+1 < N and j+1 >=0 and matrix[i+2][j+1] == 0: matrix[i+2][j+1] = 1
                if i+1 < N and i+1 >= 0 and j+2 < N and j+2 >=0 and matrix[i+1][j+2] == 0: matrix[i+1][j+2] = 1
                if i-1 < N and i-1 >= 0 and j-2 < N and j-2 >=0 and matrix[i-1][j-2] == 0: matrix[i-1][j-2] = 1
                if i-2 < N and i-2 >= 0 and j-1 < N and j-1 >=0 and matrix[i-2][j-1] == 0: matrix[i-2][j-1] = 1
                if i+1 < N and i+1 >= 0 and j-2 < N and j-2 >=0 and matrix[i+1][j-2] == 0: matrix[i+1][j-2] = 1
                if i-2 < N and i-2 >= 0 and j+1 < N and j+1 >=0 and matrix[i-2][j+1] == 0: matrix[i-2][j+1] = 1
                if i-1 < N and i-1 >= 0 and j+2 < N and j+2 >=0 and matrix[i-1][j+2] == 0: matrix[i-1][j+2] = 1
                if i+2 < N and i+2 >= 0 and j-1 < N and j-1 >=0 and matrix[i+2][j-1] == 0: matrix[i+2][j-1] = 1
    for k in range(1, N):
        for i in range(0, N):
            for j in range(0, N):
                if matrix[i][j] == k:
                    if i+2 < N and i+2 >= 0 and j+1 < N and j+1 >=0 and matrix[i+2][j+1] == 0: matrix[i+2][j+1] = k+1
                    if i+1 < N and i+1 >= 0 and j+2 < N and j+2 >=0 and matrix[i+1][j+2] == 0: matrix[i+1][j+2] = k+1
                    if i-1 < N and i-1 >= 0 and j-2 < N and j-2 >=0 and matrix[i-1][j-2] == 0: matrix[i-1][j-2] = k+1
                    if i-2 < N and i-2 >= 0 and j-1 < N and j-1 >=0 and matrix[i-2][j-1] == 0: matrix[i-2][j-1] = k+1
                    if i+1 < N and i+1 >= 0 and j-2 < N and j-2 >=0 and matrix[i+1][j-2] == 0: matrix[i+1][j-2] = k+1
                    if i-2 < N and i-2 >= 0 and j+1 < N and j+1 >=0 and matrix[i-2][j+1] == 0: matrix[i-2][j+1] = k+1
                    if i-1 < N and i-1 >= 0 and j+2 < N and j+2 >=0 and matrix[i-1][j+2] == 0: matrix[i-1][j+2] = k+1
                    if i+2 < N and i+2 >= 0 and j-1 < N and j-1 >=0 and matrix[i+2][j-1] == 0: matrix[i+2][j-1] = k+1
    
    return matrix

def Formule(y, x):
    M = 0
    x = abs(x); y = abs(y)
    p, q = 0, 0
    p = (y - 2 * x) / -3
    q = x - 2 * p

    if abs(2 * x) >= y and abs(2 * y) >= x:
        M = p + q + (x + y) % 3
    else:
        if x > y:
            if y == 0:
                if x % 4 == 0:
                    M = x
                else:
                    M = x - (x // 4 * 2)
            else:
                if x % 4 == 1:
                    M = x - (2 * x / 4 - 2)
                    if y % 2 == 0: M -= 1
                if x % 4 == 2:
                    M = x - (2 * x / 4 - 1)
                    if y % 2 == 1: M -= 1
                if x % 4 == 3:
                    M = x - (2 * x / 4 - 2)
                    if y % 2 == 1: M -= 1

            if x % 4 == 0:
                M = x / 2
                if y % 2 == 1:
                    M += 1
        elif y > x:
            if x == 0:
                if y % 4 == 0:
                    M = y
                else:
                    M = y - (y // 4 * 2)
            else:
                if y % 4 == 1:
                    M = y - (2 * y / 4 - 2)
                    if x % 2 == 0: M -= 1
                if y % 4 == 2:
                    M = y - (2 * y / 4 - 1)
                    if x % 2 == 1: M -= 1
                if y % 4 == 3:
                    M = y - (2 * y / 4 - 2)
                    if x % 2 == 1: M -= 1

            if y % 4 == 0:
                M = y / 2
                if x % 2 == 1:
                    M += 1

    return int(M)
    return M

def PR():
    for i in range(0, N):
        for j in range(0, N):
            if matrix[i][j] == 'N':
                print('  N', end = '')
                continue
            #if matrix[i][j] <= 9: print(" ", end = '')
            print("{:3}".format(matrix[i][j]), end = '')
        print()
    print()

    matrix2 = PoleOld(N)


    for i in range(0, N):
        for j in range(0, N):
            if matrix[i][j] == 'N':
                print('  N', end = '')
                continue
            #if matrix[i][j] <= 9: print(" ", end = '')
            print("{:3}".format(matrix2[i][j]), end = '')
        print()
    print()


    for i in range(0, N):
        for j in range(0, N):
            if matrix[i][j] != matrix2[i][j]:
                if matrix[i][j] == 'N':
                    print('  N', end = '')
                    continue
                #if matrix[i][j] <= 9: print(" ", end = '')
                print("{:5}".format(str(matrix[i][j]) + '-' + str(matrix2[i][j])), end = '')
            else: print("  K  ", end = '')
        print()
    print()

matrix = []
for i in range(0, N):
    matrix.append([])
    for j in range(0, N):
        matrix[i].append(Formule(N - i - 1, j))

while True:
    (x, y) = input("Введите x и y через пробел - ").split(" ")
    print(Formule(int(x), int(y)))
