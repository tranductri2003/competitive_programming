from collections import defaultdict 
t=int(input())
for _ in range(t):
    n= int(input())
    res=0
    check = defaultdict(lambda:10**9)
    for i in range(n):
        di,si = list(map(int,input().split()))
        check[di] = min(check[di], di+(si-1)//2)
    print(min(check.values()))
        