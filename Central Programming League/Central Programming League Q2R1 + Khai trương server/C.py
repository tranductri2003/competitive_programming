from collections import defaultdict
import sys
import os
from io import BytesIO, IOBase


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
n,m,q=list(map(int,input().split()))

num=0


matrix=[]
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(0)


remind=defaultdict(lambda:-1)
important=defaultdict(lambda:-1)


k=[]
for i in range(n):
    k.append([])
    for j in range(m):
        k[i].append(0)

important[0]=k

data=[]



for i in range(q):
    a=list(map(int,input().split()))
    data.append(a)
    if a[0]==4:
        remind[a[1]]=1

    

    

for d in range(q):
    a=data[d]  
    if a[0]==1:
        i=a[1]-1
        j=a[2]-1
        if matrix[i][j]==0:
            matrix[i][j]=1
            num+=1
    if a[0]==2:
        i=a[1]-1
        j=a[2]-1
        if matrix[i][j]==1:
            matrix[i][j]=0
            num-=1
    if a[0]==3:
        i=a[1]-1
        for j in range(m):
            if matrix[i][j]==0:
                matrix[i][j]=1
                num+=1
            else:
                matrix[i][j]=0
                num-=1
    if a[0]==4:
        ngay=a[1]
        matrix=important[ngay].copy()
        num=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==1:
                    num+=1
        
    
    if remind[d+1]==1:
        temp=matrix.copy()
        l=[]
        for i in range(n):
            l.append([])
            for j in range(m):
                l[i].append(temp[i][j])
        important[d+1]=l

    print(num)
