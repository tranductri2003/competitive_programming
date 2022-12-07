a,b=list(map(int,input().split()))
chuoia=list(map(int,input().split()))
chuoib=list(map(int,input().split()))
chuoic=list()



i=0
j=0
stack=0




while i<a and j<b:
    if chuoia[i]<chuoib[j]:
        stack=stack+1
        i=i+1
    else:
        chuoic.append(stack)
        j=j+1

#Chuỗi a đã hết nhưng chuỗi b vẫn chưa xử lí xong
if i==a and j<b:
    for i in range(0,b-j):
        chuoic.append(stack)


for num in chuoic:
    print(num, end=" ")