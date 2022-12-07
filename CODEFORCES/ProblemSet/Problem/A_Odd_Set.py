from re import S


testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    sole=0
    sochan=0
    for i in range(2*n):
        if a[i]%2==0:
            sochan+=1
        else:
            sole+=1
    if sochan==sole:
        print("Yes")
    else:
        print("No")