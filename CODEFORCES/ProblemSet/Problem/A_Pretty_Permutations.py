testcase=int(input())
for test in range(testcase):
    n=int(input())
    res=[]
    for i in range(1,n+1):
        res.append(i)
    if n%2==0:
        for i in range(0,n,2):
            res[i],res[i+1]=res[i+1],res[i]
    else:
        for i in range(0,n-3,2):
            res[i],res[i+1]=res[i+1],res[i]
        res[-3],res[-2],res[-1]=res[-2],res[-1],res[-3]
    print(*res)