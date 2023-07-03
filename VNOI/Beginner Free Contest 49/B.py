def getSaddlePoint(matrix):
    hang = []
    cot = []
    data = []
    for i in range(3):
        for j in range(3):
            data.append(matrix[i][j])

    if len(set(data)) == 1:
        return (0)
    hang.append(min(matrix[0][0], matrix[0][1], matrix[0][2]))
    hang.append(min(matrix[1][0], matrix[1][1], matrix[1][2]))
    hang.append(min(matrix[2][0], matrix[2][1], matrix[2][2]))

    cot.append(max(matrix[0][0], matrix[1][0], matrix[2][0]))
    cot.append(max(matrix[0][1], matrix[1][1], matrix[2][1]))
    cot.append(max(matrix[0][2], matrix[1][2], matrix[2][2]))

    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[i][j] == hang[i] and matrix[i][j] == cot[j]:
                return (matrix[i][j])
    return (0)


matrix = []
for _ in range(3):
    matrix.append(list(map(int, input().rstrip().split())))
print(getSaddlePoint(matrix))
