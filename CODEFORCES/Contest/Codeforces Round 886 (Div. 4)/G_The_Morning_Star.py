from collections import defaultdict
import math


def calculate_angle(x1, y1, x2, y2):
    angle_rad = math.atan2(y2 - y1, x2 - x1)
    angle_deg = math.degrees(angle_rad)
    return angle_deg


t = int(input())

for _ in range(t):
    n = int(input())
    data = []
    for i in range(n):
        x, y = list(map(int, input().split()))
        data.append((x, y))

    check = defaultdict(lambda: 0)
    hang = defaultdict(lambda: 0)
    cot = defaultdict(lambda: 0)
    cheo45 = defaultdict(lambda: 0)
    cheo135 = defaultdict(lambda: 0)
    res = 0
    for x, y in data:
        res += hang[x]
        res += cot[y]
        res += cheo45[x-y]
        res += cheo135[x+y]
        hang[x] += 1
        cot[y] += 1
        cheo45[x-y] += 1
        cheo135[x+y] += 1

    print(res*2)
