def show():
    for i in range(8):
        print(*matrix[i])


t = int(input())

for _ in range(t):
    space = input()
    matrix = []
    for i in range(8):
        matrix.append([])
        for j in range(8):
            matrix[i].append(0)

    for i in range(8):
        s = input()
        for j in range(8):
            matrix[i][j] = s[j]
    # show()
    res = ""
    for i in range(8):
        data = []
        for j in range(8):
            data.append(matrix[i][j])
        if len(set(data)) == 1 and data[0] != ".":
            res = data[0]
            break
    for j in range(8):
        data = []
        for i in range(8):
            data.append(matrix[i][j])
        if len(set(data)) == 1 and data[0] != ".":
            res = data[0]
            break
    print(res)
