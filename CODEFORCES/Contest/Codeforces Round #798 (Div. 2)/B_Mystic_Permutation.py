from collections import defaultdict
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    if n==1:
        print(-1)
    elif n==2:
        if a[0]==1:
            print(2,1)
        else:
            print(1,2)
    else:
        res=[-1]*n

        check=defaultdict(lambda:0)
        for i in range(n):
            check[a[i]]=i
        for i in range(1,n-2):
            for j in range(n):
                if res[j]==-1 and check[i]!=j:
                    res[j]=i
                    break
        vitritrong=[]
        for i in range(n):
            if res[i]==-1:
                vitritrong.append(i)
        res1=res.copy()
        res1[vitritrong[0]]=n-2
        res1[vitritrong[1]]=n-1
        res1[vitritrong[2]]=n
        for i in range(n):
            if res1[i]==a[i]:
                res1=[10000]*n
                break
                

        res2=res.copy()   
        res2[vitritrong[0]]=n-2
        res2[vitritrong[1]]=n
        res2[vitritrong[2]]=n-1
        for i in range(n):
            if res2[i]==a[i]:
                res2=[10000]*n
                break
                
        res3=res.copy()
        res3[vitritrong[0]]=n-1
        res3[vitritrong[1]]=n-2
        res3[vitritrong[2]]=n
        for i in range(n):
            if res3[i]==a[i]:
                res3=[10000]*n
                break
            
            
        res4=res.copy()
        res4[vitritrong[0]]=n-1
        res4[vitritrong[1]]=n
        res4[vitritrong[2]]=n-2
        for i in range(n):
            if res4[i]==a[i]:
                res4=[10000]*n
                break
            
        res5=res.copy()
        res5[vitritrong[0]]=n
        res5[vitritrong[1]]=n-1
        res5[vitritrong[2]]=n-2
        for i in range(n):
            if res5[i]==a[i]:
                res5=[10000]*n
                break
            
            
        res6=res.copy()      
        res6[vitritrong[0]]=n
        res6[vitritrong[1]]=n-2
        res6[vitritrong[2]]=n-1
        for i in range(n):
            if res6[i]==a[i]:
                res6=[10000]*n
                break
        
        data=[]
        print(max(res1,res2,res3,res4,res5,res6))
        


 

                