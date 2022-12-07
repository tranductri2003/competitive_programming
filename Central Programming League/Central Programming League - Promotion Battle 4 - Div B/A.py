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
 
 
 
from itertools import combinations
n=int(input())

a=[]
for i in range(n):
    tmp=int(input())
    a.append(tmp)

k=int(input())


for i in range(0,n+2):
    b=list(combinations(a,i))
    for num in b:
        num=list(num)
        t=sum(num)
        if t==k:
            print("Yes")
            quit()
else:
    print("No")
        
# int n;
#     ll k;
#     cin>>n;
#     for (int i =0; i<n; i++){
#         cin>>arr[i];
#     }
#     cin>>k;
#     ll res=0;
#     bool ok=0;
#     for (int x=0; x< 1<<n ; x++){
#         res=0;
#         for (int p=0; (1<<p)<=x; p++){
#             if ((1<<p) & x){
#                 res+=arr[p];
#             }
#         }
#         // cout<<res<<endl;
#         if (res==k){
#             ok=1;
#         }
#     }