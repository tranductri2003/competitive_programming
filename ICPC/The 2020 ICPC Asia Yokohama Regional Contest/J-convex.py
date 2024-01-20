from math import atan2

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def convex_hull_size(points):
    n = len(points)
    if n < 3:
        return n

    start_point = min(points, key=lambda point: (point[1], point[0]))
    sorted_points = sorted(points, key=lambda point: (atan2(point[1] - start_point[1], point[0] - start_point[0]), point))

    hull = [sorted_points[0], sorted_points[1]]
    for i in range(2, n):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i]) != -1:
            hull.pop()
        hull.append(sorted_points[i])

    return len(hull)

data = []
n = int(input("Nhập số lượng điểm: "))
for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

hull_size = convex_hull_size(data)
print("Số lượng điểm trên convex hull:", hull_size)
