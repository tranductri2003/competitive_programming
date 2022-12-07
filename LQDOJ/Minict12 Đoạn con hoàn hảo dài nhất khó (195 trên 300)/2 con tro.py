
i=0

length=0
lengthmax=0
n,limit=list(map(int,input().split()))
chuoi=list(map(int,input().split()))

listkiemtra=list(set(chuoi))

chuoitamthoi=list()
j=limit-1

if len(listkiemtra)<=limit:
    print("1"+" "+ str(n))

else:
    while i<=n-limit and j<=n:
        chuoitamthoi=chuoi[i:j+1]
        length=j-i
        if length>lengthmax:
            lengthmax=length
            l=i
            r=j
        if len(set(chuoitamthoi))<=limit:
            j=j+1
        else:
            i=i+1

    print(str(int(l+1))+" "+str(r))


