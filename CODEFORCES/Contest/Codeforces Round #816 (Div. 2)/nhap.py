t=int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    a=n-1+m-1
    b=min(n,m)
    if n==1 and m==1:
        b-=1
    print(a+b)