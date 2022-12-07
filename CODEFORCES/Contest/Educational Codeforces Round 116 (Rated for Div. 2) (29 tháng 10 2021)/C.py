import sys
import math





testcase=int(input())

for test in range(0,testcase):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))

    slot=k
    res=0
    check=False
    for i in range(0,n-1):
        
        limit=(10**(a[i+1]))//(10**(a[i]))-1
        if slot>=limit:
            slot-=limit
            res+=10**a[i]*limit
        else:
            res+=10**a[i]*(slot+1)
            check=True
            break
    if check==False:
        res+=10**a[-1]*(slot+1)

    print(res)


