N=int(input())

if N==1:
    print(1)
if N==2:
    print(2)
else:
    dp=[1,1,2]
    for i in range(3,N+1):
        dp.append(dp[0]+dp[1]+dp[2])
        dp.pop(0)
    print(dp)
    print(dp[2]%(10**9+7))
