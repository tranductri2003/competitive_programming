t=int(input())
from collections import defaultdict
for _ in range(t):
    n = int(input())
    p = list(map(int,input().split()))
    check = defaultdict(lambda:0)
    for i in range(n):
        check[p[i]]=i

    ans=0
    for i in range(n):
        if p[i]==1:
            pass
        else:
            if check[p[i]-1]>check[p[i]]:
                ans+=1
    print(ans)
        