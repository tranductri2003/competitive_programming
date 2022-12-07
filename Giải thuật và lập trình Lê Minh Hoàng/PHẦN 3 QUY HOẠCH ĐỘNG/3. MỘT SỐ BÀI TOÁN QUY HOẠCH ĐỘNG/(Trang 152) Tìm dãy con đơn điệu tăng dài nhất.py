n=int(input())
a=list(map(int,input().split()))
a=[-999999]+a+[999999]
dp=[0]*(n+2)
dp[n+1]=1

for i in range(n,-1,-1):
    current=-9999
    for j in range(i+1,n+2):
        if a[i]<a[j] and dp[j]>current:
            dp[i]=dp[j]+1
            current=dp[j]
print(dp[0]-2)