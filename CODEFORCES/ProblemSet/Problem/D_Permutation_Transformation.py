def solve(mang,l,r,k):
    current=mang[l:r+1]
    num=max(current)
    vitri=mang.index(num)
    res[num]=k
    if vitri-1>=l:          
        solve(mang,l,vitri-1,k+1)
    if r>=vitri+1:
        solve(mang,vitri+1,r,k+1)
    

t=int(input())
for _ in range(t):
    n=int(input())
    res=[0]*(n+2)
    a=list(map(int,input().split()))
    solve(a,0,n-1,0)
    for num in a:
        print(res[num],end=" ")
    print()
    