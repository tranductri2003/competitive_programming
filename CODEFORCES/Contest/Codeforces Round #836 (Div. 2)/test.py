from itertools import permutations
from random import randint


def baiminh(n, x):
    res = [0]*(n+1)
    res[1] = x
    res[n] = 1
    if n == x:
        for i in range(2, n):
            res[i] = i
        return (res[1:])
    else:
        for i in range(2, n):
            res[i] = i
        res[x] = n

        if n % x != 0:
            for i in range(x-1, 1):
                if n % i == 0 and res[i] % x == 0:
                    res[i], res[x] = res[x], res[i]
                    return (res[1:])
                    break
            else:
                return (-1)
        else:
            for i in range(x+1, n):
                if n % i == 0 and res[i] % x == 0:
                    res[i], res[x] = res[x], res[i]
                    return (res[1:])
                    break
            else:
                return (res[1:])


def check(n, x):
    hoanvi = list(permutations([i for i in range(1, n+1)]))
    data = []
    for num in hoanvi:
        if num[0] == x and num[-1] == 1:
            num = list(num)
            for i in range(1, n-1):
                if num[i] % (i+1) == 0:
                    pass
                else:
                    break
            else:
                data.append(num)
    if data != []:
        return min(data)
    return -1


for i in range(1000):
    n = randint(2, 10)
    x = randint(2, n)
    # n,x=list(map(int,input().split()))
    if baiminh(n, x) == check(n, x):
        print("True")
        # print("bai minh: ", baiminh(n, x))
        # print("dap an: ", check(n, x))
    else:
        print("False")
        print("bai minh: ", baiminh(n, x))
        print("dap an: ", check(n, x))
        break
    # s = input()
