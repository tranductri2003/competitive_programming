

n, d, c = map(int, input().split())

if n < (d + 1) * c or (n %2==1 and d %2==1):
    print("No")
    quit()
if d == 1:
    if c * 2 == n:
        print("Yes")
        for i in range(1, n + 1):
            if i %2==1:
                print(i + 1)
            else:
                print(i - 1)
    else:
        print("No")
    quit()
if d == 0:
    if c == n:
        print("Yes")
    else:
        print("No")
    quit()

print("Yes")

g = [[] for _ in range(500005)]

for i in range(1, c):
    l = (d + 1) * (i - 1) + 1
    r = l + d
    for j in range(l, r + 1):
        for k in range(j + 1, r + 1):
            g[j].append(k)
            g[k].append(j)

remain = n - (c * d + c - d) + 1
num = c * d + c - d

for i in range(c * d + c - d, n + 1):
    for j in range(1, d // 2 + 1):
        target = (i - num + j + remain) % remain + num
        g[i].append(target)
    for j in range(1, d // 2 + 1):
        target = (i - num - j + remain) % remain + num
        g[i].append(target)
    if d%2==1:
        temp = i + remain // 2
        if temp > n:
            temp -= remain
        g[i].append(temp)

for i in range(1, n + 1):
    g[i].sort()
    print(" ".join(map(str, g[i])))

