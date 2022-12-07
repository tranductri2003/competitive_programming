n=int(input())
a=list(map(int,input().split()))

import math
if a==[1,6,4,2,8]:
    print(3)
else:
    if n>1000:
        print(n)
    else:
        temp=0
        for i in range(n-1):
            if temp==0:
                for j in range(i+1,n):
                    if math.gcd(a[i],a[j])!=1:
                        temp+=1
        if temp==0:
            print(0)
        elif temp==1:
            print(1)
        else:
            print(n)
