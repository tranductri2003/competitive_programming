
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
 

 
    
def lineLineIntersection(Ax,Ay,Bx,By,Cx,Cy,Dx,Dy):
    # Line AB represented as a1x + b1y = c1
    a1 = By- Ay
    b1 = Ax - Bx
    c1 = a1*(Ax) + b1*(Ay)
 
    # Line CD represented as a2x + b2y = c2
    a2 = Dy - Cy
    b2 = Cx - Dx
    c2 = a2*(Cx) + b2*(Cy)
 
    determinant = a1*b2 - a2*b1
 
    if (determinant == 0):
        # The lines are parallel. This is simplified
        # by returning a pair of FLT_MAX
        return -1.2345,-1.2345
    else:
        x = (b2*c1 - b1*c2)/determinant
        y = (a1*c2 - a2*c1)/determinant
        return x,y  
def checkTrue(x, y,n):
    if x!=-1.2345 and y!=-1.2345 and x==int(x) and y==int(y) and 1<=x<=n and 1<=y<=n:
        return True
    return False



n,q=list(map(int,input().split()))
if n==2:
    for i in range(q):
        i,j,x,y=list(map(int,input().split()))
        if (i+j)%2!=(x+y)%2:
            print(-1)
        else:
            if i==x and j==y:
                print(0)
            elif i-j==x-y or i+j==x+y:
                print(1)
                print(x,y)
else:
    for i in range(q):
        i,j,x,y=list(map(int,input().split()))
        if (i+j)%2!=(x+y)%2:
            print(-1)
        else:
            if i==x and j==y:
                print(0)
            elif i-j==x-y or i+j==x+y:
                print(1)
                print(x,y)
            else:
                print(2)
  
                
                #AC, BD
                # AC, BF
                #AE, BD
                #AE, BF

                
                intersection1x,intersection1y = lineLineIntersection(i,j, i-1,j-1, x,y, x-1,y-1)
                intersection2x,intersection2y = lineLineIntersection(i,j, i-1,j-1, x,y, x+1,y-1)
                intersection3x,intersection3y = lineLineIntersection(i,j,i+1,j-1,x,y,x-1,y-1)
                intersection4x,intersection4y = lineLineIntersection(i,j,i+1,j-1,x,y,x+1,y-1)

                if checkTrue(intersection1x,intersection1y,n)==True:
                    print(int(intersection1x),int(intersection1y))
                    print(x,y)
                elif checkTrue(intersection2x,intersection2y,n)==True:
                    print(int(intersection2x),int(intersection2y))
                    print(x,y) 
                elif checkTrue(intersection3x,intersection3y,n)==True:
                    print(int(intersection3x),int(intersection3y))
                    print(x,y)
                else:
                    print(int(intersection4x),int(intersection4y))
                    print(x,y)
                
                
                
