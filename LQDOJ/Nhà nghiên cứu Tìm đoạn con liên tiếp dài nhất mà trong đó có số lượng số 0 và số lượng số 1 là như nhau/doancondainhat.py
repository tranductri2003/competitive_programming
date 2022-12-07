soluong1=0
soluong0=0
sum=0

i=0
chuoicon=0
vitribatdau=0


N=int(input())
chuoi=input()
chuoi=chuoi.replace(' ', '')

chuoi=str(chuoi)


#Xử lí chuỗi con bằng 0
for i in range (0,N):
    sum=sum+1*10**(i)
if int(chuoi)-0==0:
    print("0")
    quit()
if int(chuoi)-sum==0:
    print("0")
    quit()

for i in range (0,N):
    if chuoi[i]=="0":
        soluong0=soluong0+1
    if chuoi[i]=="1":
        soluong1=soluong1+1

if soluong0==soluong1:
    print(soluong1*2)
else:
    a=min(soluong0,soluong1)


    dolonchuoihientai=a*2
    soluong1=0
    soluong0=0
    while 2<=dolonchuoihientai<=2*a:
        while 0<=vitribatdau<=N-dolonchuoihientai:
            chuoicon=chuoi[vitribatdau:vitribatdau+dolonchuoihientai]
            while 0<=i<=dolonchuoihientai-1:
                if chuoicon[i]=="0":
                    soluong0=soluong0+1
                if chuoicon[i]=="1":
                    soluong1=soluong1+1
                if i==dolonchuoihientai-1:
                    if soluong0==soluong1:
                        print(str(dolonchuoihientai))
                        quit()
                    if soluong0!=soluong1:
                        break
                i=i+1  
            if vitribatdau==N-dolonchuoihientai:
                break
            vitribatdau=vitribatdau+1
            i=0
            soluong0=0
            soluong1=0
        i=0
        vitribatdau=0
        soluong1=0
        soluong0=0
        dolonchuoihientai=dolonchuoihientai-2
        


