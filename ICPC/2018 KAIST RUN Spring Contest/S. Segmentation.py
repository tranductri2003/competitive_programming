import sys
input = sys.stdin.readline

def check(recent,frequence):
    if recent<=r[0]:
        if frequence<=f[0]:
            return "New Customer"
        elif frequence<=f[2]:
            return "Potential Loyalist"
        elif frequence<=f[3]:
            return "Loyal Customer"
        else:
            return "Champion"
    elif recent<=r[1]:
        if frequence<=f[0]:
            return "Promising"
        elif frequence<=f[2]:
            return "Potential Loyalist"
        else:
            return "Loyal Customer"
    elif recent<=r[2]:
        if frequence<=f[1]:
            return "About to Sleep"
        elif frequence<=f[2]:
            return "Need Attention"
        else:
            return "Loyal Customer"
    elif recent<=r[3]:
        if frequence<=f[0]:
            return "Lost"
        elif frequence<=f[1]:
            return "Hibernating"
        else:
            return  "About to Leave"
    else:
        if frequence<=f[1]:
            return "Lost"
        elif frequence<=f[3]:
            return "About to Leave"
        else:
            return "Can't Lose Them"



from collections import defaultdict

EDGEr=defaultdict(lambda :False)
EDGEf=defaultdict(lambda :True)

r=list(map(int,input().split()))
f=list(map(int,input().split()))
N=int(input())

for num in r:
    EDGEr[num]=True

for num in f:
    EDGEf[num]=True

RECENT = defaultdict(lambda: 0)
FREQUENCY = defaultdict(lambda : 0)



for _ in range(N):
    query,  name =input().split()
    query = int(query)
    if query==1:
        RECENT[name]=_
        FREQUENCY[name]+=1
    else:
        if FREQUENCY[name]==0:
            print("None")
        else:
            recent = _ - RECENT[name]
            frequence = FREQUENCY[name]

            if EDGEr[recent]:
                recent -= 0.5
            if EDGEf[frequence]:
                frequence -= 0.5
            print(check(recent,frequence))

