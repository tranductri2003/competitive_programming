n=int(input())

phandau=n//10
phansau=n-phandau*10

if (phandau-9*phansau)%13==0:
    print("YES")
    
else:
    print("NO")