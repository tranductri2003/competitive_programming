def check(n):
    res = 0
    temp = n
    while temp % 10 == 0:
        res += 1
        temp //= 10
    return res


t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    temp0 = 0
    res = 0
    for so5 in range(0, 15):
        for so2 in range(0, 30):
            tam = 5**so5*2**so2
            if tam <= m:
                tam *= (m//tam)

                so0 = check(tam*n)
                if so0 > temp0:
                    temp0 = so0
                    res = tam*n

                elif so0 == temp0:
                    if tam*n >= res:
                        temp0 = so0
                        res = tam*n
    print(res)
