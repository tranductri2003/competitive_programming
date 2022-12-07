
from collections import Counter

t=int(input())


for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    check=Counter(a)

    maxi=max(check.values())
    remain=sum(check.values())-maxi
    
    if maxi>remain:
        res=remain
    else:
        res=n//2
    
    print(n-2*res)
    
    
