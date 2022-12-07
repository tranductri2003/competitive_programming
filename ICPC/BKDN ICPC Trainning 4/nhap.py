s="{a,v,c,s,a,a,a,a,b}"
s=s[1:len(s)-1].split(",")
res=[]
for i in s:
    if len(i)==2:
        res.append(i[1:])
    if len(i)==1:
        res.append(i)
        
print(len(set(res)))