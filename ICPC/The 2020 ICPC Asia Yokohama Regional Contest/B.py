from collections import defaultdict 

def tri(n,data):
    count2 = defaultdict(lambda:0)
    count4 = defaultdict(lambda:0)
    count6 = defaultdict(lambda:0)
    for s in data:
        count4[s[2:]]+=1
        count2[s[4:]]+=1
        count6[s]+=1



    for num in count6:
        count6[num]*=300000

    for num in count4:
        count4[num]*=4000

    for num in count2:
        count2[num]*=500


    data6=defaultdict(lambda:0)
    for num in count6:
        data6[num]=(count6[num]-count4[num[2:]]-count2[num[4:]])

    res=0
    maxVal = max(data6.values())
    for num in data6:
        if data6[num]==maxVal:
            count4[num[2:]]=0
            count2[num[4:]]=0
            res+=count6[num]
            break
    data4=defaultdict(lambda:0)
    for num in count4:
        data4[num]=(count4[num]-count2[num[2:]])

    maxVal = max(data4.values())
    for num in data4:
        if data4[num]==maxVal:
            count2[num[2:]]=0
            res+=count4[num]
            break

    data2 = list(count2.values())
    data2.sort(reverse=True)
    res+=sum(data2[:3])
    return (res)






def nhat(n,data):
    d4 = {}
    d2 = {}
    
    for s in data:
        t1 = s[2:7]
        t2 = s[4:7]
        d4[t1] = d4.get(t1, 0) + 1
        d2[t2] = d2.get(t2, 0) + 1

    v1 = [(key, value) for key, value in d4.items()]
    v2 = [(key, value) for key, value in d2.items()]

    def cmp(x, y):
        return x[1] > y[1]

    v2.sort(key=lambda x: x[1], reverse=True)
    
    temp = []
    maxn = 0

    for x in v2:
        temp.append(x)
        if len(temp) == 4:
            break

    if len(temp) == 1:
        maxn = max(maxn, temp[0][1] * 500)
        maxn = max(maxn, 300000)
    elif len(temp) == 4:
        maxn = max(maxn, 500 * (temp[0][1] + temp[1][1] + temp[2][1]) + 300000)
    else:
        d = 0
        for i in range(len(temp)):
            maxn = max(maxn, d * 500 + 300000)
            d += temp[i][1]
            maxn = max(maxn, d * 500)


    for y in v1:
        temp = []
        maxn = max(maxn, y[1] * 4000 + 300000 * (n != y[1]))
        val = 0
        
        for x in v2:
            if x[0] != y[0][2:5]:
                temp.append(x)
                val += x[1]
                if len(temp) == 4:
                    break
        
        if len(temp) != 4 and val + y[1] < n:
            maxn = max(maxn, y[1] * 4000 + val * 500 + 300000)
        
        if len(temp) == 1:
            maxn = max(maxn, y[1] * 4000 + temp[0][1] * 500)
            maxn = max(maxn, y[1] * 4000 + 300000)
        elif len(temp) == 4:
            maxn = max(maxn, y[1] * 4000 + 500 * (temp[0][1] + temp[1][1] + temp[2][1]) + 300000)
        else:
            d = 0
            for i in range(len(temp)):
                maxn = max(maxn, y[1] * 4000 + d * 500 + 300000)
                d += temp[i][1]
                maxn = max(maxn, y[1] * 4000 + d * 500)
    return (maxn)

import random

for t in range(100000):
    n = random.randint(1,10)
    data=[]
    for i in range(n):
        temps=""
        for i in range(6):
            temp=random.randint(0,9)
            temps+=str(temp)
        data.append(temps)

    
    n = len(set(data))
    data = list(set(data))

    # print(tri(n,data), nhat(n,data))
    if tri(n,data)>nhat(n,data):
        print(n)
        print(data)
        print(tri(n,data))
        print(nhat(n,data))
        print("NHAT SAI")
    elif tri(n,data)< nhat(n,data):
        print(n)
        print(data)
        print(tri(n,data))
        print(nhat(n,data))
        print("TRI SAI")

