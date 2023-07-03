# https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=DUT21E

tong = 0
for i in range(10**6):
    tong += i


n, m, a, b = list(map(int, input().split()))


hanga = a//m
res = 3
if a % m == 0:
    hanga -= 1
hangb = b//m
if b % m == 0:
    hangb -= 1

cota = a % m
if a % m == 0:
    cota = m
cotb = b % m
if b % m == 0:
    cotb = m


if hanga == hangb:
    res = 1
elif cota == 1 and cotb == m:
    res = 1
elif cota == 1 and b == n:
    res = 1

elif hangb == hanga+1:
    res = 2
elif cota == cotb+1:
    res = 2
elif cota == 1:
    res = 2
elif cotb == m:
    res = 2
elif b == n:
    res = 2

else:
    res = 3

print(res)
