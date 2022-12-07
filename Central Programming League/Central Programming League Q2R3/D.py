from collections import defaultdict
import sys
import os
from io import BytesIO, IOBase


MOD = 10**9+7
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


input = sys.stdin.readline


n, t = list(map(int, input().split()))


temp = 0
maxx = 0
maxy = 0
matrix = defaultdict(lambda: defaultdict(lambda: 0))
for i in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    maxx = max(maxx, x2)
    maxy = max(maxy, y2)
    for j in range(x1+1, x2+1):
        for k in range(y1+1, y2+1):
            if matrix[j][k] == 0:
                temp += 1
                matrix[j][k] = 1

if t == 1:
    print(temp)
else:
    print(temp)
    chuvi = 0
    for i in range(0, maxx+3):
        for j in range(0, maxy+3):
            if matrix[i][j] == 1:
                temp = 0
                if matrix[i-1][j] == 1:
                    temp += 1
                if matrix[i+1][j] == 1:
                    temp += 1
                if matrix[i][j-1] == 1:
                    temp += 1
                if matrix[i][j+1] == 1:
                    temp += 1
                chuvi += 4-temp

    print(chuvi)
