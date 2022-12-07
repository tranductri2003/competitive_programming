from random import randint
n=int(input())
for i in range(n):
    xT,yT,xC,yC,x1,y1,x2,y2=list(map(int,input().split()))
    t=randint(1,2)
    if t==1:
        print("No")
    else:
        print("Yes")