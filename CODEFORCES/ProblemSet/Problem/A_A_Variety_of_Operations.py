testcase=int(input())
for test in range(testcase):
    c,d=list(map(int,input().split()))
    if abs(c-d)%2==1:
        print(-1)
    
    else:
        if c==d==0:
            print(0)
        elif c==d:
            print(1)
        else:
            print(2)