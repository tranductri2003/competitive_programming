from queue import PriorityQueue
from collections import deque,OrderedDict,defaultdict,Counter
from heapq import heappop, heappush, heapify
import sys
import time
import os
from io import BytesIO, IOBase
import math
from random import randint
from itertools import compress


MOD=10**9+7
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 

 
 
from itertools import compress
def rwh_primes1v2(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

# O(nlogn)
a=rwh_primes1v2(10**5)
from collections import defaultdict
check=defaultdict(lambda:False)
for num in a:
    check[num] = True


# print(len(check))

# from joblib import PrintTime


# N = 10 ** 5 + 7

# prime = {}

# for i in range(N):
#     prime[i] = []
    
# prime[1] = [1]
    
# i = 2

# while (i < N):
#     j = i
#     if (prime[i] != []): 
#         i = i + 1
#         continue
#     while (j < N):        
#         prime[j].append(i)
#         j = j + i
        
#     i = i + 1

n,M=list(map(int,input().split()))
a=list(map(int,input().split()))

uoc=[]

# n * sqrt(n) = 10 ^ 7

for num in a:
    if check[num]: 
        uoc.append(num) 
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                uoc.append(i)
                uoc.append(num//i)
            
uoc=list(set(uoc))
res=[]


print(uoc)



# # for num in range(1,M+1):
# #     for i in uoc:
# #         if num%i==0:
# #             break
# #     else:
# #         res.append(num)
# # print(len(res))
# # for num in res:
# #     print(num)

# check=defaultdict(lambda:1)
# for num in uoc:
#     check[num]=-1

# for i in range(1,M+1):
#     temp=[]
#     for j in range(1,int(i**0.5)+1):
#         if i%j==0:
#             temp.append(j)
#             temp.append(i//j)
#     for num in temp:
#         if check[num]==-1:
#             break

#     else:
#         res.append(i)
# print(len(res))
# for num in res:
#     print(num)


        
        
# res=[]
# for i in range(1,M+1):
#     if check[i]==1:
#         res.append(i)
# print(len(res))
# for num in res:
#     print(num)


# from collections import defaultdict


# check=defaultdict(lambda:1)
# for num in uoc:
#     temp=num
#     while temp<=M:
#         check[temp]=-1
#         temp+=num

# res=[]
# for i in range(1,M):
#     if check[i]==1:
#         res.append(i)
# print(len(res))
# for num in res:
#     print(num)






        
    

