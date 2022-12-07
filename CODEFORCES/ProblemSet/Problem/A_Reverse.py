t=int(input())

for _ in range(t):
    n=int(input())
    l=-10**9
    r=-10**9
    a=list(map(int,input().split()))
    for i in range(1,n+1):
        pos=a.index(i)
        if pos!=i-1:
            r=pos
            l=i-1
            break
    else:
        print(*a)
    if l!=-10**9 and r!=-10**9:
        a=a[0:l]+a[l:r+1][::-1]+a[r+1:]
        print(*a)
        