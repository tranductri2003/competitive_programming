N,X=list(map(int,input().split()))

P=[0]*(N+1)
C=[0]*(N+1)
for i in range(1,N+1):
    pi,ci=list(map(int,input().split()))
    P[i]=pi
    C[i]=ci

dp=[]
for i in range(0,N+1):
    dp.append([])
    for j in range(0,X+1):
        dp[i].append(10**9)

for i in range(0,N+1):
    dp[i][0]=0
for i in range(1,N+1):
    for j in range(1,X+1):
        dp[i][j]=min(dp[i-1][j],dp[i][j-P[i]]+C[i])

print(dp[N][X])