n,k=list(map(int,(input()).split()))

a=[0]
b=list(map(int,(input()).split()))
for i in b:
    a.append(i)
dp=[0]*(n+1)    #Kiểm tra theo thứ tự lần lượt
pre=[0]*(n+1)   #Max so far

for i in range(1,k+1):
    maxx=-9999999999999    #Tổng của dãy lớn nhất có thể
    for j in range(i,n+1):
        dp[j] = max(pre[j - 1], dp[j - 1]) + a[j]   
        """
        nếu tổng trước đó là âm thì sẽ lấy pre[j-1] cộng với a[j], 
        nếu tổng trước đó là dương thì tổng này có thể sẽ được nối tiếp nên lấy a[j-1]+a[j]
        """
        pre[j-1]=maxx  #Nghĩa là xét tới ô nào thì giá trị pre sẽ là giá trị lớn nhất có thể khi xét tới ô đó
        maxx=max(maxx,dp[j])
        

print(a)
print(dp)
print(pre)
print(maxx)