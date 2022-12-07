n,limit=list(map(int,input().split()))


chuoi=list(map(int,input().split()))
sochusokhacnhautrongchuoi=0

listsokytu=list()
lengthmax=0
l=0
r=0

for i in range(0,n):
    if int(chuoi[i]) not in listsokytu:
        listsokytu.append(chuoi[i])
        sochusokhacnhautrongchuoi=sochusokhacnhautrongchuoi+1




if sochusokhacnhautrongchuoi<=limit:
    print("1"+" "+ str(n))
else:            #sochusokhacnhautrongchuoi>limit
    for vitribatdau in range(0,sochusokhacnhautrongchuoi-limit+1):    
        print("Vị trí bắt đầu hiện giờ là: "+str(vitribatdau))
        if vitribatdau==0:
            vitridau=1
            giatricuoi=listsokytu[limit]
            print("Giá trị cuối là "+ str(giatricuoi))
            for i in range(0,n):
                if chuoi[i]==giatricuoi:
                    print("i là "+str(i))
                    
                    vitricuoi=i
            length=vitricuoi-vitridau+1
            print("Độ dài chuỗi vừa rồi: "+str(length))
            if length>lengthmax:
                lengthmax=length
                l=vitridau
                print("l là: "+ str(l))
                r=vitricuoi
                print("r là: "+ str(r))

        elif vitribatdau==sochusokhacnhautrongchuoi-limit:
            vitricuoi=n
            giatridau=listsokytu[sochusokhacnhautrongchuoi-limit-1]
            print("Giá trị đầu là "+ str(giatridau))
            for i in range(n-1,0,-1):
                if chuoi[i]==giatridau:
                    print("i là "+str(i))
                    vitridau=i+2
            length=vitricuoi-vitridau+1
            if length>lengthmax:
                lengthmax=length
                l=vitridau
                r=vitricuoi
                print("l là: "+ str(l))
                print("r là: "+ str(r))

        else: 
            giatridau=listsokytu[vitribatdau-1]
            print("Giá trị đầu là "+ str(giatridau))           
            for i in range(n-1,0,-1):
                if chuoi[i]==giatridau:
                    print("i là "+str(i))
                    vitridau=i+2
                    break
            giatricuoi=listsokytu[vitribatdau+limit]
            print("Giá trị cuối là "+ str(giatricuoi))  
            for i in range(0,n):
                if chuoi[i]==giatricuoi:
                    print("i là "+str(i))
                    vitricuoi=i
                    break
            length=vitricuoi-vitridau+1
            if length>lengthmax:
                lengthmax=length
                l=vitridau
                r=vitricuoi     
                print("l là: "+ str(l))
                print("r là: "+ str(r)) 
        
        print("Tăng vị trí bắt đầu")


    print(str(l)+" "+str(r))
