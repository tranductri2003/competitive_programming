
import math
# A utility function to calculate area
# of triangle formed by (x1, y1),
# (x2, y2) and (x3, y3)
 
def area(x1, y1, x2, y2, x3, y3):
 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)
 
 
# A function to check whether point P(x, y)
# lies inside the triangle formed by
# A(x1, y1), B(x2, y2) and C(x3, y3)
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
 

 
def checkCollision(a, b, c, x, y, radius):
    dist = ((abs(a * x + b * y + c)) /
            math.sqrt(a * a + b * b))

    if (radius == dist):
        return True
    elif (radius > dist):
        return False
    else:
        return True
    
    
def check(duong1,duong2,duong3,x,y,radius):
    dist = ((abs(duong1[0] * x + duong1[1] * y + duong1[2])) /
            math.sqrt(duong1[0] * duong1[0] + duong1[1] * duong1[1]))

    if (radius == dist):
        pass
    elif (radius > dist):
        return False
    else:
        pass
    
    dist = ((abs(duong2[0] * x + duong2[1] * y + duong2[2])) /
            math.sqrt(duong2[0] * duong2[0] + duong2[1] * duong2[1]))

    if (radius == dist):
        pass
    elif (radius > dist):
        return False
    else:
        pass
    
    dist = ((abs(duong3[0] * x + duong3[1] * y + duong3[2])) /
            math.sqrt(duong3[0] * duong3[0] + duong3[1] * duong3[1]))

    if (radius == dist):
        pass
    elif (radius > dist):
        return False
    else:
        pass

    return True
def lineFromPoints(P, Q):

	a = Q[1] - P[1]
	b = P[0] - Q[0]
	c = a*(P[0]) + b*(P[1])

	return a,b,-c


# radius = 1.08764044
# x = 4
# y = 0
# a = -1.1
# b = -1.8
# c = 2.2
# checkCollision(a, b, c, x, y, radius)

def Dis(Mx,My,Ax,Ay):
    return math.sqrt((Mx-Ax)**2 + (My-Ay)**2)


Ax,Ay,Bx,By,Cx,Cy=list(map(float,input().split()))
A=[Ax,Ay]
B=[Bx,By]
C=[Cx,Cy]
duongAC=lineFromPoints(A, C)
duongAB=lineFromPoints(A, B)
duongBC=lineFromPoints(B, C)

Mx,My=list(map(float,input().split()))
khoangCachMAB=abs(duongAB[0]*Mx+duongAB[1]*My+duongAB[2])/(math.sqrt(duongAB[0]**2+duongAB[1]**2))
if check(duongAB,duongAC,duongBC,Mx,My,khoangCachMAB)==True:
    pass
else:
    khoangCachMAB=-10**9
khoangCachMAC=abs(duongAC[0]*Mx+duongAC[1]*My+duongAC[2])/(math.sqrt(duongAC[0]**2+duongAC[1]**2))
if check(duongAB,duongAC,duongBC,Mx,My,khoangCachMAC)==True:
    pass
else:
    khoangCachMAC=-10**9
khoangCachMBC=abs(duongBC[0]*Mx+duongBC[1]*My+duongBC[2])/(math.sqrt(duongBC[0]**2+duongBC[1]**2))
if check(duongAB,duongAC,duongBC,Mx,My,khoangCachMBC)==True:
    pass
else:
    khoangCachMBC=-10**9
    
  
khoangCachMA=Dis(Mx,My,Ax,Ay)
khoangCachMB=Dis(Mx,My,Bx,By)
khoangCachMC=Dis(Mx,My,Cx,Cy)

if (isInside(Ax,Ay,Bx,By,Cx,Cy,Mx,My)):
    print(max(khoangCachMAB,khoangCachMAC,khoangCachMBC))
else:

    print(max(khoangCachMAB,khoangCachMAC,khoangCachMBC))