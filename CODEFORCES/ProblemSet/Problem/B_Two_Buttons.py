n,m=list(map(int,input().split()))
#Xanh tru 1, do nhan 2

res=0
while m>n:
    if m%2==1:
        res+=1
        m+=1
    else:
        m//=2
        res+=1
res+=n-m
print(res)