a = list(map(int, input().split()))
X = a[-1]
a.pop(-1)

data = [1, 5, 10, 50, 100, 500]
i = 5
res = 0
while X > 0:
    can = min(X//data[i], a[i])
    res += can
    X -= can*data[i]
    i -= 1
    if X == 0:
        break

    if i == -1:
        break
if X > 0:
    print(-1)
else:
    print(res)
