
n = int(input())
d4 = {}
d2 = {}

for i in range(1, n + 1):
    s = input()
    t1 = s[2:7]
    t2 = s[4:7]
    if t1 in d4:
        d4[t1] += 1
    else:
        d4[t1] = 1
    if t2 in d2:
        d2[t2] += 1
    else:
        d2[t2] = 1

v1 = [(key, value) for key, value in d4.items()]
v2 = [(key, value) for key, value in d2.items()]

v2.sort(key=lambda x: x[1], reverse=True)

temp = []
maxn = 0

for x in v2:
    temp.append(x)
    if len(temp) == 4:
        break

if len(temp) == 1:
    maxn = max(maxn, temp[0][1] * 500)
    maxn = max(maxn, 300000)
elif len(temp) == 4:
    maxn = max(maxn, 500 * (temp[0][1] + temp[1][1] + temp[2][1]) + 300000)
else:
    d = 0
    for i in range(len(temp)):
        maxn = max(maxn, d * 500 + 300000)
        d += temp[i][1]
        maxn = max(maxn, d * 500)

for y in v1:
    temp = []
    maxn = max(maxn, y[1] * 4000 + 300000 * (n != y[1]))

    for x in v2:
        if x[0] != y[0][2:]:
            temp.append(x)
            if len(temp) == 4:
                break

    if len(temp) == 1:
        maxn = max(maxn, y[1] * 4000 + temp[0][1] * 500)
        maxn = max(maxn, y[1] * 4000 + 300000)
    elif len(temp) == 4:
        maxn = max(maxn, y[1] * 4000 + 500 * (temp[0][1] + temp[1][1] + temp[2][1]) + 300000)
    else:
        d = 0
        for i in range(len(temp)):
            maxn = max(maxn, y[1] * 4000 + d * 500 + 300000)
            d += temp[i][1]
            maxn = max(maxn, y[1] * 4000 + d * 500)

print(maxn)

