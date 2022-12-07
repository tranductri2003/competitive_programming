import math
n = int(input())
a = list(map(int, input().split()))

ucln = a[0]
for i in range(n-1):
    ucln = math.gcd(ucln, a[i+1])

if ucln == 1:
    print(-1)
else:
    for i in range(2, ucln+1):
        if ucln % i == 0:
            print(i)
            break
