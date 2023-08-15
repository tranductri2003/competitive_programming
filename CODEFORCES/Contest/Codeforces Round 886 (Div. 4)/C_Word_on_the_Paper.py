t = int(input())
for _ in range(t):
    matrix = []
    for i in range(8):
        matrix.append([])
        for j in range(8):
            matrix[i].append(0)
    for i in range(8):
        s = input()
        for j in range(8):
            matrix[i][j] = s[j]

    startRow = 0
    startCollumn = 0
    stop = False
    for i in range(8):
        if stop == True:
            break
        for j in range(8):

            if matrix[i][j] != ".":
                startRow = i
                startCollumn = j
                stop = True
                break

    res = ""
    for i in range(startRow, 8):
        if matrix[i][startCollumn] == ".":
            break
        else:
            res += matrix[i][startCollumn]

    print(res)
