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
71976804
57034745
19943810
55720820
54111526
9179279
90055906
12276591
44873307
19809730
31426832
15421046
99447558
83445568
99015475
89634253
44085796
99192757
84443748
44640216


11087
6271
1994381
2786041
5273
155581
672059
4092197
661
6761
79
405817
937
421
304663
89634253
2143
1319
7036979
620003
