import bisect
import random

from collections import defaultdict
N = int(input())
check = defaultdict(lambda: 0)
data = []

for _ in range(N):
    temp = int(input())
    if check[temp] == 0:
        pos = bisect.bisect_left(data, temp)
        data.insert(pos, temp)
        check[temp] += 1
    else:
        pos = bisect.bisect_left(data, temp)
        data.pop(pos)
        check[temp] -= 1

    if data == []:
        print(-1)
    else:
        print(data[0])
