
from itertools import combinations


def test(matrix, use, unuse):
    cost1 = 0

    more = []
    for ly in unuse:
        temp = []
        for lyy in use:
            temp.append(matrix[ly][lyy])
        for mo in more:
            temp.append(matrix[ly][mo])
        more.append(ly)

        cost1 += min(temp)

    cost2 = 0
    unuse = unuse[::-1]
    more = []
    for ly in unuse:
        temp = []
        for lyy in use:
            temp.append(matrix[ly][lyy])
        for mo in more:
            temp.append(matrix[ly][mo])
        more.append(ly)

        cost2 += min(temp)
    return min(cost1, cost2)


n, k = list(map(int, input().split()))
matrix = []
for i in range(n+1):
    matrix.append([])
    for j in range(n+1):
        matrix[i].append(0)

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        matrix[i+1][j+1] = a[j]

if n == k:
    print(0)
else:
    # data = []
    # for i in range(1, n+1):
    #     temp = []
    #     for j in range(1, n+1):
    #         temp.append(matrix[i][j])
    #     temp.sort()
    #     temp.pop(0)
    #     data.append(temp[0])

    # data.sort()
    # # print(data)
    # res = sum(data[:n-k])
    # print(res)

    length = range(1, n+1)
    data = list(combinations(length, k))
    res = []
    for num in data:
        use = list(num)
        unuse = []
        for i in range(1, n+1):
            if i not in use:
                unuse.append(i)
        # print(use, unuse)
        # print(test(matrix, use, unuse))
        res.append(test(matrix, use, unuse))
    print(min(res))
