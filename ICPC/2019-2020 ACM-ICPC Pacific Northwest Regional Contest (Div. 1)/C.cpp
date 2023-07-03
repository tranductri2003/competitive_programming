#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <climits>

using namespace std;

class Graph
{
private:
    unordered_map<int, vector<int>> graph;
    unordered_map<int, int> count;
    vector<int> path;
    const int INF = 1e9;

public:
    void addEdge(int u, int v)
    {
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> BFS(int vertex)
    {
        queue<int> q;
        q.push(vertex);
        unordered_map<int, bool> visited;
        count[vertex] = -1;

        while (!q.empty())
        {
            int u = q.front();
            q.pop();

            if (!visited[u])
            {
                path.push_back(u);
                visited[u] = true;

                for (int neighbor : graph[u])
                {
                    if (!visited[neighbor])
                    {
                        q.push(neighbor);
                        count[neighbor] = min(count[u] + 1, count[neighbor]);
                    }
                }
            }
        }

        return path;
    }

    int getCount(int node)
    {
        return count[node] == INF ? -1 : count[node];
    }
};

int main()
{
    int N, M;
    cin >> N >> M;

    Graph g;
    for (int i = 0; i < M; i++)
    {
        int u, v;
        cin >> u >> v;
        g.addEdge(u, v);
    }

    g.BFS(1);
    cout << g.getCount(N) << endl;

    return 0;
}
