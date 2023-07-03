
from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    if n % 2 == 1:
        print(-1)
        return
    ans = [n]
    for i in range(1, n):
        if i % 2:
            ans.append(n-i)
        else:
            ans.append(i)
    print(*ans)


for _ in range(int(input())):
    solve()
