g=0
h=0
j=0
k=0

chuoimoi=0
listdauhoi=list()
so=0
ketqua=0
n=0
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



while int(k)<10:
    sum=int(g*10**(dodaichuoi-listdauhoi[0]-1)) + int(h*10**(dodaichuoi-listdauhoi[1]-1)) + int(j*10**(dodaichuoi-listdauhoi[2]-1)) + int(k*10**(dodaichuoi-listdauhoi[3]-1)) 
    
    so=chuoimoi+sum

    if kiemtrasonguyento(so)==True:
        ketqua=ketqua+1
    n=n+1


    g=g+1
    if chuoi[0]!="?":

        if g==10 and h==9 and j==9:
            g=0
            h=0
            j=0
            k=k+1
        if g==10 and h==9:
            g=0
            h=0
            j=j+1
        if g==10:
            g=0
            h=h+1
    if chuoi[0]=="?":

        if g==9 and h==9 and j==9:
            g=0
            h=0
            j=0
            k=k+1
        if g==9 and h==9:
            g=0
            h=0
            j=j+1
        if g==9:
            g=0
            h=h+1


print(ketqua)
