t=int(input())
for _ in range(t):
    n=int(input())

    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))
    
    temp=[]
    
    so=0
    somax=max(max(a1),max(a2))
    if a2[0]==somax or a2[1]==somax:
        for j in range(1,n):
            temp.append(a1[j])
        for j in range(n-1,-1,-1):
            temp.append(a2[j]) 
    elif a1[1] ==somax:
        for j in range(0,n):
            temp.append(a2[j])
        for j in range(n-1,0,-1):
            temp.append(a1[j])
    else:
        temp=[a2[0]]
        for i in range(1,n):
            if i%2==1:  #Đi lên
                if a1[i+1]==somax:
                    for j in range(i,n):
                        temp.append(a2[j])
                    for j in range(n-1,i,-1):
                        temp.append(a1[j])
                    break  
                temp.append(a2[i])
                temp.append(a1[i])
            else:  # Đi xuống
                if a2[i]==somax or a2[i+1]==somax:
                    for j in range(i,n):
                        temp.append(a1[j])
                    for j in range(n-1,i-1,-1):
                        temp.append(a2[j])
                    break
                else:
                    temp.append(a1[i])
                    temp.append(a2[i])
                    if a1[i+1]==somax:
                        for j in range(i+1,n):
                            temp.append(a2[j])
                        for j in range(n-1,i,-1):
                            temp.append(a1[j])
                        break      
    res=0
    for num in temp:
        if res>=num:
            res+=1
        else:
            res=num+1
    print(res)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    