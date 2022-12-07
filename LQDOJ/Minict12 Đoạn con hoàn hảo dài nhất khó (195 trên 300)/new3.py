n,limit=list(map(int,input().split()))
lengthmax=0
vitriketthuc=0
chuoi=list(map(int,input().split()))

listkiemtra=list()



for i in range(0,n):
    if int(chuoi[i]) not in listkiemtra:
        listkiemtra.append(chuoi[i])
if len(listkiemtra)<=limit:
    print("1"+" "+ str(n))
else:
    listkiemtra=list()
    for vitribatdau in range(0,n):
        for i in range(vitribatdau,n):
            if (i==n-1 and len(listkiemtra)<limit) or (i==n-1 and len(listkiemtra)==limit and chuoi[i]  in listkiemtra ):
                vitriketthuc=n
                length=vitriketthuc-vitribatdau   
                if length>lengthmax:
                    lengthmax=length
                    l=vitribatdau+1
                    r=vitriketthuc
                listkiemtra=list()
                break        

            if chuoi[i] not in listkiemtra and len(listkiemtra)==limit:
                vitriketthuc=i
                length=vitriketthuc-vitribatdau
                if length>lengthmax:
                    lengthmax=length
                    l=vitribatdau+1
                    r=vitriketthuc
                listkiemtra=list()
                break

            if chuoi[i] not in listkiemtra and len(listkiemtra)<limit:
                listkiemtra.append(chuoi[i])

    print(str(l) +" "+str(r))