testcase=int(input())
for test in range(testcase):
    n=int(input())
    if n%7==0:
        print(n)
    else:
        so=n//10*10
        for i in range(0,10):
            if (so+i)%7==0:
                print(so+i)
                break