from collections import defaultdict 

t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    y = []
    for num in x:
        y.append(num)
    x.sort()
    data=list(set(x))
    data.sort()
    lonhonbang = defaultdict(lambda:0)
    nhohonbang=defaultdict(lambda:0)
    for i in range(n):
        lonhonbang[x[i]]=max(lonhonbang[x[i]],n-i)
        nhohonbang[x[i]]=max(nhohonbang[x[i]],i+1)
    # print(lonhonbang)
    # print(nhohonbang)
    suffixLonHon=defaultdict(lambda:0)
    doDaiPhanBiet =len(data)    
    
    
    suffixLonHon[x[-1]]=lonhonbang[x[-1]]
    for i in range(doDaiPhanBiet-2,-1,-1):
        suffixLonHon[data[i]]=suffixLonHon[data[i+1]]+(data[i+1]-data[i]-1)*lonhonbang[data[i+1]]+lonhonbang[data[i]]
        # print(data,i,data[i+1])
        # print(suffixLonHon[data[i+1]])
        # print((data[i+1]-data[i]-1)*lonhonbang[data[i+1]])
        # print(lonhonbang[data[i]])
        # print('b',suffixLonHon[data[i+1]]+(data[i+1]-data[i]-1)*lonhonbang[data[i+1]]+lonhonbang[data[i]])
        # print("a",suffixLonHon)

    suffixNhoHon = defaultdict(lambda:0)
    suffixNhoHon[x[0]]=nhohonbang[x[0]]
    for i in range(1,doDaiPhanBiet):
        suffixNhoHon[data[i]]=suffixNhoHon[data[i-1]]+(data[i]-data[i-1]-1)*nhohonbang[data[i-1]]+nhohonbang[data[i]]
    # print(suffixLonHon)
    # print(suffixNhoHon)
    res = defaultdict(lambda:0)
    for num in data:
        res[num]=n+suffixLonHon[num]-lonhonbang[num]+suffixNhoHon[num]-nhohonbang[num]
    # print(res)
    for num in y:
        print(res[num],end=" ")
    print()
