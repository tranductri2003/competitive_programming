testcase=int(input())
for test in range(testcase):
    n=int(input())
    res=1
    sum=1
    temp=1
    while sum<n:
        temp+=2
        sum+=temp
        res+=1
    print(res)