from collections import defaultdict
 
t=int(input())
for _ in range(t):
    check=defaultdict(lambda:False)
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    for i in range(n-1,-1,-1):
        if check[a[i]]==False:
            check[a[i]]=True
            res+=1
        else:
            break
    res=n-res
    print(res)