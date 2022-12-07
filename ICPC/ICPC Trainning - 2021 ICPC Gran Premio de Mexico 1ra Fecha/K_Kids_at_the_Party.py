t=int(input())
for _ in range(t):
    n=int(input())
    res=[]
    for i in range(2,7):
        if n%i==0:
            res.append(i)
    if len(res)==0:
        print(-1)
    else:
        print(*res)