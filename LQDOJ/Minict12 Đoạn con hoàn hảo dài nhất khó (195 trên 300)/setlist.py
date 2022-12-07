n,limit=list(map(int,input().split()))
lengthmax=0
vitriketthuc=0
chuoi=list(map(int,input().split()))

listkiemtra=set(chuoi)

if len(listkiemtra)<=limit:
    print("1"+" "+ str(n))
else:


    for vitribatdau in range(0,n):
        print("Vị trí bắt đầu là: "+str(vitribatdau))
        listkiemtra=list()
        for i in range(vitribatdau,n):
            listkiemtra=set(chuoi[vitribatdau:i+1])
            print(listkiemtra)
            print(len(listkiemtra))
            if len(listkiemtra)<=limit and i==n-1:
                vitridau=vitribatdau+1 
                vitricuoi=n
                length=vitricuoi-vitridau+1
                print("length là: "+str(length))
                if length>lengthmax:
                    lengthmax=length
                    l=vitridau
                    print("l hiện tại chính là: "+str(l))
                    r=vitricuoi
                    print("r hiện tại chính là: "+str(r))

            elif len(listkiemtra)>limit:
                vitridau=vitribatdau+1 
                vitricuoi=i
                length=vitricuoi-vitridau+1
                print("length là: "+str(length))
                if length>lengthmax:
                    lengthmax=length
                    l=vitridau
                    print("l hiện tại chính là: "+str(l))
                    r=vitricuoi
                    print("r hiện tại chính là: "+str(r))
                break
 
                
    print(str(l)+" "+str(r))
