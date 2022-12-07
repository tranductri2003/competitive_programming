testcase=int(input())
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

for test in range(0,testcase):
    n=int(input()) #the number of intergers
    a=list(map(int,input().split()))
    if len(set(a))==1:
        print(-1)
    #neu co chan co le thi in 1
    else:
        chan=False
        le=False
        for num in a:
            if num%2==0:
                chan=True
            else:
                le=True
        else:
            #truong hop chi chan hoac chi le
            #tim ucln giua min va cac so con lai
            x=min(a)
            for j in range(0,n):
                a[j]=a[j]-x
            res=max(a)
            for num in a:
                res=gcd(res,num)
            print(res)

