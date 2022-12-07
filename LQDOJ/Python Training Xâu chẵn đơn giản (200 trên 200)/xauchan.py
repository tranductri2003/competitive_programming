chuoi=str(input())
chuoitach=list()
for i in range(0,len(chuoi)):
    chuoitach.append(chuoi[i])


    
chuoitach=list(set(chuoitach))


stack=0
for kytu in chuoitach:
    for i in range(0,len(chuoi)):
        if chuoi[i]==kytu:
            stack=stack+1
    if stack%2!=0:
        print("No")
        break
else:
    print("Yes")