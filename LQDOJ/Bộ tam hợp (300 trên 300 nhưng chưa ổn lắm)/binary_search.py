def binary_search(chuoinhatbien,giatricanxacdinhvitri):
    bottom=0
    top=len(chuoinhatbien)-1

    while bottom<=top:
        middle=(bottom+top)//2

        if chuoinhatbien[middle]==giatricanxacdinhvitri:
            return True
    
        elif chuoinhatbien[middle]>giatricanxacdinhvitri:
            top=middle-1
        else:
            bottom=middle+1







n=int(input())
chuoi=list(map(int,input().split()))

chuoi.sort()
chuoichan=list()
chuoile=list()



for num in chuoi:
    if num%2==0:
        chuoichan.append(num)        
    else:
        chuoile.append(num)


dodaichuoichan=len(chuoichan)
dodaichuoile=n-dodaichuoichan


soluongtamhop=0
maxchan=maxle=-1000000

if dodaichuoichan>=2:
    for i in range(0,dodaichuoichan-1):
        for j in range(i+1,dodaichuoichan):
            trungbinhcong=round((chuoichan[i]+chuoichan[j])/2)
            if binary_search(chuoi,trungbinhcong)==True:
                soluongtamhop=soluongtamhop+1
                maxchan=max(maxchan,trungbinhcong*3)



if dodaichuoile>=2:
    for i in range(0,dodaichuoile-1):
        for j in range(i+1,dodaichuoile):
            trungbinhcong=round((chuoile[i]+chuoile[j])/2)
            if binary_search(chuoi,trungbinhcong)==True:
                soluongtamhop=soluongtamhop+1
                maxle=max(maxle,trungbinhcong*3)



print(soluongtamhop)
print(max(maxchan,maxle))


