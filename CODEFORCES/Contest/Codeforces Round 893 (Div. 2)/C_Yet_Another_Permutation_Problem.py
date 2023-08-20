t=int(input())
from collections import defaultdict 
for _ in range(t):
    n=int(input())
    res=[1]
    check = defaultdict(lambda:False)
    check[1] = True
    for i in range(2,n//2+1):
        if check[i]==False:
            res.append(i)
            check[i] = True
            res.append(2*i)
            check[2*i] = True
            
            temp = 4*i
            while 2<=temp<=n and check[temp]==False:
                res.append(temp)
                check [temp]= True
                temp*=2
            
    used = []
    for i in range(1,n+1):
        if check[i]==False:
            res.append(i)
    print(*res)
        