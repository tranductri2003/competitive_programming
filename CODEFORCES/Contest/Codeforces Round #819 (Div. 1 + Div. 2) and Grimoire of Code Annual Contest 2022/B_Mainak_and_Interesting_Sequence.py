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


t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    if n == 1:
        print("Yes")
        print(m)
    else:
        if m < n:
            print("No")
        else:
            if m % n == 0:
                print("Yes")
                for i in range(n):
                    print(m//n, end=" ")
                print()
            else:
                if n % 2 == 1:

                    print("Yes")
                    print(1+m-n, end=" ")
                    for i in range(1, n):
                        print(1, end=" ")
                    print()
                if n % 2 == 0:
                    if (m % n) % 2 == 1:
                        print("No")
                    else:
                        temp = m//n
                        print("Yes")
                        print(temp+(m-temp*n)//2, end=" ")
                        print(temp+(m-temp*n)//2, end=" ")
                        for i in range(2, n):
                            print(temp, end=" ")
                        print()
