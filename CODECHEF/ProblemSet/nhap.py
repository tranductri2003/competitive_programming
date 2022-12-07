import math
import random
t = int(input())
for _ in range(t):
    a = random.randint(1, 1000)
    b = random.randint(a, 1000)
    trueRes = True
    for i in range(0, 10000):
        if (b+i) % (a+i) == 0:
            trueRes = True
            break
    else:
        trueRes = False
    for temp in range(b//a, 1, -1):
        if (b-temp*a) % (temp-1) == 0:
            if trueRes == False:
                print(a, b)
            break
    else:
        if trueRes == True:
            print(a, b)
