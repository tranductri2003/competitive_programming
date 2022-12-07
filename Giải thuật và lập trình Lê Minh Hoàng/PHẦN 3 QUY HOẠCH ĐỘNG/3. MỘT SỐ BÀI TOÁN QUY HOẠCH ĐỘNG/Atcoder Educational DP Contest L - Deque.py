"""
Taro và Jiro chơi với nhau một trò chơi như sau:

Cho tập hợp gồm N số nguyên dương a=(a1,a2,...,aN). Hai người chơi sẽ lần lượt thực hiện các nước đi sau đến khi a rỗng, với Taro là người bắt đầu:

Loại bỏ phần tử đầu tiên hoặc cuối cùng của dãy a. Người chơi đó sẽ kiếm được x điểm, với x là phần tử bị loại bỏ.
Cho X và Y lần lượt là số điểm của Taro và Jiro sau khi trò chơi kết thúc. Taro muốn X−Y lớn nhất có thể, trong Jiro lại muốn làm X−Y bé nhất có thể.

Giả sử cả hai người đều chơi tối ưu, tìm giá trị của X−Y.

Input:
Dòng thứ nhất chứa hai số nguyên dương N(1≤N≤3000).
Dòng thứ hai chứa N số nguyên dương thỏa mãn a1,a2,a3,...,aN(1≤ai≤109).
Output:
In ra giá trị X−Y cần tìm."""

"""
Time Complexity: O(N2)
Define dp[i][j] as the optimal score for Jiro (X−Y) using the range [i,j]. Then, we can either choose ai to append to the left of the range, or aj on the right. Then, our two transitions are

dp[i][j]=maxj>i{ai−dp[i+1][j]aj−dp[i][j−1]
Our initial states are dp[i][i]=0, since any range of size 0 will have difference 0."""


N=int(input())
a=list(map(int,input().split()))
#dp[i][j] là giá trị tối ưu của Jiro khi sử dụng các số trong khoảng từ i đến j

dp=[]
for i in range(0,N):
    dp.append([])
    for j in range(0,N):
        dp[i].append([])

for i in range(0,N):
    dp[i][i]=a[i]
"""for i in range(0,N):
    print(dp[i])"""
for i in range(N-1,-1,-1):
    for j in range(i+1,N):
        dp[i][j]=max(a[i]-dp[i+1][j],a[j]-dp[i][j-1])

for i in range(0,N):
    print(dp[i])
print(dp[0][N-1])