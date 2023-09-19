from collections import defaultdict 
import math
N, M = list(map(int,input().split()))
a = list(map(int,input().split()))
check = defaultdict(lambda: True)
for num in a:
    check[num] = False
res=0
for i in range(1,N+1):
    if check[i] == True:
        power_of_two = math.floor(math.log(i, 2))   
        
        res+=2*(i-2**(power_of_two))
print(res)