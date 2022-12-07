import math

def kiemtra(n):
    if n==1:
        return 1
    if n==0:
        return 0
    count=0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            count+=2
    return count



while True:

    try:
        n,k=list(map(int,input().split()))
    except ValueError:
        break

    num=math.comb(n,k)
    print(kiemtra(num))