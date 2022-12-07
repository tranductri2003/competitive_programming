s=input()

i=0

stack=[0]*(len(s)+1)
ans=0
for i in range(1,len(s)+1):
    if s[i-1]=='1':
        stack[i]=stack[i-1]+1
    else:
        stack[i]=stack[i-1]
for i in range(1,len(s)+1):
    if s[i-1]=='0':
        ans+=stack[i]
        
if ans %3==0:
    print('Bob')
else:
    print("Alice")
                
        
            
            