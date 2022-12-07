N,X=list(map(int,input().split()))

P=[0]*(N+1)
C=[0]*(N+1)
for i in range(1,N+1):
    pi,ci=list(map(int,input().split()))
    P[i]=pi
    C[i]=ci

sumcost=sum(C)*2
dp=[]
for i in range(0,N+1):
    dp.append([])
    for j in range(0,sumcost+1):
        dp[i].append(0)

for i in range(0,N+1):
    dp[i][0]=0

for i in range(1,N+1):
    for j in range(1,sumcost+1):
        if j<=C[i]:
            dp[i][j]=min(P[i],dp[i-1][j])
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-C[i]]+P[i])

for i in range(0,N+1):
    print(dp[i])
for i in range(0,sumcost+1):
    if dp[N][i]>=X:
        print(i)
        quit()