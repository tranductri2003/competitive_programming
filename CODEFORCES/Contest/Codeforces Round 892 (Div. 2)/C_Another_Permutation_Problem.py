from itertools import permutations
t=int(input())
for _ in range(t):
    n=int(input())
    data=[i for i in range(1,n+1)]
    res=[]
    for i in range(n):
        temp=data[:i]
        for j in range(n,i,-1):
            temp.append(j)
        tempRes=0
        maxx =0
        for j in range(n):
            tempRes+=(j+1)*temp[j]
            maxx = max(maxx,(j+1)*temp[j])
        res.append(tempRes-maxx)
        # print(temp)
        # print(tempRes, maxx)
    print(max(res))



# n=int(input())
# data = list(permutations([i for i in range(1,n+1)]))
# print(data)
# for mang in data:
#     res =0
#     mang = list(mang)
#     for i in range(0,n):
#         res+=(i+1)*mang[i]
#     temp = 0
#     for i in range(0,n):
#         temp = max(temp, (i+1)*mang[i])
#     if res-temp==303:
#         print(mang)
        
    