
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a == sorted(a) or len(set(a)) == 1:
        print(0)
    else:
        l = 0
        r = n-1
        res = 0
        while l < r:
            if a[l] == 1 and a[r] == 0:
                res += 1
                l += 1
                r -= 1
            else:
                if a[l] == 1:
                    pass
                else:
                    l += 1

                if a[r] == 1:
                    r -= 1
                else:
                    pass
            # print(l, r)
        print(res)
