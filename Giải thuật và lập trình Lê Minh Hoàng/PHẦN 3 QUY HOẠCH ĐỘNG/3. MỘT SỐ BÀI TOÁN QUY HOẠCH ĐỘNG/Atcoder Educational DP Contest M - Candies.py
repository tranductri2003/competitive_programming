"""
Có N đứa trẻ được đánh số từ 1 tới N.

Bọn trẻ quyết định chia nhau K viên kẹo. Với mỗi đứa trẻ, đứa thứ i(1≤i≤N) phải nhận được số viên kẹo trong phạm vi từ 0 tới ai. K viên kẹo phải được dùng hết.

Hãy đếm số cách bọn trẻ có thể chia nhau những viên kẹo chia lấy dư cho 109+7.

Hai cách chia được gọi là khác nhau nếu tồn tại một đứa trẻ nhận số viên kẹo khác nhau giữa hai cách.

Input
Dòng đầu tiên là hai số nguyên N(1≤N≤100) và K(0≤K≤105).

Dòng thứ hai có N số nguyên a1,a2,a3,...,an(0≤ai≤K).
Output
Số cách chia kẹo cho bọn trẻ chia lấy dư cho 109+7."""

#Cách cơ bản không AC: 5/16


N,K=list(map(int,input().split()))
a=list(map(int,input().split()))
a.insert(0,0)   #Insert để a[1] là số kẹo giới hạn của bạn 1
#Let dp[i][j] represent the number of ways to distribute j candies to the first i children.
dp=[]
for i in range(0,N+1):
    dp.append([])
    for j in range(0,K+1):
        dp[i].append(0)
#Chia 0 viên kẹo cho bất cứ số lượng người nào đều luôn có 1 cách
for i in range(0,N+1):
    dp[i][0]=1

for i in range(1,N+1):
    for j in range(1,K+1):
        x=sum(dp[i-1][max(j-a[i],0):j+1]) #Bởi vì thằng i mới thêm vô có thể chứa tối đa là a[j] viên kẹo, chia đều cho đủ bọn a[j] đứa trở xuống thôi
        dp[i][j]=x
        
            
print(dp[N][K]%(10**9+7))

#Cách prefixSum:  7/16


N,K=list(map(int,input().split()))
a=list(map(int,input().split()))
a.insert(0,0)   #Insert để a[1] là số kẹo giới hạn của bạn 1
#Let dp[i][j] represent the number of ways to distribute j candies to the first i children.
dp=[]
for i in range(0,N+1):
    dp.append([])
    for j in range(0,K+1):
        dp[i].append(0)
#Chia 0 viên kẹo cho bất cứ số lượng người nào đều luôn có 1 cách
for i in range(0,N+1):
    dp[i][0]=1

prefixSum=[1]*(K+2)  #Bản thân prefixSum có nhiều hơn 1 phần tử so với tổng ban đầu, nhưng do bắt đầu từ 1 nên...
prefixSum[0]=0

for i in range(1,N+1):
    #print(f"Lúc này i là {i}, j là {j} có prefix là {prefixSum}")
    for j in range(1,K+1):
        x=prefixSum[j+1]-prefixSum[max(j-a[i],0)]
        dp[i][j]=x
    #print(f"Với i={i}, dãy hoàn chỉnh là {dp[i]}")
    #print(f"PrefixSum trước khi cập nhật là {prefixSum}")
    for j in range(1,K+2):
        prefixSum[j]=prefixSum[j-1]+dp[i][j-1]
    #print(f"PrefixSum sau khi cập nhật là {prefixSum}")
        
"""for i in range(0,N+1):
    print(dp[i])"""
print(dp[N][K]%(10**9+7))