t=int(input())
import math


#Tính số hình vuông tạo thành từ n hàng chấm, mỗi hàng gồm m chấm

for i in range(t):
    res=0
    n,m=list(map(int,input().split()))
    data=[]
    for j in range(1,max(n,m)+1):
        res+=max(0,(n-j)*(m-j))
    print(res)
    for j in range(1,max(n,m)+1):
        for k in range(1,max(n,m)+1):
            if j**2+k**2<=(m-1)*(n-1):
                res+=(min(m,n)-1-max(j,k))**2
                print(j,k,(min(m,n)-1-max(j,k))**2)
    print(res)
        

            
