n,q=list(map(int,input().split()))
s=input()
for i in range(q):
    l,r=list(map(int,input().split()))
    subString=list(s[l-1:r])


    stackLeft=0
    stackRight=0
    
    res=0
    tieptuc=1

    stop=0
    
    while tieptuc==1:
        stackLeft=0
        stackRight=0
        stop=0
        for i in range(len(subString)):
            tieptuc=0
            if s[i]=="(":
                stackLeft+=1
            if s[i]==")" and stackLeft>0:
                for j in range(i,len(subString)):
                    if s[j]==")" and j==len(subString)-1:
                        stackRight+=1
                        res+=1
                        tieptuc=1
                        
                        subString2=[]
                        for k in range(len(subString)):
                            if k<=j-2*(min(stackRight,stackLeft)):
                                subString2.append(subString[k])
                        subString=subString2
                        stop=1   
                        break
                    elif s[j]==")" and stackRight<stackLeft:
                        stackRight+=1
                    else:  #Dừng
                        # print(min(stackRight,stackLeft),j)
                        res+=1
                        tieptuc=1
                        
                        subString2=[]
                        for k in range(len(subString)):
                            if k<j-2*(min(stackRight,stackLeft)) or k>=j:
                                subString2.append(subString[k])
                        subString=subString2
                        stop=1   
                        break
            if stop==1:
                tieptuc=1
                break
        else:
            break
    print(res)                        