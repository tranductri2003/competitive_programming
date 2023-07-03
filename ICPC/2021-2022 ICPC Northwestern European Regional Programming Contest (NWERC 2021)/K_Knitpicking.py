from collections import defaultdict
count = defaultdict(lambda: defaultdict(lambda: 0))

check = defaultdict(lambda: 0)
typeSockData = []
t = int(input())
for _ in range(t):
    typeSock, foot, number = input().split()
    number = int(number)
    count[typeSock][foot] += number
    if check[typeSock] == 0:
        typeSockData.append(typeSock)
        check[typeSock] = 1


otherSocks = 0
for type in typeSockData:
    otherSocks += max(1, count[type]
                      ["right"], count[type]["left"])

res = -1
checkImpossible = True
for type in typeSockData:
    if count[type]['left'] > 0 and count[type]['right'] == 0 and count[type]['any'] == 0:
        continue
    if count[type]['right'] > 0 and count[type]['left'] == 0 and count[type]['any'] == 0:
        continue
    if count[type]['left'] == 0 and count[type]['right'] == 0 and count[type]['any'] <= 1:
        continue

    checkImpossible = False


if checkImpossible:
    print("impossible")
else:
    print(1+otherSocks)
