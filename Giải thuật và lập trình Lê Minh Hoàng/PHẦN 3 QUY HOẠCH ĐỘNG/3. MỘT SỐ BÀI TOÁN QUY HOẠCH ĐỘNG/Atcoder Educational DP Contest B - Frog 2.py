n,K=list(map(int,input().split()))
a=list(map(int,input().split()))
a.insert(0,0)

dp=[10**9]*(n+1)
dp[1]=0

for i in range(2,n+1):
    for j in range(i-K,i):
        if j>=1:
            dp[i]=min(dp[i],dp[j]+abs(a[j]-a[i]))

print(dp[n])

#Nộp bằng Python 3 trên VNOI sẽ bị TLE dù code đúng hoàn toàn
#Nộp bằng Pypi hoặc bất cứ nơi nào khác sẽ luôn đúng