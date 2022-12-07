a,b=list(map(int,input().split()))
chuoia=list(map(int,input().split()))
chuoib=list(map(int,input().split()))
chuoic=list()

i=0
j=0

while i<a and j<b:
    chuoic.append(min(chuoia[i],chuoib[j]))
    if chuoia[i]<chuoib[j]:
        i=i+1
    else:
        j=j+1

if i==a:
    for i in range(j,b):
        chuoic.append(chuoib[i])
if j==b:
    for i in range(i,a):
        chuoic.append(chuoia[i])

for num in chuoic:
    print(num, end=" ")