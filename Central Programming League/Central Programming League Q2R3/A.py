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


n, m = list(map(int, input().split()))
# check = defaultdict(list)
# matrix = []
# for i in range(n+1):
#     matrix.append([])
#     for j in range(m+1):
#         matrix[i].append(0)

# for i in range(n):
#     a = list(map(int, input().split()))
#     for j in range(m):
#         matrix[i+1][j+1] = a[j]

data = []
des = [0]*(m+1)
# for i in range(1, m+1):
#     temp = 0
#     for j in range(1, n+1):
#         if matrix[j][i] == 1:
#             temp += 1
#     check[temp].append(i)
#     data.append(temp)

# data = list(set(data))
# data.sort(reverse=True)
# for num in data:
#     for numm in check[num]:
#         print(numm, end=" ")
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        if a[j] == 1:
            des[j+1] += 1
data = []
for num in des:
    data.append(num)
data = list(set(data))
data.sort(reverse=True)
data = data[:-1]


for num in data:
    for i in range(1, m+1):
        if des[i] == num:
            print(i, end=" ")
