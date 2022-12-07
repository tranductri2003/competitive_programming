n=int(input())
a=list(map(int,input().split()))
na=a[0]
a=a[1:]
b=list(map(int,input().split()))
nb=b[0]
b=b[1:]


res=0

import math
while len(a)!=0 and len(b)!=0:
    if a[0]>b[0]:
        target1=b.pop(0)
        target2=a.pop(0)
        a.append(target1)
        a.append(target2)
        res+=1
    else:
        target1=a.pop(0)
        target2=b.pop(0)
        b.append(target1)
        b.append(target2)
        res+=1
    if a==[]:
        print(res,2)
        break
    elif b==[]:
        print(res,1)
        break
    if res>=3000000:  #Đúng ra là (n+1)! xấp xỉ 40 triệu
        print(-1)
        break
        
        
    
    