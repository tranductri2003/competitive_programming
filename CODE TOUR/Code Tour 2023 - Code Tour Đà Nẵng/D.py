n, w1, w2 = list(map(int, input().split()))
a = list(map(int, input().split()))


def find_max_value(a, w1, w2):
    n = len(a)
    max_value = float('-inf')

    for i1 in range(n):
        for i2 in range(i1, n):
            for i3 in range(i2, n):
                for i4 in range(i3, n):
                    for i5 in range(i4, n):
                        current_value = (a[i1] + a[i5]) * \
                            w1 + (a[i2] + a[i4]) * w2 + a[i3]
                        if current_value > max_value:
                            max_value = current_value

    return max_value


if w1 == w2 == 0:
    print(find_max_value(a, w1, w2))
elif w1 == 0 and w2 < 0:
    res = -10**19
    for i in range(n):
        res = max(res, w2*2*a[i]+a[i])
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                res = max(res, w2*(a[i]+a[k])+a[j])
    print(res)
else:
    print(find_max_value(a, w1, w2))
