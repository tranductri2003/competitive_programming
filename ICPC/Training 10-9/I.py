def solve(n):
    res=0
    while n!=1:
        if n%2==0:
            n//=2
        else:
            n=n*3+1
        res+=1
    return res

data=[]
for i in range(1,10001):
    data.append(solve(i))

for i in range(0,len(data)-8):
    if data[i]==data[i+1]==data[i+2]==data[i+3]==data[i+4]==data[i+5]==data[i+6]==data[i+7]==data[i+8]:
        print(i,data[i])
        print(i+1,data[i+1])
        print(i+2,data[i+2])
        print(i+3,data[i+3])
        print(i+4,data[i+4])
        print(i+5,data[i+5])
        print(i+6,data[i+6])
        print(i+7,data[i+7])
        print(i+8,data[i+8])

        break
