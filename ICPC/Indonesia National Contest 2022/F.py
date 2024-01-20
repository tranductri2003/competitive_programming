import sys
import math

def Duck():
    n, p0, x = map(int, input().split())
    d = list(map(int, input().split()))
    pre = [0] * n
    pre[0] = d[0]
    for i in range(1, n):
        pre[i] = pre[i - 1] + d[i]
    tmp = pre

    if p0 >= x:
        dif = p0 - x
        cnt = (-dif) // pre[-1]
        ans = p0
        p0 += cnt * pre[-1]
        for i in range(n):
            if p0 + pre[i] >= x:
                ans = min(p0 + pre[i], ans)
        p0 += pre[-1]
        for i in range(n):
            if p0 + pre[i] >= x:
                ans = min(p0 + pre[i], ans)
        print(ans)
    else:
        print(-1)

def main():
    t = 1
    for _ in range(t):
        Duck()

if __name__ == "__main__":
    main()
