import time
"""
Thuật toán:
Tìm từ cuối dãy lên đầu cho tới khi gặp một phần tử x[i] chưa đạt cận trên
Nếu tìm thấy tăng x[i] lên 1
Đặ tất cả các phần tử phía sau x[i] bằng giới hạn dưới

Nếu không tìm thấy tức là mọi phần tử đã đạt giới hạn trên, đây là cấu hình cuối cùng
"""





n,c=list(map(int,input().split()))

a=list(range(1,c+1))
i=c-1
res=1
print(a)


while i>=0:
    if a[i]<n-c+i+1: #Cận trên
        a[i]+=1
        for j in range(i+1,c):
            a[j]=a[j-1]+1 #Cận dưới
        i=c
        print(a)
        res+=1
    i-=1
print(res) #N chập k phần tử

