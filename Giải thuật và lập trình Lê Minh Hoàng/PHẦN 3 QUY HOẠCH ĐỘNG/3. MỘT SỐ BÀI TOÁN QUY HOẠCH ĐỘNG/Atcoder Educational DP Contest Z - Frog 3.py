n,C=list(map(int,input().split()))
a=list(map(int,input().split()))
a.insert(0,0)

dp=[10**13]*(n+1)
dp[1]=0

for i in range(2,n+1):
    for j in range(1,i):
        dp[i]=min(dp[i],dp[j]+(a[i]-a[j])**2+C)

print(dp[n])

#Đương nhiên là bị TLE rồi