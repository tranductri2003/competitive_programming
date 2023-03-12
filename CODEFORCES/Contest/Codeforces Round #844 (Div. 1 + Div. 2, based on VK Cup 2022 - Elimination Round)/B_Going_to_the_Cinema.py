from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = Counter(a)
    a.sort()
    b = list(set(a))
    # print(a)
    # print(b)
    res = 0
    soNguoi = 0
    for i in range(len(a)):
        soNguoi += 1
        if i != len(a)-1:
            if soNguoi > a[i] and soNguoi < a[i+1]:
                res += 1
        else:
            if soNguoi > a[i]:
                res += 1
    if min(a) > 0:
        res += 1
    print(res)
