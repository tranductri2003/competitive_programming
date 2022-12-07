testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    sochan=[]
    sole=[]
    for num in a:
        if num%2==0:
            sochan.append(num)
        else:
            sole.append(num)
    res=sochan+sole
    print(*res)
