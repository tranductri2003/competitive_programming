n=int(input())
chuoi=list(map(int,input().split()))

demphanphoi=[0]*1000000

for i in range(0,n):
    demphanphoi[chuoi[i]]=demphanphoi[chuoi[i]]+1

for i in range(0,n):
    print(str(chuoi[i])+str(" ")+str(demphanphoi[chuoi[i]]))