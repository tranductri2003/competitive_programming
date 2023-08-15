t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    temp = []
    for i in range(n):
        if a[i] % k == 0:
            temp.append((0, i+1))
        elif a[i] > k:
            temp.append((k-a[i] % k, i+1))
        else:
            temp.append((k-a[i], i+1))
    sorted_data = sorted(temp, key=lambda x: (x[0], x[1]))
    res = []
    for i in range(n):
        res.append(sorted_data[i][1])
    print(*res)
