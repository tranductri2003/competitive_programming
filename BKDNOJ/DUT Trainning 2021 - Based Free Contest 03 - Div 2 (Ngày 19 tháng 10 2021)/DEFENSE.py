

xb,yb,vbx,vby=list(map(int,input().split()))
xr,yr,vrx,vry=list(map(int,input().split()))


 
if vrx==vbx and vry==vby:
    print(-1)

elif vrx==vbx and vry!=vby:
    ty=(yb-yr)/(vry-vby)
    if ty>=0:
        a=xb+vbx*ty
        b=yb+vby*ty
                
        print(str(a)+str("000"),end=" ")
        print(str(b)+str("000"))
elif vrx!=vbx and vry==vby:
    tx=(xb-xr)/(vrx-vbx) 
    if tx>=0:
        a=xb+vbx*tx
        b=yb+vby*tx            
        print(str(a)+str("000"),end=" ")
        print(str(b)+str("000"))
else: 
    if vrx!=vbx and vry!=vby:
        tx=(xb-xr)/(vrx-vbx)
    ty=(yb-yr)/(vry-vby)

    if tx==ty and tx>=0:
        a=xb+vbx*tx
        b=yb+vby*ty
            
        print(str(a)+str("000"),end=" ")
        print(str(b)+str("000"))

    else:
        print(-1)