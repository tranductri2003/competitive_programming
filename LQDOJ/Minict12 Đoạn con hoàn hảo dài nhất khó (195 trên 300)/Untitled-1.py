nvak=list(map(int,input().split()))

n=nvak[0]
limit=nvak[1]


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
    print("1 "+ str(n))
else:            #sochusokhacnhautrongchuoi>limit
    for vitribatdau in range(0,sochusokhacnhautrongchuoi-limit+1):       
        if vitribatdau==sochusokhacnhautrongchuoi-limit:         #Trường hợp đặc biệt khi vitribatdau khả dĩ cuối cùng
            a=listsokytu[vitribatdau]
            for i in range(0,n):
                if chuoi[i]==a:
                    vitridau=i+1
                    break
            dodai=n-vitridau+1

            if dodai>lengthmax:
                lengthmax=dodai
                l=vitridau+1
                r=n       
        else:        #Tìm vị trí của listsokytu[vitribatdau] và listsokytu[vitribatdau+sokytutoida]
            a=listsokytu[vitribatdau]
            for i in range(0,n):                
                if chuoi[i]==a:                    
                    vitridau=i+1
                    break
            b=listsokytu[vitribatdau+limit]
            for i in range(n-1,0,-1):
                if chuoi[i]==b:                    
                    vitriketthuc=i
                    break
            dodai=vitriketthuc-vitridau+1

            if dodai>lengthmax:
                lengthmax=dodai
                l=vitridau
                r=vitriketthuc
            
print(str(l)+" "+str(r))