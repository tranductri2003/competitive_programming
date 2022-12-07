n=int(input())
chuoi=list(map(int,input().split()))

def binary_search(chuoinhatbien,giatricanxacdinhvitri):
    bottom=0
    top=len(chuoinhatbien)-1

    while bottom<=top:
        middle=(bottom+top)//2

        if chuoinhatbien[middle]==giatricanxacdinhvitri:
            return middle
    
        elif chuoinhatbien[middle]>giatricanxacdinhvitri:
            top=middle-1
        else:
            bottom=middle+1
    return middle







if min(chuoi)>0 or max(chuoi)<0:
    print("0")
elif min(chuoi)==max(chuoi)==0:
    print(round(n*(n-1)/2))
else:
    chuoi.sort()

    vitriso0=binary_search(chuoi,0)

    for i in range(vitriso0,-1,-1):
        if chuoi[i]<0:
            giatriamcuoicung=i
            break
    for i in range(vitriso0,n):

        if chuoi[i]>0:
            giatriduongdautien=i
            break
    chuoiam=chuoi[0:giatriamcuoicung+1]
    chuoiduong=chuoi[giatriduongdautien:]


    dolonchuoiam=len(chuoiam)
    dolonchuoiduong=len(chuoiduong)

    soluongso0=n-dolonchuoiam-dolonchuoiduong
    capchuaso0=round(soluongso0*(soluongso0-1)/2)

    j=dolonchuoiduong-1
    i=0
    ans=0
    stacki=1
    stackj=1    

    while    i<dolonchuoiam and j>=0:

        if chuoiam[i]+chuoiduong[j]<0:
            i=i+1
        elif chuoiam[i]+chuoiduong[j]>0:
            j=j-1
        else:
            if i<=dolonchuoiam-2 and j>=1 and (chuoiam[i+1]==chuoiam[i] or chuoiduong[j-1]==chuoiduong[j]):  #Vị trí áp để mảng không bị out of index
                while i<=dolonchuoiam-2 and chuoiam[i+1]==chuoiam[i]: #Vị trí áp để mảng không bị out of index
                    stacki=stacki+1
                    i=i+1
                while j>=1 and  chuoiduong[j-1]==chuoiduong[j]: #Vị trí áp để mảng không bị out of index
                    stackj=stackj+1
                    j=j-1
                ans=ans+stacki*stackj
                stacki=1
                stackj=1
                i=i+1
                j=j-1
                #Phải thay đổi 2 con trỏ lần cuối để kết thúc hoàn toán quá trình tính stack nhân nhau
            else:
                j=j-1
                ans=ans+1



                
    print(ans+capchuaso0)