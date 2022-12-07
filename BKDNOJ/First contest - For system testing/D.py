N=int(input())
d1=0
d2=0
tamgiac=[]
v=[]
v.append(-1)

for i in range(N):
    a,b,c=list(map(int,input().split()))
    if a==0:
        d1+=1
    else:
        if b==0:
            d2+=1
        else:
            tamgiac.append((a,b))
print(tamgiac)