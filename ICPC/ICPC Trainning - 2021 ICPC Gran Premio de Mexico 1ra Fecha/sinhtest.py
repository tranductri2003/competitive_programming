from random import randint


R,C=list(map(int,input().split()))
matrix=[]
check=0
print(R,C)
for i in range(R):
    matrix.append([])
    for j in range(C):
        if check==0:
            num=randint(0,3)
        else:
            num=randint(0,2)
        if num==0:
            temp="."
        elif num==1:
            temp="#"
        elif num==2:
            temp="X"
        else:
            temp="E"
            check=1
        matrix[i].append(temp)
for i in range(R):
    x="".join(matrix[i])
    print(x)
t=int(input())
print(t)
for i in range(t):
    x=randint(1,R)
    y=randint(1,C)
    print(x,y)