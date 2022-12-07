a,b=list(map(int,input().split()))
for i in range(0,1000):
    if a*pow(3,i)-b*pow(2,i)>0:
        print(i)
        break