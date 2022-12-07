n = int(input())
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        matrix[i][j] = a[j]
res = 0
for i in range(n):
    for j in range(n):
        res += matrix[i][j]


data = []
for i in range(n):
    data.append(matrix[i][n-1-i])
print(res-min(data))
