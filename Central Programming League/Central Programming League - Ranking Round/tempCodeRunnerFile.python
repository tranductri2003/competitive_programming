#Complexity: O(10**2*10**5)=O(10^7)

N,W=list(map(int,input().split()))
w=[0]*(N+1)
v=[0]*(N+1)
for i in range(1,N+1):
    w[i],v[i]=list(map(int,input().split()))

dp=[]
for i in range(0,N+1):   # Bảng phương án quy hoạch động
    dp.append([])
    for j in range(0,W+1):
        dp[i].append([])

for i in range(0, W+1):    #Cơ sở quy hoạch động
    dp[0][i]=0

"""
dp[i][j] là giá trị lớn nhất khi lấy cái túi từ [1...i] với giới hạn khối lượng là j
Nếu như không lấy cái túi i, (khi khối lượng túi lớn hơn giới hạn khối lượng j) thì dp[i][j]=dp[i-1][j]
Nếu như có lấy cái túi i (Khối lượng cái túi nhỏ hơn hoặc bằng khối lượng cho phép j) thì
dp[i][j]=max(dp[i-1][j], v[i]+dp[i-1][j-w[i]])
"""

for i in range(1,N+1):
    for j in range(0,W+1):
        if j >= w[i]:
            dp[i][j]=max(dp[i-1][j], v[i]+dp[i-1][j-w[i]])
        else:
            dp[i][j]=dp[i-1][j]

"""
for i in range(0, N+1):
    print(dp[i])
"""

print(dp[N][W])

"""
Cách 2 mảng:
N,W=list(map(int,input().split()))
w=[0]*(N+1)
v=[0]*(N+1)
for i in range(1,N+1):
    w[i],v[i]=list(map(int,input().split()))

current=[0]*(W+1)  #Lấy 0 món đồ để khối lượng giới hạn .... thì luôn luôn giá trị là 0

for i in range(1, N+1):
    next=[0]*(W+1)
    for j in range(0, W+1):
        if j>=w[i]:
            next[j]=max(current[j], v[i]+current[j-w[i]])
        else:
            next[j]=current[j]
    current=next

print(current[W])
"""