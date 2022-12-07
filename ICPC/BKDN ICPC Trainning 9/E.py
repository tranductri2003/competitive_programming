
from math import sqrt

while True:
    try:
        a = input().split()

        R, S = a[0], a[1]
        R = float(R)
        S = float("0"+S)
        res = sqrt((R*(S+0.16))/0.067)
        print(round(res))
    except EOFError:
        break
