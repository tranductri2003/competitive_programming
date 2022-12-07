import bisect



from random import randint
from collections import defaultdict

exist=defaultdict(lambda:defaultdict(lambda:-1))
check=defaultdict(lambda:defaultdict(lambda:-1))
dodai=defaultdict(list)


data=[]
n=randint(1,10000)
for i in range(n):
    k=chr(randint(97,97+25))
    solan=randint(1,10000)
    s=str(k)*solan
    exist[s]=1
    data.append(s)
    
    id=ord(s[0])-97
    
    t=len(s)
    if check[id][t]==-1:
        dodai[id].append(t)
        check[id][t] =1

for i in range(26):
    dodai[i].sort()

ok=defaultdict(list)

for id in range(0,26):
    if dodai[id]!=[]:
        for i in range(1,dodai[id][-1]+2):
            if check[id][i]==-1:
                ok[id].append(i)

for num in data:
    id=ord(num[0])-97
    if len(dodai[id])==1:
        print(0)
    else:
        t=len(num)

        vitri=bisect.bisect_left(ok[id],t+1)
        
        kiemtra=num[0]*ok[id][vitri]
        if exist[kiemtra]==1:
            print("sai")
            break
            


