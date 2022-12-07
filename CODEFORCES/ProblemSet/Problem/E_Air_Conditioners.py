from collections import defaultdict
q=int(input())
for _ in range(q):
    space=input()
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    t=list(map(int,input().split()))
    res=[10**10]*n
    for i in range(k):
        res[a[i]-1]=t[i]

    
    for i in range(1,n):
        res[i]=min(res[i],res[i-1]+1)
    for i in range(n-2,-1,-1):
        res[i]=min(res[i],res[i+1]+1)
    print(*res)

    
    