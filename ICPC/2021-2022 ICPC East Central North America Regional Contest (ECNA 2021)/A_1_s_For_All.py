from collections import defaultdict
cost = [-1] * 150001

cost[0] = 9999999
cost[1] = 1
cost[2] = 2
cost[3] = 3
cost[4] = 4
cost[5] = 5
cost[6] = 5
cost[7] = 7
cost[8] = 6
cost[9] = 6


n = int(input())


def solve(i):
    temp = 10**9

    # Nhan
    j = 2
    while j*j <= i:
        if i % j == 0:
            temp = min(temp, cost[j]+cost[i//j])
        j += 1

    # Noi
    if i > 9:
        c = cost[i % 10] + cost[i//10]
        if c < temp:
            temp = c

    if i > 99:
        c = cost[i % 100] + cost[i // 100]
        if c < temp and i % 100 > 9:
            temp = c

    if i > 999:
        c = cost[i % 1000] + cost[i // 1000]
        if c < temp and i % 1000 > 99:
            temp = c

    if i > 9999:
        c = cost[i % 10000] + cost[i // 10000]
        if c < temp and i % 10000 > 999:
            temp = c
    # Cong
    for j in range(1, i//2+1):
        temp = min(temp, cost[j]+cost[i-j])

    cost[i] = temp


for i in range(2, n+1):
    solve(i)
    # print(cost)
print(cost[n])
