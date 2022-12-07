n=int(input("Nhập số chữ số của chuỗi: "))
chuoi=list(map(int,input("Nhập chuỗi: ").split()))
sochusotoida=int(input("Số chữ số tối đa của chuỗi: "))
print(chuoi)
sochuso=0
listsokytu=list()
dodaimax=0
for i in range(0,n):
    if int(chuoi[i]) not in listsokytu:
        listsokytu.append(chuoi[i])
        sochuso=sochuso+1

print(listsokytu)

dodaimax=0
l=0
r=0
if sochuso<=sochusotoida:
    print("1 "+ str(n))
else:            #sochuso>sochusotoida
    for vitribatdau in range(0,sochuso-sochusotoida+1): 
        
        #Trường hợp đặc biệt khi vitribatdau khả dĩ cuối cùng
        if vitribatdau==sochuso-sochusotoida:
            for i in range(0,n):
                if chuoi[i]==listsokytu[vitribatdau]:
                    vitridau=i+1
                    break
            dodai=n-vitridau+1
            if dodai>dodaimax:
                dodaimax=dodai
                l=vitridau+1
                r=n       
        else:        #Tìm vị trí của listsokytu[vitribatdau] và listsokytu[vitribatdau+sokytutoida]
            for i in range(0,n):                
                if chuoi[i]==listsokytu[vitribatdau]:                 
                    vitridau=i+1
                    break
            for i in range(n-1,0,-1):
                if chuoi[i]==listsokytu[vitribatdau+sochusotoida]:                    
                    vitriketthuc=i
                    break
            dodai=vitriketthuc-vitridau+1
            if dodai>dodaimax:
                dodaimax=dodai
                l=vitridau
                r=vitriketthuc
            
print(str(l)+" "+str(r))