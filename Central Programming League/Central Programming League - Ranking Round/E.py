from collections import Counter
N,Q=list(map(int,input().split()))
a=list(map(int,input().split()))
for i in range(Q):
    l,r=list(map(int,input().split()))
    temp=a[l-1:r]
    t=Counter(temp)
    res=0

    h=list(t.values())
    print(h.count(2))