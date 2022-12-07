
stop=False
while stop==False:
    a=input()
    if a!="":
        l,r,k=a.split(" ")
        l=int(l)
        r=int(r)
        k=int(k)
        if l%k==0:
            left=l
        else:
            left=(l//k+1)*k

        if r%k==0:
            right=r
        else:
            right=(r//k)*k

        stop=False
        currentmin="999999999"
        for i in range(left,right+1,k):
            i=str(i) 
            if i=="0" or i=="1" or (i[0]=="1" and set(i[1:])=={'0'}):
                res=i
                print(res)
                stop=True
                break
            currentmin=min(currentmin,i)

        if stop==False:
            if currentmin=="999999999":
                print("-1")
            else:
                print(currentmin)
    else:
        stop=True
