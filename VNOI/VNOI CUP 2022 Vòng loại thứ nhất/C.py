def upper_bound(my_list, key):
    large = len(my_list) -1
    small = 0

    while (small <= large):
        mid = (small + large) // 2
        if my_list[mid] < key:  #Đổi thành if my_list[mid] > key:  trong th mảng từ lớn đến bé 
            small = mid + 1
        elif my_list[mid] > key:  #Đổi thành elif my_list[mid] < key: trong th mảng từ lớn đến bé
            large = mid - 1
        else:
            return mid
    if my_list[mid]>key:
        return mid
    else:
        return mid+1   #Đổi thành mid-1 trong th mảng từ lớn đến bé
    



from collections import defaultdict
import bisect


check=defaultdict(lambda:defaultdict(lambda:-1))
dodai=defaultdict(list)
data=[]
n=int(input())
for i in range(n):
    s=input()
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
        print(ok[id][vitri]-t)
