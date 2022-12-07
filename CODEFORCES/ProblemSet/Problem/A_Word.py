from re import I


s=input()
thuong=0
hoa=0
for i in range(0,len(s)):
    if s[i].upper()==s[i]:
        hoa+=1
    else:
        thuong+=1
if hoa<=thuong:
    print(s.lower())
else:
    print(s.upper())