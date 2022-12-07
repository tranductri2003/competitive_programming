
# ? -----------------------------------------------------------------------------------------------------
# ?　　　　　　　　　　　 ∧＿∧
# ?　　　　　 ∧＿∧ 　 （´<_｀ ）
# ?　　　　 （ ´_ゝ`）　/　 ⌒i
# ?　　　　／　　　＼　 　  |　|
# ?　　　 /　　 /￣￣￣￣/　|　 |
# ?　 ＿_(__ﾆつ/　    ＿/ .| .|＿＿＿＿
# ?　 　　　＼/＿＿＿＿/　（u　⊃
# ?
# ?		 /\_/\
# ?		(= ._.)
# ?		/ >WA \>AC
# ?
#       WELCOME TO MY CODING SPACE
#!      Filename: E_Counting_Rectangles.py
# *      Folder: D:\Code\Python\Codeforces\Contest\Codeforces Round #817 (Div. 4)
# ?      Author: TranDucTri2003
# TODO   CreatedAt: 09/04/2022 18:14:01
# ? -----------------------------------------------------------------------------------------------------

# Using 2D prefix
# Consider the 2D array with a[x][y]=0 for all x,y. Increase a[h][w] by h×w if there is an h×w rectangle in the input.

# Now for each query, we need to find the sum of all a[x][y] in a rectangle
# with lower-left corner at a[hs+1][ws+1] and upper-right corner at a[hb−1][wb−1].
# This is the standard problem that can be solved with 2D prefix sums.

# The time complexity is O(n+q+max(hb)max(wb)) per testcase.
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


t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    matrix = []
    for i in range(1001):
        matrix.append([])
        for j in range(1001):
            matrix[i].append(0)

    for i in range(n):
        h, w = list(map(int, input().split()))
        matrix[h][w] += h*w

    pre = []
    for i in range(1001):
        pre.append([])
        for j in range(1001):
            pre[i].append(0)

    for i in range(1, 1001):
        for j in range(1, 1001):
            pre[i][j] = pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1]+matrix[i][j]

    for i in range(m):
        hs, ws, hb, wb = list(map(int, input().split()))
        res = pre[hb-1][wb-1]-pre[hs][wb-1]-pre[hb-1][ws]+pre[hs][ws]
        print(res)
