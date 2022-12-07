t=int(input())
from collections import defaultdict
for _ in range(t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    a.sort()
    
    check=defaultdict(lambda:0)
    res=[0]*n

    data=[0]*n
    for i in range(n):
        if a[i]%k==0:
            pass
        else:
            if i!=0 and a[i]==a[i-1]:
                res[i]=res[i-1]+k
                check[res[i]]=1
            else:
                x=k-a[i]%k
                while True:
                    if (a[i]+x)%k==0 and check[x]==0:
                        res[i]=x
                        check[x]=1
                        break
                    else:
                        x+=k
    if max(res)==0:
        print(0)
    else:
        print(max(res)+1)
        
    