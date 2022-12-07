import numpy as np

ans=0

demphanphoi = np.empty(10**9+1, dtype=int)
mangxuathien=list()
soluong,sobichia=list(map(int,input().split()))
chuoi=list(map(int,input().split()))

for so in chuoi:
    demphanphoi[so//sobichia]+=1
    if so//sobichia not in mangxuathien:
        mangxuathien.append(so//sobichia)



for vitri in mangxuathien:
    ans=ans+demphanphoi[vitri]*(demphanphoi[vitri]-1)//2

print(ans)

