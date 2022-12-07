v=int(input())

dp=[0]*(v+1)
dp[0]=1
#Phân tích số v bằng những số nhỏ hơn bằng m
#i chính là m
#j chính là v
for i in range(1,v+1):
    for j in range(i,v+1):
        dp[j]=dp[j-i]+dp[j]  #Sẽ luôn đảm bảo j lớn hơn i

print(dp[v])