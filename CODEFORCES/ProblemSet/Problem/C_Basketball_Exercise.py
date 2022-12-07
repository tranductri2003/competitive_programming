n=int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))


maxUp=[0]*(n+2)
maxDown=[0]*(n+2)

for i in range(2,n+2):
    maxUp[i] = max(maxDown[i-1]+a[i-2],maxDown[i-2]+a[i-2])
    maxDown[i] = max(maxUp[i-1]+b[i-2],maxUp[i-2]+b[i-2])

res=max(maxUp[n+1],maxDown[n+1]) 
print (res)
    