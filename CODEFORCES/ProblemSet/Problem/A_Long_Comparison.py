from cmath import log
import math

testcase=int(input())
for test in range(testcase):
    x1,p1=list(map(int,input().split()))
    x2,p2=list(map(int,input().split()))
    

    # a=math.log10(x1/x2)
    
    # if a+p1-p2>0:
    #     print(">")
    # elif a+p1-p2==0:
    #     print("=")
    # else:
    #     print("<")
    a=min(p1,p2)
    p1-=a
    p2-=a
    if p1>=7:
        print(">")
    elif p2>=7:
        print("<")
    else:
        x1=int(str(x1)+"0"*p1)
        x2=int(str(x2)+"0"*p2)
        if x1>x2:
            print(">")
        elif x1<x2:
            print("<")
        else:
            print("=")
    

    