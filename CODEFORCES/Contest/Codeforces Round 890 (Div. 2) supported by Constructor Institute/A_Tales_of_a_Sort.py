t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    for i in range(1,n):
        if a[i]<a[i-1]:
            res=max(res,a[i-1])
    print(res)
            