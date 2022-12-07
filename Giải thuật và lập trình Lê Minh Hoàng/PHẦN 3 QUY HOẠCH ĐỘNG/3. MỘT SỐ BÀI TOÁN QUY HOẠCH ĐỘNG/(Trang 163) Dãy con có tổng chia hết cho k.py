MAX=10**9
S=0
n,k=list(map(int,input().split()))
a=list(map(int,input().split()))

b=list()
b.append(MAX)

for i in range(0,n):
    S+=a[i]
    b.append(a[i])
    a[i]=a[i]%k
a.insert(0,MAX)    #Chèn để ta có a[1] là chữ số đầu tiên,...

dp=[]
for i in range(0,n+1):
    dp.append([])
    for j in range(0,k):
        dp[i].append([])

for i in range(0,k):
    dp[0][i]=MAX     #Được chọn trong 0 số để có tổng chia k dư i nên không có cách chọn, nên ta cho bằng vô hạn
dp[0][0]=0

#dp[i][j] là số phần tử tối thiểu phải chọn trong dãy a[1...i] để có tổng chia k dư j
for i in range(1,n+1):
    for j in range(0,k):   
        dp[i][j]=min(     dp[i-1][j]  , 1+    dp[i-1][(j-a[i])%k]      )  #Phần phía sau nghĩa là số dư nếu không có a[i]
#dp[i-1][j]: Nếu trong dãy không phải chọn a[i] thì dp[i][j]=dp[i-1][j]
#1+dp[i-1][(j-a[i])%k]: Nếu trong dãy phải chọn a[i] thì phải thêm 1 phép chọn cộng với i-1 số trước đó sao cho có tổng chia dư (j-a[i])%k


'''
Phép trừ trên các lớp đồng dư mod k:
Nếu như (a-b)modk>=0: return chính nó
Nếu như (a-b)modk<0: return nó cộng k

Ví dụ như một số mod 7 =-2 có nghĩa số đó là số 5,12,19
Nên cũng có nghĩa là số đó mod 7=5 

Tính chu kỳ tròn
'''

'''
Đây chính là bảng dp[i][j]: số phần tử tối thiểu phải chọn trong dãy a[1...i] để tổng chia k dư j
for i in range(0,n+1):
    print(*dp[i])
'''

'''
Đây chính là số phần tử tối thiểu cần xóa
print(dp[10][S%k])
'''

print(n-dp[10][S%k])

#Truy vết

i=n
j=S%k

sum=0
while i!=1:
    if dp[i][j]==dp[i-1][j]:   #Tức là có chọn số a[i]
        print(f"a[{i}]={b[i]}")
        sum+=b[i]
    else:  #Tức là không lấy số a[i]
        j=(j-a[i])%k
    i-=1

print(f"Sum= {sum}")