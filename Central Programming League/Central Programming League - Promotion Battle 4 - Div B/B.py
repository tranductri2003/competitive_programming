t=int(input())

#w: soi, s: cuu, c: cai
for _ in range(t):
    w,s,c,k=list(map(int,input().split()))  

    if w+c>k and s>k:
        print(0)
    elif s<k:
        print(1)
        soibo1=w
        caibo1=c


        while soibo1>0 or caibo1>0:
            soiTrenThuyen=0
            caiTrenThuyen=0
            cuuTrenThuyen=0


            cuuTrenThuyen=s
            chotrong=k-cuuTrenThuyen
            if chotrong>=caibo1:
                caiTrenThuyen=caibo1
                soiTrenThuyen=min(soibo1,chotrong-caibo1)
                soibo1-=soiTrenThuyen
                caibo1-=caiTrenThuyen
            else:
                caiTrenThuyen=chotrong
                caibo1-=caiTrenThuyen


            print(soiTrenThuyen,cuuTrenThuyen,caiTrenThuyen)
            if soibo1<=0 and caibo1<=0:
                print(-1,-1,-1)
                break
            else:
                print(0,s,0)
            

            
    elif w+c<k:
        print(1)
        
        cuubo1=s


        while cuubo1>0:
            soiTrenThuyen=0
            caiTrenThuyen=0
            cuuTrenThuyen=0


            caiTrenThuyen=c
            soiTrenThuyen=w
            cuuTrenThuyen=min(cuubo1,k-(caiTrenThuyen+soiTrenThuyen))
            cuubo1-=cuuTrenThuyen
            
            print(soiTrenThuyen,cuuTrenThuyen,caiTrenThuyen)
            if cuubo1<=0:
                print(-1,-1,-1)
                break
            else:
                print(soiTrenThuyen,0,caiTrenThuyen)
    elif w+c==k and s<=2*k:
        print(1)
        print(w,0,c)
        print(0,0,0)
        
        if k>=s:
            print(0,s,0)
            print(-1,-1,-1)
        else:  #s>k
            print(0,k,0)
            print(w,0,c)
            print(0,s-k,0)
            print(0,0,0)
            print(w,0,c)
            print(-1,-1,-1)



    elif s==k and (w+c)<=2*k:
        soibo1=w
        caibo1=c
        print(1)
        print(0,s,0)
        print(0,0,0)
        
        if w<=k:
            soiTrenThuyen=w
            caiTrenThuyen=k-soiTrenThuyen
            caibo1-=caiTrenThuyen
            print(soiTrenThuyen,0,caiTrenThuyen)
            print(0,s,0)
            
            #xong sói

            if caibo1<=k:
                print(0,0,caibo1)
                print(0,0,0)
                print(0,s,0)
                print(-1,-1,-1)
            else:
                print(0,0,k)
                caibo1=caibo1-k
                print(0,0,0)
                print(0,0,caibo1)
                print(0,0,0)
                print(0,s,0)
                print(-1,-1,-1)
        else:
            soiTrenThuyen=k
            soibo1-=soiTrenThuyen
            caiTrenThuyen=0
            print(soiTrenThuyen,0,caiTrenThuyen)
            print(0,s,0)
            print(soibo1,0,c)
            print(0,0,0)
            print(0,s,0)
            print(-1,-1,-1)

    else:
        print(0)
        

