dodai=list(map(int,input().split()))
chuoi=list(map(int,input().split()))
listsoam=list()
listvitrichuasoam=list()


def kiemtrasochan(list):
    for num in list:
        if num%2==0:
            return True
        else:
            return False




for i in range(0,len(chuoi)):
    if chuoi[i]<=0:
        listsoam.append(chuoi[i])
        listvitrichuasoam.append(i)



if len(listsoam)%2==0 or len(listsoam)==0:
    print (len(chuoi))

else:
    vitriamcuoi=int(listvitrichuasoam[len(listvitrichuasoam)-1])
    vitriapamdau=int(listvitrichuasoam[0])+1
    
    chuoi1=chuoi[0:vitriamcuoi]
    chuoi2=chuoi[vitriapamdau:]

    dodaichuoi1=len(chuoi1)
    dodaichuoi2=len(chuoi2)

    if kiemtrasochan(chuoi1) == True and kiemtrasochan(chuoi2)==True:
        print(max(dodaichuoi1,dodaichuoi2))
    elif kiemtrasochan(chuoi1) == True and kiemtrasochan(chuoi2)==False:
        print(dodaichuoi1)
    elif kiemtrasochan(chuoi1) == False and kiemtrasochan(chuoi2)==True:
        print(dodaichuoi2)   
    else:
        print(max(dodaichuoi1,dodaichuoi2)) #Full chẵn hoặc số 0 đầu :)))