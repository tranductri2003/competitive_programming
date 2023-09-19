t=int(input())
for _ in range(t):
    x,y,n = list(map(int,input().split()))
    a = [0]*n
    
    temp=0
    for i in range(n-1,-1,-1):
        a[i]=y-temp
        temp+=n-i
    if a[0]<x:
        print(-1)
    else:
        a[0] = x
        print(*a)
