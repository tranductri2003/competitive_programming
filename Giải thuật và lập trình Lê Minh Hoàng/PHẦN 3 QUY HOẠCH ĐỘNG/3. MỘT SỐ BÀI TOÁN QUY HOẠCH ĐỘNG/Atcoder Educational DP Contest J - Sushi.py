"""
Let dp[x][y][z] represent the expected moves for x number of plates 1-sushi remaining, y number of plates 2-sushi remaining, z number of plates 3-sushi remaining.

Then, we can use the relation

dp[x][y][z]=n+x⋅dp[x−1][y][z]+y⋅dp[x+1][y−1][z]+z⋅dp[x][y+1][z−1]
Note that we add 1 for the y and z equations because we take from one sushi platter which transitions into one more sushi in another grouping of either x,y. For example, by taking one sushi away from a group of size 2 then there is a corresponding increase in a sushi group of size 1.

"""
N=int(input())
x=0
y=0
z=0
a=list(map(int,input().split()))
for num in a: 
    if num==1:
        x+=1
    elif num==2:
        y+=1
    else:
        z+=1
dp=[]

for i in range(0,x):
    dp.append([])
    for j in range(0,y):
        dp[i].append([])
        for k in range(0,z):
            dp[i][j].append(0)

for i in range(0,x):
    for j in range(0,y):
        for k in range(0,z):
            if i<0 or j<0 or k<0:
                dp[i][j][k]=0
            if i==0 and j==0 and k==0:
                dp[i][j][k]=0
            else:
                dp[i][j][k]=((N+i*dp[i-1][j][k]+j*dp[i+1][j-1][k]+k*dp[i][j+1][k-1]))/(i+j+k)
            print(dp)

for i in range(0,x):
    for j in range(0,y):
        print(dp[i][j])