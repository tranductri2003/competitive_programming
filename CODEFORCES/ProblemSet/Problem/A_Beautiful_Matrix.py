res=0
for i in range(1,6):
    a,b,c,d,e=list(map(int,input().split()))
    if a==1:
        res=abs(3-i)+2
    elif b==1:
        res=abs(3-i)+1
    elif c==1:
        res=abs(3-i)
    elif d==1:
        res=abs(3-i)+1
    elif e==1:
        res=abs(3-i)+2
print(res)