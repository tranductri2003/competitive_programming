testcase=int(input())
for test in range(testcase):
    n=int(input())
    res=[2]
    for i in range(3,2*n,2):
        res.append(i)
    print(*res)


# a[i] isn't divisible by a[i-1]: a[i] không chia hết cho a[i-1]