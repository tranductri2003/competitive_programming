chuoi=input()
i=0
stack=1
n=len(chuoi)
while i<n:
    if i==n-1:
        if chuoi[i]==chuoi[i-1]:
            print(str(stack)+str(chuoi[i]))
            break
        else:
            print(chuoi[i])
            break
    if chuoi[i+1]==chuoi[i]:
        stack=stack+1
        i=i+1
    else:
        if stack==1:
            print(chuoi[i],end="")
            i=i+1
        else:
            print(str(stack)+str(chuoi[i]),end="")
            i=i+1
            stack=1

