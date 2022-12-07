INF=10**10

N,W=list(map(int,input().split()))
w=[0]*(N+1)
v=[0]*(N+1)
for i in range(1,N+1):
    w[i],v[i]=list(map(int,input().split()))

dp=[]
S=sum(v)
for i in range(0, N+1):
    dp.append([])
    for j in range(0,S+1):
        dp[i].append(INF)

for i in range(0,N+1):
    dp[i][0]=0
#dp[i][j]: Khối lượng ít nhất sử dụng các túi [1..n] để đạt được giá trị j
for i in range(1,N+1):
    for j in range(1,S+1):
        if j<=v[i]:   #Có thể lấy hoặc lấy cái cũ, chọn cái nào nhỏ hơn
            dp[i][j]=min(dp[i-1][j],w[i])
        else: 
            dp[i][j]=min(dp[i-1][j], w[i]+dp[i-1][j-v[i]])

for i in range(0,N+1):
    print(dp[i])

for i in range(S,-1,-1):
    if dp[N][i]<=W:
        print(i)
        break




'''
3 8
3 3
4 5
5 6
'''










'''




N,W=list(map(int,input().split()))
w=[0]*(N+1)
v=[0]*(N+1)
for i in range(1,N+1):
    w[i],v[i]=list(map(int,input().split()))

dp=[]
S=sum(v)
print(S)
for i in range(0,N+1):
    dp.append([])
    for j in range(0,S+1):
        dp[i].append([])

for j in range(0,S+1):
    dp[0][j]=10**10

#dp[i][j] là khối lượng ít nhất của các túi từ [1...n] để đạt được giá trị lớn hơn hoặc bằng j
for i in range(1,N+1):
    for j in range(0, S+1):
        if j<v[i]: 
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=min(dp[i-1][j], w[i]+dp[i-1][j-v[i]])
print(dp)

'''