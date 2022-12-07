N, x, y = list(map(int, input().split()))

tempX = 2**(N-1)
tempY = 2**(N-1)

targetX = x
targetY = y
res = 0
# print(tempX, tempY, targetX, targetY)
while tempX != x and tempY != y:
    if tempX < targetX and tempY < targetY:
        tempX = (tempX+2**N)//2
        tempY = (tempY+2**N)//2
    elif tempX < targetX and tempY > targetY:
        tempX = (tempX+2**N)//2
        tempY = (tempY+0)//2
    elif tempX > targetX and tempY < targetY:
        tempX = (tempX+0)//2
        tempY = (tempY+2**N)//2
    else:
        tempX = tempX//2
        tempY = tempY//2
    res += 1
    print(tempX, tempY)
print(res)
# Printing the value of tempX and tempY.
