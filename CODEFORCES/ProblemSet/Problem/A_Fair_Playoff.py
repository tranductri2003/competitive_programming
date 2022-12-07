from calendar import c


testcase=int(input())
for test in range(testcase):
    day=list(map(int,input().split()))
    nhat=0
    vitrinhat=0
    nhi=0
    vitrinhi=0
    for i in range(4):
        if day[i]>nhat:
            nhat=day[i]
            vitrinhat=i
    for i in range(4):
        if day[i]>nhi and day[i]!=nhat:
            nhi=day[i]
            vitrinhi=i
    if (vitrinhi==0 and vitrinhat==1) or (vitrinhi==1 and vitrinhat==0) or (vitrinhi==2 and vitrinhat==3) or (vitrinhi==3 and vitrinhat==2):
        print("NO")
    else:
        print("YES")
    
    
        
