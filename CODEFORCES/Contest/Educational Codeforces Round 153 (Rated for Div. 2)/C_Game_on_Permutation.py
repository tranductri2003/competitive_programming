

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    A, B = set(), set()

    B.add(a[0])

    for i in range(1, n):
        w = len([x for x in A if x <= a[i]])
        w1 = len([x for x in B if x <= a[i]])

        if w == 0 and w1 != 0:
            A.add(a[i])
            ans += 1
        B.add(a[i])

    print(ans)
