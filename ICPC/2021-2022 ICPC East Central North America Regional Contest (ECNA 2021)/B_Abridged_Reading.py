
def get_parent(Adj, v):
    for i in range(len(Adj)):
        if Adj[v][i]:
            return i
    return -1


def find(v, key):
    for i in range(len(v)):
        if v[i] == key:
            return True
    return False


def find_common_ancestor(Adj, v1, v2):
    ancestor_list1 = []
    p = v1
    while p != -1:
        p = get_parent(Adj, p)
        ancestor_list1.append(p)

    p = v2
    while p != -1:
        p = get_parent(Adj, p)
        if find(ancestor_list1, p):
            return p
    return -1


def path_to_start(Adj, lengths, v):
    total = 0
    p = v
    while p != -1:
        total += lengths[p]
        p = get_parent(Adj, p)
    return total


def path_to(Adj, lengths, source, dest):
    cur = source
    total = lengths[source]
    while cur != dest:
        cur = get_parent(Adj, cur)
        if cur != dest:
            total += lengths[cur]
    return total


n, m = map(int, input().split())
data = list(map(int, input().split()))
lengths = [0] * (n + 1)
for i in range(n):
    lengths[i + 1] = data[i]

Adj = [[False for _ in range(n + 1)] for _ in range(n + 1)]
CC = [True] * (n + 1)
CC[0] = False

for i in range(m):
    p, q = map(int, input().split())
    Adj[q][p] = True
    CC[p] = False

best = 100000000
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        if CC[i] and CC[j]:
            ancestor = find_common_ancestor(Adj, i, j)
            total = 0
            if ancestor == -1:  # no common ancestor
                total = path_to_start(Adj, lengths, i) + \
                    path_to_start(Adj, lengths, j)
            else:
                total = path_to_start(Adj, lengths, ancestor) + path_to(
                    Adj, lengths, i, ancestor) + path_to(Adj, lengths, j, ancestor)

            if total < best:
                best = total

print(best)
