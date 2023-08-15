N=int(input())
a = list(map(int,input().split()))
K = int(input())
cat = []
for i in range(K):
    cat.append(int(input()))

a.sort()
prefixSum=[0]
temp=0
for i in range(N):
    temp+=a[i]
    prefixSum.append(temp)
a.insert(0,-1)

def first_element_greater_than(arr, target):
    index = bisect.bisect_right(arr, target)
    if index < len(arr):
        return index
    else:
        return None

import bisect
for num in cat:
    pos = first_element_greater_than(a, num)
    if pos ==None:
        print(0)
    else:
        print(prefixSum[N]-prefixSum[pos-1]-(N+1-pos)*num)
    
    
