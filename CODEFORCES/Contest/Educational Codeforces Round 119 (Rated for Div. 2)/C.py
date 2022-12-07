testcase=int(input())

for test in range(testcase):
    n,k,x=list(map(int,input().split()))
    s=input()
    
    sokhoangdausao=[]
    stack=0
    current=False
    for i in range(0,n):
        if s[i]=="*":
            if current==False:
                current=True
                stack=1
            else:
                stack+=1
        else:
            if current==True:
                sokhoangdausao.append(stack)
                stack=0
                current=False
        if i==n-1 and current==True:
            sokhoangdausao.append(stack)

    for i in range(0,len(sokhoangdausao)):
        sokhoangdausao[i]=sokhoangdausao[i]*k
    
    giatridausao=[1]*len(sokhoangdausao)
    for i in range(len(sokhoangdausao)-2,-1,-1):
        giatridausao[i]=(giatridausao[i+1]+1)
    print(giatridausao)
        
    
    
    
    