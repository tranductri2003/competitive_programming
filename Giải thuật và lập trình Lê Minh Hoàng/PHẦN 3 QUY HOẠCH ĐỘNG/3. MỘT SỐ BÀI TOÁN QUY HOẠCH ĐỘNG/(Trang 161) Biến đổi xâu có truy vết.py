X=str(input())
Y=str(input())
m=len(X)
n=len(Y)

X=str("z")+X  #Chen thêm bất kỳ ký tự nào ở đầu để str bắt đầu từ 1 và đến str[m]
Y=str("z")+Y

dp=[]
for i in range(0,m+1):
    dp.append([])
    for j in range(0,n+1):
        dp[i].append([])

for i in range(0,m+1):   #F[i][0] là số phép biến đổi xâu gồm i ký tự đầu của S thành xâu rỗng, nó cần tối thiểu i phép xóa
    dp[i][0]=i
for j in range(0,n+1):   #F[0][j] là số phép biến đổi xâu rỗng thành xâu gồm j ký tự đầu của F, nó cần tối thiểu j phép chèn
    dp[0][j]=j


for i in range(1,m+1):    #Kiểm tra lần lượt từ chữ cái đầu tiên (thứ 1) đến chữ cái cuối cùng (thứ m) của dãy X
    for j in range(1,n+1):#Kiểm tra lần lượt từ chữ cái đầu tiên (thứ 1) đến chữ cái cuối cùng (thứ n) của dãy Y
        if X[i]==Y[j]:
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+1  #Theo thú tự: Chèn vào sau vị trí m của X một ký tự đúng bằng Yn, thay vị trí m của X bằng một ký tự đúng bằng Yn, xóa vị trí thứ m của X
for i in range(0,m+1):
    print(*dp[i])

print(dp[m][n])


#Truy vết
i=m
j=n
current=X[1:m+1]
while i!=0 and j!=0:
    if X[i]==Y[j]:
        i-=1
        j-=1
    else:
        if dp[i][j]==dp[i][j-1]+1:
            print(current,end=" ->")
            print(f" Insert ({i}, {Y[j]})",end=" ->")
            current=current[0:i]+str(Y[j])+current[i:]
            print(current)
            j-=1
        if dp[i][j]==dp[i-1][j-1]+1:
            print(current,end=" ->")
            print(f"Replace ({i}, {Y[j]})",end=" -> ")
            current=current[0:i-1]+str(Y[j])+current[i:]
            print(current)
            i-=1
            j-=1
        if dp[i][j]==dp[i-1][j]+1:
            print(current,end=" ->")
            print(f"Delete ({i})",end=" ->")
            current=current[0:i-1]+current[i:]
            print(current)
            i-=1