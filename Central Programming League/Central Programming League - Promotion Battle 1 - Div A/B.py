
   
n,k=list(map(int,input().split()))
s=input()
vitri=0
res=[]
while k>0:
    temp=max(s[vitri:vitri+k+1])
    for i in range(vitri,vitri+k+1):
        if s[i]==str(temp):
            res.append(s[i])
            vitri=i+1
            k+=i-vitri
            break
res+=s[vitri:]
a=''.join(res)
print(int(a))
