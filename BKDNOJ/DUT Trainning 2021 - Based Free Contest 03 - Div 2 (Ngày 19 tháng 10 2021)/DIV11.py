N=int(input())
a=list(map(int,input().split()))


demphanphoi=[]
for i in range(0,10):
    demphanphoi.append(0)



for num in a:
    demphanphoi[num]+=1

count=0
for i in range(0,N):
    if a[i]==0:
        demphanphoi[0]-=1
        count+=demphanphoi[0]
    elif a[i]==1:
        demphanphoi[1]-=1
        count+=demphanphoi[1]
    elif a[i]==2:
        demphanphoi[2]-=1
        count+=demphanphoi[2]+demphanphoi[9]
    elif a[i]==3:
        demphanphoi[3]-=1
        count+=demphanphoi[3]+demphanphoi[8]
    elif a[i]==4:
        demphanphoi[4]-=1
        count+=demphanphoi[4]+demphanphoi[7]
    elif a[i]==5:
        demphanphoi[5]-=1
        count+=demphanphoi[5]+demphanphoi[6]
    elif a[i]==6:
        demphanphoi[6]-=1
        count+=demphanphoi[6]+demphanphoi[5]
    elif a[i]==7:
        demphanphoi[7]-=1
        count+=demphanphoi[7]+demphanphoi[4]
    elif a[i]==8:
        demphanphoi[8]-=1
        count+=demphanphoi[8]+demphanphoi[3]
    elif a[i]==9:
        demphanphoi[9]-=1
        count+=demphanphoi[9]+demphanphoi[2]

print(count)