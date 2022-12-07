listso=[1,11,111,1111,11111,111111,1111111]
listsodacbiet=list()
a=0
for i in listso:
    a=i
    while a<10**len(str(i)):
        listsodacbiet.append(a)
        a=a+i



n=int(input())
chuoi=list(map(int,input().split()))

demphanphoi=[0]*10**7


for num in chuoi:
    demphanphoi[num]+=1


ans=0
for num in chuoi:
    for q in listsodacbiet:
        if num+num!=q:
            ans=ans+demphanphoi[q-num]

print(round(ans/2))