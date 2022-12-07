from collections import defaultdict
import bisect


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    buoc = [1]*(n+1)
    data = [i for i in range(0, n+1)]
    for i in range(n-1):
        if a[i] > a[i+1]:
            temp = bisect.bisect_left(data, a[i]-a[i+1])
            buoc[data[temp]] = i+1+1
            data.pop(temp)
    print(*buoc[1:n+1])
