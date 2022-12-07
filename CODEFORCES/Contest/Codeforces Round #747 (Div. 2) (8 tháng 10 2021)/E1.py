def luythua(n,k): #n^k
    ans=1
    for i in range(0,k):
        ans=ans*n%(10**9+7)
    return ans


n=int(input())
tich=1
for i in range(1,n):
    somumoi=pow(2,i,10**9+6)  #Tính chất modulo
    tich=tich*pow(4,somumoi,10**9+7)
tich=tich*6%(10**9+7)
print(tich)




