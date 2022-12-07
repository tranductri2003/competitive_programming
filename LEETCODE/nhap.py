import math


def countNum(n, a):
    return (n//a*a-a)//a+1


n, a, b, c = list(map(int, input().split()))
numA = countNum(n, a)
numB = countNum(n, b)
numC = countNum(n, c)
numAB = countNum(n, math.lcm(a, b))
numAC = countNum(n, math.lcm(a, c))
numBC = countNum(n, math.lcm(b, c))
numABC = countNum(n, math.lcm(a, b, c))
res = numA+numB+numC-numAB-numAC-numBC+numABC
print(res)
