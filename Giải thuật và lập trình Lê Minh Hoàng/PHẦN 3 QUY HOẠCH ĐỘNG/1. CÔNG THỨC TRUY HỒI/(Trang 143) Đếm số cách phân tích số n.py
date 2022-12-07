v=int(input())
dp=list()
for i in range(0,v+1):
    dp.append([])
    for j in range(0,v+1):
        dp[i].append([])

for i in range(1,v+1):
    dp[0][i]=0

dp[0][0]=1

for i in range(1,v+1):
    for j in range(0,v+1):
        if i>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j]+dp[i][j-i]



for i in range(0,v+1):
    for j in range(0,v+1):
        print(dp[i][j],end=" ")
    print(" ")
"""
for i in range(0,v+1):
    print(*dp[i])
"""