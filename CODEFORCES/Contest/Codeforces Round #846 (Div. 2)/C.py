from collections import defaultdict
t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))

    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    c.sort(reverse=True)
    check = defaultdict(lambda: 0)
    for num in a:
        check[num] += 1
    temp = list(check.values())
    temp.sort(reverse=True)
    # print(temp)
    # print(c)
    i = 0
    j = 0
    res = 0
    n = len(temp)
    while i < n and j < m:
        if temp[i] <= c[j]:
            res += temp[i]
            i += 1
            j += 1
        else:
            res += c[j]
            temp[i] -= c[j]
            j += 1
        if i >= n or j >= m:
            break

    print(res)
