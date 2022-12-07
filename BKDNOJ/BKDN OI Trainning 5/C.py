n = int(input())
current = 1
res = 1
matrix = []
for i in range(4):
    matrix.append([])
    for j in range(3):
        matrix[i].append(0)

matrix[0][1] = 1
matrix[1][0] = 4
matrix[1][1] = 2
matrix[1][2] = 3
matrix[2][1] = 6
matrix[3][1] = 5


for i in range(n):
    s = input()
    if s == "North":
        a, b, c, d = matrix[0][1], matrix[1][1], matrix[2][1], matrix[3][1]
        matrix[0][1] = b
        matrix[1][1] = c
        matrix[2][1] = d
        matrix[3][1] = a
    if s == "South":
        a, b, c, d = matrix[0][1], matrix[1][1], matrix[2][1], matrix[3][1]
        matrix[1][1] = a
        matrix[2][1] = b
        matrix[3][1] = c
        matrix[0][1] = d
    if s == "East":
        a, b, c, d = matrix[0][1], matrix[1][2], matrix[2][1], matrix[1][0]
        matrix[0][1] = d
        matrix[1][2] = a
        matrix[2][1] = b
        matrix[1][0] = c
    if s == "West":
        a, b, c, d = matrix[0][1], matrix[1][2], matrix[2][1], matrix[1][0]
        matrix[0][1] = b
        matrix[1][2] = c
        matrix[2][1] = d
        matrix[1][0] = a
    if s == "Right":
        a, b, c, d = matrix[1][0], matrix[1][1], matrix[1][2], matrix[3][1]
        matrix[1][0] = b
        matrix[1][1] = c
        matrix[1][2] = d
        matrix[3][1] = a
    if s == "Left":
        a, b, c, d = matrix[1][0], matrix[1][1], matrix[1][2], matrix[3][1]
        matrix[1][0] = d
        matrix[1][1] = a
        matrix[1][2] = b
        matrix[3][1] = c
    res += matrix[0][1]
print(res)
