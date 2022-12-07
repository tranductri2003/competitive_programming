testcase=int(input())
for test in range(testcase):
    n,s=list(map(int,input().split()))
    #1 1 1 4 4 4 4
    res=(s)//(n//2+1)
    print(res)