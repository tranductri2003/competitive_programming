from collections import defaultdict


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    check=defaultdict(lambda:1)
    
    if a==sorted(a):
        print(0)
    else:
 
        res=0
        soloaiso=1
        check[a[0]]=-1
        for i in range(1,n):
            if a[i]<a[i-1]:
                if check[a[i]]!=-1:
                    res=soloaiso
                    soloaiso+=1
                    check[a[i]]=-1
                else:
                    res=soloaiso
                
            if a[i]==a[i-1]:
                pass
            
            if a[i]>a[i-1]:
                if check[a[i]]==-1:
                    res=soloaiso
                else:
                    soloaiso+=1
                    check[a[i]]=-1
        print(res)
                

    