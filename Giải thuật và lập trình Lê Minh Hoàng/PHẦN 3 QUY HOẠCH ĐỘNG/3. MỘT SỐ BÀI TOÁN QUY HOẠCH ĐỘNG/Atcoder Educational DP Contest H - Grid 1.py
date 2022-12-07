H,W=list(map(int,input().split()))

line=[0]*(H+1)
for i in range(1,H+1):
    line[i]=input()

dp=[]

for i in range(0,H+1):
    dp.append([])
    for j in range(0,W+1):
        dp[i].append(0)

    
dp[1][1]=1

#dp[i][j]: số cách đến ô tại hàng i cột j
for i in range(1,H+1):
    for j in range (1,W+1):
        if i!=1 or j!=1:
            if line[i][j-1]==".":
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
            else:
                dp[i][j]=0
"""for i in range(0,H+1):
    print(dp[i])"""
print(dp[H][W]%(10**9+7))