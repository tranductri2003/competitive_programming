n,m=list(map(int,input().split()))

rmin=10**9
lmax=-10**9
vitri1=-1
vitri2=-1

for i in range(n):
    l,r=list(map(int,input().split()))
    if l>lmax:
        lmax=l        
        vitri2=i+1
    
    if r<rmin:
        rmin=r
        vitri1=i+1


if rmin<lmax:
    print("YES")
    print(vitri1,vitri2)
else:
    print("NO")
