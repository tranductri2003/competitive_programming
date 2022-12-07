
t = int(input())
for _ in range(t):
    n = int(input())
    res = [i for i in range(n, 1, -1)]
    res.insert(0, 1)
    print(*res)
