import math
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


for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    if n == 1:
        if k > 1:
            print(-1)
        else:
            print(1)
    else:
        a = list(map(int, input().split()))
        check = n-1
        for i in range(n-1, 0, -1):
            if a[i] == a[i-1]:
                check -= 1
            else:
                break

        a = a[check:]+a[:check]

        loop = []
        stack = 1
        for i in range(0, n-1):
            if a[i] == a[i+1]:
                stack += 1
            else:
                loop.append(stack)
                stack = 1

        loop.append(stack)
        # print(loop)
        res = 0
        for num in loop:
            if num >= k:
                for num in loop:
                    res += math.ceil(num/k)
                print(res)
                break
        else:
            print(-1)
