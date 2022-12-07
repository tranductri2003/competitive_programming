t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    #Tìm dãy gồm các index tăng dần và chia hết cho nhau sao cho số bên trong nó tăng dần
# if for any two adjacent models with indices ij and ij+1 (note that ij<ij+1, because Orac arranged them properly), ij+1 is divisible by ij and sij<sij+1


    dp=[1]*(n+1)

    for i in range(1,n//2+1):
        for j in range(2*i,n+1,i):
            if a[j-1]>a[i-1]:
                dp[j]=max(dp[j],dp[i]+1)
        print(dp[1:])
    print(max(dp))
            
        