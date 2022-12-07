
n = int(input())
xmax = -10**9
xmin = 10**9

ymax = -10**9
ymin = 10**9
for _ in range(n):
    x, y = list(map(int, input().split()))
    xmax = max(xmax, x)
    xmin = min(xmin, x)

    ymax = max(y, ymax)
    ymin = min(ymin, y)

xres = (xmax-xmin)//2
if (xmax-xmin) % 2 != 0:
    xres += 1

yres = (ymax-ymin)//2
if (ymax-ymin) % 2 != 0:
    yres += 1

print(xres, yres)
