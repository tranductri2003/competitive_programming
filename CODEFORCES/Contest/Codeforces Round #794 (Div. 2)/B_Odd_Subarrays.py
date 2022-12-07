

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    res1=0
    res2=0

    if n==1:
        res=0
    else:
        i=0
        j=0
        temp=0
        while j<=n-1:
            temp=max(temp,a[j])
            if temp>a[j]:
                res+=1
                i=j+1
                j+=1
                temp=0
            else:
                j+=1
    print(res)
        
        
        