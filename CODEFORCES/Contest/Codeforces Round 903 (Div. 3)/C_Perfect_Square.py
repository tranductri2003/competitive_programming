t=int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)

    for i in range(n):
        s = input()
        for j in range(n):
            matrix[i][j] = s[j]

    matrix1 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix1[j][n - 1 - i] = matrix[i][j]

    matrix2 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix2[j][n - 1 - i] = matrix1[i][j]

    matrix3 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix3[j][n - 1 - i] = matrix2[i][j]
    res=0
    for i in range(n):
        for j in range(n):
            temp=[]
            temp.append(matrix[i][j])
            temp.append(matrix1[i][j])
            temp.append(matrix2[i][j])
            temp.append(matrix3[i][j])
            temp.sort()
            res+=ord(temp[-1])-ord(temp[0])+ord(temp[-1])-ord(temp[1])+ord(temp[-1])-ord(temp[2])
    print(res//4)