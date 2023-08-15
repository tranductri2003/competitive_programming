from collections import defaultdict 
t=int(input())
for _ in range(t):
    n=int(input())
    soluong = defaultdict(int)
    mang = defaultdict(list)
    nhonhat=[]
    nhonhi=[]
    for i in range(n):
        soluong[i] = int(input())
        temp = list(map(int,input().split()))
        temp.sort()
        nhonhat.append(temp[0])
        nhonhi.append(temp[1])
    res = min(nhonhat)+sum(nhonhi)-min(nhonhi)
    print(res)
    

    