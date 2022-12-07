n=int(input())

chuoi=list(map(float,input().split()))

chuoi.sort()

chuoi[0]=10.0
sum=0
for num in chuoi:
    sum=sum+num

print(sum)