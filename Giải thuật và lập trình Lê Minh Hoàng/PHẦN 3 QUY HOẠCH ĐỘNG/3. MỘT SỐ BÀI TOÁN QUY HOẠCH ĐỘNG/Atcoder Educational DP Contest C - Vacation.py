N=int(input())

for i in range(1,N+1):
    a,b,c=list(map(int,input().split()))
    if i==1:
        dp=[a,b,c]   #dp[0],dp[1],dp[2] là giá trị lớn nhất có thể đạt được tại lượt thứ i nếu chọn món hàng là 1 2 hoặc 3
    else:  

        MAX1=max(dp[1],dp[2])+a   #Giá trị lớn nhất nếu chọn hoạt động a
        MAX2=max(dp[0],dp[2])+b   #Giá trị lớn nhất nếu chọn hoạt động b
        MAX3=max(dp[0],dp[1])+c   #Giá trị lớn nhất nếu chọn hoạt động c
        dp[0]=MAX1
        dp[1]=MAX2
        dp[2]=MAX3

print(max(dp))