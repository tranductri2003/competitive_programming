t=int(input())

for j in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    a.insert(0,0)

    stack=0
    for i in range(1,n+1):
        if a[i]>i+stack:
            stack+=a[i]-i-stack
    print(stack)