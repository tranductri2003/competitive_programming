
import math
def kiemtra(n):
    listuocso = list()
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            listuocso.append(i)
            listuocso.append(n/i)
        if len(listuocso)>6:
            return False
    if len(set(listuocso))==4:
        return True






n=int(input())
ans=0
listuocso=list()
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        listuocso.append(round(i))
        listuocso.append(round(n/i))

listuocso=list(set(listuocso))



for num in listuocso:
    if kiemtra(num)==True:
        ans=ans+1
print(ans)

