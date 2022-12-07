    def __init__(self,vertices):
        self.distance=defaultdict(lambda:defaultdict(lambda:self.INF))
        self.edges=defaultdict(lambda:defaultdict(lambda:self.INF))
        for i in range(1,vertices+1):
            self.distance[i][i]=0
            self.edges[i][i]=0
    def addEdge(self,u,v,w):
        self.edges[u][v]=w