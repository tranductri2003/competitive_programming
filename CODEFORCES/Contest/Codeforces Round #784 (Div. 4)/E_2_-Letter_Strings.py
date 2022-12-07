from collections import defaultdict

t=int(input())
for _ in range(t):
    first=defaultdict(lambda:0)
    second=defaultdict(lambda:0)
    fre=defaultdict(lambda:0)
    data=[]
    n=int(input())
    for i in range(n):
        s=input()
        data.append(s)
        fre[s]+=1
        first[s[0]]+=1
        second[s[1]]+=1
    
    res=0
    for num in data:
        res+=(first[num[0]]-fre[num])+(second[num[1]]-fre[num])
    res//=2
    print(res)

    