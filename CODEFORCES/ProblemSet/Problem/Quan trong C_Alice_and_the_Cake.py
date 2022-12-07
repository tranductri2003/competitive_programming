from collections import Counter
import heapq
import math

t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    check=Counter(a)
    tong=sum(a)
    heapQueue=[tong]
    
    while heapQueue:
        x=heapq.heappop(heapQueue)
        if check[x]>0:
            check[x]-=1
        else:
            down=math.floor(x/2)
            up=math.ceil(x/2)
            heapq.heappush(heapQueue,down)
            heapq.heappush(heapQueue,up)
        if len(heapQueue)>n:
            print("NO")
            break
    else:
        print("YES")
    
"""
*AC
from collections import Counter
import heapq
import math

from collections import deque
t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    check=Counter(a)
    tong=sum(a)
    heapQueue=deque([tong])
    
    while heapQueue:
        x=heapQueue.popleft()
        if check[x]>0:
            check[x]-=1
        else:
            down=math.floor(x/2)
            up=math.ceil(x/2)
            heapQueue.append(up)
            heapQueue.append(down)
        if len(heapQueue)>n:
            print("NO")
            break
    else:
        print("YES")
    
"""
    
        
"""
!TLE
from collections import Counter
import heapq
import math

t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    check=Counter(a)
    tong=sum(a)
    heapQueue=[tong]
    
    while heapQueue:
        x=heapQueue.pop(0)
        if check[x]>0:
            check[x]-=1
        else:
            down=math.floor(x/2)
            up=math.ceil(x/2)
            heapQueue.append(up)
            heapQueue.append(down)
        if len(heapQueue)>n:
            print("NO")
            break
    else:
        print("YES")
    
    
    
        



"""

