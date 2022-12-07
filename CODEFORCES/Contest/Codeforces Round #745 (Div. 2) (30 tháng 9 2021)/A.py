



testcase=int(input())
for i in range(0,testcase):
    n=int(input())
    a=1
    for i in range(3,2*n+1):
        a=a*i%(10**9+7)
    print(a)




