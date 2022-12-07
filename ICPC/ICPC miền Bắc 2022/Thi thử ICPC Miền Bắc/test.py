from collections import defaultdict
import random
from itertools import permutations


data = []
for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 6):
            for l in range(1, 6):
                for h in range(1, 6):
                    data.append((i, j, k, l, h))
temp = []
for num in data:
    num = list(num)
    if num == sorted(num):
        temp.append(num)

data = temp


final = []
for num in data:
    num = list(num)
    if num[0] == 1:
        for i in range(1, 4):
            temp = 0
            for k in range(0, i):
                if num[k] < num[i]:
                    temp += 1
            if num[i] == temp+1:
                pass
            else:
                break
        else:
            final.append(num)

k = 3

check = defaultdict(lambda: 0)
ketqua = 0
for num in final:
    temp = [0]*(k+1)
    for i in range(len(num)):

        if num[i] <= k:
            temp[num[i]] += 1
    temp = temp[1:]
    l = ""
    for num in temp:
        l += str(num)
    if check[l] == 0:
        check[l] = 1
        ketqua += 1
        print(l)
print((ketqua))
