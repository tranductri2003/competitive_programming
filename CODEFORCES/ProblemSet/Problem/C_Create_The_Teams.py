t=int(input())

for _ in range(t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    
    a.sort(reverse=True)
    
    res=0
    stack=0
    for i in range(n):
        if a[i]*(i+1-stack)>=k:
            res+=1
            stack=i+1
    
    print(res)