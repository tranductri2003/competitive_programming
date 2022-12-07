from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    check = defaultdict(lambda: 0)

    b.insert(0, 0)
    res = []
    k = n//2
    for i in range(1, n+1):
        if i > k:
            if b[i] == n+1:
                # Trước i không có số nào lớn hơn k
                if check[i] == 0 and check[b[i]] == 0:
                    res.insert(0,i)
                elif check[i] == 1:
                    pass
                else:
                    res.append(i)
            elif b[i] == 0:
                # Trước i không có số nào nhỏ hơn hoặc bằng k
                if check[i] == 0 and check[b[i]] == 0:
                    res.append(i)
                elif check[i] == 1:
                    pass
                else:
                    res.append(i)
            else:
                # Trước i có b[i]: b[i]->i
                if check[i] == 0 and check[b[i]] == 0:
                    res.append(b[i])
                    res.append(i)
                elif check[i] == 1:
                    pos = res.index(i)
                    res.insert(pos, b[i])

        else:
            if b[i] == n+1:
                # Trước i không có số nào lớn hơn k
                if check[i] == 0 and check[b[i]] == 0:
                    res.append(i)
                elif check[i] == 1:
                    pass
                else:
                    res.append(i)
            elif b[i] == 0:
                # Trước i không có số nào nhỏ hơn hoặc bằng k
                if check[i] == 0 and check[b[i]] == 0:
                    res.append(i)
                elif check[i] == 1:
                    pass
                else:
                    res.append(i)
            else:
                # Trước i có b[i]: b[i]->i
                if check[i] == 0 and check[b[i]] == 0:
                    res.append(b[i])
                    res.append(i)
                elif check[i] == 1:
                    pos = res.index(i)
                    res.insert(pos, b[i])

    dm = defaultdict(lambda: 0)
    ans = []
    for num in res:
        if dm[num] == 0:
            ans.append(num)
            dm[num] = 1
    print(k)
    print(*ans)
