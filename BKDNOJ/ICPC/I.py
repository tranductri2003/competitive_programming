import random

data1 = []
data2 = []
for _ in range(20):
    res = 10**8
    n = random.randint(1, 100000000)
    data1.append(n)
    check = 1
    temp = 1
    stop = False
    for i in range(1, n+1):
        temp *= i
        if temp % n == 0:
            data2.append(i)
            stop = True
            break
        if i**2 > n:
            break
        if i**2 == n:
            break
        if n % i == 0:
            res = n//i

    if stop == False:
        data2.append(res)
for num in data1:
    print(num)

print()
print()
print()

for num in data2:
    print(num)
52930453
6731284
1278654
564833
64413333
8865981
92855268
98095607
38256813
89129183
76061960
95174624
55648252
61845923
19693258
65094024
55010696
8337023
79712421
92243416



52930453
773
97
19477
2385679
985109
1663
80209
4937
623281
146273
63281
1264733
272449
757433
2712251
967
8337023
4229
107761