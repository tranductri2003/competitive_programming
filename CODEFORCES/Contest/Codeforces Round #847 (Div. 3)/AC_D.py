import sys
from array import array


def input(): return sys.stdin.buffer.readline().decode().strip()
def inp(dtype): return [dtype(x) for x in input().split()]


debug = lambda *x: print(*x, file=sys.stderr)
def ceil1(a, b): return (a + b - 1) // b


Mint, Mlong, out = 2 ** 31 - 1, 2 ** 63 - 1, []


class dict_(dict):
    def __missing__(self, key):
        return 0


for _ in range(int(input())):
    n, a = int(input()), array('i', sorted(inp(int)))
    print(n)
    print(a)
    mem = dict_()
    for i in a:
        mem[i] += 1

    ans = mem[a[0]]
    for i in range(1, n):
        if a[i] != a[i - 1]:
            if a[i] > a[i - 1] + 1:
                ans += mem[a[i]]
            elif mem[a[i]] >= mem[a[i - 1]]:
                ans += mem[a[i]] - mem[a[i - 1]]

    out.append(ans)
print('\n'.join(map(str, out)))
