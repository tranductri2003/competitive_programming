import math
n = int(input())
a = list(map(int, input().split()))


temp = a[-1]
for i in range(0, n):
    temp = math.gcd(temp, a[i])
if temp != a[0]:
    print(-1)
else:
    res = []
    for i in range(n):
        res.append(a[i])
        res.append(temp)
    res.pop(-1)
    print(len(res))
    print(*res)
