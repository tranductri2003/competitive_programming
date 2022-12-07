"""
Given a collection of infinite lines, what is the largest possible perimeter of a triangle defined by some three lines in the collection?

Input
The first line of input contains a single integer n (3≤n≤100) indicating the number of infinite lines.

The next n lines describe the collection of infinite lines. The ith such line contains four integers x1,y1,x2,y2 (−10000≤x1,y1,x2,y2≤10000) where (x1,y1)≠(x2,y2) are two points lying on the ith infinite line.

Output
Display a single real value which is the perimeter of the largest triangle that can be formed from three of the infinite lines. Your output will be considered correct if it is within an absolute or relative error of 10−5 of the correct answer.

If no triangle can be formed using the given lines, then you should instead display the message no triangle.
"""
import math


def intersection(line1,line2):
    xdb1=-999999
    xdb2=-999999
    if line1[0]-line1[2]==0:
        xdb1=line1[0]
    else:
        a1=(line1[1]-line1[3])/(line1[0]-line1[2])
        b1=line1[1]-a1*line1[0]

    if line2[0]-line2[2]==0:
        xdb2=line2[0]
    else:   
        a2=(line2[1]-line2[3])/(line2[0]-line2[2])
        b2=line2[1]-a2*line2[0]

    if (xdb1!=-999999 and xdb2!=-999999):
        return False
    if xdb1!=-999999:
        y=a2*xdb1+b2
        x=xdb1
        return x,y
    if xdb2!=-999999:
        y=a1*xdb2+b1
        x=xdb2
        return x,y
    else:
        if a1==a2:
            return False
        else:
            x=(b2-b1)/(a1-a2)
            y=a1*x+b1
            return x,y
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

n=int(input())
#Number of infinite lines
line=[0]*n
commonpoint1x=0
commonpoint2x=0
commonpoint3x=0
commonpoint1y=0
commonpoint2y=0
commonpoint3y=0
dis1=0
dis2=0
dis3=0
res=0
for i in range(0,n):
    line[i]=list(map(int,input().split()))
""""
for i in range(n):
    for j in range(i):
        for k in range(j):
"""
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if intersection(line[i],line[j])!=False and intersection(line[j],line[k])!=False and intersection(line[k],line[i])!= False:                
                commonpoint1x,commonpoint1y=intersection(line[i],line[j])                
                commonpoint2x,commonpoint2y=intersection(line[j],line[k])                
                commonpoint3x,commonpoint3y=intersection(line[k],line[i])
                dis1=distance(commonpoint1x,commonpoint1y,commonpoint2x,commonpoint2y)
                dis2=distance(commonpoint2x,commonpoint2y,commonpoint3x,commonpoint3y)
                dis3=distance(commonpoint3x,commonpoint3y,commonpoint1x,commonpoint1y)
                
                if (commonpoint1x==commonpoint2x==commonpoint3x and commonpoint1y==commonpoint2y==commonpoint3y) or (commonpoint1x==commonpoint2x and commonpoint1y==commonpoint2y) or (commonpoint1x==commonpoint3x and commonpoint1y==commonpoint3y) or (commonpoint2x==commonpoint3x and commonpoint2y==commonpoint3y) or dis1+dis2<=dis3 or dis2+dis3<=dis1 or dis1+dis3<=dis2:
                    continue
                else:
                    dis1=distance(commonpoint1x,commonpoint1y,commonpoint2x,commonpoint2y)
                    dis2=distance(commonpoint2x,commonpoint2y,commonpoint3x,commonpoint3y)
                    dis3=distance(commonpoint3x,commonpoint3y,commonpoint1x,commonpoint1y)

                    res=max(res,dis1+dis2+dis3)
if res<=0:
    print("no triangle")
else:       
    print(res)