n,t=list(map(int,input().split()))
chuoi=list(map(int,input().split()))

#Thỏa thì cộng a[i]
#Không thỏa thì trừ a[j]


tong=0
j=0
lengthmax=1

for i in range (0,n):
    tong+=chuoi[i]
    
    if tong>t:
        tong-=chuoi[j]
        j+=1

    length=i-j+1
    lengthmax=max(length,lengthmax)

print(lengthmax)