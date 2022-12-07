n,x=list(map(int, input().split()))
chuoi=list(map(int, input().split()))

i=0
j=n-1

while sum!=x:
    sum=chuoi[i]+chuoi[j]
    if sum<x:
        i=i+1
    else:
        j=j-1
    if sum==x:
        print(str(i+1)+" "+str(j+2))
        break
    if i==j:
        print("No solution")
        break



