n = int(input())


data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

LeftUp = -10**9
RightUp = -10**9
LeftDown = -10**9
RightDown = -10**9

for pair in data:
    LeftDown = max(LeftDown, -pair[0]-pair[1])
    LeftUp = max(LeftUp, -pair[0]+pair[1])
    RightDown = max(RightDown, pair[0]-pair[1])
    RightUp = max(RightUp, pair[0]+pair[1])

if n == 1:
    print(4)
else:
    res = (LeftDown+LeftUp+RightDown+RightUp+4)

    if RightUp == -LeftDown:
        res += 1
    if RightDown == -LeftUp:
        res += 1

    print(res)
