from collections import defaultdict 

t=int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    first = defaultdict(lambda:10**9)
    checkFirst = defaultdict(lambda:False)
    
    last = defaultdict(lambda:0)
    checkLast = defaultdict(lambda:False)
    for i in range(n):
        if checkFirst[a[i]] == False:
            checkFirst[a[i]] =True
            first[a[i]] = i

    for i in range(n-1,-1,-1):
        if checkLast[a[i]] == False:
            checkLast[a[i]] =True
            last[a[i]] = i 
    
    for i in range(k-1,0,-1):
        if checkFirst[i]==True:
            first[i]= min(first[i], first[i+1])
            last[i] = max(last[i], last[i+1])

    res=[]
    # print(first)
    # print(last)
    for i in range(1,k+1):
        if checkFirst[i]==True:
            res.append(2*(last[i] - first[i]+1))
        else:
            res.append(0)
    
    print(*res)
        
