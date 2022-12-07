t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    n=min(a)
    m=max(a)
    if a.count(n)==1:
        print(a.index(n)+1)
    else:
        print(a.index(m)+1)