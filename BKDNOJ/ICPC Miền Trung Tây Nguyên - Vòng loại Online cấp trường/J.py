n, m = list(map(int, input().split()))
a, b = list(map(int, input().split()))
matrix = []

dp = []
for i in range(m+1):
    matrix.append([])
    dp.append([])
    for j in range(n+1):
        matrix[i].append(0)
        dp[i].append(0)

for i in range(1, m+1):
    t = list(map(int, input().split()))
    for j in range(n):
        if t[j] != -1:
            matrix[i][j+1] = t[j]
        else:
            matrix[i][j+1] = 10**9


for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+matrix[i][j]

for i in range(m+1):
    print(*dp[i])


res = 10**10
for i in range(b, m+1):
    for j in range(a, n+1):
        res = min(res, dp[i][j]-dp[i-b-1][j-a-1])
print(res)
