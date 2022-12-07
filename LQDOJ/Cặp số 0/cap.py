n=int(input())
chuoi=list(map(int,input().split()))

mangtongdon=list()
#Mảng tổng phải có số 0 đầu tiên đề phòng mangtong[i-1]
#Công thức tính tổng: tổng từ i tới j là bằng a[j] -a[i-1]



sum=0
so0=0





for num in chuoi:
    sum=sum+int(num)
    mangtongdon.append(sum)
    if sum==0:
        so0=so0+1

mangtongdon.sort()
print(mangtongdon)
listcacsophanbiet=list(set(mangtongdon))
listcacsophanbiet.sort()
print(listcacsophanbiet)
breakpoint=0
stack=0
ans=0
part=0
for num in listcacsophanbiet:
    print("Num: "+str(num))
    for i in range(breakpoint,n):
        print("I: "+str(i))
        print("mangtongdon[i]: "+str(mangtongdon[i]))
        while mangtongdon[i]==num:
            stack=stack+1
            i=i+1
        ans=ans+stack*(stack-1)/2
        stack=0
        breakpoint=i
        break

print(ans+so0)

