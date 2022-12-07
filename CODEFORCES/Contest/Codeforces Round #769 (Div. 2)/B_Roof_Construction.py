testcase=int(input())

# from collections import defaultdict
# check=defaultdict(lambda:0)
# for i in range(0,30):
#     check[2**i] =1

# for test in range(testcase):
#     n=int(input())
#     a=[]
#     for i in range(0,n):
#         a.append(i)
#     start=0
#     res=[]
    
#     i=n-1
#     stop=False
#     qua=True
#     while stop==False:
#         if check[i+1]==1 and qua==True and i!=n-1:
#             res.append(start)
#             start+=1
#             qua=False
            

#         else:
#             res.append(i)
#             i-=1
#             qua=True
        
#         if start>i:
#             stop=True
#             break
#     print(*res)

import math
for test in range(testcase):
    n=int(input())
    res=[]
    for i in range(n-1,0,-1):
        res.append(i)
    limit=2**int(math.log2(n-1))
    vitri=res.index(limit)
    res.insert(vitri+1,0)
    print(*res)