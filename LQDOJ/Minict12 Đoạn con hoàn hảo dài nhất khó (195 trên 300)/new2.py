n,limit=list(map(int,input().split()))
lengthmax=0
vitriketthuc=0
chuoi=list(map(int,input().split()))

ketthucvongfor=False
listkiemtra=list()




for vitribatdau in range(0,n-5):
    for i in range(vitribatdau,n):
        if chuoi[i] not in listkiemtra and len(listkiemtra)==limit:
            vitriketthuc=i
            ketthucvongfor=True
        if chuoi[i] not in listkiemtra and len(listkiemtra)<limit:
            listkiemtra.append(chuoi[i])

        if ketthucvongfor==True:
            length=vitriketthuc-vitribatdau
            if length>lengthmax:
                lengthmax=length
                l=vitribatdau+1
                r=vitriketthuc

            ketthucvongfor=False
            listkiemtra=list()
            break
            


print(str(l) +" "+str(r))