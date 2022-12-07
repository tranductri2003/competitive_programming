n,limit=list(map(int,input().split()))  

mangcheck=[0]*(limit+1)
mangcheck[0]=1
mangtinhtongbu=[0]*(limit+1) #Có thể hiểu là tại mỗi vị trí, thiếu giá trị trong vị trí đó để đạt được mục đích
money=[0]*(limit+1)


for sohang in range(0,n):
    weight,value=list(map(int,input().split()))
    for i in range(limit,0,-1):
        if mangcheck[i]==0 and mangcheck[i-weight]==1:
            mangcheck[i]=1
            if money[i-weight]+value>money[i]:
                money[i]=money[i-weight]+value
            mangtinhtongbu[i]=i-weight
        if i-weight==0:
            break

print(mangtinhtongbu)

i=max(money)
while i>0:
    print(i-mangtinhtongbu[i], end=" ")
    i=mangtinhtongbu[i]