#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 7;
vector<int> adj[N];
int minPrime[N];
void sieve()
{
    for (int i = 2; i * i < N; ++i)
    {
        if (minPrime[i] == 0)
        {
            for (int j = i * i; j < N; j += i)
            {
                if (minPrime[j] == 0)
                    minPrime[j] = i;
            }
        }
    }
    for (int i = 2; i < N; ++i)
    {
        if (minPrime[i] == 0)
            minPrime[i] = i;
    }
}
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}
void dfs(int x, int y, vector<int> &a, int &cnt)
{
    cnt++;
    for (int u : adj[x])
    {
        if (a[u] % y != 0)
            continue;
        while (a[u] % y == 0)
            a[u] /= y;
        dfs(u, y, a, cnt);
    }
}
int main()
{
    sieve();
    int n;
    cin >> n;
    vector<int> a(n);
    for (int &x : a)
        cin >> x;
    for (int i = 1; i < n; ++i)
    {
        int u, v;
        cin >> u >> v;
        u--, v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    int best = 0;
    for (int i = 0; i < n; ++i)
    {
        int &x = a[i];
        if (a[i] == 1)
            continue;
        while (x > 1)
        {
            int cnt = 0;
            int y = minPrime[x];
            while (y == minPrime[x])
            {
                x /= y;
            }
            dfs(i, y, a, cnt);
            best = max(best, cnt);
        }
    }
    cout << best << endl;
    return 0;
}
