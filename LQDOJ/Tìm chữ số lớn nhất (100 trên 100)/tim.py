n=int(input())

chusomax=0
for i in range(0,len(str(n))):
    n=str(n)
    chuso=n[i]
    chuso=int(chuso)
    if chuso>chusomax:
        chusomax=chuso

print(chusomax)