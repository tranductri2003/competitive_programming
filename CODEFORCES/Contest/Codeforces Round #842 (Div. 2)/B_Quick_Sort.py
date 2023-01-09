
import math

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if a == sorted(a):
        print(0)
    else:
        b = sorted(a)
        time = 0
        i = 0
        j = 0
        while i < n:
            if a[i] != b[j]:
                time += 1
                i += 1
            else:
                i += 1
                j += 1
        print(math.ceil(time/k))
