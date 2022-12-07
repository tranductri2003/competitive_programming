soluong,sobichia=list(map(int,input().split()))
chuoi=list(map(int,input().split()))


chuoi.sort()

stack=0
ans=0
temp=chuoi[0]//sobichia
for i in range(0,soluong):
    
    if chuoi[i]//sobichia==temp:
        stack=stack+1
        if i==soluong-1:
            ans=ans+(stack*(stack-1))//2

    else:
        ans=ans+(stack*(stack-1))//2
        temp=chuoi[i]//sobichia
        stack=1

print(ans)

