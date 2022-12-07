n=int(input())
chuoi=list(map(int,input().split()))


check=[1]*n


for i in range(0,n):
    for j in range(0,i):
        if chuoi[i]>chuoi[j]:
            check[i]=max(check[j]+1,check[i])

print(max(check))