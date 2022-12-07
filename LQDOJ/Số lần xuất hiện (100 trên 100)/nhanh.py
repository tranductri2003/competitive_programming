n=int(input())
chuoi=list(map(int,input().split()))

demphanphoi=[0]*1000000

for num in chuoi:
    demphanphoi[num]=demphanphoi[num]+1

for num in chuoi:
    print(str(num)+str(" ")+str(demphanphoi[num]))