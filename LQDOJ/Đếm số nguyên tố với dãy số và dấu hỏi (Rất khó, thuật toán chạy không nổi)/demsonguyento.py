g=0
h=0
j=0
k=0
l=0
chuoimoi=0
listdauhoi=list()
socauhoi=0
so=0
ketqua=0
n=0
def kiemtrasonguyento(n):
    bienthu=0
    bienhotro=0
    vitribienthu=0
    

    listsonguyento=list(range(2,10*10**(6)))	        


    while listsonguyento[vitribienthu] != max(listsonguyento):
        bienthu=listsonguyento[vitribienthu]
        bienhotro=listsonguyento[vitribienthu]
        bienthu=bienthu+bienhotro
        while bienthu<=n:
            
            
            if bienthu in listsonguyento:
                listsonguyento.remove(bienthu)
            bienthu=bienthu+bienhotro
            
        
        bienthu=0
        bienhotro=0
        vitribienthu=vitribienthu+1
        
    if n in listsonguyento:
        return True



chuoi=str(input())




dodaichuoi=int(len(chuoi))

for i in range(0,dodaichuoi):
    if i==0 and chuoi[i]=="?":
        listdauhoi.append(i)
        chuoimoi=1
        socauhoi=socauhoi+1

    else:
        if chuoi[i]=="?":
            chuoimoi=chuoimoi*10
            listdauhoi.append(i)
            socauhoi=socauhoi+1
        else:
            chuoimoi=chuoimoi*10+int(chuoi[i])


if socauhoi==5:
    while int(l)<10:
        sum=int(g*10**(dodaichuoi-listdauhoi[0]-1)) + int(h*10**(dodaichuoi-listdauhoi[1]-1)) + int(j*10**(dodaichuoi-listdauhoi[2]-1)) + int(k*10**(dodaichuoi-listdauhoi[3]-1)) + int(l*10**(dodaichuoi-listdauhoi[4]-1))
        
        so=chuoimoi+sum

        if kiemtrasonguyento(so)==True:
            ketqua=ketqua+1
        

        g=g+1
        if chuoi[0]!="?":
            if g==10 and h==9 and j==9 and k==9:
                g=0
                h=0
                j=0
                k=0
                l=l+1

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
            if g==9 and h==9 and j==9 and k==9:
                g=0
                h=0
                j=0
                k=0
                l=l+1

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
if socauhoi==4: 
    while int(k)<10:
        sum=int(g*10**(dodaichuoi-listdauhoi[0]-1)) + int(h*10**(dodaichuoi-listdauhoi[1]-1)) + int(j*10**(dodaichuoi-listdauhoi[2]-1)) + int(k*10**(dodaichuoi-listdauhoi[3]-1)) 
        
        so=chuoimoi+sum

        if kiemtrasonguyento(so)==True:
            ketqua=ketqua+1
        


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
if socauhoi==3: 
    while int(j)<10:
        sum=int(g*10**(dodaichuoi-listdauhoi[0]-1)) + int(h*10**(dodaichuoi-listdauhoi[1]-1)) + int(j*10**(dodaichuoi-listdauhoi[2]-1)) 
        
        so=chuoimoi+sum

        if kiemtrasonguyento(so)==True:
            ketqua=ketqua+1
        


        g=g+1
        if chuoi[0]!="?":

            if g==10 and h==9:
                g=0
                h=0
                j=j+1
            if g==10:
                g=0
                h=h+1
        if chuoi[0]=="?":

            if g==9 and h==9:
                g=0
                h=0
                j=j+1
            if g==9:
                g=0
                h=h+1

if socauhoi==2:
    while int(h)<10:
        sum=int(g*10**(dodaichuoi-listdauhoi[0]-1)) + int(h*10**(dodaichuoi-listdauhoi[1]-1)) 
        
        so=chuoimoi+sum
        if kiemtrasonguyento(so)==True:
            ketqua=ketqua+1



        g=g+1
        if chuoi[0]!="?":
    
            if g==10:
                g=0
                h=h+1
        if chuoi[0]=="?":

            if g==9:
                g=0
                h=h+1
if socauhoi==1: 

    while int(g)<10:
        sum=int(g*10**(dodaichuoi-listdauhoi[0]-1)) 
        
        so=chuoimoi+sum
        if kiemtrasonguyento(so)==True:
            ketqua=ketqua+1



        g=g+1

print(ketqua)



