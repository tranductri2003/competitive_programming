#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define int long long
#define pb push_back
const int N = 1e5 + 9;
ll n;
ll a[N];
ll u[N], v[N], c1[N], c2[N], p[N];
vector<ll> path[N];
ll num[N];
bool haveN[N];
void DFS(ll i, ll j)
{
    if (i == n)
        haveN[i] = 1;
    num[i] = 1;
    for (auto x : path[i])
    {
        if (x == j)
            continue;
        DFS(x, i);
        if (haveN[x])
        {
            haveN[i] = 1;
        }
        num[i]++;
        p[x] = i;
    }
}
void Input()
{
    cin >> n;
}
void solve()
{
    for (int i = 1; i <= n - 1; i++)
    {
        cin >> u[i] >> v[i] >> c1[i] >> c2[i];
        path[u[i]].pb(v[i]);
        path[v[i]].pb(u[i]);
    }
    DFS(1, 0);

    ll res = 0;
    for (int i = 1; i <= n - 1; i++)
    {
        if (p[u[i]] == v[i])
        {
            ll cnt = 2 * num[u[i]];
            if (haveN[u[i]])
                cnt--;

            res += min(cnt * c1[i], c2[i]);
            cout << cnt << endl;
        }
        else
        {
            ll cnt = 2 * num[v[i]];
            if (haveN[v[i]])
                cnt--;

            res += min(cnt * c1[i], c2[i]);
            // cout << cnt << endl;
        }
    }
    cout << res;
    // for (int i = 1; i <= n; i++)
    //     cout << num[i] << " ";
    // cout << endl;
    // for (int i = 1; i <= n; i++)
    //     cout << haveN[i] << " ";
    // cout << endl;
}

int32_t main()
{

    if (fopen("input.txt", "r"))
    {
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    }
    int t = 1;
    // cin >> t;
    while (t--)
    {
        Input();
        solve();
    }
}
