n=int(input())
chuoi=str(input())

lengthmax=0
soso1=0
if chuoi[0]==chuoi[n-1] and n>2000:
    for i in range(0,n):
        if chuoi[i]=="1":
            soso1+=1
    lengthmax=2*min(soso1-2,n-soso1)
    print(lengthmax)

else:
    chuoiconverted=list()
    mangtongdon=list()
    mangtongdon.append(0)
    sum=0
    for i in range(0,n):
        if chuoi[i]=="1":
            chuoiconverted.append(1)
        else:
            chuoiconverted.append(-1)
        sum=sum+chuoiconverted[i]
        mangtongdon.append(sum)



    for j in range(n,0,-1):
        for i in range(0,n):
            if mangtongdon[i]==mangtongdon[j]:
                length=j-i
                lengthmax=max(length,lengthmax)
    print(lengthmax)