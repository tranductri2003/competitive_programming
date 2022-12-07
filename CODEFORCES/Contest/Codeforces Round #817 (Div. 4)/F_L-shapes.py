def show(matrix, n, m):
    for i in range(1, n+1):
        print(*matrix[i][1:m+1])


def check(matrix, n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            # print(i, j)
            if matrix[i][j] == "*":
                if matrix[i+1][j] == "*" and matrix[i+1][j+1] == "*":
                    # TH1:
                    # *
                    # **
                    # print('th1')
                    for k in range(j-1, j+2):
                        if matrix[i-1][k] == "*":
                            return False
                    for k in range(j-1, j+3):
                        if matrix[i+2][k] == "*":
                            return False
                    if matrix[i][j-1] == "*" or matrix[i][j+1] == "*" or matrix[i][j+2] == "*":
                        return False
                    if matrix[i+1][j-1] == "*" or matrix[i+1][j+2] == "*":
                        return False

                    matrix[i+1][j] = "."
                    matrix[i+1][j+1] = "."
                    matrix[i][j] = "."
                elif matrix[i+1][j] == "*" and matrix[i+1][j-1] == "*":
                    # TH2:
                    #  *
                    # **
                    # print('th2')
                    for k in range(j-1, j+2):
                        if matrix[i-1][k] == "*":
                            return False
                    for k in range(j-2, j+2):
                        if matrix[i+2][k] == "*":
                            return False
                    if matrix[i][j-2] == "*" or matrix[i][j-1] == "*" or matrix[i][j+1] == "*":
                        return False
                    if matrix[i+1][j-2] == "*" or matrix[i+1][j+1] == "*":
                        return False
                    matrix[i+1][j] = "."
                    matrix[i+1][j-1] = "."
                    matrix[i][j] = "."
                elif matrix[i][j+1] == "*" and matrix[i+1][j+1] == "*":
                    # TH3:
                    # **
                    #  *
                    # print('th3')
                    for k in range(j-1, j+3):
                        if matrix[i-1][k] == "*":
                            return False
                    for k in range(j, j+3):
                        if matrix[i+2][k] == "*":
                            return False
                    if matrix[i][j-1] == "*" or matrix[i][j+2] == "*":
                        return False
                    if matrix[i+1][j-1] == "*" or matrix[i+1][j] == "*" or matrix[i+1][j+2] == "*":
                        return False
                    matrix[i][j+1] = "."
                    matrix[i+1][j+1] = "."
                    matrix[i][j] = "."
                elif matrix[i][j+1] == "*" and matrix[i+1][j] == "*":
                    # TH4:
                    # **
                    # *
                    # print('th4')
                    for k in range(j-1, j+3):
                        if matrix[i-1][k] == "*":
                            return False
                    for k in range(j-1, j+2):
                        if matrix[i+2][k] == "*":
                            return False
                    if matrix[i][j-1] == "*" or matrix[i][j+2] == "*":
                        return False
                    if matrix[i+1][j-1] == "*" or matrix[i+1][j+1] == "*" or matrix[i+1][j+2] == "*":
                        return False
                    matrix[i][j+1] = "."
                    matrix[i+1][j] = "."
                    matrix[i][j] = "."
                else:
                    # print('th5')
                    # show(matrix, n, m)
                    return False
    return True


t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    matrix = []
    for i in range(n+2):
        matrix.append([])
        for j in range(m+2):
            matrix[i].append(".")
    for i in range(n):
        s = input()
        for j in range(m):
            matrix[i+1][j+1] = s[j]
    if check(matrix, n, m):
        print("YES")
    else:
        print("NO")
