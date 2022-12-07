testcase=int(input())

for test in range(0,testcase):
    n=int(input())
    a=list(map(int,input().split()))
    z=a
    queries=int(input())
    breakloop=10**12
    constant=[]
    for que in range(0,queries):
        a=z    
        position,time=list(map(int,input().split()))
        if time>=breakloop:
            print(constant[position-1])
        else:
            if time==0:
                print(a[position-1])
            else:
                stop=False
                loop=0
                breakloop=0
                constant=[]
                while stop==False and loop<time:
                    check=True
                    key=list(range(0,2001))
                    value=[0]*2001
                    demphanphoi=dict(zip(key,value))
                    for num in a:
                        demphanphoi[num]+=1
                    for i in range(0,n):
                        a[i]=demphanphoi[a[i]]

                    loop+=1
                    for num in a:
                        if demphanphoi[num]!=num:
                            pass
                    else:
                        breakloop=loop
                        stop=True
                        constant=a

                    

                print(a[position-1])

            

