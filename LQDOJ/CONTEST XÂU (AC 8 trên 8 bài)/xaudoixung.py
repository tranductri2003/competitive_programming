

chuoi=input()
sole=0
stack=0
listkytu=set(chuoi)

for kytu in listkytu:
    for i in range(0,len(chuoi)):
        if chuoi[i]==kytu:
            stack=stack+1

    if stack%2!=0:
        sole=sole+1 
    stack=0


print(sole-1)