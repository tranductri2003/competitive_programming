import math

testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    for num in a:
        if num<0:
            print("NO")
            break
    else:
        print("YES")
        bcnn=a[0]
        for i in range(1,n):
            bcnn=math.gcd(bcnn,a[i])
        so=max(a)//bcnn+1
        print(so)
        for i in range(max(a),-1,-bcnn):
            print(i, end=" ")
        print()
            