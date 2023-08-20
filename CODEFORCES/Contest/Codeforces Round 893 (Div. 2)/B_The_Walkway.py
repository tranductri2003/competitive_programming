t=int(input())
from collections import defaultdict
for _ in range(t):
    n,m,d = list(map(int,input().split()))   #so banh, so nguoi ban, so phut doi
    s = list(map(int,input().split()))
    canxoa = []
    # blacklist = defaultdict(lambda: False)
    # for i in range(m):
    #     timeTruoc = 1+(s[i]-1)//d*d
    #     # print(s[i], timeTruoc)
    #     if timeTruoc==s[i]:
    #         timeTruoc-=d
        
    #     if i!=0:
    #         timeTruoc = max(timeTruoc, s[i-1])
    #     if s[i]-timeTruoc<d:
    #         canxoa.append(s[i])
    # print(canxoa)
    data = defaultdict(lambda: 0)
    for num in s:
        truocdo = (num-2)//d+1
        tudo = (n-num)//d+1
        data[num] = truocdo+tudo
    tot = max(data.values())
    for num in data:
        if data[num]==tot:
            canxoa.append(num)
    print(canxoa)

        
