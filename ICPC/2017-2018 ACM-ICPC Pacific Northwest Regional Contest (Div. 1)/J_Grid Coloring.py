
from collections import defaultdict
n,m = list(map(int,input().split()))
matrix = defaultdict(lambda: defaultdict(lambda: "."))
dp = defaultdict(lambda: defaultdict(lambda: 1))

for i in range(n):
    s=input()
    for j in range(m):
        matrix[i+1][j+1]=s[j]

for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i][j]=="B":
            for xi in range(1,i+1):
                for xj in range(1,j+1):
                    if matrix[xi][xj]=="R":
                        print(0)
                        quit()
                    else:
                        matrix[xi][xj] = "B"
        elif matrix[i][j]=="R":
            for xi in range(i,n+1):
                for xj in range(j,m+1):
                    if matrix[xi][xj]=="B":
                        print(0)
                        quit()
                    else:
                        matrix[xi][xj] = "R"
for i in range(n,0,-1):
    for j in range(1,m+1):
        if matrix[i][j]==".":
            dp[i][j]=dp[i+1][j]+dp[i][j-1]
        elif matrix[i][j]=="B":
            dp[i][j]=dp[i+1][j]
        else:
            dp[i][j]=dp[i][j-1]

print(dp[1][m])
                    