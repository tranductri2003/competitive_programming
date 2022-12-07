n,M=list(map(int,input().split()))
w=[0]*(n+1)
v=[0]*(n+1)
for i in range(1,n+1):
    w[i],v[i]=list(map(int,input().split()))

dp=[]
for i in range(0,n+1):   #Thiết lập bảng phương án công thức truy hồi
    dp.append([])
    for j in range(0,M+1):
        dp[i].append([])

for i in range(0,M+1):   #Điền cơ sở quy hoạch động
    dp[0][i]=0

for i in range(1,n+1):
    for j in range(0,M+1):
        if j<w[i]:   #Nếu như không chọn gói thứ i thì F[i,j]=F[i-1,j]
            dp[i][j]=dp[i-1][j]
        else:          #Nếu có chọn gói thứ i thì F[i,j]=v[i]+F[i-1,j-w[i]]
            dp[i][j]=max(dp[i-1][j],v[i]+dp[i-1][j-w[i]])
'''
for i in range(0,n+1):
    print(dp[i])
'''
print(dp[n][M])



#Truy vết
while n!=0:   #Hàng 0 thì không còn chọn gì nữa nên dừng lại
    if dp[n][M]!=dp[n-1][M]:   #Nếu F[n,M]=F[n-1,M] tức là không chọn gói n, ta truy tiếp F[n-1,M]
        print(n)               #Nếu F[n,M]!=F[n-1,M] tức là đã chọn gói n. Ta thông báo phép chọn tối ưu có chọn gói thứ n và truy tiếp F[n-1,M-w[n]]
        M-=w[n]
    n-=1