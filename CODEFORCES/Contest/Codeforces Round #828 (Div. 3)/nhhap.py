import math
import random


def checkk(a, b, c, d, i, j):
    if (i*j) % (a*b) == 0 and a < i <= c and b < j <= d:
        return True
    return False


for _ in range(10000):
    a = random.randint(1, 100000)
    b = random.randint(1, 100000)
    c = random.randint(1, 100000)
    d = random.randint(1, 100000)
    if a < c and b < d:
        check = False
        for i in range(a+1, c+1):
            tu = i
            mau = a*b
            chung = math.gcd(tu, mau)
            tu //= chung
            mau //= chung
            res = (d//math.lcm(tu, mau))*math.lcm(tu, mau)
            if b < res and res <= d:
                if checkk(a, b, c, d, i, res):
                    pass
                else:
                    print('dit me')
                check = True
                break
            res = (d//mau)*mau
            if res*tu % mau == 0:
                if b < res and res <= d:
                    if checkk(a, b, c, d, i, res):
                        pass
                    else:
                        print('dit me')
                    check = True
                    break

        if check == False:
            # print(-1, -1)
            pass
