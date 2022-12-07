chuoi1=list(map(int,input().split()))
chuoi2=list(map(int,input().split()))
i=0
j=0
chuoimoi=list()
while i<len(chuoi1) or j < len(chuoi2):

    if chuoi1[i]>chuoi2[j]:
        chuoimoi.append(chuoi2[j])
        j=j+1
        #Chuỗi 2 hết
        if j==len(chuoi2):
            for num in range(i,len(chuoi1)):
                chuoimoi.append(chuoi1[num])
            break
    elif chuoi1[i]<chuoi2[j]:
        chuoimoi.append(chuoi1[i])
        i=i+1
        #Chuỗi 1 hết
        if i==len(chuoi1):
            for num in range(j,len(chuoi2)):
                chuoimoi.append(chuoi2[num])
            break
    else:
        chuoimoi.append(chuoi1[i])
        i=i+1
        #Chuỗi 1 hết
        if i==len(chuoi1):
            for num in range(j,len(chuoi2)):
                chuoimoi.append(chuoi2[num])
            break
print(chuoimoi)


