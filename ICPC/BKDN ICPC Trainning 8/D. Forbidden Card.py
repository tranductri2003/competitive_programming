from collections import defaultdict


class DisjSet:
    def __init__(self, n):
        self.rank = [1] * (n+1)
        self.parent = [i for i in range(n+1)]

    def find(self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] = self.rank[xroot] + 1


n, m = list(map(int, input().split()))
res = [0]*(n+1)
player = [(0, 0)]*(n+1)  # Các lá bài của người chơi thứ i

for i in range(1, n+1):
    a, b = list(map(int, input().split()))
    player[i] = (a, b)


for forbidden in range(1, m+1):

    played = defaultdict(lambda: 0)  # Kiểm tra xem lá thứ i đã được chơi chưa

    # Kiểm tra xem người chơi thứ i đã đánh được mấy lá bài
    num = defaultdict(lambda: 0)

    now = 0  # Người chơi hiện tại
    while True:
        now = now % n+1

        # Đi tìm lá bài thích hợp

        stop = False
        while True:
            currentCard = player[now][num[now]]
            if played[currentCard] == 0 and currentCard != forbidden:
                break  # Lá bài hợp lệ
            else:
                num[now] += 1
                if num[now] == 2:
                    res[now] += 1
                    stop = True
                    break

        if stop == True:
            break

        played[currentCard] = 1

for i in range(1, n+1):
    print(res[i])
