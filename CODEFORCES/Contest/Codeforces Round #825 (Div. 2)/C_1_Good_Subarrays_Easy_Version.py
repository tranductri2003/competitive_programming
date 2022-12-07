t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    check = 1
    res = 0
    for num in a:
        if num < check:
            check = num
        res += check
        check += 1
    print(res)
