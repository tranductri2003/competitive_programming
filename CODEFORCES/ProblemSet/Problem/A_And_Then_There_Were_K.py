import math
testcase=int(input())
for test in range(testcase):
    n=int(input())
    temp=int(math.log2(n))
    print(2**temp-1)