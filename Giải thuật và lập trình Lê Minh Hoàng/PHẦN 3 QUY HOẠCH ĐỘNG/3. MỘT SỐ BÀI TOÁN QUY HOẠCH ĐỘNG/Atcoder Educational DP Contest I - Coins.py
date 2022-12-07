n=int(input())
a=list(map(float,input().split()))
a=[0]+a


dp=[]
for i in range(0,n+1):
    dp.append([])
    for j in range(0,n+1):
        dp[i].append(0)



tich=1
for i in range(1,n+1):
    tich=tich*a[i]
    dp[i][i]=tich
tich=1
for i in range(1,n+1):
    tich=tich*(1-a[i])
    dp[i][0]=tich

#dp[i][j]: Xác suất lia i coin và nhận được j mặt ngửa
for i in range(2,n+1):
    for j in range(1,i):
        dp[i][j]=dp[i-1][j-1]*a[i]+dp[i-1][j]*(1-a[i])
        #Lia được i-1 lần, ngửa j-1 lần và lia trúng
        #Lia được i-1 lần, ngửa j lần và lia trật

"""for i in range(0,n+1):
    print(*dp[i])
"""
res=0
for i in range(n//2+1,n+1):
    res+=dp[n][i]
print(res)