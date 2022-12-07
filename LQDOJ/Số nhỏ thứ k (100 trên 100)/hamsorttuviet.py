n,k=list(map(int,input().split()))
chuoi=list(map(int,input().split()))

chuoisorted=list()

while len(chuoi)>0:
    min=chuoi[0]
    for num in chuoi:
        if num<=min:
            min=num
    chuoi.remove(min)
    chuoisorted.append(min)

print(chuoisorted[k-1])
