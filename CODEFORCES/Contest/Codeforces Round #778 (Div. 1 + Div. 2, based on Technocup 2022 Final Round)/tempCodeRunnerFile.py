t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    res=a[0]+a[1]
    print(res)