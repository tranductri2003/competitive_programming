n=int(input())
chuoi=list(map(int,input().split()))

chuoi.sort(reverse=True)
so0=0
stack=0
sum=0
for num in chuoi:
    sum=sum+num
    if num==0:
        so0+=1
        


if so0==n:
    print(0)
elif so0==0:
    print(-1)
else:
    if sum%3==1:
        if 1 in chuoi:
            chuoi.remove(1)
        elif 4 in chuoi:
            chuoi.remove(4)
        elif 7 in chuoi:
            chuoi.remove(7)
        else:
            while stack<2:
                if 2 in chuoi:
                    chuoi.remove(2)
                elif 5 in chuoi:
                    chuoi.remove(5)
                elif 8 in chuoi:
                    chuoi.remove(8)
                stack=stack+1

    if sum%3==2:
        
        if 2 in chuoi:
            chuoi.remove(2)
        elif 5 in chuoi:
            chuoi.remove(5)
        elif 8 in chuoi:
            chuoi.remove(8)
        else:
            while stack<2:
                
                if 1 in chuoi:
                    chuoi.remove(1)
                elif 4 in chuoi:
                    chuoi.remove(4)
                elif 7 in chuoi:
                    chuoi.remove(7)
                stack=stack+1
                

    if list(set(chuoi))==[0]:
        print(0)
    else:
        for num in chuoi:
            print(num,end="")
            