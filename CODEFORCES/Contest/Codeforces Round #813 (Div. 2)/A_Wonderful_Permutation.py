
t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))

    b=a.copy()
    b.sort()
    b=b[:k]
    res=0
    for i in range(k):
        if a[i] not in b:
            res+=1
    print(res)