s=input()
num=0
for i in range(len(s)):
    if s[i]=="4" or s[i]=="7":
        num+=1
if num==4 or num==7:
    print("YES")
else:
    print("NO")