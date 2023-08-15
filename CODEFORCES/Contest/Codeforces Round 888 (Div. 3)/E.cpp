#include <bits/stdc++.h>
#include <utility>
using namespace std;

const int INF = INT_MAX;

vector<int> dijkstra(int n, vector<vector<pair<int, int>>> &adj, vector<int> &costs, vector<int> &potion)
{
    vector<int> dist(n + 1, INF);
    dist[0] = 0;
    vector<bool> visited(n + 1, false);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, 0));
    while (!pq.empty())
    {
        int u = pq.top().second;
        pq.pop();
        if (visited[u])
            continue;
        visited[u] = true;
        for (auto edge : adj[u])
        {
            int v = edge.first;
            int weight = edge.second;

            if (dist[v] > dist[u] + weight)
            {
                dist[v] = dist[u] + weight;
                pq.push(make_pair(dist[v], v));
            }
        }
    }
    return dist;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        vector<int> costs(n + 1);
        vector<int> potion(n + 1, 0);
        vector<vector<pair<int, int>>> adj(n + 1);
        for (int i = 0; i < k; i++)
        {
            int x;
            cin >> x;
            potion[x]++;
        }
        for (int i = 1; i <= n; i++)
        {
            int m;
            cin >> m;
            if (m == 0)
            {
                adj[i].push_back(make_pair(0, 0));
            }
            else
            {
                for (int j = 0; j < m; j++)
                {
                    int e;
                    cin >> e;
                    adj[i].push_back(make_pair(e, costs[e]));
                }
            }
        }

        // Set the cost of nodes with potions to 0
        for (int i = 1; i <= n; i++)
        {
            if (potion[i])
            {
                costs[i] = 0;
                adj[i].push_back(make_pair(0, 0));
            }
        }

        vector<int> dist = dijkstra(n, adj, costs, potion);
        for (int i = 1; i <= n; i++)
        {
            cout << dist[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
