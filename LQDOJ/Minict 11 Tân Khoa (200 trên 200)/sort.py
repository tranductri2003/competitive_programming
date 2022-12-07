n,k=list(map(int,input().split()))
diem=list(map(int,input().split()))


diem.sort(reverse=True)
diemchuan=diem[k-1]
ans=0
for num in diem:
    
    if num<diemchuan:
        break
    if num>0:
        ans=ans+1

print(ans)