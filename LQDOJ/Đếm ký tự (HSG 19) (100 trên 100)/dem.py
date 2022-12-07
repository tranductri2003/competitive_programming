n=str(input())

blacklist=list()
whilelist=list()
ans=0
for i in range(0,len(n)):
    if n[i] in whilelist:
        blacklist.append(n[i])

    else:
        whilelist.append(n[i])
        

for chu in whilelist:
    if chu not in blacklist:
        ans=ans+1

print(ans)
