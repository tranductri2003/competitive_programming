n,m=list(map(int,input().split()))

matrix=[]

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(0)
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(0,m):
        matrix[i][j]=a[j]
        
dp=[]
#Gọi dp[i][j] là kích thước của hình vuông có góc đáy là ô [i][j].

for i in range(n):
    dp.append([])
    for j in range(m):
        dp[i].append(1)

res=1
for i in range(1,n):
    for j in range(1,m):
        if matrix[i][j]==matrix[i-1][j-1]==matrix[i-1][j]==matrix[i][j-1]:
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
            res=max(res,dp[i][j])
        else:
            dp[i][j]=1
"""for i in range(n):
    print(matrix[i])
    
print("\n\n")
for i in range(n):
    print(dp[i])"""
print(res**2)
