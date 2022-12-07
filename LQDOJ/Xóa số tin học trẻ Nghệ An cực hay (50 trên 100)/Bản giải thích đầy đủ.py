solankhongchiahet=0


n=int(input())
chuoi=list(map(int,input().split()))
print(chuoi)

chuoireplica=chuoi
print(chuoireplica)
listchiadu=list()

def kiemtra(list):
    for num in list:
        if num!=0:
            break
    else:
        return True

while kiemtra(listchiadu)!=True or chuoireplica==chuoi:

    for num in chuoireplica:
        print("Đang kiểm tra số: "+str(num))
        for i in chuoireplica:
            if num%i!=0 and i%num!=0:
                solankhongchiahet=solankhongchiahet+1
        print("Số lần chia dư là: "+str(solankhongchiahet))
        listchiadu.append(int(solankhongchiahet))

        solankhongchiahet=0
    print("list chia dư hiện tại là: "+str(listchiadu))
    if kiemtra(listchiadu)==True:
        break
    vitrichiadunhieunhat=listchiadu.index(max(listchiadu))
    print("Vị trí chia dư nhiều nhất là:" +str(vitrichiadunhieunhat))
    chuoireplica.remove(chuoireplica[vitrichiadunhieunhat])
    print("Chuỗi replica hiện tại là: "+str(chuoireplica))
    listchiadu=list()
    

ketqua=n-len(chuoireplica)
print(ketqua)