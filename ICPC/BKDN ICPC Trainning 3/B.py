
from collections import deque,OrderedDict,defaultdict,Counter
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
from collections import Counter

while True:
    n=int(input())
    if n==0:
        break
    else:
        res=0
        array=defaultdict(list)
        count=defaultdict(int)
        tong=0
        for i in range(n):
            array[i] =list(map(int,input().split()))
            count[i]=len(array[i])
            tong+=count[i]
        # print((array))
        # print(count)
        # print(tong)
        # print()
        
        current=-1
        while tong>0:
            current=(current+1)%n
            if count[current]==0:
                pass
            else:
                temp=Counter(array[current])
                delete=[]
                for num in temp:
                    if temp[num]==2:
                        delete.append(num)
                        
                temp=[]
                for i in range(0,len(array[current])):
                    if array[current][i] not in delete:
                        temp.append(array[current][i])
                    else:
                        count[current]-=1
                        tong-=1
                array[current]=temp.copy()
                
                if count[current]==0:
                    pass
                else:
                    # print(count)
                    temp=min(array[current])
                    array[current].remove(temp)
                    count[current]-=1
                    
                    tamthoi=current
                    
                    for j in range(1,n+1):
                        if count[(tamthoi+j)%n]!=0:
                            array[(tamthoi+j)%n].append(temp)
                            count[(tamthoi+j)%n]+=1
                            res+=1
                            break
                    else:
                        break
            # print(array)
            # print(count)
            # print("current",res)
        print(res)
                


            
                



            
        
        
        
        