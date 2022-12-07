
from collections import defaultdict


def check(edge, degree, num, k, n):
    while num > 0:
        stop = True
        for i in range(n):
            for j in range(i+1, n):
                if edge[i][j] == 0 and degree[i]+degree[j] >= k:
                    edge[i][j] = 1
                    degree[i] += 1
                    degree[j] += 1
                    if degree[i] == n-1:
                        num -= 1
                    if degree[j] == n-1:
                        num -= 1
                    stop = False
        if stop == True:
            return False
    return True


N, M = list(map(int, input().split()))

num = N
degree = defaultdict(lambda: 0)
edge = defaultdict(lambda: defaultdict(lambda: 0))
left = 0
for _ in range(M):
    u, v = list(map(int, input().split()))
    if u > v:
        u, v = v, u
    u = u-1
    v = v-1
    edge[u][v] = 1
    degree[u] += 1
    degree[v] += 1
    if degree[u] == N-1:
        num -= 1
    if degree[v] == N-1:
        num -= 1
print(degree)
print(edge)

left = 0
right = 2*N
while left < right:
    print(left, right)
    if left+1 == right:
        if check(edge, degree, num, right, N) == True:
            left = right
        break
    mid = (left+right)//2

    if check(edge, degree, num, mid, N) == True:
        left = mid
    else:
        right = mid-1
print(left)
