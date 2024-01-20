n = int(input())
a = list(map(int, input().split()))

l = 0 
r = n-1

res=0
while l < r:
    if a[l]==a[r]:
        l+=1
        r-=1
    else:
        while (a[l]!=a[r]):
            while (a[l]<a[r] and l<r):
                a[l+1]+=a[l]
                l+=1
                res+=1
            while (a[r]<a[l] and l<r):
                a[r-1]+=a[r]
                r-=1
                res+=1
print(res)

        