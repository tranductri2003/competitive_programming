

string,m=input().split()

count=0
stop=False
while stop==False:
    string=list(string)
    string.insert(0,-1)
    string.append(-1)
    stack=1
    data=[]
    vitribatdau=[]
    for i in range(1,len(string)):
        if string[i]==string[i-1]:
            stack+=1
        else:
            if stack!=0:
                data.append(stack)
                vitribatdau.append(i-1-stack)
            
                stack=1
    data.pop(0) 
    vitribatdau.pop(0)
    string.pop(0)
    string.pop(-1)
    print(data)
    print(vitribatdau)
    if max(data)<int(m):
        stop=True
    else:
        vitri=data.index(max(data))
        batdau=vitribatdau[vitri]
        print(batdau)
        for i in range(max(data)):
            string.pop(batdau)
        print(string)
    count+=1
    if count==3:
        quit()

    
        
