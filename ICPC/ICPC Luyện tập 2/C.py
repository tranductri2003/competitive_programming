import itertools
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
k = int(input())


def findsubsets(s, n):
    return list(itertools.combinations(s, n))


subset = []

res = []
for i in range(0, n+1):
    temp = list(itertools.combinations(data, i))
    for num in temp:
        res.append(sum(num))

if k in res:
    print("Yes")
else:
    print("No")
