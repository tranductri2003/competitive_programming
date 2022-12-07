a={}


soluong,sobichia=list(map(int,input().split()))
chuoi=list(map(int,input().split()))

for so in chuoi:
    if so//sobichia  in a:   #Đây là key
        a[so//sobichia]+=1
    else:
        a[so//sobichia]=1


ans=0
ketqua=list(a.values())
for so in ketqua:
    ans=ans+so*(so-1)//2

print(ans)