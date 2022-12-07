# t=int(input())

# for _ in range(t):
#     n=int(input())
    
# def different(a,b):
#     res=0
#     for i in range(0,len(a)):
#         if a[i] != b[i]:
#             res+=1
#     return res
            
# maxlen=len(bin(200))-2

# data=[]
# for i in range(20):
#     data.append([])

# for num in range(0,201):
#     a=str(bin(num))[2:]
#     a="0"*(maxlen-len(a))+a

#     b=str(bin(num+1 ))[2:]
#     b="0"*(maxlen-len(b))+b
#     data[different(a,b)].append((num,num+1))

# for i in range(0,10):
#     print(f"Thu {i} la")
#     print(data[i])
    
#Với khoảng cách thứ i sẽ bắt đầu tại số thứ 2**(i-1)-1
#Khoảng cách giữa các số là 2**i

import math
t=int(input())

for _ in range(t):
    n=int(input())
    last=int(math.log2(n+1)+1)
    res=0
    for num in range(1,last+1):
        start=2**(num-1)-1
        if (n-start)%(2**num)==0:
            end=n-2**num
        else:
            end=start+(n-start)//(2**num)*(2**num)
        p=((end-start)//(2**num)+1)*num

        res+=p
        
    print(res)
            
            
                

        
    
    
    