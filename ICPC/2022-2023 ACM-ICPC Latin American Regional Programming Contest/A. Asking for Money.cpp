#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1005;
vector<int> graph[MAXN];
int visited[MAXN];

void dfs(int node, int ancestor)
{
    visited[node] = 1;
    for (int neighbor : graph[node])
    {
        if (neighbor != ancestor && !visited[neighbor])
        {
            dfs(neighbor, ancestor);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    vector<pair<int, int>> edges(n);
    for (int i = 0; i < n; ++i)
    {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        edges[i] = {u, v};
        graph[u].push_back(i);
        graph[v].push_back(i);
    }

    for (int i = 0; i < n; ++i)
    {
        vector<int> count(n);
        for (int node : {i, edges[i].first, edges[i].second})
        {
            memset(visited, 0, sizeof(visited));
            dfs(node, i);
            for (int j = 0; j < n; ++j)
            {
                count[j] += visited[j];
            }
        }

        int can = 0;
        for (int j = 0; j < n; ++j)
        {
            if (count[j] == 3)
            {
                can = 1;
                break;
            }
        }
        cout << (can ? "Y" : "N");
    }
    cout << "\n";

    return 0;
}
