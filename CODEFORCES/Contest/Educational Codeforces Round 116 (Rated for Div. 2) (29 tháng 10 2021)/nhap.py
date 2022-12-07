a=[]

for i in range(0,14):
    for j in range(0,14-i):
        for k in range(0,14-j):
            tien=i*1+j*10+k*100
            a.append(tien)

a=list(set(a))
a.sort()
print(*a)