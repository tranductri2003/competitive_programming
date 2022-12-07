

a,b,p=list(map(int,input().split()))

binh=[a,b]


for i in range(0,2):
    if int(binh[i])>int(p):
        binh[i],p=p,binh[i]

print(max(binh))