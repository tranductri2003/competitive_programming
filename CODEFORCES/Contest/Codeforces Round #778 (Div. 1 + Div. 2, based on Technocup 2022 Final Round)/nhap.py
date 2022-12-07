

from collections import defaultdict
import math
from collections import deque


t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print("YES")
    else:
        check=defaultdict(lambda:-10)
        for num in a:
            check[num] =0
        for num in a:
            check[num]+=1
                    
        
        hangdoi=deque([sum(a)])
        
        count=0
        while hangdoi!=[] and count<1500:
            down=hangdoi[0]//2
            up=math.ceil(hangdoi[0]/2)
            if check[down]>0:
                check[down]-=1
            else:
                hangdoi.append(down)
            if check[up]>0:
                check[up]-=1
            else:
                hangdoi.append(up)
            
            hangdoi.popleft()
            if hangdoi==[]:
                break
            if hangdoi[-1]==0:
                break
            count+=1

        if hangdoi==[]:
            print("YES")
        else:
            print("NO")
            
            
    
    
    
    