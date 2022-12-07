n,x0,y0=list(map(int,input().split()))

x=[]
y=[]
for i in range(n):
    a,b=list(map(int,input().split()))
    x.append(a)
    y.append(b)

res=0

deleteX=0
deleteY=0

X=[]
Y=[]
for i in range(n):
    if x[i]==x0:
        deleteX+=1
    elif y[i]==y0:
        deleteY+=1
    else:
        X.append(x[i])
        Y.append(y[i])

if deleteX!=0:
    res+=1

if deleteY!=0:
    res+=1

angular=[]

for i in range(len(X)):
    angular.append((Y[i]-y0)/(X[i] - x0))

angular.sort()
res+=len(set(angular))
print(res)
        
        
        


    