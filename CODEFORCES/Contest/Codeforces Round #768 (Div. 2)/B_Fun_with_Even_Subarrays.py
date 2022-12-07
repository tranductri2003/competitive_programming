testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))==1:
        print(0)
    else:
        caichot=a[-1]
        numcaichot=0
        for i in range(n-1,-1,-1):
            if a[i]==caichot:
                numcaichot+=1
            else:
                break
        i=n-1
        res=0
        while i>=0:
            if a[i]==caichot:
                i-=1
            else:
                res+=1
                i-=numcaichot
            numcaichot=n-1-i
        print(res)
                