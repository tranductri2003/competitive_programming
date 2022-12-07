from math import gcd


testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    sosochan=0
    le=[]
    for num in a:
        if num%2==0:
            sosochan+=1
        else:
            le.append(num)
    start=n-sosochan
    end=n-1
    res=0
    res+=(end-start+1)*(end+start)//2
    for i in range(0,len(le)-1):
        for j in range(i+1,len(le)):
            if gcd(le[i],le[j]*2)>1:
                res+=1
    print(res)
    
    