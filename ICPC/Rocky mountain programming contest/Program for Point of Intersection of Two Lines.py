line1=list(map(int,input().split()))
line2=list(map(int,input().split()))
xdb1=-9999
xdb2=-9999


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


if xdb1!=-9999 and xdb2!=-9999:
    print("False")
elif xdb1!=-9999:
    y=a2*xdb1+b2
    x=xdb1
elif xdb2!=-9999:
    y=a1*xdb2+b1
    x=xdb2
else:
    x=(b2-b1)/(a1-a2)
    y=a1*x+b1

print(x)
print(y)




