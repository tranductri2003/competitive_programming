n, m, M = list(map(int, input().split()))
res = [0]*(n+1)
res[0] = 1
for i in range(1, m+1):
    for j in range(i, n+1):
        res[j] = res[j]+res[j-i]
    # print(f"số đống là {i}", res[1:])

print(res[n] % M)
