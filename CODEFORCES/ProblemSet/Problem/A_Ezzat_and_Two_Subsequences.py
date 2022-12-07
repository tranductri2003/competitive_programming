testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    res=sum(a[:-1])/(n-1)+a[-1]
    print(res)