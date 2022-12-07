n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

if a[0]+b[0]+c[0]==0 and a[1]+b[1]+c[1]==0 and a[2]+b[2]+c[2]==0:
    print("YES")
else:
    print("NO")