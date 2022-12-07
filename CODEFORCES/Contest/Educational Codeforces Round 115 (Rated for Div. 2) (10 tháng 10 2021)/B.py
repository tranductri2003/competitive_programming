testcase=int(input())

for i in range(0,testcase):
    n=int(input())  
    day=[0]*5
    day[0]=[]
    day[1]=[]
    day[2]=[]
    day[3]=[]
    day[4]=[]
    for j in range(1,n+1): 
        day0,day1,day2,day3,day4=list(map(int,input().split()))  
        if day0==1:
            day[0].append(j)
        if day1==1:
            day[1].append(j)
        if day2==1:
            day[2].append(j)
        if day3==1:
            day[3].append(j)
        if day4==1:
            day[4].append(j)
    
    acceptedlist=[]
   
    for j in range(0,5):
        if len(day[j])>=n//2:
            acceptedlist.append(j)
    if len(acceptedlist)<2:
        print("NO")
    else:
        quit=False
        for j in acceptedlist:
            for k in acceptedlist:
                if j!=k and quit==False:
                    if len(set(day[j]+day[k]))==n:
                        print("YES")
                        quit=True
        if quit==False:
            print("NO")