
N = 10**5+5
M = 10**6+6

ancestor = [0]*(M)
played = [0]*(M)

a = [0]*(N)  # Lá bài đầu tiên của người thứ i
b = [0]*(N)  # Lá bài thứ hai của người thứ i

res = [0]*(N)


def find(x):
    if (ancestor[x] != x):
        ancestor[x] = find(ancestor[x])
    return ancestor[x]


def join(x, y):
    xroot = find(x)
    yroot = find(y)
    if xroot == yroot:
        return
    else:
        ancestor[yroot] = xroot


n, m = list(map(int, input().split()))
for i in range(n):
    a[i], b[i] = list(map(int, input().split()))


for i in range(1, m+1):
    played[i] = -1
    ancestor[i] = i


temp = -1

now = 0
while True:

    if played[a[now]] == -1:
        played[a[now]] = now

        if played[b[now]] == -1:
            join(b[now], a[now])
    elif played[b[now]] == -1:
        played[b[now]] = now
    else:
        temp = now
        break

    now = (now+1) % n  # Người chơi hiện tại

for i in range(1, m+1):

    root = find(i)
    if played[root] == -1:
        res[temp] += 1
    else:
        res[played[root]] += 1

for i in range(n):
    print(res[i])
