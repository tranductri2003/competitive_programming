t=int(input())

for _ in range(t):
    s=input()
    data=[0]*26
    for i in range(0,len(s)):
        temp=ord(s[i])-97
        data[temp]+=1
    
    l=0
    for i in range(0,len(s)):
        temp=ord(s[i])-97
        if data[temp]>1:
            l+=1
            data[temp]-=1
        else:
            break
    print(s[l:])