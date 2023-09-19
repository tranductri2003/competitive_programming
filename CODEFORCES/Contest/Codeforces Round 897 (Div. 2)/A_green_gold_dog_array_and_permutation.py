from collections import defaultdict 
t=int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    count = defaultdict(list)
    for i in range(n):
        count[a[i]].append(i)
    
    phanbiet = list(set(a))
    phanbiet.sort()
    
    i=n
    res = [-1]*n
    
    for num in phanbiet:
        for pos in count[num]:
            res[pos] = i
            i-=1
    print(*res)
            
            
