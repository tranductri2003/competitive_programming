# import sys

# sys.stdin = open("milk.in", "r")
t = int(input())
for _ in range(t):
    N, Q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.insert(0, 0)
    for q in range(Q):
        l, r = list(map(int, input().split()))
        start = 10**9
        finish = -10**9
        if l <= r:
            for i in range(N):
                if a[i] <= l:
                    start = i
                    break
            for i in range(N-1, -1, -1):
                if a[i] >= r:
                    finish = i
                    break
            if start <= finish:
                print("Yes")
            else:
                print("No")
        else:
            for i in range(N):
                if a[i] >= l:
                    start = i
                    break
            for i in range(N-1, -1, -1):
                if a[i] <= r:
                    finish = i
                    break
            if start <= finish:
                print("Yes")
            else:
                print("No")
