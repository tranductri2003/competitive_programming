from collections import defaultdict 
n=int(input())
data=[]
count2 = defaultdict(lambda:0)
count4 = defaultdict(lambda:0)
count6 = defaultdict(lambda:0)
for _ in range(n):
    s = input()
    count2[s[4]+s[5]]+=1
    count4[s[2]+s[3]+s[4]+s[5]]+=1
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

print(data6)
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
print(res)