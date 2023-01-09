t = int(input())
for _ in range(t):
    n = int(input())
    data = [i for i in range(1, n**2+1)]
    i = 0
    j = n**2-1
    new = []
    while i <= j:
        if i == j:
            new.append(data[i])
            break
        else:
            new.append(data[i])
            new.append(data[j])
            i += 1
            j -= 1
    for i in range(n, n**2+1, 2*n):
        new[i:i+n] = new[i:i+n][::-1]
    res = []
    for i in range(n):
        res.append([])
        for j in range(n):
            res[i].append(0)
    for i in range(n):
        for j in range(n):
            res[i][j] = new[i*n+j]
    for i in range(n):
        print(*res[i])
