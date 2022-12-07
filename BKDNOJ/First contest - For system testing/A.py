l,n=list(map(int,input().split()))
x=list(map(int,input().split()))

temp=[]
temp2=[]
for num in x:
    temp.append(min(num,l-num))
    temp2.append(max(num,l-num))
print(max(temp),max(temp2))