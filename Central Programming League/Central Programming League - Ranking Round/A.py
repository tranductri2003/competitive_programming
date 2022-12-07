
def area(x1, y1, x2, y2, x3, y3):
     
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)   
def isInside(x1, y1, x2, y2, x3, y3, x, y):
     
    # Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3)
 
    # Calculate area of triangle PBC
    A1 = area (x, y, x2, y2, x3, y3)
     
    # Calculate area of triangle PAC
    A2 = area (x1, y1, x, y, x3, y3)
     
    # Calculate area of triangle PAB
    A3 = area (x1, y1, x2, y2, x, y)
     
    # Check if sum of A1, A2 and A3
    # is same as A
    if(A == A1 + A2 + A3):
        return True
    else:
        return False 

x1,y1=list(map(int,input().split()))
x2,y2=list(map(int,input().split()))
x3,y3=list(map(int,input().split()))
print(area(x1, y1, x2, y2, x3, y3))
import math



  

n=int(input())
res=0
for i in range(n):
    x,y=list(map(int,input().split()))
    if isInside(x1,y1, x2, y2, x3, y3,x,y)==True:
        res+=1
print(res)
