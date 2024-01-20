a,b,c,d = list(map(int,input().split()))
data = []

i=1
while i*i<=c:
    if i*i==c:
        data.append(i)
        break
    else:
        if c%i==0:
            data.append(c//i)
            data.append(i)
    i+=1

data.sort()
for num in data:
    if num%a==0 and num%b!=0 and c%num==0 and d%num!=0:
        print(num)
        break
