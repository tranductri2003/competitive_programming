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





from collections import defaultdict
from collections import Counter,deque

while True:
    n=int(input())
    if n==0:
        break
    else:
        # Q = Queue(maxsize = n+100)
        array=defaultdict(list)
        Queue=deque()
        tong=0
        for i in range(n):
            a,b=list(map(int,input().split()))
            if a==b:
                continue
            if a>b:
                a,b=b,a
            array[i].append(a)
            array[i].append(b)
            Queue.append(i)
            # Q.put(i)


        res=0 
        while Queue:  
            now=Queue.popleft()   
            # now=Q.get()
            next=Queue[0]
            # next=Q[0]
            array[next].append(array[now][0])
            array[now].pop(0)

            res+=1

            if len(array[now])>0:
                Queue.append(now)
                # Q.put(now)
            
            array[next].sort()
            if len(array[next])==2:
                if array[next][0]==array[next][1]:
                    array[next]=[]
                    Queue.popleft()
                    # Q.get()
            else:
                if array[next][0]==array[next][1]:
                    temp=array[next][2]
                    array[next]=[]
                    array[next].append(temp)
                elif array[next][1]==array[next][2]:
                    temp=array[next][0]
                    array[next]=[]
                    array[next].append(temp)
        print(res)

