def check(a,n):
    for i in range(1,n-1):
        if a[i-1]>a[i] <a[i+1] or a[i+1]<a[i]>a[i-1]:
            pass
        else:
            return False
    if a[-1]<a[0]>a[1] or a[-1]>a[0]<a[1]:
        pass
    else:
        return False
    if a[-2]<a[-1]>a[0] or a[-2]>a[-1]<a[0]:
        pass
    else:
        return False
    return True
    

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    a.sort()

    if n%2==0:
        nho=a[:n//2]
        lon=a[n//2:]
        res=[]
        i=0
        j=0
        while i<=len(nho)-1:
            res.append(nho[i])
            i+=1
            res.append(lon[j])
            j+=1
        if check(res,n)==True:
            print("YES")
            print(*res)
        else:
            print("NO")
    else:
        print("NO")
        