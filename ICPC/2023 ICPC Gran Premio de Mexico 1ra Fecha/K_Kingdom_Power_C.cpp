#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 500005;
const int MAX_M = 300005;

int n, m, source, sink;
int book[MAX_N];
int head[MAX_N], vertex[MAX_M], capacity[MAX_M], nextEdge[MAX_M], distanceFromSource[MAX_N];
int currentEdge[MAX_N];
queue<int> bfsQueue;
int totalEdges = 1;
const int INF = 1 << 29;
int maxFlow = 0;

void addEdge(int from, int to, int cap)
{
    vertex[++totalEdges] = to;
    capacity[totalEdges] = cap;
    nextEdge[totalEdges] = head[from];
    head[from] = totalEdges;

    vertex[++totalEdges] = from;
    capacity[totalEdges] = 0;
    nextEdge[totalEdges] = head[to];
    head[to] = totalEdges;
}

bool bfs()
{
    memset(distanceFromSource, 0, sizeof(distanceFromSource));
    while (!bfsQueue.empty())
    {
        bfsQueue.pop();
    }
    bfsQueue.push(source);
    distanceFromSource[source] = 1;
    currentEdge[source] = head[source];
    while (!bfsQueue.empty())
    {
        int currentVertex = bfsQueue.front();
        bfsQueue.pop();
        for (int i = head[currentVertex]; i; i = nextEdge[i])
        {
            if (capacity[i] && !distanceFromSource[vertex[i]])
            {
                bfsQueue.push(vertex[i]);
                currentEdge[vertex[i]] = head[vertex[i]];
                distanceFromSource[vertex[i]] = distanceFromSource[currentVertex] + 1;
                if (vertex[i] == sink)
                {
                    return true;
                }
            }
        }
    }
    return false;
}

int dfs(int currentVertex, int currentFlow)
{
    if (currentVertex == sink)
    {
        return currentFlow;
    }
    int remainingFlow = currentFlow;
    for (int &i = currentEdge[currentVertex]; i; i = nextEdge[i])
    {
        if (capacity[i] && distanceFromSource[vertex[i]] == distanceFromSource[currentVertex] + 1)
        {
            int bottleneck = dfs(vertex[i], min(remainingFlow, capacity[i]));
            if (!bottleneck)
            {
                distanceFromSource[vertex[i]] = 0;
            }
            capacity[i] -= bottleneck;
            capacity[i ^ 1] += bottleneck;
            remainingFlow -= bottleneck;
            if (!remainingFlow)
            {
                break;
            }
        }
    }
    return currentFlow - remainingFlow;
}

int main()
{
    int S, E;
    cin >> n >> S >> E;
    source = 1;
    sink = 2 * n + 4;
    for (int i = 1; i <= S; i++)
    {
        int x;
        cin >> x;
        x++;
        addEdge(1, 2 * x, 1);
    }
    for (int i = 2; i <= n + 1; i++)
    {
        addEdge(2 * i, 2 * i + 1, 1);
    }
    for (int i = 1; i <= E; i++)
    {
        int x;
        cin >> x;
        x++;
        addEdge(2 * x + 1, sink, 1);
    }

    cin >> m;
    for (int i = 1; i <= m; i++)
    {
        int x, y;
        cin >> x >> y;
        x++;
        y++;
        if (book[x])
        {
            continue;
        }
        else
        {
            addEdge(2 * x + 1, 2 * y, 1);
        }
    }
    int flow = 0;
    while (bfs())
    {
        while (flow = dfs(source, INF))
        {
            maxFlow += flow;
        }
    }
    cout << maxFlow << endl;
    return 0;
}
