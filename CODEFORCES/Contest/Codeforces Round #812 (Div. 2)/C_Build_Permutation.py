


from itertools import permutations

import math
# n=int(input())
# res=list(permutations([i for i in range(n)]))
# def check(a):
#     for i in range(len(a)):
#         if math.sqrt(i+a[i])==int(math.sqrt(i+a[i])):
#             pass
#         else:
#             return False
#     return True

# for num in res:
#     if check(num): 
#         print(num)

from collections import defaultdict

t=int(input())
for _ in range(t):
    n=int(input())
    res=[-1]*n
    somax=n-1

    vitrinhamtoi=math.ceil(math.sqrt(somax))**2
    sohientai=somax
    vitri=vitrinhamtoi-somax
    temp=0
    for i in range(vitri,n):
        res[i]=sohientai
        temp+=1
        sohientai-=1
    while temp<n:
        vitrinhamtoi=math.ceil(math.sqrt(sohientai))**2  
        if vitrinhamtoi==0 and res[0]!=-1:
            vitrinhamtoi=1
        for i in range(vitrinhamtoi-sohientai,n):
            if res[vitrinhamtoi-sohientai]==-1:
                res[vitrinhamtoi-sohientai]=sohientai
                temp+=1
                sohientai-=1
            else:
                break

    
    print(*res)



