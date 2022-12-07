# Miếng bánh được gọi là rực rỡ nếu như với mỗi màu sắc của từng cây nến trên miếng bánh,
# tồn tại đúng k cây nến với màu sắc đó trên miếng bánh, 
# với  là số lớn nhất mà em gái đã đếm được trên đầu ngón tay.
from collections import Counter

n,k=list(map(int,input().split()))
c=list(map(int,input().split()))
q=int(input())
for i in range(q):
    l,r=list(map(int,input().split()))
    temp=c[l-1:r]
    
    
    g=Counter(temp)

    for num in g:
        if g[num]!=k:
            print(num)
            break
    else:
        print(0)


