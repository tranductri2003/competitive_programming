def check_collinear(x1, y1, x2, y2, x3, y3):

    det = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

    if det == 0:
        return True
    else:
        return False


cam = []
n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))
    cam.append((x, y))

m = int(input())
bi = []
for _ in range(m):
    x, y = list(map(int, input().split()))
    bi.append((x, y))

if n == 0 and m == 2:
    center = ((bi[0][0]+bi[1][0])//2, (bi[0][1]+bi[1][1])//2)
    res = 0
    for i in range(m):
        res += abs(bi[i][0]-center[0]) + abs(bi[i][1]-center[1])
    print(res)
elif n == 1 and m == 2:
    center = ((bi[0][0]+bi[1][0])//2, (bi[0][1]+bi[1][1])//2)
    res = 0
    for i in range(m):
        res += abs(bi[i][0]-center[0]) + abs(bi[i][1]-center[1])
    if check_collinear(bi[0][0], bi[0][1], bi[1][0], bi[1][1], center[0], center[1]):
        res += 2

    print(res)


elif n == 0 and m <= 100:
    center = ((bi[0][0]+bi[1][0])//2, (bi[0][1]+bi[1][1])//2)
    xCenter = 0
    yCenter = 0

    tempX = 0
    tempY = 0
    for i in range(m):
        tempX += bi[i][0]
        tempY += bi[i][1]
    xCenter = tempX//m
    yCenter = tempY//m

    res = 0
    for i in range(m):
        res += abs(bi[i][0]-xCenter) + abs(bi[i][1]-yCenter)
    print(res)
