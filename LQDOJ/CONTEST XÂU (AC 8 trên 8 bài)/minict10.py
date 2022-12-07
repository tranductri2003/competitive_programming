chuoi=input()

chuoi=chuoi.split("+")
chuoi.sort()


for i in range(0,len(chuoi)):
    if i==len(chuoi)-1:
        print(chuoi[i])
    else:
        print(chuoi[i]+str("+"),end="")
    
    

