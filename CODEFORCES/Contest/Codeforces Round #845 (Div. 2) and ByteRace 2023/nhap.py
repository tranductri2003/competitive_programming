from itertools import permutations
n = int(input())
data = []
data = list(permutations(i for i in range(1, n+1)))
res = 0

for num in data:
    new = num+num[::-1]
    # print(new)
    temp = 0
    for i in range(len(new)-1):
        for j in range(i+1, len(new)):
            if new[i] > new[j]:
                temp += 1
    # print(temp)
    res += temp
print(res)
