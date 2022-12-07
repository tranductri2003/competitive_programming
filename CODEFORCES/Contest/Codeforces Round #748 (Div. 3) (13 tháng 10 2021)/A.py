

testcase=int(input())
for test in range(0,testcase):
    a,b,c=list(map(int,input().split()))
    maxx=max(a,b,c)
    if maxx==a and (b ==a or c==a):
        print(1, end=" ")
    elif maxx==a:
        print(0, end=" ")
    else:
        print(maxx+1-a, end=" ")
    if maxx==b and (a==b or c==b):
        print(1, end=" ")
    elif maxx==b:
        print(0, end=" ")
    else:
        print(maxx-b+1, end=" ")
    if maxx==c and (a==c or b==c):
        print(1)
    elif maxx==c:
        print(0)
    else:
        print(maxx+1-c)    
    

