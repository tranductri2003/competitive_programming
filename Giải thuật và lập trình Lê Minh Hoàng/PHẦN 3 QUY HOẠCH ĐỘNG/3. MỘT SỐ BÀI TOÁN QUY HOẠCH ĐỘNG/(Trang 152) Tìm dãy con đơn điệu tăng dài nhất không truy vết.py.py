n=int(input())
a=list(map(int,input().split()))
a=[-999999]+a+[999999]
dp=[0]*(n+2)
dp[n+1]=1   #Cơ sở quy hoạch động
T=[0]*(n+2)

for i in range(n,-1,-1):   #Tính bảng phương án
    current=-9999
    for j in range(i+1,n+2):
        if a[i]<a[j] and dp[j]>current: 
            dp[i]=dp[j]+1   #Lưu độ dài dãy con tăng dài nhất bắt đầu tại a[i]
            T[i]=j   #Lưu vết: Phần tử đứng liền sau a[i] là T[i], trong đó T[i] là vị trí của phần tử đứng liền sau a[i]
            current=dp[j]
#print(max(dp[1:n+1])-1)
print(dp[0]-2)
res=(dp[0]-2)
b=0
#T[0] chính là phần tử đầu tiên được chọn
#T[T[0]] là phần tử thứ 2 được chọn
#T[T[T[0]]] là phần tử thứ 3 được chọn
for i in range(0,res):
    b=T[b]
    print(f"a[{b}]={a[b]}")   #{b} tức là vị trí của phần tử liền sau, {a[b]} tức là giá trị liền sau