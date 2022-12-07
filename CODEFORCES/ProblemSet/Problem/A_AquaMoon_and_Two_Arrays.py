
testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    if a==b:
        print(0)
    else:

        if sum(a)!=sum(b):
            print(-1)
        else:
            res=0
            tang=[]
            giam=[]
            for i in range(n):
                if a[i]<b[i]:
                    for j in range(b[i]-a[i]):
                        tang.append(i+1)
            for i in range(n):
                if a[i]>b[i]:
                    for j in range(a[i]-b[i]):
                        giam.append(i+1)
            res=len(tang)
            print(res)
            for i in range(res):
                print(giam[i],tang[i])
            

                    
                        
                    
                    

            