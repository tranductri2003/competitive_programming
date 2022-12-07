a=[4,4,4,4,3,3,3,2,2]

from itertools import permutations

perm=list(permutations(a))

res=0
data=[]
print(len(perm))
for list in perm:
    for i in range(8):
        if list[i] == list[i+1]:
            break
    else:
        if list not in data:
            res+=1
            data.append(list)
            
print(res)
for num in data:
    print(*num)

check=set(data)
print(len(check))