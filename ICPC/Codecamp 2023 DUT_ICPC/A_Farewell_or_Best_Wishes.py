for _ in range(int(input())):
    n, m, x, y = map(int, input().split())

    check = True

    if (x == 1 and y == 1) or (x == 1 or y == m):
        check = False

    auto1 = y - 1
    auto2 = m - 1 + x - 1

    a = x - 1
    d = 2 * (n - 1)

    if auto1 >= a and (auto1 - a) % d == 0:
        check = False

    a = n - x + n - 1
    d = 2 * (n - 1)
    if auto1 >= a and (auto1 - a) % d == 0:
        check = False

    a = m - y
    d = 2 * (m - 1)
    if (auto2 - a) >= 0 and (auto2 - a) % d == 0:
        check = False

    a = y - 1 + m - 1
    d = 2 * (m - 1)
    if (auto2 - a) >= 0 and (auto2 - a) % d == 0:
        check = False

    if check:
        print("Farewell")
    else:
        print("BestWishes")
