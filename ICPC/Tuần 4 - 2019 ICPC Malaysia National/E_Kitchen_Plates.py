
vitri=["A","B","C","D","E"]



data=[]
for i in range(5):
    string=input()
    data.append(string)

stop=False
touch=False
time=0
while stop!=True:
    touch=False
    for string in data:
        chudau=string[0]
        dau=string[1]
        chusau=string[2]
        
        if dau=="<":
            chudau,chusau=chusau,chudau
        if vitri.index(chudau)>vitri.index(chusau):
            pass
        else:
            vitri1=vitri.index(chudau)
            vitri2=vitri.index(chusau)
            vitri[vitri1],vitri[vitri2]=vitri[vitri2],vitri[vitri1]
            touch=True
                
    time+=1
    if time==1000:
        print("impossible")
        quit()
    if touch==False:
        for num in vitri:
            print(num,end="")
        quit()
    
    
            
            
    