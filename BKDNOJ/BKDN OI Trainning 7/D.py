def show(matrix, r, c):
    for i in range(r+1):
        print(*matrix[i])


def test(matrix, r, c):
    res = 0
    for i in range(1, c+1):
        so0 = 0
        for j in range(1, r+1):
            if matrix[j][i] == 0:
                so0 += 1
        res += max(so0, r-so0)
    return res


r, c = list(map(int, input().split()))
n = 5

data = []
for i in range(2**r, 2**(r+1)):
    data.append(bin(i)[3:])


matrix = []
res = 0
for i in range(r+1):
    matrix.append([])
    for j in range(1+c):
        matrix[i].append(0)

for i in range(r):
    a = list(map(int, input().split()))
    for j in range(c):
        matrix[i+1][j+1] = a[j]


res = 0

for num in data:
    temp = []
    for i in range(r+1):
        temp.append([])
        for j in range(1+c):
            temp[i].append(matrix[i][j])
    for i in range(len(num)):
        if num[i] == "0":
            pass
        else:  # hang i bi doi
            for j in range(1, c+1):
                temp[i+1][j] = 1-temp[i+1][j]
    # show(temp, r, c)
    res = max(res, test(temp, r, c))

print(res)
