import math

testcase=int(input())
solvedcase=0



def tich(x,y,b):
    
    ca=math.sqrt((b-y)**2 +x**2)
    cb=math.sqrt(y**2+(((-1*b*x)/(y-b))-x)**2)
    return ca*cb


while solvedcase<testcase:


    diem=list(map(int,input().split()))
    if diem[0]==diem[1]:
        print(2*   (diem[0]**2))
        solvedcase=solvedcase+1
    

    else:

        b=diem[1]*1.000005

        while 0<b:
            
            if tich(diem[0],diem[1],b)<tich(diem[0],diem[1],b+diem[1]*0.01):
                
                if tich(diem[0],diem[1],b)>tich(diem[0],diem[1],b+0.000004):     #Trường hợp 1 2 và 4
                    while tich(diem[0],diem[1],b)>tich(diem[0],diem[1],b+0.000004):
                        b=b+diem[1]*0.000004                  
                    print(round(tich(diem[0],diem[1],b)))
                    solvedcase=solvedcase+1
                    break
                if tich(diem[0],diem[1],b)<tich(diem[0],diem[1],b+0.000004):     #Trường hợp 1 và 2 4
                    while tich(diem[0],diem[1],b)<tich(diem[0],diem[1],b+0.000004):
                        b=b-diem[1]*0.000004
                    print(round(tich(diem[0],diem[1],b+0.000004)))
                    solvedcase=solvedcase+1
                    break

            b=b+diem[1]*0.01

