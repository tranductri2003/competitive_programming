testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    nho=min(a)
    print(n-a.count(nho))