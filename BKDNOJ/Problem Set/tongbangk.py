
a = [0]
n = int(input())
for i in range(n):
    j = int(input())
    a.append(j)
k = int(input())

matrix = []
for i in range(0, n+1):
    matrix.append([])
    for j in range(0, k+1):
        matrix[i].append(0)
for i in range(0, n+1):
    matrix[i][0] = 1

for i in range(1, n+1):
    for j in range(1, k+1):
        if matrix[i-1][j] == 1 or matrix[i-1][j-a[i]] == 1:
            matrix[i][j] = 1

if matrix[n][k] == 1:
    print("Yes")
else:
    print("No")
