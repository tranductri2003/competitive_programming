

def check(s1,s2):
    s1=str(s1)
    s1="0"*(2-len(s1))+s1
    s2=str(s2)
    s2="0"*(2-len(s2))+s2
    chuoi=s1+s2
    if chuoi==chuoi[::-1]:
        return True
    else:
        return False

t=int(input())
for _ in range(t):
    s,x=input().split()
    x=int(x)
    gio=int(s[0]+s[1])
    phut=int(s[3]+s[4])
    

    res=0
    
    if check(gio,phut)==True:
        res+=1
    
    giogoc=gio
    phutgoc=phut
    
    giomoi=gio
    phutmoi=phut
    
    giomoi=(giomoi+(phutmoi+x)//60)%24  
    phutmoi=(phutmoi+x)%60
    
    
    
    while giomoi!=giogoc or phutmoi!=phutgoc:
        if check(giomoi,phutmoi)==True:
            res+=1
        giomoi=(giomoi+(phutmoi+x)//60)%24  
        phutmoi=(phutmoi+x)%60
    print(res)
