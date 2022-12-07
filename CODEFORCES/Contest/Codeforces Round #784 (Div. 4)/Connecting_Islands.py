
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
    
n,q=list(map(int,input().split()))
g=DisjSet(n+1)
for i in range(q):
    t,x,y=list(map(int,input().split()))
    if t==0:
        g.Union(x,y)
    else:
        if g.find(x)==g.find(y):
            print("Yes")
        else:
            print("No")