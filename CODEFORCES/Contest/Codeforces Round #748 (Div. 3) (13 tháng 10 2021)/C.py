testcase=int(input())

#n: toa do lo
#k: so chuot
for test in range(0,testcase):
    n,k=list(map(int,input().split()))
    x=list(map(int,input().split()))    #Chuot thu i co toa do xi

    duongdidainhatdechuotsonghet=n*k-sum(x)
    if n-1>=duongdidainhatdechuotsonghet:
        print(k)
    else:
        x.sort(reverse=True) #tang dan
        res=0
        duongdi=0
        for i in range(0,k):
            x[i]=n-x[i]
        for chuot in x:
            duongdi+=chuot
            if duongdi<n-1:
                res+=1
            elif duongdi==n-1:
                res+=1
                break
        print(res)





    

