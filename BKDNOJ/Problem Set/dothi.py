# https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=DUT21A

xa,ya=list(map(int,input().split()))
xb,yb=list(map(int,input().split()))
xc,yc=list(map(int,input().split()))



if xa==xb: #Đường thẳng có dạng x=xa=xb
    if xc>xa:
        if yb>ya:
            print("RIGHT")
        else:
            print("LEFT")
    elif xc==xa:
        if ya<yb:
            if yc>yb:
                print("TOWARDS")
            else:
                print("RIGHT")
        else:
            if yc<yb:
                print("TOWARDS")
            else:
                print("RIGHT")
    else:
        if yb>ya:
            print("LEFT")
        else:
            print("RIGHT")
elif ya==yb: #Đường thẳng có dạng y=ya=yb
    if yc>ya:
        if xa<xb:
            print("LEFT")
        else:
            print("RIGHT")
    elif yc==ya:
        if xa<xb:
            if xc>xb:
                print("TOWARDS")
            else:
                print("RIGHT")
        else:
            if xc<xb:
                print("TOWARDS")
            else:
                print("RIGHT")
    else:
        if xa<xb:
            print("RIGHT")
        else:
            print("LEFT")
else:       
    a=(ya-yb)/(xa-xb)
    b=ya-a*xa    
    #Phương trình là y=ax+b
    if a*xc+b-yc==0:
        if xa<xb:
            if xc>xb:
                print("TOWARDS")
            else:
                print("RIGHT")
        else:
            if xc<xb:
                print("TOWARDS")
            else:
                print("RIGHT")
    elif a*xc+b-yc>0:
        if xa<xb:
            print("RIGHT")
        else:
            print("LEFT")
    else:
        if xa<xb:
            print("LEFT")
        else:
            print("RIGHT")