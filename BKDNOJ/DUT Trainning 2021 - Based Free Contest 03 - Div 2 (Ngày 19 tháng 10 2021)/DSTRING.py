s=input()

n=len(s)

a=list()
current=0
for i in range(0,n):
    if s[i]!=current:
        a.append(s[i])
        current=s[i]
for i in a:
    print(i,end="")
