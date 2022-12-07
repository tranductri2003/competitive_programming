t=int(input())
for _ in range(t):
    n,H,M=list(map(int,input().split()))
    now=H*60+M
    
    res=10**9
    for i in range(n):
        h,m=list(map(int,input().split()))
        temp=h*60+m
        if temp<now:
            temp+=24*60
        res=min(res,temp-now)
    gio=res//60
    phut=res-gio*60
    print(gio,phut)

    