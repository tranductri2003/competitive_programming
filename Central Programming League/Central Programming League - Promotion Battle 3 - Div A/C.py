matrix=[]

n=int(input())
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)

r,c=list(map(int,input().split()))
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(n):
        matrix[i][j]=a[j]

stop=False
res=1
r-=1; c-=1
while stop==False:

    hangtren=r-1
    hangduoi=r+1
    cottrai=c-1
    cotphai=c+1

    nhonhathangtren=10**9
    nhonhathangduoi=10**9
    nhonhatcottrai=10**9
    nhonhatcotphai=10**9 
        
    #Hang tren
    if hangtren>=0:
        row=-1
        collumn=-1
        for i in range(n):
            if i==c or i==c-1 or i==c+1:
                pass
            else:
                if matrix[hangtren][i]<nhonhathangtren and matrix[hangtren][i]>matrix[r][c]:
                    rowtren=hangtren
                    collumntren=i
                    nhonhathangtren=matrix[hangtren][i]
    
    #Hang duoi
    if hangduoi<=n-1:
        row=-1
        collumn=-1
        for i in range(n):
            if i==c or i==c-1 or i==c+1:
                pass
            else:
                if matrix[hangduoi][i]<nhonhathangduoi and matrix[hangduoi][i]>matrix[r][c]:
                    rowduoi=hangduoi
                    collumnduoi=i
                    nhonhathangduoi=matrix[hangduoi][i]
    
    #Cot trai
    if cottrai>=0:
        row=-1
        collumn=-1
        for i in range(n):
            if i==r or i==r-1 or i==r+1:
                pass
            else:
                if matrix[i][cottrai]<nhonhatcottrai and matrix[i][cottrai]>matrix[r][c]:
                    rowtrai=i
                    collumntrai=cottrai
                    nhonhatcottrai=matrix[i][cottrai]
                
    #Cot phai
    if cotphai<=n-1:
        row=-1
        collumn=-1
        for i in range(n):
            if i==r or i==r-1 or i==r+1:
                pass
            else:
                if matrix[i][cotphai]<nhonhatcotphai and matrix[i][cotphai]>matrix[r][c]:
                    rowphai=i
                    collumnphai=cotphai
                    nhonhatcotphai=matrix[i][cotphai]


    h=[]
    h.append(nhonhathangduoi)
    h.append(nhonhathangtren)
    h.append(nhonhatcottrai)
    h.append(nhonhatcotphai)
    
    if min(h)==10**9:
        stop=True
    else:
        vitri=h.index(min(h))
        if vitri==0:
            r=rowduoi
            c=collumnduoi
            res+=1
        elif vitri==1:
            r=rowtren
            c=collumntren
            res+=1
        elif vitri==2:
            r=rowtrai
            c=collumntrai
            res+=1
        elif vitri==3:
            r=rowphai
            c=collumnphai
            res+=1
print(res)
    