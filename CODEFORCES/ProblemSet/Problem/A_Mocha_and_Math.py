testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    res=a[0]
    for i in range(n):
        res=res&a[i]
    print(res)