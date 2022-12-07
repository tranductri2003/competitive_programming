r, c = list(map(int, input().split()))
matrix = []
for i in range(r+1):
    matrix.append([])
    for j in range(c+1):
        matrix[i].append('.')
for i in range(r):
    s = input()
    for j in range(c):
        matrix[i+1][j+1] = s[j]

res = 0
if r == 1:
    for i in range(2, c):
        if matrix[1][i] == ".":
            res += 1

elif c == 1:
    for i in range(2, r):
        if matrix[i][1] == ".":
            res += 1

elif r == 2:
    for i in range(2, c):
        if matrix[1][i] == "." and matrix[2][i] == ".":
            res += 1

elif c == 2:
    for i in range(2, r):
        if matrix[i][1] == "." and matrix[i][2] == ".":
            res += 1

else:

    res = 0
    for i in range(2, r):
        for j in range(2, c):
            if matrix[i][j] == ".":
                res += 1
    stop = 0
    for i in range(2, c):
        if matrix[1][i] == "#":
            stop = 1
            break
        if matrix[r][i] == "#":
            stop = 1
            break
    for j in range(2, r):
        if matrix[j][1] == "#":
            stop = 1
            break
        if matrix[j][c] == "#":
            stop = 1
            break
    if stop == 0:
        res += 1
print(res)
