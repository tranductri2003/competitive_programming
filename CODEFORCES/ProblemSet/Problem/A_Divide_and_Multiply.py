testcase=int(input())

for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    k=0
    for i in range(n):
        while a[i]%2==0:
            a[i]//=2
            k+=1
    a.sort()
    a[-1]*=2**k
    res=sum(a)
    print (res)
    
    
 
                    