# https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=DUT21E

n, m, a, b = list(map(int, input().split()))


hanga = a//m
if a % m == 0:
    hanga -= 1
hangb = b//m
if b % m == 0:
    hangb -= 1


ans = []
res = 3
if hanga == hangb:
    res = 1
    cota = a % m
    if cota == 0:
        cota = m
    cotb = b % m
    if cotb == 0:
        cotb = m
    print(res)
    print(cota-1, hanga, cotb, hangb+1)


elif a % m == 1 and b % m == 0:
    res = 1
    cota = 1
    cotb = m
    print(res)
    print(cota-1, hanga, cotb, hangb+1)

elif a % m == 1 and b == n:
    res = 1
    cota = 1
    cotb = m
    print(res)
    print(cota-1, hanga, cotb, hangb+1)


elif hangb-hanga == 1:
    res = 2
    print(res)
    cota = a % m
    if cota == 0:
        a = m
    print(cota-1, hanga, m, hanga+1)
    cotb = b % m
    if cotb == 0:
        b = m
    print(0, hangb, cotb, hangb+1)


elif b == n:
    res = 2
    print(res)
    cota = a % m
    if cota == 0:
        a = m
    print(cota-1, hanga, m, hanga+1)
    cotb = m
    print(0, hanga+1, m, hangb+1)
elif a % m-b % m == 1 or (a % m == 0 and b % m == m-1):
    res = 2
    cota = a % m
    if cota == 0:
        cota = m
    print(res)
    print(cota-1, hanga, m, hangb)
    cotb = b % m
    if cotb == 0:
        cotb = m
    print(0, hanga, cotb+1, hangb+1)

elif a % m == 1 and b % m != 0:
    res = 2
elif a % m != 1 and b % m == 0:
    res = 2

else:
    res = 3
