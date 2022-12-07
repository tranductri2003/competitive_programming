import math
testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=math.gcd(n,100)
    print(100//a)