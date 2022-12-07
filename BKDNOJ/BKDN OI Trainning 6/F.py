from dataclasses import dataclass


n, m = list(map(int, input().split()))
matrix = []
for i in range(n+1):
    matrix.append([])
    for j in range(m+1):
        matrix[i].append(0)

data = []
for i in range(int(input())):
    x, y = list(map(int, input().split()))
    data.append((x, y))

matrix[1][1] = 1
for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 and j == 1:
            pass
        else:
            if (i, j) in data:
                matrix[i][j] = 0
            else:
                matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]

print(matrix[n][m])
