
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    temp=min(a)
    res=0
    for num in a:
        res+=(num-temp)
    print(res)
        