from collections import defaultdict

res = defaultdict(lambda: 0)
n = int(input())
chu1 = []
chu2 = []
chu3 = []
chu4 = []
chu5 = []

for i in range(n):
    name, num = input().split()
    res[name] += int(num)
    if len(name) == 1:
        chu1.append(name)
    elif len(name) == 2:
        chu2.append(name)
    elif len(name) == 3:
        chu3.append(name)
    elif len(name) == 4:
        chu4.append(name)
    else:
        chu5.append(name)

chu1 = list(set(chu1))
chu2 = list(set(chu2))
chu3 = list(set(chu3))
chu4 = list(set(chu4))
chu5 = list(set(chu5))

chu1.sort()
chu2.sort()
chu3.sort()
chu4.sort()
chu5.sort()


for name in chu1:
    print(name, res[name])
for name in chu2:
    print(name, res[name])
for name in chu3:
    print(name, res[name])
for name in chu4:
    print(name, res[name])
for name in chu5:
    print(name, res[name])
