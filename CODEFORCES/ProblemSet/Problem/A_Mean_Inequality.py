testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))    
    a.sort()
    i=0
    j=2*n-1
    while i<j:
        a[i],a[j]=a[j],a[i]
        i+=2
        j-=2
    print(*a)