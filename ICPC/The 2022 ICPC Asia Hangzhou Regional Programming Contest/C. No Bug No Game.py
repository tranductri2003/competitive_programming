from collections import defaultdict 

# Khai báo và khởi tạo dp với giá trị mặc định
dp = [[[-1e9 for _ in range(2)] for _ in range(3005)] for _ in range(3005)]

# Khai báo và khởi tạo w với giá trị mặc định
w = [[0 for _ in range(3005)] for _ in range(3005)]

# Khai báo và khởi tạo p
p = [0 for _ in range(3005)]


n,k = list(map(int,input().split()))

for i in range(1,n+1):
    a = list(map(int,input().split()))
    p[i] =a[0]
    for j in range(1,p[i]+1):
        w[i][j] = a[j]

for i in range(n+1):
    for j in range(1,k+1):
        dp[i][j][0] = dp[i][j][1] = -10**9
        
dp[0][0][0]=0
for i in range(1,n+1):
    for j in range(0,k+1):
        dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][0])
        dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][1])
        
        if j>=p[i]:
            dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-p[i]][0]+w[i][p[i]])
            dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-p[i]][1]+w[i][p[i]])
        
        for h in range(1,p[i]+1):
            if j>=h:
                dp[i][j][1] = max(dp[i][j][1],dp[i-1][j-h][0]+w[i][h])
            
res =0
for i in range(1,n+1):
    for j in range(0,k+1):
        res = max(res, dp[i][j][0])
        
        if j==k:
            res = max(res,dp[i][j][1])

print(res)
        
    