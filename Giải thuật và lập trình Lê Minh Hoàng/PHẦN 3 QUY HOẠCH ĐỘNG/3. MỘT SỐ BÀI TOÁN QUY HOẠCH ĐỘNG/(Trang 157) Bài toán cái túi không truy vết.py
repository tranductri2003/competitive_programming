n,M=list(map(int,input().split()))
w=[0]*(n+1)
v=[0]*(n+1)
for i in range(1,n+1):
    w[i],v[i]=list(map(int,input().split()))

dp=[]
for i in range(0,n+1):
    dp.append([])
    for j in range(0,M+1):
        dp[i].append([])

for i in range(0,M+1):
    dp[0][i]=0

for i in range(1,n+1):
    for j in range(0,M+1):
        if j<w[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],v[i]+dp[i-1][j-w[i]])
'''
for i in range(0,n+1):
    print(dp[i])
'''
print(dp[n][M])