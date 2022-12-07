g=0


chuoimoi=0
listdauhoi=list()
so=0
ketqua=0

def kiemtrasonguyento(n):
    if n==1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                break #Nếu bị break sẽ bỏ qua else phía dưới
        else: 
            return True


chuoi=str(input())

dodaichuoi=int(len(chuoi))

for i in range(0,dodaichuoi):
    if i==0 and chuoi[i]=="?":
        listdauhoi.append(i)
        chuoimoi=1

    else:
        if chuoi[i]=="?":
            chuoimoi=chuoimoi*10
            listdauhoi.append(i)
        else:
            chuoimoi=chuoimoi*10+int(chuoi[i])



while int(g)<10:
    sum=int(g*10**(dodaichuoi-listdauhoi[0]-1)) 
    
    so=chuoimoi+sum
    if kiemtrasonguyento(so)==True:
        ketqua=ketqua+1



    g=g+1


print(ketqua)
