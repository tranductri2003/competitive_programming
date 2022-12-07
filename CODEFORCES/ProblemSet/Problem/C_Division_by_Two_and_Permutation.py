from collections import defaultdict



testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    check=defaultdict(lambda:0)
    
    quit=False
    for i in range(n):
        if a[i]<=n:
            if check[a[i]]==0:
                check[a[i]]=1
                a[i]=-1
            else:
                while True:
                    if a[i]>=1:
                        if check[a[i]]==0:
                            check[a[i]]=1
                            a[i]=-1
                            break
                        else:
                            a[i]//=2
                    else:
                        quit=True
                        break
    if quit==True:
        print("NO")
    else:
        mangmoi=[]
        for num in a:
            if num!=-1:
                mangmoi.append(num)
        if mangmoi==[]:
            print("YES")
        else:
            stop=False
            for num in mangmoi:
                while True:
                    if num>=1:
                        if check[num]==0 and num<=n:
                            check[num]=1
                            break
                        else:
                            num//=2
                    else:
                        stop=True
                        break
                if stop==True:
                    print("NO")
                    break
            else:
                print("YES")
                        
                    
                    
                        
            
        
            
    
                            
            
            
    