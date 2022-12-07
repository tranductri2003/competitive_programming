
t=int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    if n<m:
        n,m=m,n
    if n==1 and m==1:
        print(0)
    else:
        print(n+m+m-2)