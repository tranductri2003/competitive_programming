
from random import randint


testcase=10000

for test in range(0,testcase):
    x=randint(2,100000000) 
    while x%2!=0:
       x=randint(2,100000000)  
    y=randint(2,100000000)
    while y%2!=0:
        y=randint(2,100000000)

    res=0
    if x==y:
        res=x
    elif x>y:
        a=(x+y)//2
        res=a*(a//min(x,y)+1)
    else:
        a=(x+y)//2
        res=a*(a//max(x,y)+1)

    