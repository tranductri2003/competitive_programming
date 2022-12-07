
import sys
import time
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
 

 
def DFS(row,col):
    global IsHill
    Visit[row][col]=True
    for i in range(0,8):
        r=row+drow[i]
        c=col+dcol[i]
        if (r>=0 and r<N and c>=0 and c<M):
            if IsHill==True and Map[r][c]>Map[row][col]:
                IsHill=False
            if(Map[r][c] == Map[row][col] and Visit[r][c]==False):
                DFS(r, c);

res=0

MAX=705
Map=[]
Visit=[]
for i in range(MAX):
    Map.append([])
    Visit.append([])
    for j in range(MAX):
        Map[i].append(0)
        Visit[i].append(0)


drow=[-1,-1,-1, 0,0, 1,1,1]
dcol=[-1, 0, 1,-1,1,-1,0,1]

N,M=list(map(int,input().split()))
for i in range(N):
    a=list(map(int,input().split()))
    for j in range(M):
        Map[i][j]=a[j]
        Visit[i][j]=False
IsHill = True
for i in range(N):
    for j in range(M):
        if (Visit[i][j]==False):
            IsHill=True
            DFS(i,j)
            if IsHill==True:
                res+=1
print(res)