solankhongchiahet=0


n=int(input())
chuoi=list(map(int,input().split()))


chuoireplica=chuoi

listchiadu=list()

def kiemtra(list):
    for num in list:
        if num!=0:
            break
    else:
        return True

while kiemtra(listchiadu)!=True or chuoireplica==chuoi:

    for num in chuoireplica:

        for i in chuoireplica:
            if num%i!=0 and i%num!=0:
                solankhongchiahet=solankhongchiahet+1

        listchiadu.append(int(solankhongchiahet))

        solankhongchiahet=0

    if kiemtra(listchiadu)==True:
        break
    vitrichiadunhieunhat=listchiadu.index(max(listchiadu))

    chuoireplica.remove(chuoireplica[vitrichiadunhieunhat])

    listchiadu=list()
    

ketqua=n-len(chuoireplica)
print(ketqua)