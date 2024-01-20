data=[1,1]
for i in range(82):
    data.append(data[-1]+data[-2])
cnt={}
data=data[2:]
l=len(data)
for i in range(l):
    for j in range(l):
        x=data[i]
        print(x)
        for k in range(j,l):
            while x%data[k]==0: x//=data[k]
       # print(x)
        if x-1: cnt.get(data[i]+1)
print(cnt)
            
    
