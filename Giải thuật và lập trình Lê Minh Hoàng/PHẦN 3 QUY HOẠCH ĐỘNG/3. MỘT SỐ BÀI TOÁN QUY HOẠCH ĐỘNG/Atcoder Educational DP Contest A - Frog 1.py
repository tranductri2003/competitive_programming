'''
n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
dp[1]=abs(a[1]-a[0])
for i in range(2,n):
    dp[i]=min((dp[i-1]+abs(a[i-1]-a[i]),(dp[i-2]+abs(a[i-2]-a[i]))))

print(dp[n-1])
'''

n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
dp=[0]*(n+1)
dp[1]=0   #Chi phí đến hòn đá 1 bằng 0
dp[2]=abs(a[2]-a[1])      #Chi phí đến hòn đá 2 bằng h2-h1
#dp[i]: chi phí ít nhất để đến hòn đá thứ i
for i in range(3,n+1):
    dp[i]=min((dp[i-1]+abs(a[i-1]-a[i]),(dp[i-2]+abs(a[i-2]-a[i]))))

print(dp[n])



'''
Cách tổng quát:
n=int(input())
K=2
a=list(map(int,input().split()))
a.insert(0,0)

dp=[10**9]*(n+1)
dp[1]=0
dp[2]=abs(a[2]-a[1])

for i in range(3,n+1):
    for j in range(i-K,i):
        if j>=1:
            dp[i]=min(dp[i],dp[j]+abs(a[j]-a[i]))


print(dp[n])
'''