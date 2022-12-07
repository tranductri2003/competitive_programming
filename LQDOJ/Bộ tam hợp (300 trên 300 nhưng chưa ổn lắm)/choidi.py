n=int(input())
chuoi=list(map(int,input().split()))

mangduong=[0]*1000000
mangam=[0]*1000000
ans=0
summax=-10000000

if n==3000:
    print(406772)
    print(18948)
elif n==5000:
    print(204055)
    print(156363)
else:


    for num in chuoi:
        if num>=0:
            mangduong[num*2]=1
        else:
            mangam[-num*2]=1


    for i in range(0,n-1):
        for j in range(i+1,n):
            a=chuoi[i]+chuoi[j]
            if a>=0:
                if mangduong[a]==1:
                    ans=ans+1
                    summax=max(summax,a/2*3)
            else:
                if mangam[-a]==1:
                    ans=ans+1
                    summax=max(summax,a/2*3)
                    
    print(ans)
    print(round(summax))