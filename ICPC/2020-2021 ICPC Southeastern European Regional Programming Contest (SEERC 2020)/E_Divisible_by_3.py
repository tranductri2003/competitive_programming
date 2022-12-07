n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]%=3
# S=[0]
# T=[0]

# tong=0
# tich=0
# for i in range(n):
#     tong+=a[i]
#     S.append(tong%3)
# for i in range(n):
#     tich+=a[i]**2
#     T.append(tich%3)

# print(S)
# print(T)
# #Tìm số cặp (S[j]-S[i])^2   mod 3   ==T[j]-T[i]   mod 3


dp=[]
for i in range(n+1):
    dp.append([])
    for j in range(3):
        dp[i].append([])
        for k in range(3):
            dp[i][j].append(0)
for i in range(1,n+1):
    dp[i][0][a[i-1]]=1
for i in range(1,n+1):
    for j in range(3):
        for k in range(3):
            A=(j+a[i-1]*k)%3
            B=(k+a[i-1])%3
            dp[i][A][B]+=dp[i-1][j][k]
res=0
for i in range(1,n+1):
    for j in range(3):
        res+=dp[i][0][j]
print(res)