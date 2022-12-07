t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    check = []
    c0 = 0
    c1 = 0
    c2 = 0
    for num in a:
        if num % 3 == 0:
            c0 += 1
        elif num % 3 == 1:
            c1 += 1
        else:
            c2 += 1
    equal = (c0+c1+c2)//3
    res = 0
    if c2 == equal:
        pass
    elif c2 < equal:
        c1 -= equal-c2
        res += equal-c2
        c2 = equal
    else:
        c0 += c2-equal
        res += c2-equal
        c2 = equal

    if c1 == equal:
        pass
    elif c1 < equal:
        c0 -= equal-c1
        res += equal-c1
        c1 = equal
    else:
        c2 += c1-equal
        res += c1-equal
        c1 = equal

    if c0 == equal:
        pass
    elif c0 < equal:
        c2 -= equal-c0
        res += equal-c0
        c0 = equal
    else:
        c1 += c0-equal
        res += c0-equal
        c0 = equal

    if c2 == equal:
        pass
    elif c2 < equal:
        c1 -= equal-c2
        res += equal-c2
        c2 = equal
    else:
        c0 += c2-equal
        res += c2-equal
        c2 = equal

    if c1 == equal:
        pass
    elif c1 < equal:
        c0 -= equal-c1
        res += equal-c1
        c1 = equal
    else:
        c2 += c1-equal
        res += c1-equal
        c1 = equal

    if c0 == equal:
        pass
    elif c0 < equal:
        c2 -= equal-c0
        res += equal-c0
        c0 = equal
    else:
        c1 += c0-equal
        res += c0-equal
        c0 = equal
    print(res)
