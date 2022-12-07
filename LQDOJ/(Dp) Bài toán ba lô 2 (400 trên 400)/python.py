n,limit=list(map(int,input().split()))
khoiluongitnhat=[10**11]*100001
khoiluongitnhat[0]=0
sumvalue=0
for i in range(0,n):
    weight,value=list(map(int,input().split())) 
    sumvalue=sumvalue+value

    for j in range(sumvalue,value-1,-1):
        khoiluongitnhat[j]=min(khoiluongitnhat[j],khoiluongitnhat[j-value]+weight)

for value in range(sumvalue,0,-1):
    if khoiluongitnhat[value]<=limit:
        print(value)
        break