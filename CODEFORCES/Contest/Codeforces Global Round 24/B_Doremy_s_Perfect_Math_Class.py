import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    temp = a[0]
    for i in range(1, n):
        temp = math.gcd(temp, a[i])
    print(max(a)//temp)
