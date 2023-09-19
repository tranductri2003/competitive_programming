#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

void solve()
{
    int n, m;
    cin >> n >> m;
    vector<vector<char>> g(n, vector<char>(m));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> g[i][j];
        }
    }
    vector<vector<int>> L(m), U(n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (g[i][j] == 'L')
            {
                L[j].push_back(i);
            }
            else if (g[i][j] == 'U')
            {
                U[i].push_back(j);
            }
        }
    }
    bool ok = true;
    for (const auto &l : L)
    {
        if (l.size() & 1)
        {
            ok = false;
            break;
        }
    }
    for (const auto &u : U)
    {
        if (u.size() & 1)
        {
            ok = false;
            break;
        }
    }
    if (!ok)
    {
        cout << "-1" << endl;
        return;
    }
    for (int j = 0; j < m; j++)
    {
        for (int k = 0; k < L[j].size(); k += 2)
        {
            int i1 = L[j][k];
            int i2 = L[j][k + 1];
            g[i1][j] = 'W';
            g[i2][j] = 'B';
            g[i1][j + 1] = 'B';
            g[i2][j + 1] = 'W';
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int k = 0; k < U[i].size(); k + 2)
        {
            int j1 = U[i][k];
            int j2 = U[i][k + 1];
            g[i][j1] = 'W';
            g[i][j2] = 'B';
            g[i + 1][j1] = 'B';
            g[i + 1][j2] = 'W';
        }
    }
    for (const auto &row : g)
    {
        for (char c : row)
        {
            cout << c;
        }
        cout << endl;
    }
}
main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}