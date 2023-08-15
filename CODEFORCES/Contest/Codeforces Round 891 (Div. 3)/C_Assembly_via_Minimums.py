t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    data=[]
    temp=0
    space=n-1
    for i in range(n-1):
        data.append(temp)
        temp+=space
        space-=1
    res=[]
    for num in data:
        res.append(a[num])
    res.append(10**9)
    print(*res)
            