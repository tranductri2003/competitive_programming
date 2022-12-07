testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    if sum(a)==n:
        print(0)
    else:
        if sum(a)<n:
            print(1)
        else:
            print(sum(a)-n)