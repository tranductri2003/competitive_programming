#AND nhân: cả 2 cùng bằng 1 thì trả về 1, kết quả luôn giảm đi
#OR cộng: chỉ cần 1 trong 2 bằng thì trả về 1, kết quả luôn tăng lên


# Select an index i (1≤i≤n) and replace ai with ai OR 2^j where j is any integer between 0 and 30 inclusive. 
# In other words,
# in an operation you can choose an index i (1≤i≤n) and set the j-th bit of ai to 1 (0≤j≤30).

#Tìm max của a1 AND a2 AND … AND an after performing at most k operations.
#Vậy thì mình sẽ cố gắng OR sao cho cái số ngoài cùng là lớn nhất

#Quan trọng bit ngoài cùng nhất

#Cách làm
#Chạy từ bit ngoài cùng về bit 0
#Nếu bit ngoài cùng k>n: thì gán
#Nếu bit ngoài cùng k<n thì bỏ qua

def update(s):
    for i in range(0,31):
        if s[i]=='1':
            bit[i]+=1

t=int(input())

for _ in range(t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    res=0
    bit=[0]*31
    for num in a:
        s=bin(num)[2:]
        s=str("0"*(31-len(s))+s)
        update(s)
    for i in range(31):
        if bit[i]+k>=n:
            k=k-(n-bit[i])
            bit[i]=n
    bit=bit[::-1]
    for i in range(31):
        if bit[i]==n:
            res+=2**i
    print(res)
    